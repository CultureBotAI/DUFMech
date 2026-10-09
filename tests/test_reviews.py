"""Historical Markdown compatibility and shared native artifact primitives.

New saver/CLI behavior is exercised in test_structured_reviews.py.
"""

from __future__ import annotations

import copy
import json
import os
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


def legacy_review_fixture(root: Path, payload: dict) -> Path:
    """Construct historical v1 test input; never a supported production save route."""
    reviews._validate_content(root, payload)
    context = payload["context"]
    current = reviews.inspect_review(
        root, context["kind"], context["slug"], members=context["members"],
        selection=context["selection"], snapshot_id=context["snapshot_id"],
        scope_paths=context["scope_paths"],
    )["context"]
    if context != current:
        raise ValueError("review input context changed")
    value = {**payload, "review_version": 1, "status": "saved"}
    stamp = reviews.utc_timestamp(payload["finished_utc"]).strftime("%Y%m%dT%H%M%SZ")
    return reviews.append_document(
        root, reviews.REPORT_DIRS[context["kind"]], f"{stamp}-{context['slug']}", ".md",
        lambda _: reviews._render_report(value),
    )


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
    first = legacy_review_fixture(root, payload)
    original = first.read_bytes()
    second = legacy_review_fixture(root, payload)
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
        paths = list(pool.map(lambda _: legacy_review_fixture(root, payload), range(8)))
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
        legacy_review_fixture(root, payload)
    assert not (root / "reports").exists()


def test_missing_or_placeholder_section_is_not_a_review(root):
    payload = review_payload(root)
    payload["sections"]["Evidence"] = "TODO: investigate"
    with pytest.raises(ValueError, match="actual"):
        legacy_review_fixture(root, payload)
    del payload["sections"]["Evidence"]
    with pytest.raises(ValueError, match="sections must be exactly"):
        legacy_review_fixture(root, payload)


def test_substantive_review_can_quote_scaffold_markers_and_source_fields(root):
    payload = review_payload(root)
    payload["sections"]["Findings"] = (
        "The source retains a TODO marker and placeholder label in <protein_id>; "
        "this audit records that concrete gap rather than treating it as functional evidence."
    )
    saved = legacy_review_fixture(root, payload)
    assert payload["sections"]["Findings"] in saved.read_text()
    assert reviews.load_review_metadata(root)[0]["verdict"] == payload["verdict"]


@pytest.mark.parametrize("scaffold", [
    "TODO\nTBD", "<protein_id>\n<source_url>", "[fill evidence]\n[insert reference]",
    "TODO\n\npending",
])
def test_multiline_scaffold_only_sections_remain_invalid(root, scaffold):
    payload = review_payload(root)
    payload["sections"]["Findings"] = scaffold
    with pytest.raises(ValueError, match="actual"):
        legacy_review_fixture(root, payload)
    assert not (root / "reports").exists()


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
        legacy_review_fixture(root, payload)


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
        legacy_review_fixture(root, review_payload(root))
    assert not list(destination.iterdir())


def test_exact_output_symlink_collision_is_refused(root):
    payload = review_payload(root)
    output = root / "reports/yaml_record_review/20261007T010400Z-PF04149.md"
    output.parent.mkdir(parents=True)
    output.symlink_to(root / "README.md")
    with pytest.raises(ValueError, match="not a regular file"):
        legacy_review_fixture(root, payload)
    assert (root / "README.md").read_text() == "# DUFMech\n"


def test_snapshot_and_projection_symlinks_are_refused(root):
    directory = root / "data/families"
    directory.mkdir()
    (directory / "PF04149.yaml").symlink_to(root / "README.md")
    with pytest.raises(ValueError, match="symlink"):
        reviews.inspect_review(root, "record", "PF04149")


