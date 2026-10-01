"""Parse eggNOG-mapper annotation tables."""

from __future__ import annotations

import csv
import io
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass

EGGNOG_MAPPER_URL = "https://eggnog-mapper.cgmlab.org"

EGGNOG_TSV_FIELDNAMES = [
    "query_id",
    "seed_ortholog",
    "seed_evalue",
    "seed_score",
    "eggnog_ogs",
    "tax_ceiling",
    "farthest_donor_lineage",
    "cog_category",
    "preferred_name",
    "go_terms",
    "ec_numbers",
    "kegg_kos",
    "kegg_pathways",
    "kegg_modules",
    "kegg_reactions",
    "kegg_rclasses",
    "brite_terms",
    "kegg_tcs",
    "cazy_terms",
    "bigg_reactions",
    "pfams",
    "annotation_confidence",
    "source_url",
]


class EggNogMapperError(RuntimeError):
    """Raised when an eggNOG-mapper annotation table is invalid."""


@dataclass(frozen=True)
class EggNogAnnotationRow:
    """One normalized eggNOG-mapper annotation row."""

    query_id: str
    seed_ortholog: str
    seed_evalue: str
    seed_score: str
    eggnog_ogs: tuple[str, ...]
    tax_ceiling: str
    farthest_donor_lineage: str
    cog_category: str
    preferred_name: str
    go_terms: tuple[str, ...]
    ec_numbers: tuple[str, ...]
    kegg_kos: tuple[str, ...]
    kegg_pathways: tuple[str, ...]
    kegg_modules: tuple[str, ...]
    kegg_reactions: tuple[str, ...]
    kegg_rclasses: tuple[str, ...]
    brite_terms: tuple[str, ...]
    kegg_tcs: tuple[str, ...]
    cazy_terms: tuple[str, ...]
    bigg_reactions: tuple[str, ...]
    pfams: tuple[str, ...]
    annotation_confidence: str

    @property
    def source_url(self) -> str:
        return EGGNOG_MAPPER_URL

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        for key in _TUPLE_FIELDS:
            row[key] = ";".join(getattr(self, key))
        row["source_url"] = self.source_url
        return row


def parse_emapper_annotations(text: str) -> list[EggNogAnnotationRow]:
    """Parse a standard eggNOG-mapper ``.emapper.annotations`` TSV."""

    header: list[str] | None = None
    rows: list[EggNogAnnotationRow] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if not line or line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.removeprefix("#").split("\t")
            continue
        if header is None:
            raise EggNogMapperError("eggNOG-mapper annotations had no header")

        cells = line.split("\t")
        if len(cells) < len(header):
            cells.extend([""] * (len(header) - len(cells)))
        row = row_from_emapper_record(dict(zip(header, cells)))
        if row is None or row.query_id in seen:
            continue
        seen.add(row.query_id)
        rows.append(row)

    if header is None:
        raise EggNogMapperError("eggNOG-mapper annotations had no header")
    return sorted(rows, key=lambda row: row.query_id)


def row_from_emapper_record(
    record: Mapping[str, str],
) -> EggNogAnnotationRow | None:
    """Return a normalized eggNOG annotation row, or ``None`` if malformed."""

    query_id = _string(record.get("query"))
    if not query_id:
        return None

    return EggNogAnnotationRow(
        query_id=query_id,
        seed_ortholog=_string(record.get("seed_ortholog")),
        seed_evalue=_string(record.get("evalue")),
        seed_score=_string(record.get("score")),
        eggnog_ogs=_split_terms(record.get("eggNOG_OGs")),
        tax_ceiling=_string(record.get("tax_ceiling")),
        farthest_donor_lineage=_string(record.get("farthest_donor_lineage")),
        cog_category=_string(record.get("COG_category")),
        preferred_name=_string(record.get("Preferred_name")),
        go_terms=_split_terms(record.get("GOs")),
        ec_numbers=_split_terms(record.get("EC")),
        kegg_kos=_split_terms(record.get("KEGG_ko")),
        kegg_pathways=_split_terms(record.get("KEGG_Pathway")),
        kegg_modules=_split_terms(record.get("KEGG_Module")),
        kegg_reactions=_split_terms(record.get("KEGG_Reaction")),
        kegg_rclasses=_split_terms(record.get("KEGG_rclass")),
        brite_terms=_split_terms(record.get("BRITE")),
        kegg_tcs=_split_terms(record.get("KEGG_TC")),
        cazy_terms=_split_terms(record.get("CAZy")),
        bigg_reactions=_split_terms(record.get("BiGG_Reaction")),
        pfams=_split_terms(record.get("PFAMs")),
        annotation_confidence=_string(record.get("annotation_confidence")),
    )


def render_eggnog_tsv(rows: Iterable[EggNogAnnotationRow]) -> str:
    """Render eggNOG annotation rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=EGGNOG_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_eggnog_json(rows: Iterable[EggNogAnnotationRow]) -> str:
    """Render eggNOG annotation rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


_TUPLE_FIELDS = (
    "eggnog_ogs",
    "go_terms",
    "ec_numbers",
    "kegg_kos",
    "kegg_pathways",
    "kegg_modules",
    "kegg_reactions",
    "kegg_rclasses",
    "brite_terms",
    "kegg_tcs",
    "cazy_terms",
    "bigg_reactions",
    "pfams",
)


def _split_terms(value: str | None) -> tuple[str, ...]:
    if not value or value == "-":
        return ()

    terms: list[str] = []
    seen: set[str] = set()
    for term in value.split(","):
        term = term.strip()
        if not term or term == "-" or term in seen:
            continue
        seen.add(term)
        terms.append(term)
    return tuple(terms)


def _string(value: object) -> str:
    if not isinstance(value, str):
        return ""
    text = value.strip()
    return "" if text == "-" else text
