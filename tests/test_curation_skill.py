"""Keep the native helper files consumed by fleet review adapters available."""

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("relative", [
    ".claude/skills/curate-yaml-record/SKILL.md",
    ".claude/skills/curate-yaml-record/references/review-checklist.md",
    ".agents/skills/curate-yaml-record/SKILL.md",
])
def test_native_curation_skill_dependency_is_retained(relative):
    path = ROOT / relative
    assert path.is_file(), f"Missing fleet review dependency: {relative}"
    assert path.read_text(encoding="utf-8").strip(), f"Empty review dependency: {relative}"