def test_loaders_refuse_tampered_headers_or_unsafe_context_links(root):
    path = legacy_review_fixture(root, review_payload(root))
    source = path.read_text()
    path.write_text(source.replace("- Verdict: SEED_ONLY", "- Verdict: PASS"))
    with pytest.raises(ValueError, match="disagree"):
        reviews.load_review_metadata(root)
    path.write_text(source.replace("data/worklists/", "../worklists/"))
    with pytest.raises(ValueError, match="unsafe"):
        reviews.load_review_metadata(root)


def test_hidden_invalid_report_is_checked(root):
    path = legacy_review_fixture(root, review_payload(root))
    (path.parent / ".ignored.md").write_text("# An unfilled report\n")
    with pytest.raises(ValueError, match="missing review metadata"):
        reviews.load_review_metadata(root)


def test_cli_inspect_save_check_list(root, capsys):
    args = ["--repo-root", str(root)]
    assert reviews.main([*args, "inspect", "record", "PF04149"]) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "inspection_only"
    content = root / "review-input.yaml"
    content.write_text(yaml.safe_dump(review_payload(root)))
    assert reviews.main([*args, "finalize", "--content", str(content)]) == 1
    assert "structured contract" in capsys.readouterr().err
    legacy_review_fixture(root, review_payload(root))
    assert reviews.main([*args, "check"]) == 0
    assert json.loads(capsys.readouterr().out) == {"valid_reports": 1}
    assert reviews.main([*args, "list", "--pfam-id", "PF19054"]) == 0
    assert json.loads(capsys.readouterr().out) == []


def test_record_digest_excludes_only_bookkeeping_and_derived_events():
    original = {"pfam_id": "PF04149", "curation_status": "IN_PROGRESS", "assertions": []}
    reviewed = {**original, "curation_status": "REVIEWED", "review_id": "reports/review.md"}
    assert reviews.record_content_digest(original) == reviews.record_content_digest(reviewed)
    exported = {**reviewed, "curation_events": [{"summary": "Appended canonical event index"}]}
    assert reviews.record_content_digest(original) == reviews.record_content_digest(exported)
    for key in ("curation_history", "assertions", "discussions", "datasets", "cross_corpus_links", "provenance"):
        assert reviews.record_content_digest(original) != reviews.record_content_digest({**exported, key: "changed"})
    changed = copy.deepcopy(reviewed)
    changed["assertions"].append({"statement": "Changed content."})
    assert reviews.record_content_digest(original) != reviews.record_content_digest(changed)


def test_review_source_sink_preserves_validated_bytes_after_path_replacement(root, monkeypatch):
    path = legacy_review_fixture(root, review_payload(root))
    relative = path.relative_to(root).as_posix()
    original = path.read_bytes()
    capture = reviews.read_source_bytes
    calls = []

    def replace_after_capture(base, name):
        calls.append(name)
        raw = capture(base, name)
        (base / name).write_bytes(b"Unvalidated replacement, not the reviewed document.\n")
        return raw

    monkeypatch.setattr(reviews, "read_source_bytes", replace_after_capture)
    captured = {relative: b"untrusted sink entry is not input"}
    metadata = reviews.load_review_metadata(root, source_bytes=captured)
    assert calls == [relative]
    assert captured == {relative: original}
    assert metadata[0]["verdict"] == "SEED_ONLY"
    assert "## Evidence\n" in captured[relative].decode("utf-8")
    assert "sections" not in metadata[0] and "source_bytes" not in metadata[0]
    json.dumps(metadata)
    failed_capture = {}
    with pytest.raises(ValueError, match="missing review metadata"):
        reviews.load_review_metadata(root, source_bytes=failed_capture)
    assert failed_capture == {}


def test_review_source_sink_only_contains_selected_validated_reports(root):
    selected = legacy_review_fixture(root, review_payload(root))
    legacy_review_fixture(root, review_payload(root, "repo"))
    captured = {}
    metadata = reviews.load_review_metadata(root, "PF04149", source_bytes=captured)
    assert [item["path"] for item in metadata] == [selected.relative_to(root).as_posix()]
    assert captured == {selected.relative_to(root).as_posix(): selected.read_bytes()}


