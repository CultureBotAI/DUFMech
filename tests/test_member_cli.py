from __future__ import annotations

import json
from pathlib import Path

import pytest

from dufmech.member_cli import load_seed_pfam_ids


def test_load_seed_pfam_ids_preserves_first_seen_order() -> None:
    assert load_seed_pfam_ids(
        [
            {"pfam_id": "PF01579"},
            {"pfam_id": "PF01519"},
            {"pfam_id": "PF01579"},
            {"pfam_id": None},
            {},
        ]
    ) == ["PF01579", "PF01519"]


def test_load_seed_pfam_ids_rejects_non_list_payload() -> None:
    with pytest.raises(TypeError, match="expected a frozen InterPro/Pfam"):
        load_seed_pfam_ids({"results": [{"pfam_id": "PF01519"}]})


def test_committed_worklist_snapshot_loads_seed_pfam_ids() -> None:
    payload = json.loads(
        Path("data/worklists/interpro-pfam-duf-2026-10-01.json").read_text(
            encoding="utf-8"
        )
    )

    pfam_ids = load_seed_pfam_ids(payload)

    assert len(pfam_ids) == 6532
    assert pfam_ids[0] == "PF04149"
