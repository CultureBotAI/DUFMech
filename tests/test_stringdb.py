from __future__ import annotations

import csv
import json
from io import StringIO

import httpx

from dufmech.stringdb import (
    STRING_ERROR_FIELDNAMES,
    STRING_INTERACTION_FIELDNAMES,
    StringDbClient,
    StringDbClientError,
    StringDbSeed,
    collect_stringdb_rows,
    parse_string_tsv,
    render_stringdb_json,
    render_stringdb_tsv,
)

STRING_MAPPING_TSV = """queryItem\tqueryIndex\tstringId\tncbiTaxonId\ttaxonName\tpreferredName\tannotation
P68871\t0\t9606.ENSP00000494175\t9606\tHomo sapiens\tHBB\tHemoglobin subunit beta
"""

STRING_PARTNERS_TSV = """stringId_A\tstringId_B\tpreferredName_A\tpreferredName_B\tncbiTaxonId\tscore\tnscore\tfscore\tpscore\tascore\tescore\tdscore\ttscore
9606.ENSP00000494175\t9606.ENSP00000251595\tHBB\tHBA2\t9606\t0.999\t0\t0\t0.064\t0.686\t0.998\t0.9\t0.9
9606.ENSP00000494175\t9606.ENSP00000322421\tHBB\tHBA1\t9606\t0.999\t0\t0\t0.064\t0.999\t0.973\t0.72\t0.903
"""


def test_stringdb_client_maps_uniprot_and_fetches_partners() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        body = request.read().decode("utf-8")
        if request.url.path.endswith("/get_string_ids"):
            assert "identifiers=P68871" in body
            assert "species=9606" in body
            assert "echo_query=1" in body
            return httpx.Response(200, text=STRING_MAPPING_TSV)

        assert request.url.path.endswith("/interaction_partners")
        assert "identifiers=9606.ENSP00000494175" in body
        assert "limit=2" in body
        assert "required_score=400" in body
        return httpx.Response(200, text=STRING_PARTNERS_TSV)

    rows = collect_stringdb_rows(
        [StringDbSeed("P68871", "9606"), StringDbSeed("P68871", "9606")],
        StringDbClient(transport=httpx.MockTransport(handler)),
        limit_partners_per_protein=2,
    )

    assert len(rows) == 2
    assert rows[0].uniprot_accession == "P68871"
    assert rows[0].taxon_id == "9606"
    assert rows[0].string_id == "9606.ENSP00000494175"
    assert rows[0].preferred_name == "HBB"
    assert rows[0].partner_preferred_name == "HBA2"
    assert rows[0].score == 0.999
    assert rows[0].cooccurrence_score == 0.064
    assert rows[0].source_url.endswith("/9606.ENSP00000494175")


def test_stringdb_error_tsv_is_no_evidence() -> None:
    assert (
        parse_string_tsv(
            "\t".join(STRING_ERROR_FIELDNAMES) + "\n",
            expected_fieldnames=STRING_INTERACTION_FIELDNAMES,
            context="STRING interaction partners",
        )
        == []
    )


def test_stringdb_client_raises_on_http_failure() -> None:
    client = StringDbClient(
        transport=httpx.MockTransport(lambda request: httpx.Response(500))
    )

    try:
        collect_stringdb_rows([StringDbSeed("P68871", "9606")], client)
    except StringDbClientError as exc:
        assert "could not fetch STRING get_string_ids" in str(exc)
    else:
        raise AssertionError("expected StringDbClientError")


def test_parse_string_tsv_raises_on_unexpected_fieldnames() -> None:
    try:
        parse_string_tsv(
            "<html>not tsv</html>",
            expected_fieldnames=STRING_INTERACTION_FIELDNAMES,
            context="STRING interaction partners",
        )
    except StringDbClientError as exc:
        assert "unexpected TSV fieldnames" in str(exc)
    else:
        raise AssertionError("expected StringDbClientError")


def test_render_stringdb_tsv_and_json_are_stable() -> None:
    rows = collect_stringdb_rows(
        [StringDbSeed("P68871", "9606")],
        StringDbClient(
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    200,
                    text=(
                        STRING_MAPPING_TSV
                        if request.url.path.endswith("/get_string_ids")
                        else STRING_PARTNERS_TSV
                    ),
                )
            )
        ),
        limit_partners_per_protein=2,
    )

    tsv = render_stringdb_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["partner_preferred_name"] for row in parsed] == ["HBA2", "HBA1"]
    assert parsed[0]["experimental_score"] == "0.998"

    payload = json.loads(render_stringdb_json(rows))
    assert payload[0]["source_url"].endswith("/9606.ENSP00000494175")
