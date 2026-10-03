from __future__ import annotations

from dufmech.docs import (
    BEGIN,
    END,
    render_current_corpus_block,
    replace_current_corpus_block,
)
from dufmech.report import build_report
from tests.test_report import worklist_row


def test_render_current_corpus_block_includes_generated_summary() -> None:
    block = render_current_corpus_block(
        build_report(
            [
                worklist_row("PF00001", proteins=10),
                worklist_row("PF00002", proteins=20),
            ]
        ),
        input_ids={"worklist": "interpro-pfam-duf-2026-10-01"},
    )

    assert block.startswith(BEGIN)
    assert block.endswith(END)
    assert "**2 DUF/Pfam families**" in block
    assert "`worklist=interpro-pfam-duf-2026-10-01`" in block
    assert "| `short_name_matches_duf` | 2 |" in block


def test_replace_current_corpus_block_replaces_only_generated_block() -> None:
    readme = f"# Title\n\n{BEGIN}\nstale\n{END}\n\n## Next\n"

    assert replace_current_corpus_block(readme, "fresh") == (
        "# Title\n\nfresh\n\n## Next\n"
    )
