"""Issue #183: semantic digests must describe the hash-bound inspected bytes."""

import hashlib
import subprocess
from copy import deepcopy

import pytest
import yaml
from test_history import save_event
from test_records import assertion
from test_structured_reviews import payload
from test_structured_reviews import root as review_root

from dufmech import history, records, reviews, structured_reviews
from dufmech.site_metadata import load_review_site_metadata, load_site_metadata

root = review_root


def prepared(root):
    records.write_records(root, records.build_records(root), apply=True)
    overlay = root / "curation/families/PF04149.yaml"
    overlay.parent.mkdir(parents=True)
    curated = {"pfam_id": "PF04149", "curation_status": "IN_PROGRESS",
               "curation_history": "history/records/PF04149"}
    overlay.write_text(yaml.safe_dump(curated))
    save_event(root, event="EDIT", outcome="changed", timestamp="2026-10-07T00:50:00Z",
               target_path="curation/families/PF04149.yaml")
    value = payload(root, projection=True)
    value["scientific_review"] = True
    return value, overlay, curated


def retain_projection(root, value):
    path = value["targets"][0]["path"]
    raw = (root / path).read_bytes()
    item = {"evidence_id": "retained-projection", "kind": "record_content", "reference": path,
            "locator": structured_reviews.PROJECTION_BINDING, "accessed_at": value["finished_at"],
            "support": "context_only", "summary": "Exact inspected fixture projection.",
            "quote": raw.decode(), "snapshot_sha256": hashlib.sha256(raw).hexdigest()}
    value["evidence"].append(item)
    return item


