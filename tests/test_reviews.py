from __future__ import annotations

import copy
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from dufmech import reviews
from dufmech.snapshot import write_worklist_snapshot
from dufmech.worklist import DufFamilyRow


def make_root(root: Path) -> Path:
    rows = [DufFamilyRow(
        pfam_id=pfam, short_name=name, name=f"Domain of unknown function ({name})",
        interpro_id="IPR007278", unknown_status="UNKNOWN_CANDIDATE",
        candidate_reasons=("short_name_matches_duf",), proteins=4, matches=4,
        proteomes=1, taxa=1, structures=0, alphafold_models=4, domain_architectures=1,
        description="The function of this family is unknown.",
    ) for pfam, name in (("PF04149", "DUF397"), ("PF19054", "DUF5753"))]
    write_worklist_snapshot(
        rows, root / "data/worklists", snapshot_date="2026-10-05",
        generated_at=datetime(2026, 10, 5, tzinfo=timezone.utc),
    )
    (root / "README.md").write_text("# DUFMech\n")
    (root / "pyproject.toml").write_text('[project]\nname = "dufmech"\n')
    return root


def review_payload(root: Path, kind: str = "record") -> dict:
    kwargs = {"members": ["PF19054", "PF04149"], "selection": "Both fixture snapshot families."}
    inspection = reviews.inspect_review(
        root, kind, "PF04149" if kind == "record" else "seed-audit",
        **(kwargs if kind == "category" else {}),
    )
    return {
        "context": inspection["context"], "started_utc": "2026-10-07T01:00:00Z",
        "finished_utc": "2026-10-07T01:04:00Z", "verdict": "SEED_ONLY",
        "reviewer": "test-reviewer", "scientific_review": False,
        "review_scope": "Inspect fixture metadata and manifest integrity only.",
        "sections": {heading: "Checked fixture metadata; no experimental support was assessed."
                     for heading in inspection["required_sections"]},
    }


@pytest.fixture
def root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(reviews, "_revision", lambda _: "a" * 40)
    return make_root(tmp_path)


def test_inspection_resolves_verified_row_without_projection_and_does_not_write(root):
    before = sorted(p.relative_to(root) for p in root.rglob("*"))
    first = reviews.inspect_review(root, "record", "PF04149")
    assert first == reviews.inspect_review(root, "record", "PF04149")
    assert first["status"] == "inspection_only"
    assert first["context"]["targets"][0]["locator"].endswith(".json#pfam_id=PF04149")
    assert first["context"]["record_digests"] == {}
    assert sorted(p.relative_to(root) for p in root.rglob("*")) == before


def test_inspection_fails_on_checksum_mismatch(root):
    path = next((root / "data/worklists").glob("*.tsv"))
    path.write_text(path.read_text() + "\n")
    with pytest.raises(RuntimeError, match="differs"):
        reviews.inspect_review(root, "record", "PF04149")


@pytest.mark.parametrize("kind", ["record", "category", "repo"])
def test_real_report_structure_timestamps_and_append_only_collision(root, kind):
    payload = review_payload(root, kind)
    first = reviews.save_review(root, payload)
    original = first.read_bytes()
    second = reviews.save_review(root, payload)
    assert second.stem == first.stem + "-02"
    assert first.read_bytes() == original
    loaded = reviews.read_review(root, first)
    assert loaded["finished_utc"] == "2026-10-07T01:04:00Z"
    assert loaded["started_utc"] == "2026-10-07T01:00:00Z"
    assert loaded["status"] == "saved" and loaded["scientific_review"] is False
    assert set(loaded["sections"]) == set(reviews.SECTIONS[kind])
    if kind == "category":
        assert loaded["context"]["members"] == ["PF04149", "PF19054"]
        assert "## Lump and Split Review" in first.read_text()
    first_listing = reviews.load_review_metadata(root)
    assert first_listing == reviews.load_review_metadata(root)
    assert len(first_listing) == 2
    assert first_listing[0]["href"].startswith(reviews.REPORT_DIRS[kind])


def test_concurrent_saves_never_clobber_or_leave_partial_files(root):
    payload = review_payload(root)
    with ThreadPoolExecutor(max_workers=4) as pool:
        paths = list(pool.map(lambda _: reviews.save_review(root, payload), range(8)))
    assert len(set(paths)) == 8
    assert len(reviews.load_review_metadata(root)) == 8
    assert not list((root / "reports").rglob(".append-*"))


@pytest.mark.parametrize("field,value", [
    ("reviewer", "TODO"), ("review_scope", ""), ("scientific_review", "false"),
    ("finished_utc", "2026-10-07T00:00:00Z"),
    ("started_utc", "2026-10-07T01:00:00"), ("verdict", "COMPLETED"),
])
def test_scaffold_or_invalid_content_never_creates_report(root, field, value):
    payload = review_payload(root)
    payload[field] = value
    with pytest.raises((ValueError, TypeError)):
        reviews.save_review(root, payload)
    assert not (root / "reports").exists()


