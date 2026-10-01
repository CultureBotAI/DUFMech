"""Score DUF-family characterization status from frozen evidence rows."""

from __future__ import annotations

import csv
import io
import json
from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

from dufmech.worklist import KNOWN_HISTORICAL_DUF, UNKNOWN_CANDIDATE

PARTIALLY_CHARACTERIZED = "PARTIALLY_CHARACTERIZED"
EXPERIMENTAL_GO_EVIDENCE = {
    "EXP",
    "IDA",
    "IPI",
    "IMP",
    "IGI",
    "IEP",
    "HTP",
    "HDA",
    "HMP",
    "HGI",
    "HEP",
}
EGGNOG_FUNCTION_FIELDS = (
    "go_terms",
    "ec_numbers",
    "kegg_kos",
    "kegg_reactions",
    "cazy_terms",
    "bigg_reactions",
)

SCORE_TSV_FIELDNAMES = [
    "pfam_id",
    "short_name",
    "seed_unknown_status",
    "characterization_status",
    "member_count",
    "representative_count",
    "known_evidence_count",
    "partial_evidence_count",
    "context_evidence_count",
    "rhea_reaction_count",
    "experimental_go_mf_count",
    "specific_cdd_hit_count",
    "eggnog_function_count",
    "quickgo_mf_count",
    "cdd_superfamily_count",
    "cath_funfam_count",
    "mgnify_protein_count",
    "mgnify_full_length_count",
    "mgnify_biome_count",
    "rcsb_structure_count",
    "pdbe_kb_annotation_count",
    "alphafold_model_count",
    "threedbeacons_model_count",
    "string_edge_count",
    "eggnog_ortholog_count",
    "demotion_reasons",
    "context_sources",
    "source_url",
]


@dataclass(frozen=True)
class EvidenceBundle:
    """Frozen evidence rows keyed by their source snapshot."""

    alphafold: tuple[Mapping[str, Any], ...] = ()
    cath: tuple[Mapping[str, Any], ...] = ()
    cdsearch: tuple[Mapping[str, Any], ...] = ()
    eggnog: tuple[Mapping[str, Any], ...] = ()
    mgnify: tuple[Mapping[str, Any], ...] = ()
    pdbe_kb: tuple[Mapping[str, Any], ...] = ()
    quickgo: tuple[Mapping[str, Any], ...] = ()
    rcsb: tuple[Mapping[str, Any], ...] = ()
    rhea: tuple[Mapping[str, Any], ...] = ()
    stringdb: tuple[Mapping[str, Any], ...] = ()
    threedbeacons: tuple[Mapping[str, Any], ...] = ()


@dataclass(frozen=True)
class FamilyScoreRow:
    """One first-pass DUF-family characterization score."""

    pfam_id: str
    short_name: str
    seed_unknown_status: str
    characterization_status: str
    member_count: int
    representative_count: int
    known_evidence_count: int
    partial_evidence_count: int
    context_evidence_count: int
    rhea_reaction_count: int
    experimental_go_mf_count: int
    specific_cdd_hit_count: int
    eggnog_function_count: int
    quickgo_mf_count: int
    cdd_superfamily_count: int
    cath_funfam_count: int
    mgnify_protein_count: int
    mgnify_full_length_count: int
    mgnify_biome_count: int
    rcsb_structure_count: int
    pdbe_kb_annotation_count: int
    alphafold_model_count: int
    threedbeacons_model_count: int
    string_edge_count: int
    eggnog_ortholog_count: int
    demotion_reasons: tuple[str, ...]
    context_sources: tuple[str, ...]
    source_url: str

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["demotion_reasons"] = ";".join(self.demotion_reasons)
        row["context_sources"] = ";".join(self.context_sources)
        return row


