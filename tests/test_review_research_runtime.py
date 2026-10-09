"""The actual review helper and selected research runtime must share loader ownership."""

import importlib
import threading
from concurrent.futures import ThreadPoolExecutor

import pytest
import yaml
from kg_microbe_research import records as research

from dufmech.structured_reviews import common


@pytest.mark.parametrize("first_contract", ["review", "research"])
def test_native_review_and_research_loader_overlap_and_restoration(monkeypatch, first_contract):
    contract = common()
    loader = importlib.import_module("linkml_runtime.loaders.yaml_loader")
    assert contract._LINKML_LOADER_LOCK is research._LINKML_LOADER_LOCK, (
        "The selected research runtime has an incompatible private LinkML loader lock"
    )
    assert contract._LINKML_LOADER_LOCK is loader._claw_linkml_loader_lock

    class DamagedLoader(yaml.SafeLoader):
        def get_single_data(self):
            raise RuntimeError("the foreign global loader leaked into a contract operation")

    monkeypatch.setattr(loader, "DupCheckYamlLoader", DamagedLoader)
    first, second = ((contract, research) if first_contract == "review"
                     else (research, contract))
    attempting, entered, first_exited = (threading.Event() for _ in range(3))

    def overlapping_operation():
        attempting.set()
        with second._pure_linkml_loader():
            entered.set()
            assert first_exited.wait(5)
            return yaml.load("value: 1\n", Loader=loader.DupCheckYamlLoader)

    with ThreadPoolExecutor(max_workers=1) as executor:
        try:
            with first._pure_linkml_loader():
                future = executor.submit(overlapping_operation)
                assert attempting.wait(5)
                assert not entered.wait(0.1), "overlapping loader context entered before release"
        finally:
            first_exited.set()
        assert future.result(timeout=5) == {"value": 1}
    assert entered.is_set()
    assert loader.DupCheckYamlLoader is DamagedLoader
