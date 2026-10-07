"""Keep native agent entry points and fleet review dependencies available."""

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("relative", [
    ".claude/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/curate-yaml-record/references/review-checklist.md",
    ".agents/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/review-open-issues/SKILL.md",
    ".agents/skills/review-open-issues/SKILL.md",
])
def test_native_curation_skill_dependency_is_retained(relative):
    path = ROOT / relative
    assert path.is_file(), f"Missing fleet review dependency: {relative}"
    assert path.read_text(encoding="utf-8").strip(), f"Empty review dependency: {relative}"


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
