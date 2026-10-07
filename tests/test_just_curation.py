"""Exercise the actual curation recipes across their shell argument boundary."""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
JUST = shutil.which("just")
UV = shutil.which("uv")


@pytest.mark.skipif(JUST is None, reason="just is installed by the full QC workflow")
@pytest.mark.parametrize(("recipe", "module_args"), [
    ("review", ["dufmech.reviews"]),
    ("history", ["dufmech.history"]),
    ("new-history", ["dufmech.history", "new"]),
    ("knowledge-gap-scan", ["dufmech.knowledge_gaps"]),
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
