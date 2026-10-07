"""Native tests and an explicit, separate-runtime real OAK regression harness."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _deny_network(event, args):
    if event in {"socket.connect", "socket.getaddrinfo", "socket.sendto", "urllib.Request"}:
        raise RuntimeError(f"network forbidden during offline regression: {event}")


def oak_regression(root: Path) -> dict:
    """Run under CLAW only: no DUF/LinkML imports and no substituted OAK adapter."""
    sys.addaudithook(_deny_network)
    from importlib.metadata import version

    from oaklib import get_adapter

    root = root.resolve()
    provenance = json.loads((root / "conf/id_labels/provenance.json").read_text())
    raw = (root / provenance["source_path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == provenance["source"]["sha256"]
    rows = json.loads(raw)
    expected = {"Pfam:" + row["pfam_id"]: row["name"] for row in rows}
    assert expected and len(expected) == len(rows) == provenance["index"]["entities"]
    index = root / "conf/id_labels/pfam.obo"
    assert hashlib.sha256(index.read_bytes()).hexdigest() == provenance["index"]["sha256"]
    adapter = get_adapter("simpleobo:" + str(index))
    assert set(adapter.entities()) == set(expected)
    assert all(adapter.label(curie) == label for curie, label in expected.items())

    with tempfile.TemporaryDirectory(prefix="duf-oak-regression-") as temporary:
        copy = Path(temporary)
        shutil.copytree(root / "data/families", copy / "data/families")
        shutil.copytree(root / "conf/id_labels", copy / "conf/id_labels")
        (copy / "scripts").mkdir()
        for filename in ("validate_id_label_correspondence.py", "chem_formula.py"):
            shutil.copyfile(root / "scripts" / filename, copy / "scripts" / filename)
        shutil.copyfile(root / "conf/id_label_targets.yaml", copy / "conf/id_label_targets.yaml")
        results = {}

        def run(name, code, verdicts):
            command = [sys.executable, "-I", "-B", str(Path(__file__).resolve()),
                       "--validator", str(copy / "scripts/validate_id_label_correspondence.py"),
                       "--config", str(copy / "conf/id_label_targets.yaml")]
            done = subprocess.run(command, cwd=copy, capture_output=True, text=True, timeout=180,
                                  check=False)
            counts = {key: int(value) for key, value in re.findall(
                r"^\s+([A-Z_]+): (\d+)\s*$", done.stdout, re.MULTILINE)}
            assert "OFFLINE_AUDIT_ACTIVE" in done.stderr, done.stderr
            assert done.returncode == code and counts == verdicts, (
                name, done.returncode, done.stdout, done.stderr)
            results[name] = {"exit_code": code, "verdicts": counts}

        run("full-corpus", 0, {"OK_CANONICAL": len(expected)})
        shutil.rmtree(copy / "data/families")
        (copy / "data/families").mkdir()
        record = copy / "data/families/negative.yaml"
        curie, label = next(iter(expected.items()))
        for name, value, verdict in (
            ("mismatch", {"id": curie, "name": "intentionally wrong label"}, "MISMATCH"),
            ("missing-id", {"id": "Pfam:PF00000", "name": label}, "ID_NOT_FOUND"),
            ("empty-label", {"id": curie, "name": ""}, "EMPTY_LABEL"),
            ("missing-label", {"id": curie}, "EMPTY_LABEL"),
            ("unknown-prefix", {"id": "NotPfam:PF00000", "name": label}, "UNKNOWN_PREFIX"),
        ):
            record.write_text(json.dumps(value))
            run(name, 2, {verdict: 1})
        record.unlink()
        run("missing-target", 2, {"MISSING_GLOB": 1})
        record.write_text(json.dumps({"id": curie, "name": label}))
        (copy / "conf/id_labels/pfam.obo").write_text("format-version: 1.2\n\n")
        # Document the shared skip; native preflight must reject this reference.
        run("empty-adapter-is-not-adoption", 0, {"SKIPPED_EMPTY_ADAPTER": 1})
    assert not any(name == "dufmech" or name.startswith("dufmech.") for name in sys.modules)
    return {"status": "PASS", "oaklib_version": version("oaklib"),
            "adapter": "simpleobo:conf/id_labels/pfam.obo", "checked_pairs": len(expected),
            "source_sha256": provenance["source"]["sha256"],
            "index_sha256": provenance["index"]["sha256"],
            "network_denied": True, "native_duf_imported": False, "cases": results}


if __name__ != "__main__":
    import pytest

    from dufmech import id_labels
    from dufmech.snapshot import write_worklist_snapshot
    from dufmech.worklist import DufFamilyRow
    from tests.test_report import worklist_row

    @pytest.fixture
    def corpus(tmp_path):
        row = worklist_row("PF00001", proteins=10)
        row["interpro_id"] = "IPR000001"
        del row["source_url"]
        write_worklist_snapshot([DufFamilyRow(**row)], tmp_path / "data/worklists",
                                snapshot_date="2026-10-01")
        (tmp_path / "data/families").mkdir()
        (tmp_path / "data/families/PF00001.yaml").write_text(json.dumps(
            {"id": "Pfam:PF00001", "name": row["name"]}))
        (tmp_path / "conf").mkdir()
        (tmp_path / id_labels.CONFIG_PATH).write_text(json.dumps(id_labels.CONFIG))
        (tmp_path / "scripts").mkdir()
        for filename in ("validate_id_label_correspondence.py", "chem_formula.py"):
            shutil.copyfile(id_labels.REPO_ROOT / "scripts" / filename,
                            tmp_path / "scripts" / filename)
        id_labels.write_index(tmp_path)
        return tmp_path

    def files(root):
        return {str(path.relative_to(root)): path.read_bytes()
                for path in root.rglob("*") if path.is_file()}

    def test_native_reproduction_no_oak_no_scientific_writes(corpus, monkeypatch):
        monkeypatch.setitem(sys.modules, "oaklib", None)
        before = files(corpus)
        assert id_labels.write_index(corpus) == []
        artifacts = id_labels.build_artifacts(corpus)
        assert artifacts[id_labels.INDEX].endswith(b"\n")
        assert not artifacts[id_labels.INDEX].endswith(b"\n\n")
        assert all((corpus / path).read_bytes() == raw for path, raw in artifacts.items())
        receipt = id_labels.check_index(corpus)
        assert receipt["status"] == "REFERENCE_VERIFIED" and receipt["expected_pairs"] == 1
        assert files(corpus) == before
        record = corpus / "data/families/PF00001.yaml"
        record.write_text('{"id":"Pfam:PF00001","name":"wrong curated label"}')
        assert id_labels.build_artifacts(corpus) == artifacts

    @pytest.mark.parametrize("name", [id_labels.INDEX, id_labels.PROVENANCE])
    def test_changed_or_empty_reference_rejected(corpus, name):
        (corpus / name).write_bytes(b"")
        with pytest.raises(id_labels.IdLabelError, match="stale or missing"):
            id_labels.check_index(corpus)
        assert id_labels.write_index(corpus) == [name]
        assert id_labels.check_index(corpus)["expected_pairs"] == 1

    @pytest.mark.parametrize("suffix", [".json", ".tsv", ".manifest.json"])
    def test_unverified_frozen_source_rejected(corpus, suffix):
        path = corpus / ("data/worklists/interpro-pfam-duf-2026-10-01" + suffix)
        path.write_bytes(path.read_bytes() + b"tampered")
        with pytest.raises((ValueError, RuntimeError)):
            id_labels.build_artifacts(corpus)

    @pytest.mark.parametrize("mutation", ["missing", "extra", "wrong-id", "duplicate-key"])
    def test_record_inventory_and_identity(corpus, mutation):
        record = corpus / "data/families/PF00001.yaml"
        if mutation == "missing":
            record.unlink()
        elif mutation == "extra":
            (record.parent / "PF00002.yaml").write_bytes(record.read_bytes())
        elif mutation == "wrong-id":
            record.write_text('{"id":"Pfam:PF00002","name":"x"}')
        else:
            record.write_text("id: Pfam:PF00001\nid: Pfam:PF00002\nname: x\n")
        with pytest.raises((ValueError, RuntimeError)):
            id_labels.check_index(corpus)

    @pytest.mark.parametrize("mutation", ["ignored", "optional", "warn", "synonym", "remote"])
    def test_weakened_config_rejected(corpus, mutation):
        path = corpus / id_labels.CONFIG_PATH
        config = json.loads(path.read_text())
        if mutation == "ignored":
            config["ignored_prefixes"] = ["Pfam"]
        elif mutation == "remote":
            config["adapters"]["Pfam"] = "sqlite:obo:go"
        else:
            key, value = {"optional": ("required", False), "warn": ("severity", "warn"),
                          "synonym": ("policy", "canonical_or_synonym")}[mutation]
            config["targets"][0][key] = value
        path.write_text(json.dumps(config))
        with pytest.raises(id_labels.IdLabelError, match="configuration"):
            id_labels.check_index(corpus)

    @pytest.mark.parametrize("relative", [id_labels.INDEX, id_labels.CONFIG_PATH,
                                          "data/families/PF00001.yaml"])
    def test_symlink_refused(corpus, relative):
        path = corpus / relative
        other = corpus / "other"
        path.rename(other)
        path.symlink_to(other)
        with pytest.raises((ValueError, RuntimeError), match="symlink"):
            id_labels.check_index(corpus)

    @pytest.mark.parametrize("label", ["", " label ", "injected\n[Term]", "x\\n", "x!y", "x{y}"])
    def test_unrepresentable_source_label_refused(corpus, label):
        row = worklist_row("PF00001", proteins=10)
        del row["source_url"]
        row["name"] = label
        write_worklist_snapshot([DufFamilyRow(**row)], corpus / "data/worklists",
                                snapshot_date="2026-10-02")
        with pytest.raises((ValueError, RuntimeError)):
            id_labels.build_artifacts(corpus)

    def test_empty_source_refused(corpus):
        write_worklist_snapshot([], corpus / "data/worklists", snapshot_date="2026-10-02")
        with pytest.raises(id_labels.IdLabelError, match="at least one"):
            id_labels.build_artifacts(corpus)

    @pytest.mark.parametrize("code,stdout,passes", [
        (0, "  OK_CANONICAL: 1\n", True),
        (0, "  SKIPPED_EMPTY_ADAPTER: 1\n", False),
        (0, "", False), (0, "  OK_CANONICAL: 0\n", False),
        (0, "  OK_CANONICAL: 2\n", False),
        (0, "  OK_SYNONYM: 1\n", False), (2, "  MISMATCH: 1\n", False),
    ])
    def test_isolated_runtime_command_and_nonvacuous_gate(corpus, monkeypatch, code, stdout, passes):
        runtime = corpus / "runtime"
        runtime.mkdir()
        for name in ("pyproject.toml", "uv.lock"):
            (runtime / name).write_text("test runtime contract")
        for name in ("VIRTUAL_ENV", "UV_PROJECT_ENVIRONMENT", "PYTHONPATH", "PYTHONHOME"):
            monkeypatch.setenv(name, "/bad/inherited/native/environment")

        def run(command, **kwargs):
            assert command[:7] == ["uv", "run", "--project", str(runtime), "--locked",
                                   "--offline", "python"]
            assert command[7:9] == ["-I", "-B"]
            assert command[9:] == [str(corpus / id_labels.VALIDATOR),
                                   "-c", str(corpus / id_labels.CONFIG_PATH)]
            assert kwargs["cwd"] == corpus and "--report" not in command
            assert not {"VIRTUAL_ENV", "UV_PROJECT_ENVIRONMENT", "PYTHONPATH", "PYTHONHOME"} & set(
                kwargs["env"])
            return subprocess.CompletedProcess(command, code, stdout, "")

        monkeypatch.setattr(id_labels.subprocess, "run", run)
        if passes:
            assert id_labels.check(corpus, runtime)["checked_pairs"] == 1
        else:
            with pytest.raises(id_labels.IdLabelError, match="failed or skipped"):
                id_labels.check(corpus, runtime)

    def test_concurrent_record_change_rejected(corpus, monkeypatch):
        runtime = corpus / "runtime"
        runtime.mkdir()
        for name in ("pyproject.toml", "uv.lock"):
            (runtime / name).write_text("test runtime contract")

        def run(command, **kwargs):
            path = corpus / "data/families/PF00001.yaml"
            path.write_bytes(path.read_bytes() + b"\n")
            return subprocess.CompletedProcess(command, 0, "  OK_CANONICAL: 1\n", "")

        monkeypatch.setattr(id_labels.subprocess, "run", run)
        with pytest.raises(id_labels.IdLabelError, match="inputs changed"):
            id_labels.check(corpus, runtime)

    def test_cli_cannot_claim_oak_without_runtime(corpus, monkeypatch, capsys):
        monkeypatch.delenv("CLAW_ROOT", raising=False)
        assert id_labels.main(["--repo-root", str(corpus)]) == 1
        assert "--claw-root" in capsys.readouterr().err
        assert id_labels.main(["--repo-root", str(corpus), "--check-index"]) == 0
        assert json.loads(capsys.readouterr().out)["status"] == "REFERENCE_VERIFIED"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--oak-regression", action="store_true")
    mode.add_argument("--validator", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--config", type=Path)
    args = parser.parse_args()
    if args.validator:
        sys.addaudithook(_deny_network)
        print("OFFLINE_AUDIT_ACTIVE", file=sys.stderr)
        sys.argv = [str(args.validator), "-c", str(args.config)]
        runpy.run_path(str(args.validator), run_name="__main__")
    else:
        print(json.dumps(oak_regression(args.repo_root), indent=2, sort_keys=True))