def score_families(
    worklist_rows: Iterable[Mapping[str, Any]],
    *,
    member_rows: Iterable[Mapping[str, Any]] = (),
    evidence: EvidenceBundle | None = None,
) -> list[FamilyScoreRow]:
    """Score worklist families with optional member and evidence snapshots."""

    evidence = evidence or EvidenceBundle()
    families = [
        row for row in worklist_rows if isinstance(row, Mapping) and row.get("pfam_id")
    ]
    members = _members_by_pfam(member_rows)
    accession_to_pfam_ids = _accession_pfam_index(members)

    rhea = _evidence_by_pfam(evidence.rhea, accession_to_pfam_ids, "rhea_id")
    quickgo = _evidence_by_pfam(evidence.quickgo, accession_to_pfam_ids, "go_id")
    experimental_go = _experimental_quickgo_by_pfam(
        evidence.quickgo,
        accession_to_pfam_ids,
    )
    specific_cdd, superfamily_cdd = _cdsearch_by_pfam(
        evidence.cdsearch,
        accession_to_pfam_ids,
    )
    cath = _cath_funfam_by_pfam(evidence.cath, accession_to_pfam_ids)
    eggnog_function, eggnog_ortholog = _eggnog_by_pfam(
        evidence.eggnog,
        accession_to_pfam_ids,
    )
    mgnify_proteins, mgnify_full_length, mgnify_biomes = _mgnify_by_pfam(
        evidence.mgnify
    )
    rcsb = _evidence_by_pfam(evidence.rcsb, accession_to_pfam_ids, "pdb_id")
    pdbe_kb = _evidence_by_pfam(
        evidence.pdbe_kb,
        accession_to_pfam_ids,
        "annotation_accession",
        accession_field="seed_uniprot_accession",
    )
    alphafold = _evidence_by_pfam(
        evidence.alphafold,
        accession_to_pfam_ids,
        "model_entity_id",
    )
    threedbeacons = _evidence_by_pfam(
        evidence.threedbeacons,
        accession_to_pfam_ids,
        "model_identifier",
    )
    stringdb = _evidence_by_pfam(
        evidence.stringdb,
        accession_to_pfam_ids,
        "partner_string_id",
    )

    scores = [
        _score_family(
            family,
            member_count=len(members.get(_string(family.get("pfam_id")), ())),
            representative_count=_representative_count(
                members.get(_string(family.get("pfam_id")), ())
            ),
            rhea_reaction_count=len(rhea.get(_string(family.get("pfam_id")), ())),
            experimental_go_mf_count=len(
                experimental_go.get(_string(family.get("pfam_id")), ())
            ),
            specific_cdd_hit_count=len(
                specific_cdd.get(_string(family.get("pfam_id")), ())
            ),
            eggnog_function_count=len(
                eggnog_function.get(_string(family.get("pfam_id")), ())
            ),
            quickgo_mf_count=len(quickgo.get(_string(family.get("pfam_id")), ())),
            cdd_superfamily_count=len(
                superfamily_cdd.get(_string(family.get("pfam_id")), ())
            ),
            cath_funfam_count=len(cath.get(_string(family.get("pfam_id")), ())),
            mgnify_protein_count=len(
                mgnify_proteins.get(_string(family.get("pfam_id")), ())
            ),
            mgnify_full_length_count=len(
                mgnify_full_length.get(_string(family.get("pfam_id")), ())
            ),
            mgnify_biome_count=len(
                mgnify_biomes.get(_string(family.get("pfam_id")), ())
            ),
            rcsb_structure_count=len(rcsb.get(_string(family.get("pfam_id")), ())),
            pdbe_kb_annotation_count=len(
                pdbe_kb.get(_string(family.get("pfam_id")), ())
            ),
            alphafold_model_count=len(
                alphafold.get(_string(family.get("pfam_id")), ())
            ),
            threedbeacons_model_count=len(
                threedbeacons.get(_string(family.get("pfam_id")), ())
            ),
            string_edge_count=len(stringdb.get(_string(family.get("pfam_id")), ())),
            eggnog_ortholog_count=len(
                eggnog_ortholog.get(_string(family.get("pfam_id")), ())
            ),
        )
        for family in families
    ]

    return sorted(scores, key=lambda row: (row.characterization_status, row.pfam_id))


