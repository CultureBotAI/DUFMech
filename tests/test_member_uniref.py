from __future__ import annotations

import csv
import json
from io import StringIO

from dufmech.member_uniref import (
    join_members_to_uniref,
    render_member_uniref_json,
    render_member_uniref_tsv,
)
from dufmech.protein_members import PfamProteinMemberRow
from dufmech.uniref import UniRefMappingRow


def member(accession: str = "B2BDZ4") -> PfamProteinMemberRow:
    return PfamProteinMemberRow(
        pfam_id="PF01519",
        uniprot_accession=accession,
        name="Uncharacterized protein",
        source_database="unreviewed",
        length=163,
        taxon_id="2104",
        organism="Mycoplasmoides pneumoniae",
        gene="MPN139",
        in_alphafold=True,
        match_count=1,
        match_ranges=("39-154",),
    )


def uniref(accession: str = "B2BDZ4") -> UniRefMappingRow:
    return UniRefMappingRow(
        uniprot_accession=accession,
        uniref_id="UniRef90_P75259",
        uniref_type="UniRef90",
        name="Cluster: UPF0134 protein MPN_139",
        updated="2026-06-10",
        member_count=2,
        organism_count=2,
        common_taxon_id="2104",
        common_taxon_name="Mycoplasmoides pneumoniae",
        representative_accession="P75259",
        representative_member_id="Y139_MYCPN",
        representative_protein_name="UPF0134 protein MPN_139",
        representative_taxon_id="272634",
        representative_length=163,
        seed_id="P75259",
    )


def test_join_members_to_uniref_carries_member_and_cluster_metadata() -> None:
    rows = join_members_to_uniref([member()], [uniref()])

    assert len(rows) == 1
    row = rows[0]
    assert row.pfam_id == "PF01519"
    assert row.uniprot_accession == "B2BDZ4"
    assert row.match_ranges == ("39-154",)
    assert row.uniref_id == "UniRef90_P75259"
    assert row.uniref_updated == "2026-06-10"
    assert row.uniref_member_count == 2
    assert row.representative_accession == "P75259"
    assert row.member_source_url.endswith("/B2BDZ4/")
    assert row.uniref_source_url.endswith("/UniRef90_P75259")


def test_join_members_to_uniref_preserves_unmapped_members() -> None:
    rows = join_members_to_uniref([member("B2BDZ3")], [])

    assert len(rows) == 1
    assert rows[0].uniprot_accession == "B2BDZ3"
    assert rows[0].uniref_id == ""
    assert rows[0].uniref_member_count is None
    assert rows[0].uniref_source_url == ""


def test_render_member_uniref_tsv_and_json_are_stable() -> None:
    rows = join_members_to_uniref(
        [member("B2BDZ4"), member("B2BDZ3")],
        [uniref("B2BDZ4"), uniref("B2BDZ3")],
    )

    tsv = render_member_uniref_tsv(rows)
    parsed = list(csv.DictReader(StringIO(tsv), dialect="excel-tab"))
    assert [row["uniprot_accession"] for row in parsed] == ["B2BDZ3", "B2BDZ4"]
    assert parsed[0]["match_ranges"] == "39-154"

    payload = json.loads(render_member_uniref_json(rows))
    assert [row["uniprot_accession"] for row in payload] == ["B2BDZ3", "B2BDZ4"]
