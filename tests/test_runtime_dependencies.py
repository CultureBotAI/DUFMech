"""Dependency relocks must preserve the supported interpreter's import paths."""

import subprocess
import sys


def test_shex_dependencies_import_without_network():
    program = (
        "from unittest.mock import patch\n"
        "with patch('socket.socket.connect', side_effect=RuntimeError('network forbidden')), "
        "patch('socket.create_connection', side_effect=RuntimeError('network forbidden')):\n"
        "    from pyshex import ShExEvaluator\n"
        "    assert callable(ShExEvaluator)\n"
    )
    subprocess.run(
        [sys.executable, "-B", "-c", program],
        check=True, capture_output=True, text=True, timeout=90,
    )
