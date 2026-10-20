"""Keep native agent entry points and fleet review dependencies available."""

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("relative", [
    ".claude/skills/add-record/SKILL.md",
    ".agents/skills/add-record/SKILL.md",
    ".claude/skills/curate-causal-graphs/SKILL.md",
    ".agents/skills/curate-causal-graphs/SKILL.md",
    ".claude/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/curate-yaml-record/references/review-checklist.md",
    ".agents/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/dufmech-evolve-workflow/SKILL.md",
    ".agents/skills/dufmech-evolve-workflow/SKILL.md",
    ".claude/skills/ground-causal-graph-proteins/SKILL.md",
    ".agents/skills/ground-causal-graph-proteins/SKILL.md",
    ".claude/skills/review-open-issues/SKILL.md",
    ".agents/skills/review-open-issues/SKILL.md",
])
def test_native_curation_skill_dependency_is_retained(relative):
    path = ROOT / relative
    assert path.is_file(), f"Missing fleet review dependency: {relative}"
    assert path.read_text(encoding="utf-8").strip(), f"Empty review dependency: {relative}"


def test_add_record_skill_contract_and_router():
    adapter = ROOT / ".claude/skills/add-record/SKILL.md"
    text = adapter.read_text(encoding="utf-8")
    for required in (
        "name: add-record",
        "data/worklists/interpro-pfam-duf-*.json",
        "scripts/migrate_exduf_worklist.py",
        "curation/families/PFxxxxx.yaml",
        "src/dufmech/schema/dufmech.yaml",
        "dufmech.records --apply",
        "dufmech.causal_graphs --apply",
        "dufmech.history check",
    ):
        assert required in text
    router = ROOT / ".agents/skills/add-record/SKILL.md"
    target = "../../../.claude/skills/add-record/SKILL.md"
    assert f"]({target})" in router.read_text(encoding="utf-8")
    assert (router.parent / target).resolve() == adapter


def test_curate_causal_graphs_skill_contract_and_router():
    adapter = ROOT / ".claude/skills/curate-causal-graphs/SKILL.md"
    text = adapter.read_text(encoding="utf-8")
    for required in (
        "name: curate-causal-graphs",
        "curation/families/PF*.yaml",
        "src/dufmech/schema/dufmech.yaml",
        "dufmech.causal_graphs --apply",
        "dufmech.records --check",
        "dufmech.history check",
    ):
        assert required in text
    router = ROOT / ".agents/skills/curate-causal-graphs/SKILL.md"
    target = "../../../.claude/skills/curate-causal-graphs/SKILL.md"
    assert f"]({target})" in router.read_text(encoding="utf-8")
    assert (router.parent / target).resolve() == adapter


def test_issue_triage_skill_is_native_scoped_and_read_only():
    adapter = ROOT / ".claude/skills/review-open-issues/SKILL.md"
    text = adapter.read_text(encoding="utf-8")
    for required in (
        "CultureBotAI/DUFMech", "src/dufmech/schema/dufmech.yaml",
        "data/families/*.yaml", "DUFMECH_ROOT",
        "This is a read-only review. It does not implement fixes, close or edit issues",
    ):
        assert required in text
    router = ROOT / ".agents/skills/review-open-issues/SKILL.md"
    target = "../../../.claude/skills/review-open-issues/SKILL.md"
    assert f"]({target})" in router.read_text(encoding="utf-8")
    assert (router.parent / target).resolve() == adapter


def test_ground_causal_graph_proteins_skill_contract_and_router():
    adapter = ROOT / ".claude/skills/ground-causal-graph-proteins/SKILL.md"
    text = adapter.read_text(encoding="utf-8")
    for required in (
        "name: ground-causal-graph-proteins",
        "curation/families/PF*.yaml",
        "src/dufmech/schema/dufmech.yaml",
        "Do not ground downstream non-protein assay readouts",
        "Do not ground oligonucleotide knockdown reagent nodes",
        "dufmech.records --apply",
        "dufmech.causal_graphs --apply",
        "dufmech.history check",
    ):
        assert required in text
    router = ROOT / ".agents/skills/ground-causal-graph-proteins/SKILL.md"
    target = "../../../.claude/skills/ground-causal-graph-proteins/SKILL.md"
    assert f"]({target})" in router.read_text(encoding="utf-8")
    assert (router.parent / target).resolve() == adapter
