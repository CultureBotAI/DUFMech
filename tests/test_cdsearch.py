from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.cdsearch import (
    CdSearchClient,
    CdSearchClientError,
    collect_cdsearch_rows,
    parse_cdsearch_tsv,
    render_cdsearch_json,
    render_cdsearch_tsv,
)

CDSEARCH_RUNNING_TSV = """#Batch CD-search tool\tNIH/NLM/NCBI
#cdsid\tQM3-qcdsearch-1234-5678
#datatype\thitsStandard Results
#status\t3\tmsg\tJob is still running
"""

CDSEARCH_SUCCESS_TSV = """#Batch CD-search tool\tNIH/NLM/NCBI
#cdsid\tQM3-qcdsearch-1234-5678
#datatype\thitsStandard Results
#status\t0
#Start time\t2026-10-01T02:47:17\tRun time\t0:00:00:00
#status\tsuccess

Query\tHit type\tPSSM-ID\tFrom\tTo\tE-Value\tBitscore\tAccession\tShort name\tIncomplete\tSuperfamily
Q#1 - P68871[hemoglobin subunit beta [Homo sapiens]]\tspecific\t381262\t8\t146\t7.88544e-87\t249.479\tcd08925\tHb-beta-like\t - \tcl21461
Q#1 - P68871[hemoglobin subunit beta [Homo sapiens]]\tsuperfamily\t473869\t8\t146\t7.88544e-87\t249.479\tcl21461\tGlobin-like superfamily\t - \t -
"""


def test_cdsearch_client_submits_and_polls_domain_hits() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        if "queries=P68871%0AB2BDZ3" in str(request.url):
            assert request.url.params["useid1"] == "true"
            assert request.url.params["tdata"] == "hits"
            assert request.url.params["db"] == "cdd"
            assert request.url.params["dmode"] == "all"
            assert request.url.params["qdefl"] == "true"
            return httpx.Response(200, text=CDSEARCH_RUNNING_TSV)

        assert request.url.params["cdsid"] == "QM3-qcdsearch-1234-5678"
        assert request.url.params["dmode"] == "all"
        return httpx.Response(200, text=CDSEARCH_SUCCESS_TSV)

    rows = collect_cdsearch_rows(
        ["P68871", "B2BDZ3", "P68871"],
        CdSearchClient(
            poll_interval=0,
            transport=httpx.MockTransport(handler),
        ),
    )

    assert len(calls) == 2
    assert [row.cdd_accession for row in rows] == ["cd08925", "cl21461"]
    assert rows[0].uniprot_accession == "P68871"
    assert rows[0].query_label == "Q#1 - P68871[hemoglobin subunit beta [Homo sapiens]]"
    assert rows[0].hit_type == "specific"
    assert rows[0].pssm_id == "381262"
    assert rows[0].start == 8
    assert rows[0].end == 146
    assert rows[0].e_value == 7.88544e-87
    assert rows[0].bitscore == 249.479
    assert rows[0].short_name == "Hb-beta-like"
    assert rows[0].incomplete == ""
    assert rows[0].superfamily_accession == "cl21461"
    assert rows[0].source_url.endswith("uid=cd08925")


def test_cdsearch_client_raises_on_http_failure() -> None:
    client = CdSearchClient(
        poll_interval=0,
        transport=httpx.MockTransport(lambda request: httpx.Response(500)),
    )

    try:
        collect_cdsearch_rows(["P68871"], client)
    except CdSearchClientError as exc:
        assert "could not fetch Batch CD-Search" in str(exc)
    else:
        raise AssertionError("expected CdSearchClientError")


def test_cdsearch_client_raises_on_unfinished_search() -> None:
    client = CdSearchClient(
        poll_interval=0,
        max_polls=0,
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, text=CDSEARCH_RUNNING_TSV)
        ),
    )

    try:
        collect_cdsearch_rows(["P68871"], client)
    except CdSearchClientError as exc:
        assert "was still running after 0 polls" in str(exc)
    else:
        raise AssertionError("expected CdSearchClientError")


def test_parse_cdsearch_tsv_raises_on_unexpected_fieldnames() -> None:
    try:
        parse_cdsearch_tsv("<html>not tsv</html>")
    except CdSearchClientError as exc:
        assert "unexpected TSV fieldnames" in str(exc)
    else:
        raise AssertionError("expected CdSearchClientError")


def test_render_cdsearch_tsv_and_json_are_stable() -> None:
    rows = collect_cdsearch_rows(
        ["P68871"],
        CdSearchClient(
            poll_interval=0,
            transport=httpx.MockTransport(
                lambda request: httpx.Response(200, text=CDSEARCH_SUCCESS_TSV)
            ),
        ),
    )

    tsv = render_cdsearch_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["cdd_accession"] for row in parsed] == ["cd08925", "cl21461"]
    assert parsed[0]["e_value"] == "7.88544e-87"

    payload = json.loads(render_cdsearch_json(rows))
    assert payload[0]["source_url"].endswith("uid=cd08925")
