"""Join Pfam-to-UniProt member rows to UniRef cluster mappings."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable
from dataclasses import asdict, dataclass

from dufmech.protein_members import PfamProteinMemberRow
from dufmech.uniref import UniRefMappingRow

MEMBER_UNIREF_TSV_FIELDNAMES = [
    "pfam_id",
    "uniprot_accession",
    "name",
    "source_database",
    "length",
    "taxon_id",
    "organism",
    "gene",
    "in_alphafold",
    "match_count",
    "match_ranges",
    "uniref_id",
    "uniref_type",
    "uniref_name",
    "uniref_updated",
    "uniref_member_count",
    "uniref_organism_count",
    "uniref_common_taxon_id",
    "uniref_common_taxon_name",
    "representative_accession",
    "representative_member_id",
    "representative_protein_name",
    "representative_taxon_id",
    "representative_length",
    "uniref_seed_id",
    "member_source_url",
    "uniref_source_url",
]


@dataclass(frozen=True)
class PfamMemberUniRefRow:
    """One Pfam member row with any mapped UniRef cluster."""

    pfam_id: str
    uniprot_accession: str
    name: str
    source_database: str
    length: int | None
    taxon_id: str
    organism: str
    gene: str
    in_alphafold: bool | None
    match_count: int
    match_ranges: tuple[str, ...]
    uniref_id: str
    uniref_type: str
    uniref_name: str
    uniref_updated: str
    uniref_member_count: int | None
    uniref_organism_count: int | None
    uniref_common_taxon_id: str
    uniref_common_taxon_name: str
    representative_accession: str
    representative_member_id: str
    representative_protein_name: str
    representative_taxon_id: str
    representative_length: int | None
    uniref_seed_id: str
    member_source_url: str
    uniref_source_url: str

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["match_ranges"] = ";".join(self.match_ranges)
        return row


def join_members_to_uniref(
    members: Iterable[PfamProteinMemberRow],
    mappings: Iterable[UniRefMappingRow],
) -> list[PfamMemberUniRefRow]:
    """Join Pfam member rows to UniRef mappings by UniProt accession."""

    mappings_by_accession = {row.uniprot_accession: row for row in mappings}
    rows = [
        row_from_member_uniref(member, mappings_by_accession.get(member.uniprot_accession))
        for member in members
    ]
    return sorted(rows, key=lambda row: (row.pfam_id, row.uniprot_accession))


def row_from_member_uniref(
    member: PfamProteinMemberRow,
    uniref: UniRefMappingRow | None,
) -> PfamMemberUniRefRow:
    """Return a joined Pfam member / UniRef row."""

    return PfamMemberUniRefRow(
        pfam_id=member.pfam_id,
        uniprot_accession=member.uniprot_accession,
        name=member.name,
        source_database=member.source_database,
        length=member.length,
        taxon_id=member.taxon_id,
        organism=member.organism,
        gene=member.gene,
        in_alphafold=member.in_alphafold,
        match_count=member.match_count,
        match_ranges=member.match_ranges,
        uniref_id="" if uniref is None else uniref.uniref_id,
        uniref_type="" if uniref is None else uniref.uniref_type,
        uniref_name="" if uniref is None else uniref.name,
        uniref_updated="" if uniref is None else uniref.updated,
        uniref_member_count=None if uniref is None else uniref.member_count,
        uniref_organism_count=None if uniref is None else uniref.organism_count,
        uniref_common_taxon_id="" if uniref is None else uniref.common_taxon_id,
        uniref_common_taxon_name="" if uniref is None else uniref.common_taxon_name,
        representative_accession="" if uniref is None else uniref.representative_accession,
        representative_member_id="" if uniref is None else uniref.representative_member_id,
        representative_protein_name=(
            "" if uniref is None else uniref.representative_protein_name
        ),
        representative_taxon_id="" if uniref is None else uniref.representative_taxon_id,
        representative_length=None if uniref is None else uniref.representative_length,
        uniref_seed_id="" if uniref is None else uniref.seed_id,
        member_source_url=member.source_url,
        uniref_source_url="" if uniref is None else uniref.source_url,
    )


def render_member_uniref_tsv(rows: Iterable[PfamMemberUniRefRow]) -> str:
    """Render joined Pfam member / UniRef rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=MEMBER_UNIREF_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_member_uniref_json(rows: Iterable[PfamMemberUniRefRow]) -> str:
    """Render joined Pfam member / UniRef rows as stable JSON."""

    return json.dumps([asdict(row) for row in rows], indent=2, sort_keys=True)