def commit_inputs(root, value):
    for args in (("add", "data", "curation", "history"),
                 ("-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                  "commit", "-m", "Synthetic inspected projection")):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)
    revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"]).decode().strip()
    value["source"].update(state="git_commit", git_revision=revision)


def linked_future(root, value, report, overlay, curated, future):
    review_id = report.relative_to(root).as_posix()
    curated.update(review_id=review_id, curation_status="REVIEWED")
    if "assertions" in future:
        curated["assertions"] = future["assertions"]
    overlay.write_text(yaml.safe_dump(curated))
    save_event(root, event="REVIEW", outcome="no_change", target_path="data/families/PF04149.yaml",
               urls=[reviews.review_report_url(review_id)])
    future.update(curation_status="REVIEWED", review_id=review_id,
                  curation_events=history.project_curation_events(root, "PF04149"))
    return review_id


@pytest.mark.parametrize("binding", ["current", "retained", "git"])
def test_common_saved_false_digest_rejected_at_ingestion_promotion_and_pages(root, monkeypatch, binding):
    value, overlay, curated = prepared(root)
    if binding == "retained":
        retain_projection(root, value)
    elif binding == "git":
        commit_inputs(root, value)
    inspected = yaml.safe_load((root / "data/families/PF04149.yaml").read_text())
    future = deepcopy(inspected)
    future["assertions"] = [assertion(root)]
    assert not inspected.get("assertions")
    value["targets"][0]["semantic_digest"]["sha256"] = reviews.record_content_digest(future)
    with pytest.raises(ValueError, match="semantic digest differs"):
        reviews.save_review(root, value)
    report = structured_reviews.common().save_review(root, value)
    review_id = linked_future(root, value, report, overlay, curated, future)
    assert structured_reviews.common().read_review(root, review_id) == value
    captured = {}
    with pytest.raises(ValueError, match="semantic digest differs"):
        reviews.load_review_metadata(root, source_bytes=captured)
    assert captured == {}
    with pytest.raises(ValueError, match="semantic digest differs"):
        reviews.require_completed_review(root, "PF04149", review_id, future)
    with pytest.raises(records.RecordError, match="semantic digest differs"):
        records.build_records(root)
    with pytest.raises(ValueError, match="semantic digest differs"):
        load_review_site_metadata(root, {"PF04149"}, source_pins={})
    # Exercise Pages' independent captured-review check, even if record loading
    # has already supplied an otherwise valid future projection.
    monkeypatch.setattr(records, "load_records", lambda _: [future])
    with pytest.raises(ValueError, match="semantic digest differs"):
        load_site_metadata(root, {"worklist": value["source"]["snapshot_id"]}, source_pins={})


@pytest.mark.parametrize("producer", ["native", "common-retained", "common-git"])
def test_verified_binding_survives_only_legitimate_bookkeeping_changes(root, producer):
    value, overlay, curated = prepared(root)
    before = deepcopy(value)
    projection_path = root / value["targets"][0]["path"]
    inspected_raw = projection_path.read_bytes()
    if producer == "common-retained":
        retain_projection(root, value)
    elif producer == "common-git":
        commit_inputs(root, value)
    report = (reviews.save_review if producer == "native" else structured_reviews.common().save_review)(root, value)
    if producer == "native":
        assert value == before
        saved = structured_reviews.common().read_review(root, report.relative_to(root).as_posix())
        binding = next(e for e in saved["evidence"] if e.get("locator") == structured_reviews.PROJECTION_BINDING)
        assert binding["quote"].encode() == inspected_raw
        assert binding["support"] == "context_only"
    future = yaml.safe_load(inspected_raw)
    review_id = linked_future(root, value, report, overlay, curated, future)
    projected = records.build_records(root)
    records.write_records(root, projected, apply=True)
    assert projection_path.read_bytes() != inspected_raw
    assert reviews.require_completed_review(root, "PF04149", review_id, projected["PF04149.yaml"])
    save_event(root, event="AUDIT", outcome="no_change", target_path="data/families/PF04149.yaml")
    projected = records.build_records(root)
    records.write_records(root, projected, apply=True)
    schema = root / "src/dufmech/schema/dufmech.yaml"
    schema.parent.mkdir(parents=True)
    schema.write_bytes(records.SCHEMA.read_bytes())
    metadata, _, copies = load_site_metadata(root, {"worklist": value["source"]["snapshot_id"]}, source_pins={})
    assert metadata["PF04149"]["curation_status"] == "REVIEWED"
    assert copies[f"source/{review_id}"] == report.read_text()
    projected["PF04149.yaml"]["assertions"] = [assertion(root)]
    with pytest.raises(ValueError, match="content changed"):
        reviews.require_completed_review(root, "PF04149", review_id, projected["PF04149.yaml"])


@pytest.mark.parametrize("damage", ["quote", "hash", "kind", "missing-quote", "duplicate"])
def test_unverified_retained_binding_cannot_fall_back_to_current_bytes(root, damage):
    value = payload(root, projection=True)
    item = retain_projection(root, value)
    if damage == "quote":
        item["quote"] += "# Not the inspected bytes\n"
    elif damage == "hash":
        item["snapshot_sha256"] = "a" * 64
    elif damage == "kind":
        item["kind"] = "primary_source"
    elif damage == "missing-quote":
        del item["quote"]
    else:
        value["evidence"].append({**item, "evidence_id": "duplicate-binding"})
    report = structured_reviews.common().save_review(root, value)
    with pytest.raises(ValueError, match="retained projection"):
        reviews.read_review(root, report)


def test_common_save_without_retained_or_git_bytes_fails_closed_after_projection_change(root):
    value = payload(root, projection=True)
    report = structured_reviews.common().save_review(root, value)
    path = root / value["targets"][0]["path"]
    changed = yaml.safe_load(path.read_text())
    changed["curation_status"] = "IN_PROGRESS"
    path.write_text(yaml.safe_dump(changed))
    assert reviews.record_content_digest(changed) == value["targets"][0]["semantic_digest"]["sha256"]
    with pytest.raises(ValueError, match="cannot verify reviewed projection bytes"):
        reviews.read_review(root, report)
