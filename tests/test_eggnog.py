from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.eggnog import (
    EggNogMapperError,
    parse_emapper_annotations,
    render_eggnog_json,
    render_eggnog_tsv,
    row_from_emapper_record,
)


def tsv_line(*cells: str) -> str:
    return "\t".join(cells)


EMAPPER_HEADER = tsv_line(
    "#query",
    "seed_ortholog",
    "evalue",
    "score",
    "eggNOG_OGs",
    "tax_ceiling",
    "farthest_donor_lineage",
    "COG_category",
    "Preferred_name",
    "GOs",
    "EC",
    "KEGG_ko",
    "KEGG_Pathway",
    "KEGG_Module",
    "KEGG_Reaction",
    "KEGG_rclass",
    "BRITE",
    "KEGG_TC",
    "CAZy",
    "BiGG_Reaction",
    "PFAMs",
    "annotation_confidence",
)


def emapper_line(query: str = "P75259") -> str:
    return tsv_line(
        query,
        "1224.MPN139",
        "1e-80",
        "250.5",
        "COG4004@1|root,arCOG01234@2157|Archaea",
        "2157",
        "Archaea",
        "S",
        "upf0134",
        "GO:0003674,GO:0008150",
        "1.2.3.4",
        "ko:K00001",
        "map00010",
        "M00001",
        "R00001",
        "RC00001",
        "ko00001",
        "1.A.1",
        "GH1",
        "RXN-1",
        "PF01519",
        "1111111111111111111111",
    )


def test_row_from_emapper_record_normalizes_annotation_metadata() -> None:
    row = row_from_emapper_record(
        dict(zip(EMAPPER_HEADER.removeprefix("#").split("\t"), emapper_line().split("\t")))
    )

    assert row is not None
    assert row.query_id == "P75259"
    assert row.seed_ortholog == "1224.MPN139"
    assert row.seed_evalue == "1e-80"
    assert row.seed_score == "250.5"
    assert row.eggnog_ogs == ("COG4004@1|root", "arCOG01234@2157|Archaea")
    assert row.tax_ceiling == "2157"
    assert row.farthest_donor_lineage == "Archaea"
    assert row.cog_category == "S"
    assert row.preferred_name == "upf0134"
    assert row.go_terms == ("GO:0003674", "GO:0008150")
    assert row.ec_numbers == ("1.2.3.4",)
    assert row.kegg_kos == ("ko:K00001",)
    assert row.kegg_pathways == ("map00010",)
    assert row.kegg_modules == ("M00001",)
    assert row.kegg_reactions == ("R00001",)
    assert row.kegg_rclasses == ("RC00001",)
    assert row.brite_terms == ("ko00001",)
    assert row.kegg_tcs == ("1.A.1",)
    assert row.cazy_terms == ("GH1",)
    assert row.bigg_reactions == ("RXN-1",)
    assert row.pfams == ("PF01519",)
    assert row.annotation_confidence == "1111111111111111111111"
    assert row.source_url == "https://eggnog-mapper.cgmlab.org"


def test_parse_emapper_annotations_skips_comments_deduplicates_and_sorts() -> None:
    rows = parse_emapper_annotations(
        "\n".join(
            [
                "## eggNOG-mapper annotations",
                EMAPPER_HEADER,
                emapper_line("P75259"),
                emapper_line("B2BDZ3"),
                emapper_line("P75259"),
            ]
        )
    )

    assert [row.query_id for row in rows] == ["B2BDZ3", "P75259"]


def test_parse_emapper_annotations_rejects_missing_header() -> None:
    try:
        parse_emapper_annotations(emapper_line())
    except EggNogMapperError as exc:
        assert "no header" in str(exc)
    else:
        raise AssertionError("expected EggNogMapperError")


def test_render_eggnog_tsv_and_json_are_stable() -> None:
    rows = parse_emapper_annotations(f"{EMAPPER_HEADER}\n{emapper_line()}")

    tsv = render_eggnog_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert parsed[0]["eggnog_ogs"] == "COG4004@1|root;arCOG01234@2157|Archaea"
    assert parsed[0]["go_terms"] == "GO:0003674;GO:0008150"
    assert parsed[0]["pfams"] == "PF01519"

    payload = json.loads(render_eggnog_json(rows))
    assert payload[0]["query_id"] == "P75259"
    assert payload[0]["go_terms"] == ["GO:0003674", "GO:0008150"]
