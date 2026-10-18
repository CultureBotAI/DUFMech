"""Keep native agent entry points and fleet review dependencies available."""

import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("relative", [
    "AGENTS.md",
    ".claude/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/curate-yaml-record/references/review-checklist.md",
    ".agents/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/dufmech-protein-examples/SKILL.md",
    ".agents/skills/dufmech-protein-examples/SKILL.md",
    ".claude/skills/ground-causal-graph-proteins/SKILL.md",
    ".agents/skills/ground-causal-graph-proteins/SKILL.md",
    ".claude/skills/review-open-issues/SKILL.md",
    ".agents/skills/review-open-issues/SKILL.md",
])
def test_native_curation_skill_dependency_is_retained(relative):
    path = ROOT / relative
    assert path.is_file(), f"Missing fleet review dependency: {relative}"
    assert path.read_text(encoding="utf-8").strip(), f"Empty review dependency: {relative}"


def test_agents_md_local_links_resolve():
    agents_md = ROOT / "AGENTS.md"
    text = agents_md.read_text(encoding="utf-8")
    assert "CLAUDE.md" in text
    assert ".agents/skills" in text
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#"):
            continue
        target = (agents_md.parent / link.split("#", 1)[0]).resolve()
        assert target.is_relative_to(ROOT)
        assert target.is_file(), f"Broken link in AGENTS.md: {link}"


def test_every_claude_skill_is_exposed_under_agents_skills():
    claude_skills = sorted((ROOT / ".claude/skills").glob("*/SKILL.md"))
    agents_skills = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
    assert claude_skills
    assert {p.parent.name for p in agents_skills} == {p.parent.name for p in claude_skills}
    for adapter in claude_skills:
        skill_name = adapter.parent.name
        router = ROOT / ".agents/skills" / skill_name / "SKILL.md"
        assert router.is_file(), f"Missing .agents/skills router for {skill_name}"
        text = router.read_text(encoding="utf-8")
        assert text.startswith("---\n")
        end = text[4:].find("\n---")
        assert end != -1
        meta = yaml.safe_load(text[4 : 4 + end + 1])
        assert isinstance(meta, dict)
        assert meta.get("name") == skill_name
        assert isinstance(meta.get("description"), str) and meta["description"].strip()
        target = f"../../../.claude/skills/{skill_name}/SKILL.md"
        assert f"]({target})" in text
        assert (router.parent / target).resolve() == adapter.resolve()


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