def test_missing_or_placeholder_section_is_not_a_review(root):
    payload = review_payload(root)
    payload["sections"]["Evidence"] = "TODO: investigate"
    with pytest.raises(ValueError, match="actual"):
        reviews.save_review(root, payload)
    del payload["sections"]["Evidence"]
    with pytest.raises(ValueError, match="sections must be exactly"):
        reviews.save_review(root, payload)


def test_projection_and_overlay_changes_invalidate_unsaved_context(root):
    projection = root / "data/families/PF04149.yaml"
    projection.parent.mkdir()
    projection.write_text("id: Pfam:PF04149\npfam_id: PF04149\nname: DUF397\n")
    payload = review_payload(root)
    assert payload["context"]["record_digests"]["PF04149"]
    overlay = root / "curation/families/PF04149.yaml"
    overlay.parent.mkdir(parents=True)
    overlay.write_text("pfam_id: PF04149\ncuration_status: IN_PROGRESS\n")
    with pytest.raises(ValueError, match="context changed"):
        reviews.save_review(root, payload)


@pytest.mark.parametrize("bad", ["../evil", "/tmp/evil", "..", "x/y", "x\\y", "x#y"])
def test_unsafe_slug_is_refused(root, bad):
    with pytest.raises(ValueError):
        reviews.inspect_review(root, "category", bad, members=["PF04149"], selection="One family.")


@pytest.mark.parametrize("path", ["reports", "reports/yaml_record_review"])
def test_symlink_output_ancestor_is_refused(root, path, tmp_path_factory):
    destination = tmp_path_factory.mktemp("outside")
    link = root / path
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(destination, target_is_directory=True)
    with pytest.raises((ValueError, OSError)):
        reviews.save_review(root, review_payload(root))
    assert not list(destination.iterdir())


def test_exact_output_symlink_collision_is_refused(root):
    payload = review_payload(root)
    output = root / "reports/yaml_record_review/20261007T010400Z-PF04149.md"
    output.parent.mkdir(parents=True)
    output.symlink_to(root / "README.md")
    with pytest.raises(ValueError, match="not a regular file"):
        reviews.save_review(root, payload)
    assert (root / "README.md").read_text() == "# DUFMech\n"


def test_snapshot_and_projection_symlinks_are_refused(root):
    directory = root / "data/families"
    directory.mkdir()
    (directory / "PF04149.yaml").symlink_to(root / "README.md")
    with pytest.raises(ValueError, match="symlink"):
        reviews.inspect_review(root, "record", "PF04149")


def test_loaders_refuse_tampered_headers_or_unsafe_context_links(root):
    path = reviews.save_review(root, review_payload(root))
    source = path.read_text()
    path.write_text(source.replace("- Verdict: SEED_ONLY", "- Verdict: PASS"))
    with pytest.raises(ValueError, match="disagree"):
        reviews.load_review_metadata(root)
    path.write_text(source.replace("data/worklists/", "../worklists/"))
    with pytest.raises(ValueError, match="unsafe"):
        reviews.load_review_metadata(root)


def test_hidden_invalid_report_is_checked(root):
    path = reviews.save_review(root, review_payload(root))
    (path.parent / ".ignored.md").write_text("# An unfilled report\n")
    with pytest.raises(ValueError, match="missing review metadata"):
        reviews.load_review_metadata(root)


def test_cli_inspect_save_check_list(root, capsys):
    args = ["--repo-root", str(root)]
    assert reviews.main([*args, "inspect", "record", "PF04149"]) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "inspection_only"
    content = root / "review-input.yaml"
    content.write_text(yaml.safe_dump(review_payload(root)))
    assert reviews.main([*args, "finalize", "--content", str(content)]) == 0
    capsys.readouterr()
    assert reviews.main([*args, "check"]) == 0
    assert json.loads(capsys.readouterr().out) == {"valid_reports": 1}
    assert reviews.main([*args, "list", "--pfam-id", "PF19054"]) == 0
    assert json.loads(capsys.readouterr().out) == []


def test_record_digest_excludes_only_bookkeeping():
    original = {"pfam_id": "PF04149", "curation_status": "IN_PROGRESS", "assertions": []}
    reviewed = {**original, "curation_status": "REVIEWED", "review_id": "reports/review.md"}
    assert reviews.record_content_digest(original) == reviews.record_content_digest(reviewed)
    changed = copy.deepcopy(reviewed)
    changed["assertions"].append({"statement": "Changed content."})
    assert reviews.record_content_digest(original) != reviews.record_content_digest(changed)


def test_duplicate_yaml_key_and_header_injection_are_rejected(root):
    with pytest.raises(ValueError, match="duplicate YAML key"):
        reviews.read_yaml("verdict: SEED_ONLY\nverdict: PASS\n")
    payload = review_payload(root)
    payload["reviewer"] = "reviewer\n## Evidence\nAn injected section"
    with pytest.raises(ValueError, match="single line"):
        reviews.save_review(root, payload)


def test_invalid_context_reports_validation_error_without_crashing(root):
    payload = review_payload(root)
    del payload["context"]["scope_paths"]
    with pytest.raises(ValueError, match="context fields"):
        reviews.save_review(root, payload)
