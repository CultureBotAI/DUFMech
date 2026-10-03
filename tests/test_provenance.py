from __future__ import annotations

import hashlib
import json

from dufmech.provenance import check_manifest, check_worklist_manifests


def write_manifest(tmp_path, *, bytes_: int, sha256: str) -> None:
    (tmp_path / "snapshot.manifest.json").write_text(
        json.dumps(
            {
                "snapshot": {"id": "snapshot"},
                "files": {
                    "json": {
                        "path": "snapshot.json",
                        "bytes": bytes_,
                        "sha256": sha256,
                    }
                },
            }
        ),
        encoding="utf-8",
    )


def test_check_manifest_accepts_matching_files(tmp_path) -> None:
    data = b"[]\n"
    (tmp_path / "snapshot.json").write_bytes(data)
    write_manifest(
        tmp_path,
        bytes_=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
    )

    assert check_manifest(tmp_path / "snapshot.manifest.json") == []
    assert check_worklist_manifests(tmp_path) == []


def test_check_manifest_reports_size_hash_and_missing_files(tmp_path) -> None:
    (tmp_path / "snapshot.json").write_bytes(b"[]\n")
    write_manifest(tmp_path, bytes_=99, sha256="0" * 64)
    (tmp_path / "missing.manifest.json").write_text(
        json.dumps(
            {
                "snapshot": {"id": "missing"},
                "files": {
                    "tsv": {
                        "path": "missing.tsv",
                        "bytes": 0,
                        "sha256": "1" * 64,
                    }
                },
            }
        ),
        encoding="utf-8",
    )

    issues = check_worklist_manifests(tmp_path)

    assert [issue.message for issue in issues] == [
        "files.tsv.path is missing: missing.tsv",
        "files.json.bytes differs for snapshot.json",
        "files.json.sha256 differs for snapshot.json",
    ]
