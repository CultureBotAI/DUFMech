from __future__ import annotations

import copy

import pytest
import yaml
from bs4 import BeautifulSoup
from linkml_runtime.dumpers import json_dumper

from dufmech.causal_graphs import inventory
from dufmech.records import RecordError, build_records, validate_record, write_records
from dufmech.reviews import record_content_digest
from tests import test_records
from tests.test_records import append_family_audit, assertion

corpus = test_records.corpus
history_corpus = test_records.history_corpus


@pytest.fixture
def overlay(corpus):
    return {
        "pfam_id": "PF00001", "curation_status": "IN_PROGRESS",
        "curation_history": "history/records/PF00001",
        "causal_graphs": [{
            "graph_id": "test", "title": "Fixture mechanism", "scope": "One tested protein",
            "context": "In vitro with the required substrate",
            "family_mapping": "Synthetic test fixture, not scientific evidence",
            "scope_status": "MECHANISTIC", "limitations": "No family-wide transfer",
            "nodes": [
                {"node_id": "a", "label": "Protein activity", "node_type": "ACTIVITY",
                 "grounding": ["UniProtKB:P12345"]},
                {"node_id": "b", "label": "Measured outcome", "node_type": "STATE"},
            ],
            "edges": [{
                "edge_id": "ab", "subject": "a", "object": "b", "predicate": "enables",
                "mechanism": "Synthetic experimental relation", "directness": "DIRECT",
                "support": "OBSERVED", "evidence_kind": "EXPERIMENTAL",
                "evidence": assertion(corpus)["evidence"],
            }],
        }],
    }


def test_graph_survives_overlay_builder_and_model(history_corpus, overlay):
    import json

    from dufmech.datamodel.dufmech import FamilyRecord

    root = history_corpus
    append_family_audit(root)
    path = root / "curation/families/PF00001.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(overlay))
    record = build_records(root)["PF00001.yaml"]
    assert record["causal_graphs"] == overlay["causal_graphs"]
    restored = json.loads(json_dumper.dumps(FamilyRecord(**record), inject_type=False))
    assert restored == record
    validate_record(restored, root)
    write_records(root, {"PF00001.yaml": record}, apply=True)
    assert write_records(root, build_records(root), check=True) == []
    changed = copy.deepcopy(record)
    changed["causal_graphs"][0]["edges"][0]["predicate"] = "decreases"
    assert record_content_digest(changed) != record_content_digest(record)


@pytest.mark.parametrize("field", ["nodes", "edges", "scope", "context", "family_mapping", "limitations"])
def test_missing_graph_contract_fields_rejected(corpus, overlay, field):
    del overlay["causal_graphs"][0][field]
    with pytest.raises(RecordError):
        validate_record(overlay, corpus, target="FamilyCuration")


@pytest.mark.parametrize("mutation", [
    lambda g: g.update(nodes=[]),
    lambda g: g.update(edges=[]),
    lambda g: g["nodes"].append(copy.deepcopy(g["nodes"][0])),
    lambda g: g["edges"].append(copy.deepcopy(g["edges"][0])),
    lambda g: g["edges"].append({**g["edges"][0], "edge_id": "other"}),
    lambda g: g["nodes"].append({"node_id": "orphan", "label": "Unused", "node_type": "STATE"}),
    lambda g: g["edges"][0].update(subject="missing"),
    lambda g: g["edges"][0].update(object="missing"),
    lambda g: g["edges"][0].update(predicate="correlated_with"),
    lambda g: g["edges"][0].update(evidence=[]),
    lambda g: g["edges"][0].update(evidence_kind="COMPUTATIONAL"),
    lambda g: g["edges"][0].update(directness="INDIRECT"),
    lambda g: g["edges"][0].update(mechanism="  "),
    lambda g: g["edges"][0].update(support="HYPOTHESIZED"),
    lambda g: g["nodes"][0].update(label="  "),
    lambda g: g.update(scope="  "),
    lambda g: g.update(scope_status="HYPOTHETICAL"),
    lambda g: g.update(invented=True),
    lambda g: g["edges"][0]["evidence"][0].update(snippet="invented quotation"),
    lambda g: g["edges"][0]["evidence"][0].update(cache_sha256="0" * 64),
    lambda g: g["edges"][0]["evidence"][0].update(cache_path="evidence/../../secret.txt"),
    lambda g: g["edges"][0]["evidence"][0].update(source_url="https://user:password@example.org"),
])
def test_malformed_or_overstated_graphs_fail_closed(corpus, overlay, mutation):
    mutation(overlay["causal_graphs"][0])
    with pytest.raises(RecordError):
        validate_record(overlay, corpus, target="FamilyCuration")


def test_graphs_need_unique_ids_and_canonical_history(corpus, overlay):
    overlay["causal_graphs"] *= 2
    with pytest.raises(RecordError, match="duplicate graph_id"):
        validate_record(overlay, corpus, target="FamilyCuration")
    record = build_records(corpus)["PF00001.yaml"]
    record["causal_graphs"] = overlay["causal_graphs"][:1]
    with pytest.raises(RecordError, match="curation_history"):
        validate_record(record, corpus)