def test_source_reader_preserves_bytes_and_refuses_unsafe_or_nonregular_paths(tmp_path):
    path = tmp_path / "source.yaml"
    raw = b"summary: caf\xc3\xa9\r\n"
    path.write_bytes(raw)
    assert reviews.read_source_bytes(tmp_path, path.name) == raw
    for relative in ("../escape", "/etc/passwd", "a/../source.yaml", "a//source.yaml"):
        with pytest.raises(ValueError, match="unsafe"):
            reviews.read_source_bytes(tmp_path, relative)
    for relative in ("missing.yaml", "missing/leaf.yaml"):
        with pytest.raises(FileNotFoundError):
            reviews.read_source_bytes(tmp_path, relative)
    (tmp_path / "directory.yaml").mkdir()
    os.mkfifo(tmp_path / "pipe.yaml")
    for relative in ("directory.yaml", "pipe.yaml"):
        with pytest.raises((ValueError, OSError)):
            reviews.read_source_bytes(tmp_path, relative)


@pytest.mark.parametrize("swap", ["root-before", "root-after", "parent-before", "parent-after", "leaf-before"])
def test_source_reader_does_not_follow_a_racing_directory_or_leaf_symlink(tmp_path, monkeypatch, swap):
    root, outside = tmp_path / "root", tmp_path / "outside"
    inside = root / "inside"
    inside.mkdir(parents=True)
    outside.mkdir()
    (inside / "source.yaml").write_bytes(b"validated inside bytes\n")
    (outside / "source.yaml").write_bytes(b"outside secret must not be read\n")
    (outside / "inside").mkdir()
    (outside / "inside/source.yaml").write_bytes(b"outside secret must not be read\n")
    original_open = os.open
    swapped = False

    def racing_open(path, flags, *args, **kwargs):
        nonlocal swapped
        if path == "root" and not swapped and swap.startswith("root"):
            swapped = True
            descriptor = original_open(path, flags, *args, **kwargs) if swap == "root-after" else None
            root.rename(tmp_path / "original-root")
            root.symlink_to(outside, target_is_directory=True)
            return descriptor if descriptor is not None else original_open(path, flags, *args, **kwargs)
        if path == "inside" and not swapped and swap.startswith("parent"):
            swapped = True
            descriptor = original_open(path, flags, *args, **kwargs) if swap == "parent-after" else None
            inside.rename(root / "original")
            inside.symlink_to(outside, target_is_directory=True)
            return descriptor if descriptor is not None else original_open(path, flags, *args, **kwargs)
        if path == "source.yaml" and not swapped and swap == "leaf-before":
            swapped = True
            (inside / "source.yaml").unlink()
            (inside / "source.yaml").symlink_to(outside / "source.yaml")
        return original_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(reviews.os, "open", racing_open)
    if swap.endswith("after"):
        assert reviews.read_source_bytes(root, "inside/source.yaml") == b"validated inside bytes\n"
    else:
        with pytest.raises(OSError):
            reviews.read_source_bytes(root, "inside/source.yaml")
    assert swapped


def test_source_reader_rejects_preexisting_root_symlink(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "source.yaml").write_bytes(b"outside secret must not be read\n")
    root = tmp_path / "root"
    root.symlink_to(outside, target_is_directory=True)
    with pytest.raises(OSError):
        reviews.read_source_bytes(root, "source.yaml")


def test_duplicate_yaml_key_and_header_injection_are_rejected(root):
    with pytest.raises(ValueError, match="duplicate YAML key"):
        reviews.read_yaml("verdict: SEED_ONLY\nverdict: PASS\n")
    payload = review_payload(root)
    payload["reviewer"] = "reviewer\n## Evidence\nAn injected section"
    with pytest.raises(ValueError, match="single line"):
        legacy_review_fixture(root, payload)


def test_invalid_context_reports_validation_error_without_crashing(root):
    payload = review_payload(root)
    del payload["context"]["scope_paths"]
    with pytest.raises(ValueError, match="context fields"):
        legacy_review_fixture(root, payload)
