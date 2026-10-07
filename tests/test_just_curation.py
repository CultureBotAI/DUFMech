"""Exercise the actual curation recipes across their shell argument boundary."""

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from tests.test_exports import inventory, make_corpus

ROOT = Path(__file__).resolve().parents[1]
JUST = shutil.which("just")
UV = shutil.which("uv")


@pytest.mark.skipif(JUST is None, reason="just is installed by the full QC workflow")
@pytest.mark.parametrize(("recipe", "module_args"), [
    ("review", ["dufmech.reviews"]),
    ("history", ["dufmech.history"]),
    ("new-history", ["dufmech.history", "new"]),
    ("knowledge-gap-scan", ["dufmech.knowledge_gaps"]),
    ("research", ["dufmech.research"]),
    ("exports", ["dufmech.exports"]),
    ("id-labels", ["dufmech.id_labels"]),
])
@pytest.mark.parametrize("with_prose", [False, True], ids=["no-args", "quoted-prose"])
def test_curation_recipe_preserves_argument_boundaries(tmp_path, recipe, module_args, with_prose):
    capture = tmp_path / "argv.bin"
    sentinel = tmp_path / "SHELL_COMMAND_RAN"
    commands = tmp_path / "bin"
    commands.mkdir()
    claw = tmp_path / "claw with spaces" / "src"
    (claw / "kg_microbe_kgscan").mkdir(parents=True)
    uv = commands / "uv"
    uv.write_text("#!/bin/sh\nprintf '%s\\0' \"$@\" > \"$DUFMECH_ARGV_CAPTURE\"\n")
    uv.chmod(0o755)
    args = [
        "--summary", "Added a protein-scoped assertion.",
        "--details", f"Literal $(touch {sentinel}); 'single' \"double\"\nsecond line $HOME",
        "--content", "a directory/completed review.json", "", "*.yaml",
    ] if with_prose else []
    env = dict(os.environ, PATH=str(commands) + os.pathsep + os.environ.get("PATH", ""),
               DUFMECH_ARGV_CAPTURE=str(capture), CLAW_SRC=str(claw))
    subprocess.run(
        [JUST, "--no-dotenv", "--justfile", str(ROOT / "justfile"), recipe, *args],
        cwd=tmp_path, env=env, check=True, capture_output=True, text=True,
    )
    actual = capture.read_bytes().split(b"\0")
    assert actual[-1] == b""
    assert [item.decode() for item in actual[:-1]] == [
        "run", "--locked", "python", "-m", *module_args, *args,
    ]
    assert not sentinel.exists(), "recipe evaluated a literal argument as shell code"