def test_hypotheses_and_phenotype_effects_are_distinct(corpus, overlay):
    graph = overlay["causal_graphs"][0]
    graph["scope_status"] = "PHENOTYPIC"
    graph["edges"][0]["directness"] = "INDIRECT"
    validate_record(overlay, corpus, target="FamilyCuration")
    graph["scope_status"] = "HYPOTHETICAL"
    graph["edges"][0].update(support="HYPOTHESIZED", evidence_kind="CONTEXTUAL")
    validate_record(overlay, corpus, target="FamilyCuration")
    graph["scope_status"] = "PHENOTYPIC"
    with pytest.raises(RecordError, match="observed experimental"):
        validate_record(overlay, corpus, target="FamilyCuration")


def test_feedback_requires_explanation_not_blanket_cycle_ban(corpus, overlay):
    graph = overlay["causal_graphs"][0]
    graph["edges"].append({**copy.deepcopy(graph["edges"][0]),
                           "edge_id": "ba", "subject": "b", "object": "a"})
    with pytest.raises(RecordError, match="feedback_explanation"):
        validate_record(overlay, corpus, target="FamilyCuration")
    graph["feedback_explanation"] = "  "
    with pytest.raises(RecordError, match="feedback_explanation"):
        validate_record(overlay, corpus, target="FamilyCuration")
    graph["feedback_explanation"] = "Fixture feedback; scientific support still needs review."
    validate_record(overlay, corpus, target="FamilyCuration")


def test_inventory_accounts_for_graphless_records_without_claiming_review(corpus, overlay):
    seeded = build_records(corpus)["PF00001.yaml"]
    other = {**seeded, "pfam_id": "PF00002", "causal_graphs": overlay["causal_graphs"]}
    result = inventory([other, seeded])
    assert result["records"] == 2
    assert result["graph_states"] == {"ABSENT": 1, "PRESENT": 1}
    assert [r["pfam_id"] for r in result["families"]] == ["PF00001", "PF00002"]
    assert result["kind"] == "structural_inventory_not_scientific_review"
    assert result["families"][0]["edge_count"] == 0
    with pytest.raises(ValueError, match="duplicate Pfam"):
        inventory([seeded, seeded])


def test_explicit_self_feedback_is_supported(corpus, overlay):
    graph = overlay["causal_graphs"][0]
    graph["nodes"] = graph["nodes"][:1]
    graph["edges"][0]["object"] = "a"
    with pytest.raises(RecordError, match="feedback_explanation"):
        validate_record(overlay, corpus, target="FamilyCuration")
    graph["feedback_explanation"] = "The experimentally supported activity reinforces itself."
    validate_record(overlay, corpus, target="FamilyCuration")


def test_graph_rendering_preserves_direction_scope_evidence_and_escaping(overlay):
    from dufmech.site import curated_graphs

    overlay["causal_graphs"][0]["title"] = '<script>alert("bad")</script>'
    html = BeautifulSoup(curated_graphs(overlay), "html.parser")
    assert not html.select("script")
    assert 'alert("bad")' in html.get_text()
    assert "One tested protein" in html.get_text()
    assert "Synthetic test fixture" in html.get_text()
    assert "OBSERVED" in html.get_text()
    assert "DIRECT" in html.get_text()
    assert "UniProtKB:P12345" in html.get_text()
    assert html.find(id="causal-edge.test.ab")
    assert html.select_one("td.causal-relation").get_text() == "enables"
    assert "The tested protein bound the substrate" in html.get_text()
    assert "Protein activity" in html.select_one("tbody tr").get_text()
    assert "Measured outcome" in html.select_one("tbody tr").get_text()
    assert html.select_one('a[href="https://example.org/study"]')
    assert html.select_one("details:not([open]) summary").get_text() == "Evidence (1)"
    assert "No curated causal graph" in curated_graphs({})


def test_context_specific_opposite_edges_and_html_anchors(corpus, overlay):
    from dufmech.site import curated_graphs

    first = overlay["causal_graphs"][0]
    first.update(graph_id="a-b", context="Medium one", scope_status="PHENOTYPIC")
    first["edges"][0].update(edge_id="c", predicate="decreases", directness="INDIRECT")
    second = copy.deepcopy(first)
    second.update(graph_id="a", context="Medium two")
    second["edges"][0].update(edge_id="b-c", predicate="increases")
    overlay["causal_graphs"].append(second)
    validate_record(overlay, corpus, target="FamilyCuration")
    html = BeautifulSoup(curated_graphs(overlay), "html.parser")
    ids = [tag["id"] for tag in html.select("[id]")]
    assert len(ids) == len(set(ids))
    assert html.find(id="causal-edge.a-b.c")
    assert html.find(id="causal-edge.a.b-c")
    assert len(html.select("tbody tr")) == 2
    assert "Medium one" in html.get_text() and "Medium two" in html.get_text()
