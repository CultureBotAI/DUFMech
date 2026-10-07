from __future__ import annotations

import gzip
import json
from pathlib import Path

import httpx
import pytest

from dufmech.pfam_history import (
    PfamHistoryError,
    is_unknown_name,
    parse_seed_headers,
    previous_name_index,
    read_seed,
)
from dufmech.pfam_history_snapshot import main, write_pfam_previous_names_snapshot
from dufmech.provenance import check_manifest

SEED = """\
# STOCKHOLM 1.0
#=GF ID   Abi_alpha
#=GF AC   PF14337.11
#=GF DE   Abortive infection alpha
#=GF PI   DUF4393;
#=GS seq/1-10 AC A0A000
seq/1-10  MKLV
//
# STOCKHOLM 1.0
#=GF ID   2-Hacid_dh
#=GF AC   PF00389.37
#=GF DE   D-isomer specific 2-hydroxyacid dehydrogenase, catalytic domain
#=GF PI   2-Hacid_DH;
//
# STOCKHOLM 1.0
#=GF ID   DUF3458_C
#=GF AC   PF17432.5
#=GF DE   Domain of unknown function (DUF3458_C)
#=GF PI   DUF1285_N; Old_name;
#=GF PI   UPF0265;
//
"""


def _gz(text: str, *, members: int = 1) -> bytes:
    # Pfam ships concatenated gzip members; split the text to exercise that path.
    parts = text.split("//\n")
    size = max(1, len(parts) // members)
    chunks = ["//\n".join(parts[i : i + size]) + ("//\n" if i + size < len(parts) else "")
              for i in range(0, len(parts), size)]
    return b"".join(gzip.compress(chunk.encode()) for chunk in chunks)


def test_unknown_name_matches_bare_and_compound_names() -> None:
    for name in ("DUF4393", "UPF0265", "DUF1285_N", "QueG_DUF1730", "DUF488-N3i"):
        assert is_unknown_name(name)
    for name in ("2-Hacid_DH", "Abi_alpha", "DUFFY", "PF14337"):
        assert not is_unknown_name(name)


def test_parse_seed_keeps_only_families_with_unknown_previous_names() -> None:
    rows, scanned, with_previous = parse_seed_headers(SEED.splitlines())

    assert (scanned, with_previous) == (3, 3)
    assert [row.pfam_id for row in rows] == ["PF14337", "PF17432"]
    abi, duf = rows
    assert abi.short_name == "Abi_alpha"
    assert abi.pfam_version == "PF14337.11"
    assert abi.previous_unknown_names == ("DUF4393",)
    assert abi.currently_unknown_name is False
    # PI can span several lines; every identifier is kept, unknown names flagged.
    assert duf.previous_ids == ("DUF1285_N", "Old_name", "UPF0265")
    assert duf.previous_unknown_names == ("DUF1285_N", "UPF0265")
    assert duf.currently_unknown_name is True


def test_parse_seed_rejects_truncated_family() -> None:
    with pytest.raises(PfamHistoryError, match="ended inside a family"):
        parse_seed_headers(["#=GF ID   X", "#=GF AC   PF00001.1"])


def test_read_seed_handles_multimember_gzip_and_records_bytes(tmp_path: Path) -> None:
    data = _gz(SEED, members=3)
    path = tmp_path / "Pfam-A.seed.gz"
    path.write_bytes(data)

    read = read_seed(seed_gz=path)

    assert [row.pfam_id for row in read.rows] == ["PF14337", "PF17432"]
    assert read.families_scanned == 3
    assert read.compressed_bytes == len(data)


def test_read_seed_rejects_truncated_gzip(tmp_path: Path) -> None:
    path = tmp_path / "Pfam-A.seed.gz"
    path.write_bytes(_gz(SEED)[:-20])
    with pytest.raises(PfamHistoryError, match="truncated"):
        read_seed(seed_gz=path)


def test_read_seed_download_checks_length_and_records_headers() -> None:
    data = _gz(SEED)

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/Pfam38.2/Pfam-A.seed.gz")
        return httpx.Response(
            200,
            stream=httpx.ByteStream(data),
            headers={
                "Last-Modified": "Thu, 22 Jan 2026 16:03:00 GMT",
                "Content-Length": str(len(data)),
            },
        )

    read = read_seed(transport=httpx.MockTransport(handler))
    assert read.last_modified == "Thu, 22 Jan 2026 16:03:00 GMT"
    assert len(read.rows) == 2

    def short(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, stream=httpx.ByteStream(data), headers={"Content-Length": str(len(data) + 5)}
        )

    with pytest.raises(PfamHistoryError):
        read_seed(transport=httpx.MockTransport(short))


def test_snapshot_is_exclusive_and_manifest_validates(tmp_path: Path) -> None:
    path = tmp_path / "Pfam-A.seed.gz"
    path.write_bytes(_gz(SEED))
    out = tmp_path / "worklists"

    assert main(["--seed-gz", str(path), "--out-dir", str(out), "--snapshot-date", "2026-10-07"]) == 0
    manifest_path = out / "pfam-previous-unknown-names-2026-10-07.manifest.json"
    assert check_manifest(manifest_path) == []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["rows"] == {
        "total": 2,
        "unique_previous_unknown_names": 3,
        "currently_unknown_name": 1,
        "renamed_away_from_unknown": 1,
    }
    assert manifest["source"]["release"] == "38.2"
    rows = json.loads((out / "pfam-previous-unknown-names-2026-10-07.json").read_text("utf-8"))
    assert previous_name_index(rows)["DUF4393"][0]["short_name"] == "Abi_alpha"

    with pytest.raises(FileExistsError):
        write_pfam_previous_names_snapshot(
            read_seed(seed_gz=path), out, release="38.2", source_url="x",
            snapshot_date="2026-10-07",
        )


def test_report_resolves_unlisted_names_through_previous_ids() -> None:
    from dufmech.cross_mech_report import _renamed_section

    curated = [
        {"pfam_id": "", "short_name": "DUF4393", "source_mech": "TraitMech"},
        {"pfam_id": "", "short_name": "UPF0265", "source_mech": "CellStructureMech"},
    ]
    previous = [{
        "pfam_id": "PF14337", "short_name": "Abi_alpha", "description": "Abortive infection alpha",
        "previous_unknown_names": ["DUF4393"],
    }]
    lines = _renamed_section(curated, ["DUF4393", "UPF0265"], previous, "pfam-previous-x")

    assert "| DUF4393 | TraitMech | PF14337 Abi_alpha | Abortive infection alpha | no |" in lines
    marked = _renamed_section(
        curated, ["DUF4393"], previous, "pfam-previous-x", frozenset({"PF14337"})
    )
    assert marked[-1].endswith("| yes |")
    assert any("UPF0265" in line and "UniProt UPF nomenclature" in line for line in lines)
    assert _renamed_section(curated, ["DUF4393"], None, "") == []