def render_scores_tsv(rows: Iterable[FamilyScoreRow]) -> str:
    """Render score rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=SCORE_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_scores_json(rows: Iterable[FamilyScoreRow]) -> str:
    """Render score rows as stable JSON."""

    return json.dumps([asdict(row) for row in rows], indent=2, sort_keys=True)


def _score_family(
    family: Mapping[str, Any],
    *,
    member_count: int,
    representative_count: int,
    rhea_reaction_count: int,
    experimental_go_mf_count: int,
    specific_cdd_hit_count: int,
    eggnog_function_count: int,
    quickgo_mf_count: int,
    cdd_superfamily_count: int,
    cath_funfam_count: int,
    mgnify_protein_count: int,
    mgnify_full_length_count: int,
    mgnify_biome_count: int,
    rcsb_structure_count: int,
    pdbe_kb_annotation_count: int,
    alphafold_model_count: int,
    threedbeacons_model_count: int,
    string_edge_count: int,
    eggnog_ortholog_count: int,
) -> FamilyScoreRow:
    seed_status = _string(family.get("unknown_status"))
    known_count = rhea_reaction_count + experimental_go_mf_count
    partial_count = (
        specific_cdd_hit_count
        + eggnog_function_count
        + max(
            0,
            quickgo_mf_count - experimental_go_mf_count,
        )
    )
    context_count = (
        cdd_superfamily_count
        + cath_funfam_count
        + mgnify_biome_count
        + rcsb_structure_count
        + pdbe_kb_annotation_count
        + alphafold_model_count
        + threedbeacons_model_count
        + string_edge_count
        + eggnog_ortholog_count
    )

    reasons: list[str] = []
    if seed_status == KNOWN_HISTORICAL_DUF:
        reasons.append("historical_interpro_annotation")
    if rhea_reaction_count:
        reasons.append("has_rhea_reaction")
    if experimental_go_mf_count:
        reasons.append("has_experimental_go_molecular_function")
    if specific_cdd_hit_count:
        reasons.append("has_specific_cdd_hit")
    if eggnog_function_count:
        reasons.append("has_eggnog_function")

    if seed_status == KNOWN_HISTORICAL_DUF or known_count:
        characterization_status = KNOWN_HISTORICAL_DUF
    elif partial_count:
        characterization_status = PARTIALLY_CHARACTERIZED
    else:
        characterization_status = UNKNOWN_CANDIDATE

    return FamilyScoreRow(
        pfam_id=_string(family.get("pfam_id")),
        short_name=_string(family.get("short_name")),
        seed_unknown_status=seed_status,
        characterization_status=characterization_status,
        member_count=member_count,
        representative_count=representative_count,
        known_evidence_count=known_count,
        partial_evidence_count=partial_count,
        context_evidence_count=context_count,
        rhea_reaction_count=rhea_reaction_count,
        experimental_go_mf_count=experimental_go_mf_count,
        specific_cdd_hit_count=specific_cdd_hit_count,
        eggnog_function_count=eggnog_function_count,
        quickgo_mf_count=quickgo_mf_count,
        cdd_superfamily_count=cdd_superfamily_count,
        cath_funfam_count=cath_funfam_count,
        mgnify_protein_count=mgnify_protein_count,
        mgnify_full_length_count=mgnify_full_length_count,
        mgnify_biome_count=mgnify_biome_count,
        rcsb_structure_count=rcsb_structure_count,
        pdbe_kb_annotation_count=pdbe_kb_annotation_count,
        alphafold_model_count=alphafold_model_count,
        threedbeacons_model_count=threedbeacons_model_count,
        string_edge_count=string_edge_count,
        eggnog_ortholog_count=eggnog_ortholog_count,
        demotion_reasons=tuple(reasons),
        context_sources=_context_sources(
            cdd_superfamily_count=cdd_superfamily_count,
            cath_funfam_count=cath_funfam_count,
            mgnify_biome_count=mgnify_biome_count,
            rcsb_structure_count=rcsb_structure_count,
            pdbe_kb_annotation_count=pdbe_kb_annotation_count,
            alphafold_model_count=alphafold_model_count,
            threedbeacons_model_count=threedbeacons_model_count,
            string_edge_count=string_edge_count,
            eggnog_ortholog_count=eggnog_ortholog_count,
        ),
        source_url=_string(family.get("source_url")),
    )


def _members_by_pfam(
    rows: Iterable[Mapping[str, Any]],
) -> dict[str, list[Mapping[str, Any]]]:
    by_pfam: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        pfam_id = _string(row.get("pfam_id"))
        if pfam_id:
            by_pfam[pfam_id].append(row)
    return dict(by_pfam)


def _accession_pfam_index(
    members: Mapping[str, Iterable[Mapping[str, Any]]],
) -> dict[str, set[str]]:
    by_accession: dict[str, set[str]] = defaultdict(set)
    for pfam_id, rows in members.items():
        for row in rows:
            for key in ("uniprot_accession", "representative_accession"):
                accession = _string(row.get(key))
                if accession:
                    by_accession[accession].add(pfam_id)
    return dict(by_accession)


def _evidence_by_pfam(
    rows: Iterable[Mapping[str, Any]],
    accession_to_pfam_ids: Mapping[str, set[str]],
    key_field: str,
    *,
    accession_field: str = "uniprot_accession",
) -> dict[str, set[str]]:
    by_pfam: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        accession = _string(row.get(accession_field))
        key = _string(row.get(key_field))
        if not accession or not key:
            continue
        for pfam_id in accession_to_pfam_ids.get(accession, ()):
            by_pfam[pfam_id].add(key)
    return dict(by_pfam)


def _experimental_quickgo_by_pfam(
    rows: Iterable[Mapping[str, Any]],
    accession_to_pfam_ids: Mapping[str, set[str]],
) -> dict[str, set[str]]:
    by_pfam: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        go_evidence = _string(row.get("go_evidence")).upper()
        if go_evidence not in EXPERIMENTAL_GO_EVIDENCE:
            continue
        accession = _string(row.get("uniprot_accession"))
        go_id = _string(row.get("go_id"))
        for pfam_id in accession_to_pfam_ids.get(accession, ()):
            by_pfam[pfam_id].add(go_id)
    return dict(by_pfam)


def _cdsearch_by_pfam(
    rows: Iterable[Mapping[str, Any]],
    accession_to_pfam_ids: Mapping[str, set[str]],
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    specific: dict[str, set[str]] = defaultdict(set)
    superfamily: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        accession = _string(row.get("uniprot_accession"))
        cdd_accession = _string(row.get("cdd_accession"))
        hit_type = _string(row.get("hit_type"))
        if not accession or not cdd_accession:
            continue
        target = superfamily if hit_type == "superfamily" else specific
        for pfam_id in accession_to_pfam_ids.get(accession, ()):
            target[pfam_id].add(cdd_accession)
    return (dict(specific), dict(superfamily))


def _cath_funfam_by_pfam(
    rows: Iterable[Mapping[str, Any]],
    accession_to_pfam_ids: Mapping[str, set[str]],
) -> dict[str, set[tuple[str, str]]]:
    by_pfam: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        accession = _string(row.get("uniprot_accession"))
        superfamily_id = _string(row.get("superfamily_id"))
        funfam_number = _string(row.get("funfam_number"))
        if not accession or not superfamily_id or not funfam_number:
            continue
        for pfam_id in accession_to_pfam_ids.get(accession, ()):
            by_pfam[pfam_id].add((superfamily_id, funfam_number))
    return dict(by_pfam)


def _eggnog_by_pfam(
    rows: Iterable[Mapping[str, Any]],
    accession_to_pfam_ids: Mapping[str, set[str]],
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    functions: dict[str, set[str]] = defaultdict(set)
    orthologs: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        accession = _string(row.get("query_id"))
        if not accession:
            continue

        function_terms = _eggnog_function_terms(row)
        ortholog_terms = {
            f"eggnog_og:{term}" for term in _string_terms(row.get("eggnog_ogs"))
        }
        seed_ortholog = _string(row.get("seed_ortholog"))
        if seed_ortholog:
            ortholog_terms.add(f"seed_ortholog:{seed_ortholog}")

        for pfam_id in accession_to_pfam_ids.get(accession, ()):
            functions[pfam_id].update(function_terms)
            orthologs[pfam_id].update(ortholog_terms)
    return (dict(functions), dict(orthologs))


def _mgnify_by_pfam(
    rows: Iterable[Mapping[str, Any]],
) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, set[str]]]:
    proteins: dict[str, set[str]] = defaultdict(set)
    full_length: dict[str, set[str]] = defaultdict(set)
    biomes: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        pfam_id = _string(row.get("pfam_id"))
        mgyp = _string(row.get("mgyp"))
        if not pfam_id or not mgyp:
            continue

        proteins[pfam_id].add(mgyp)
        if row.get("full_length") is True:
            full_length[pfam_id].add(mgyp)
        biomes[pfam_id].update(_string_terms(row.get("biome_names")))

    return (dict(proteins), dict(full_length), dict(biomes))


def _representative_count(rows: Iterable[Mapping[str, Any]]) -> int:
    accessions = {
        _string(row.get("representative_accession"))
        for row in rows
        if _string(row.get("representative_accession"))
    }
    return len(accessions)


def _context_sources(
    *,
    cdd_superfamily_count: int,
    cath_funfam_count: int,
    mgnify_biome_count: int,
    rcsb_structure_count: int,
    pdbe_kb_annotation_count: int,
    alphafold_model_count: int,
    threedbeacons_model_count: int,
    string_edge_count: int,
    eggnog_ortholog_count: int,
) -> tuple[str, ...]:
    sources = []
    if cdd_superfamily_count:
        sources.append("cdd_superfamily")
    if cath_funfam_count:
        sources.append("cath_gene3d")
    if mgnify_biome_count:
        sources.append("mgnify")
    if rcsb_structure_count:
        sources.append("rcsb_pdb")
    if pdbe_kb_annotation_count:
        sources.append("pdbe_kb")
    if alphafold_model_count:
        sources.append("alphafold")
    if threedbeacons_model_count:
        sources.append("3dbeacons")
    if eggnog_ortholog_count:
        sources.append("eggnog")
    if string_edge_count:
        sources.append("string")
    return tuple(sources)


def _eggnog_function_terms(row: Mapping[str, Any]) -> set[str]:
    return {
        f"{field}:{term}"
        for field in EGGNOG_FUNCTION_FIELDS
        for term in _string_terms(row.get(field))
    }


def _string_terms(value: object) -> tuple[str, ...]:
    if isinstance(value, str):
        values: Iterable[object] = (value,)
    elif isinstance(value, Iterable):
        values = value
    else:
        return ()
    return tuple(term for item in values if (term := _string(item)))


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