@pytest.mark.skipif(UV is None, reason="uv is installed by the full QC workflow")
def test_source_pin_cli_uses_locked_project_environment(tmp_path):
    env = dict(os.environ, UV_OFFLINE="1", UV_NO_SYNC="1", PYTHONDONTWRITEBYTECODE="1",
               UV_CACHE_DIR=str(tmp_path / "uv-cache"))
    env.pop("PYTHONPATH", None)
    env.pop("VIRTUAL_ENV", None)
    result = subprocess.run(
        [UV, "run", "--locked", "python", "-m", "dufmech.site_sources", "--help"],
        cwd=ROOT, env=env, check=False, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "capture" in result.stdout


def offline_environment(tmp_path):
    env = dict(os.environ, UV_OFFLINE="1", UV_NO_SYNC="1", PYTHONDONTWRITEBYTECODE="1",
               UV_CACHE_DIR=str(tmp_path / "uv-cache"))
    env.pop("VIRTUAL_ENV", None)
    env.pop("UV_PROJECT_ENVIRONMENT", None)
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    return env


@pytest.mark.skipif(JUST is None or UV is None, reason="just and uv are full QC prerequisites")
def test_research_recipe_real_dummy_scaffold_preserves_literal_question(tmp_path):
    sentinel = tmp_path / "SHELL_COMMAND_RAN"
    question = f"Literal $(touch {sentinel}); 'single' \"double\"\n$HOME *.yaml"
    root = tmp_path / "input with spaces"
    (root / "conf").mkdir(parents=True)
    (root / "data/families").mkdir(parents=True)
    for name in ("conf/deep_research_provider.yaml", "data/families/PF04149.yaml"):
        shutil.copyfile(ROOT / name, root / name)
    before = inventory(root)
    result = subprocess.run(
        [JUST, "--no-dotenv", "--justfile", str(ROOT / "justfile"), "research",
         "scaffold-result", "--root", str(root), "--simulate", "--pfam-id", "PF04149",
         "--question", question],
        cwd=ROOT, env=offline_environment(tmp_path), capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    payload = json.loads(result.stdout)
    assert payload["status"] == "DRY_RUN"
    assert payload["plan"]["question"]["text"].endswith(question)
    assert inventory(root) == before
    assert not sentinel.exists()


@pytest.mark.skipif(JUST is None or UV is None, reason="just and uv are full QC prerequisites")
def test_exports_recipe_real_dry_run_and_failed_check_do_not_apply(tmp_path):
    sentinel = tmp_path / "SHELL_COMMAND_RAN"
    root = make_corpus(tmp_path / "literal ; $(touch SHELL_COMMAND_RAN) ' corpus")
    before = inventory(root)
    command = [JUST, "--no-dotenv", "--justfile", str(ROOT / "justfile"),
               "exports", "--root", str(root)]
    for args, code in (([], 0), (["--check"], 1)):
        result = subprocess.run(command + args, cwd=tmp_path, env=offline_environment(tmp_path),
                                capture_output=True, text=True, check=False)
        assert result.returncode == code, result.stderr + result.stdout
        assert inventory(root) == before
        assert not sentinel.exists()
        assert not (ROOT / "SHELL_COMMAND_RAN").exists()


@pytest.mark.skipif(JUST is None, reason="just is installed by the full QC workflow")
def test_full_qc_recipe_rejects_missing_claw_root_before_running_uv(tmp_path):
    env = offline_environment(tmp_path)
    env.pop("CLAW_ROOT", None)
    claw = tmp_path / "src"
    (claw / "kg_microbe_kgscan").mkdir(parents=True)
    env["CLAW_SRC"] = str(claw)
    result = subprocess.run([JUST, "--no-dotenv", "--justfile", str(ROOT / "justfile"), "qc"],
                            cwd=tmp_path, env=env, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert "Set CLAW_ROOT" in result.stderr
    assert "=== qc:" not in result.stdout


@pytest.mark.skipif(JUST is None, reason="just is installed by the full QC workflow")
@pytest.mark.parametrize("mode", ["sync", "regression"])
def test_ci_oak_runtime_commands_strip_native_environment_and_quote_paths(tmp_path, mode):
    workflow = yaml.safe_load((ROOT / ".github/workflows/validate.yaml").read_text())
    job = workflow["jobs"]["qc"]
    steps = job["steps"]
    checkout = next(step for step in steps
                    if step.get("with", {}).get("repository") == "CultureBotAI/culturebotai-claw")
    assert re.fullmatch(r"[0-9a-f]{40}", checkout["with"]["ref"])
    assert job["env"]["CLAW_ROOT"] == "${{ github.workspace }}/.claw"
    sync = next(step for step in steps if step["name"] == "Install separate locked OAK runtime")
    qc = next(step for step in steps if step["name"] == "Run offline quality checks")
    regression = next(step for step in steps
                      if step["name"] == "Exercise real offline OAK rejection cases")
    assert steps.index(sync) < steps.index(qc) < steps.index(regression)
    assert qc["run"] == "just qc"
    claw = tmp_path / "claw ; $(touch SHELL_COMMAND_RAN) ' checkout"
    claw.mkdir()
    for name in ("pyproject.toml", "uv.lock"):
        (claw / name).touch()
    commands = tmp_path / "bin"
    commands.mkdir()
    capture = tmp_path / "argv.bin"
    uv = commands / "uv"
    uv.write_text(
        "#!/bin/sh\n"
        "test -z \"${VIRTUAL_ENV+x}${UV_PROJECT_ENVIRONMENT+x}${PYTHONPATH+x}${PYTHONHOME+x}\" "
        "|| exit 91\n"
        "printf '%s\\0' \"$@\" > \"$DUFMECH_ARGV_CAPTURE\"\n"
    )
    uv.chmod(0o755)
    env = dict(os.environ, PATH=str(commands) + os.pathsep + os.environ.get("PATH", ""),
               CLAW_ROOT=str(claw), DUFMECH_ARGV_CAPTURE=str(capture), VIRTUAL_ENV="native",
               UV_PROJECT_ENVIRONMENT="native", PYTHONPATH="native", PYTHONHOME="native")
    selected = sync if mode == "sync" else regression
    done = subprocess.run(["sh", "-eu", "-c", selected["run"]], cwd=ROOT, env=env,
                          capture_output=True, text=True, check=False)
    assert done.returncode == 0, done.stderr
    actual = [part.decode() for part in capture.read_bytes().split(b"\0")[:-1]]
    expected = ["sync", "--project", str(claw), "--locked"] if mode == "sync" else [
        "run", "--project", str(claw), "--locked", "--offline", "python", "-I", "-B",
        str(ROOT / "tests/test_id_labels.py"), "--oak-regression", "--repo-root", str(ROOT),
    ]
    assert actual == expected
    assert not (ROOT / "SHELL_COMMAND_RAN").exists()
