"""Sequence-coordinate-aware reasoning, normalization, synthesis, and graph views.

This module implements DUFMech's coordinate-aware reasoning layer over protein
sequences, explicit 1-based inclusive regions, coordinate mappings, standardized
experimental/computational observations, deduplicated evidence groups, and
evidence-graded functional claims.

Key invariants enforced:
1. Canonical coordinates are 1-based inclusive ``[start, end]`` intervals on an
   identified reference sequence (with SHA-256 digest and sequence length).
2. Discontinuous (multi-segment) domains are represented as ordered, strictly
   disjoint intervals; residues in inter-segment gaps are outside the domain.
3. Overlapping coordinate ranges do not establish domain equivalence
   (``PARTIAL_OVERLAP_NOT_EQUIVALENT``), and sequence-version/isoform/checksum
   mismatches block silent coordinate transfer (``SEQUENCE_VERSION_MISMATCH``).
4. Observations are separated from interpretations; repeated literature reports
   and mirrored database annotations sharing a ``primary_experiment_key`` are
   grouped into a single ``EvidenceGroup`` rather than counted as independent
   replication.
5. Computational scores from distinct methods (``E_VALUE``, ``BITSCORE``,
   ``CATH_CONFIDENCE``, ``PLDDT``, ``KM_MM``) are preserved with their metrics
   and never combined as interchangeable probabilities.
6. Epistemic links (``EVIDENCE_LINK``, ``COORDINATE_MAPPING_LINK``,
   ``INFERENCE_LINK``) are strictly separated from ``CAUSAL_BIOLOGICAL_LINK``
   edges; predictions, correlations, and coordinate overlaps cannot become
   causal edges or ``OBSERVED`` support.
7. Absence of annotation is ``INSUFFICIENT_EVIDENCE`` / ``UNKNOWN_FUNCTION``,
   never negative experimental evidence (``NEGATIVE_EVIDENCE_ONLY``).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from dufmech.reviews import actual_text, read_yaml, safe_path


class SequenceReasoningError(ValueError):
    """A sequence coordinate, observation, mapping, or reasoning graph is invalid."""


PFAM_ID_RE = re.compile(r"^PF\d{5}$")
INTERPRO_CURIE_RE = re.compile(r"^InterPro:IPR\d{6}$")
UNIPROT_ACCESSION_RE = re.compile(
    r"^([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$"
)
ISOFORM_RE = re.compile(
    r"^([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})-[0-9]+$"
)
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
MD5_RE = re.compile(r"^[a-f0-9]{32}$")
TOKEN_ID_RE = re.compile(r"^[A-Za-z0-9_.:-]+$")
EXPERIMENT_KEY_RE = re.compile(r"^[A-Za-z0-9_.:/-]+$")
AA_SEQUENCE_RE = re.compile(r"^[A-Z]+$")
MUTATION_SUB_RE = re.compile(r"^([A-Z])([1-9][0-9]*)([A-Z*])$")
ONTOLOGY_TERM_RE = re.compile(
    r"^(GO:[0-9]{7}|Rhea:[0-9]+|EC:[0-9]+(\.[0-9-]+){0,3}|CHEBI:[0-9]+"
    r"|Pfam:PF[0-9]{5}|InterPro:IPR[0-9]{6}|UniProtKB:[A-Z0-9-]+)$"
)

REGION_KINDS = frozenset({
    "DOMAIN_HIT",
    "DISCONTINUOUS_DOMAIN",
    "EXPERIMENTAL_CONSTRUCT",
    "CATALYTIC_SITE",
    "BINDING_SITE",
    "MUTATION_SITE",
    "STRUCTURAL_OBSERVATION_REGION",
    "ADJACENT_ARCHITECTURAL_DOMAIN",
    "FULL_LENGTH_PROTEIN",
    "UNKNOWN_LOCALIZATION",
})
COORDINATE_STATUSES = frozenset({
    "EXACT",
    "UNCERTAIN_BOUNDARY",
    "DISCONTINUOUS",
    "WHOLE_PROTEIN_UNLOCALIZED",
    "UNKNOWN_LOCALIZATION",
})
COORDINATE_SYSTEMS = frozenset({
    "UNIPROT_CANONICAL",
    "UNIPROT_ISOFORM",
    "CONSTRUCT_NUMBERING",
    "MATURE_PEPTIDE",
    "PDB_SEQRES",
    "PDB_AUTHOR",
    "HMM_PROFILE",
    "ALIGNMENT_COLUMN",
    "UNSPECIFIED",
})
MAPPING_KINDS = frozenset({
    "CONSTRUCT_TO_REFERENCE",
    "DOMAIN_TO_CONSTRUCT",
    "STRUCTURE_TO_UNIPROT",
    "ISOFORM_TO_CANONICAL",
    "HOMOLOG_ALIGNMENT",
    "PROFILE_TO_SEQUENCE",
    "MUTATION_TO_DOMAIN",
})
EQUIVALENCE_STATUSES = frozenset({
    "EXACT_MATCH",
    "CONSTRUCT_CONTAINS_DOMAIN",
    "DOMAIN_CONTAINS_REGION",
    "RESIDUE_INSIDE_REGION",
    "PARTIAL_OVERLAP_NOT_EQUIVALENT",
    "DISJOINT_OUTSIDE_REGION",
    "DISCONTINUOUS_MAPPING",
    "SEQUENCE_VERSION_MISMATCH",
    "UNRESOLVED_MAPPING",
})
OBSERVATION_SOURCES = frozenset({
    "LITERATURE_ASSAY",
    "PDBE_KB",
    "INTERPRO_PFAM",
    "CDSEARCH",
    "CATH_FUNFAM",
    "NCBIFAM",
    "QUICKGO",
    "RHEA",
    "ALPHAFOLD",
    "CURATED_ANNOTATION",
})
EVIDENCE_KINDS = frozenset({"EXPERIMENTAL", "COMPUTATIONAL", "CONTEXTUAL"})
POLARITIES = frozenset({"POSITIVE", "NEGATIVE", "NEUTRAL_OR_UNCHANGED"})
SCORE_METRICS = frozenset({
    "E_VALUE",
    "BITSCORE",
    "CATH_CONFIDENCE",
    "PLDDT",
    "KM_MM",
    "KCAT_PER_S",
    "QUALITATIVE",
})
FUNCTION_ASPECTS = frozenset({
    "CATALYTIC_ACTIVITY",
    "SUBSTRATE_SPECIFICITY",
    "COFACTOR_BINDING",
    "LIGAND_BINDING",
    "PROTEIN_INTERACTION",
    "SUBCELLULAR_LOCALIZATION",
    "PROCESS_CONTRIBUTION",
    "STRUCTURAL_ROLE",
    "ARCHITECTURAL_COOCCURRENCE",
    "UNKNOWN_FUNCTION",
})
CLAIM_SCOPES = frozenset({
    "TESTED_REGION_ONLY",
    "TESTED_CONSTRUCT",
    "SPECIFIC_PROTEIN",
    "CONSERVED_SUBFAMILY",
    "FAMILY_WIDE",
    "UNRESOLVED_SCOPE",
})
SYNTHESIS_STATUSES = frozenset({
    "EXPERIMENTALLY_DEMONSTRATED",
    "SUPPORTED_INFERENCE",
    "COMPUTATIONAL_HYPOTHESIS",
    "CONFLICTING_UNRESOLVED",
    "INSUFFICIENT_EVIDENCE",
    "NEGATIVE_EVIDENCE_ONLY",
})
EDGE_CATEGORIES = frozenset({
    "EVIDENCE_LINK",
    "COORDINATE_MAPPING_LINK",
    "INFERENCE_LINK",
    "CAUSAL_BIOLOGICAL_LINK",
})
SUPPORT_STATUSES = frozenset({"OBSERVED", "INFERRED", "HYPOTHESIZED", "CONTESTED"})

CAUSAL_BIOLOGICAL_PREDICATES = frozenset({
    "enables_biological_activity",
    "produces_metabolite",
    "degrades_substrate",
    "required_for_process",
})
EPISTEMIC_PREDICATES = frozenset({
    "anchored_to_sequence",
    "maps_to_region",
    "observed_on_region",
    "grouped_into_evidence_unit",
    "supports_claim",
    "contradicts_claim",
    "constrains_claim_scope",
    "inferred_from_homolog_region",
    "cooccurs_with_domain",
})
REASONING_PREDICATES = CAUSAL_BIOLOGICAL_PREDICATES | EPISTEMIC_PREDICATES

EXPERIMENTAL_GO_EVIDENCE_CODES = frozenset({
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
    "ECO:0000269", "ECO:0000314", "ECO:0000353",
    "ECO:0000315", "ECO:0000316", "ECO:0000270",
})
CONTEXTUAL_GO_EVIDENCE_CODES = frozenset({
    "TAS", "NAS", "IC", "ND", "ECO:0000304", "ECO:0000303", "ECO:0000305",
})


def _require_token(value: Any, label: str, pattern: re.Pattern[str] = TOKEN_ID_RE) -> str:
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise ValueError(f"{label} must match {pattern.pattern}: {value!r}")
    return value


def _require_positive_int(value: Any, label: str, *, minimum: int = 1) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum}: {value!r}")
    return value


def build_sequence_identity(
    uniprot_accession: str,
    *,
    sequence: str | None = None,
    sequence_length: int | None = None,
    sequence_sha256: str | None = None,
    sequence_md5: str | None = None,
    isoform: str | None = None,
    sequence_version: int | None = None,
    taxon_id: str | None = None,
    organism: str | None = None,
    uniprot_release: str | None = None,
    source_url: str | None = None,
    sequence_id: str | None = None,
) -> dict[str, Any]:
    """Create and validate a SequenceIdentity dictionary."""
    if not isinstance(uniprot_accession, str) or not UNIPROT_ACCESSION_RE.fullmatch(uniprot_accession):
        raise ValueError(f"invalid UniProt accession: {uniprot_accession!r}")
    if isoform is not None:
        if not isinstance(isoform, str) or not ISOFORM_RE.fullmatch(isoform):
            raise ValueError(f"invalid UniProt isoform: {isoform!r}")
        if not isoform.startswith(f"{uniprot_accession}-"):
            raise ValueError(
                f"isoform {isoform!r} does not belong to accession {uniprot_accession!r}"
            )
    if sequence is not None:
        if not isinstance(sequence, str) or not AA_SEQUENCE_RE.fullmatch(sequence):
            raise ValueError("sequence must be a non-empty uppercase amino-acid string")
        computed_len = len(sequence)
        computed_sha256 = hashlib.sha256(sequence.encode("ascii")).hexdigest()
        computed_md5 = hashlib.md5(sequence.encode("ascii")).hexdigest()
        if sequence_length is not None and sequence_length != computed_len:
            raise ValueError(
                f"sequence_length mismatch for {uniprot_accession}: "
                f"declared {sequence_length} != actual {computed_len}"
            )
        if sequence_sha256 is not None and sequence_sha256 != computed_sha256:
            raise ValueError(
                f"sequence_sha256 mismatch for {uniprot_accession}: "
                f"declared {sequence_sha256} != actual {computed_sha256}"
            )
        if sequence_md5 is not None and sequence_md5 != computed_md5:
            raise ValueError(
                f"sequence_md5 mismatch for {uniprot_accession}: "
                f"declared {sequence_md5} != actual {computed_md5}"
            )
        sequence_length = computed_len
        sequence_sha256 = computed_sha256
        if sequence_md5 is None:
            sequence_md5 = computed_md5

    length = _require_positive_int(sequence_length, "sequence_length", minimum=1)
    if not isinstance(sequence_sha256, str) or not SHA256_RE.fullmatch(sequence_sha256):
        raise ValueError(f"sequence_sha256 must be a 64-character lowercase hex digest: {sequence_sha256!r}")
    if sequence_md5 is not None and (not isinstance(sequence_md5, str) or not MD5_RE.fullmatch(sequence_md5)):
        raise ValueError(f"sequence_md5 must be a 32-character lowercase hex digest: {sequence_md5!r}")
    if sequence_version is not None:
        _require_positive_int(sequence_version, "sequence_version", minimum=1)
    if sequence_id is None:
        base = isoform if isoform else uniprot_accession
        version_suffix = f"_v{sequence_version}" if sequence_version is not None else ""
        sequence_id = f"seq_{base}{version_suffix}"
    _require_token(sequence_id, "sequence_id")

    result: dict[str, Any] = {
        "sequence_id": sequence_id,
        "uniprot_accession": uniprot_accession,
        "sequence_length": length,
        "sequence_sha256": sequence_sha256,
    }
    if isoform is not None:
        result["isoform"] = isoform
    if sequence_version is not None:
        result["sequence_version"] = sequence_version
    if sequence_md5 is not None:
        result["sequence_md5"] = sequence_md5
    if taxon_id is not None:
        if not isinstance(taxon_id, str) or not re.fullmatch(r"^NCBITaxon:[0-9]+$", taxon_id):
            raise ValueError(f"invalid taxon_id: {taxon_id!r}")
        result["taxon_id"] = taxon_id
    if organism is not None:
        result["organism"] = actual_text(organism, "organism")
    if uniprot_release is not None:
        result["uniprot_release"] = actual_text(uniprot_release, "uniprot_release")
    if source_url is not None:
        result["source_url"] = actual_text(source_url, "source_url")
    return result


def sequence_identity_from_example_row(
    row: Mapping[str, Any],
    *,
    sequence_version: int | None = None,
    isoform: str | None = None,
    sequence_id: str | None = None,
) -> dict[str, Any]:
    """Normalize a DUFMech protein_examples row into a SequenceIdentity."""
    accession = str(row["uniprot_accession"])
    taxon_raw = str(row.get("taxon_id", "")).strip()
    taxon_curie = None
    if taxon_raw:
        taxon_curie = taxon_raw if taxon_raw.startswith("NCBITaxon:") else f"NCBITaxon:{taxon_raw}"
    return build_sequence_identity(
        accession,
        sequence=row.get("sequence"),
        sequence_length=row.get("sequence_length"),
        sequence_sha256=row.get("sequence_sha256"),
        isoform=isoform,
        sequence_version=sequence_version,
        taxon_id=taxon_curie,
        organism=row.get("organism"),
        uniprot_release=row.get("uniprot_version"),
        source_url=f"https://www.uniprot.org/uniprotkb/{accession}/entry",
        sequence_id=sequence_id,
    )


def validate_sequence_intervals(
    intervals: Sequence[Mapping[str, Any]],
    *,
    sequence_length: int,
    coordinate_status: str,
    reference_sequence: str | None = None,
    label: str = "intervals",
) -> list[dict[str, Any]]:
    """Validate 1-based inclusive intervals against sequence length and residue identity."""
    if coordinate_status not in COORDINATE_STATUSES:
        raise ValueError(f"{label}: invalid coordinate_status {coordinate_status!r}")
    if coordinate_status == "UNKNOWN_LOCALIZATION":
        if intervals:
            raise ValueError(f"{label}: UNKNOWN_LOCALIZATION region must not declare intervals")
        return []
    if not isinstance(intervals, Sequence) or isinstance(intervals, (str, bytes)) or not intervals:
        raise ValueError(f"{label}: localized region ({coordinate_status}) requires at least one interval")
    if coordinate_status == "DISCONTINUOUS" and len(intervals) < 2:
        raise ValueError(f"{label}: DISCONTINUOUS region requires at least 2 disjoint intervals")
    if coordinate_status != "DISCONTINUOUS" and len(intervals) > 1:
        raise ValueError(
            f"{label}: multi-segment intervals require coordinate_status='DISCONTINUOUS', got {coordinate_status!r}"
        )

    normalized: list[dict[str, Any]] = []
    previous_end = 0
    for idx, raw in enumerate(intervals):
        if not isinstance(raw, Mapping):
            raise SequenceReasoningError(f"{label}[{idx}] must be a mapping")
        start = _require_positive_int(raw.get("start"), f"{label}[{idx}].start", minimum=1)
        end = _require_positive_int(raw.get("end"), f"{label}[{idx}].end", minimum=1)
        if start > end:
            raise ValueError(
                f"{label}[{idx}] has inverted 1-based interval: start {start} > end {end}"
            )
        if end > sequence_length:
            raise ValueError(
                f"{label}[{idx}] interval {start}..{end} exceeds sequence_length {sequence_length}"
            )
        if previous_end and start <= previous_end:
            raise ValueError(
                f"{label}[{idx}] interval {start}..{end} overlaps or is not strictly ordered "
                f"after previous interval ending at {previous_end}"
            )
        previous_end = end

        item: dict[str, Any] = {"start": start, "end": end}
        if "start_uncertain" in raw and raw["start_uncertain"] is not None:
            if not isinstance(raw["start_uncertain"], bool):
                raise ValueError(f"{label}[{idx}].start_uncertain must be a boolean")
            item["start_uncertain"] = raw["start_uncertain"]
        if "end_uncertain" in raw and raw["end_uncertain"] is not None:
            if not isinstance(raw["end_uncertain"], bool):
                raise ValueError(f"{label}[{idx}].end_uncertain must be a boolean")
            item["end_uncertain"] = raw["end_uncertain"]
        if "residue_identity" in raw and raw["residue_identity"] is not None:
            residue = str(raw["residue_identity"])
            if not AA_SEQUENCE_RE.fullmatch(residue):
                raise ValueError(f"{label}[{idx}].residue_identity must be uppercase amino acids")
            expected_span_len = end - start + 1
            if len(residue) != expected_span_len:
                raise ValueError(
                    f"{label}[{idx}].residue_identity length {len(residue)} does not match "
                    f"interval {start}..{end} length {expected_span_len}"
                )
            if reference_sequence is not None:
                actual_subseq = reference_sequence[start - 1 : end]
                if actual_subseq != residue:
                    raise ValueError(
                        f"{label}[{idx}] residue mismatch at {start}..{end}: "
                        f"expected {residue!r}, sequence has {actual_subseq!r}"
                    )
            item["residue_identity"] = residue
        normalized.append(item)
    return normalized


def build_sequence_region(
    *,
    region_id: str,
    sequence_identity: Mapping[str, Any],
    label: str,
    region_kind: str,
    coordinate_status: str = "EXACT",
    intervals: Sequence[Mapping[str, Any]] = (),
    source_coordinate_system: str = "UNIPROT_CANONICAL",
    source_coordinates_text: str | None = None,
    conversion_provenance: str | None = None,
    pfam_id: str | None = None,
    interpro_id: str | None = None,
    reference_sequence: str | None = None,
) -> dict[str, Any]:
    """Create and validate a SequenceRegion anchored to a SequenceIdentity."""
    _require_token(region_id, "region_id")
    seq_id = _require_token(sequence_identity.get("sequence_id"), "sequence_identity.sequence_id")
    seq_len = _require_positive_int(sequence_identity.get("sequence_length"), "sequence_identity.sequence_length")
    if region_kind not in REGION_KINDS:
        raise ValueError(f"invalid region_kind: {region_kind!r}")
    if source_coordinate_system not in COORDINATE_SYSTEMS:
        raise ValueError(f"invalid source_coordinate_system: {source_coordinate_system!r}")
    checked_intervals = validate_sequence_intervals(
        intervals,
        sequence_length=seq_len,
        coordinate_status=coordinate_status,
        reference_sequence=reference_sequence,
        label=f"region[{region_id}].intervals",
    )
    if coordinate_status == "UNCERTAIN_BOUNDARY" and not any(
        iv.get("start_uncertain") or iv.get("end_uncertain") for iv in checked_intervals
    ):
        raise ValueError(
            f"region[{region_id}] has coordinate_status='UNCERTAIN_BOUNDARY' "
            "but no interval marks start_uncertain or end_uncertain"
        )
    result: dict[str, Any] = {
        "region_id": region_id,
        "sequence_id": seq_id,
        "label": actual_text(label, f"region[{region_id}].label"),
        "region_kind": region_kind,
        "coordinate_status": coordinate_status,
        "intervals": checked_intervals,
        "source_coordinate_system": source_coordinate_system,
    }
    if source_coordinates_text is not None:
        result["source_coordinates_text"] = actual_text(
            source_coordinates_text, f"region[{region_id}].source_coordinates_text"
        )
    if conversion_provenance is not None:
        result["conversion_provenance"] = actual_text(
            conversion_provenance, f"region[{region_id}].conversion_provenance"
        )
    if pfam_id is not None:
        if not PFAM_ID_RE.fullmatch(pfam_id):
            raise ValueError(f"invalid pfam_id: {pfam_id!r}")
        result["pfam_id"] = pfam_id
    if interpro_id is not None:
        if not INTERPRO_CURIE_RE.fullmatch(interpro_id):
            raise ValueError(f"invalid interpro_id: {interpro_id!r}")
        result["interpro_id"] = interpro_id
    return result


def convert_construct_to_reference(
    *,
    construct_start_on_ref: int,
    construct_end_on_ref: int,
    local_start: int,
    local_end: int,
    sequence_identity: Mapping[str, Any],
    region_id: str,
    label: str,
    region_kind: str = "MUTATION_SITE",
    residue_identity: str | None = None,
    reference_sequence: str | None = None,
) -> dict[str, Any]:
    """Convert 1-based construct-local coordinates to 1-based reference sequence coordinates."""
    c_start = _require_positive_int(construct_start_on_ref, "construct_start_on_ref")
    c_end = _require_positive_int(construct_end_on_ref, "construct_end_on_ref")
    if c_start > c_end:
        raise ValueError(f"construct_start_on_ref {c_start} > construct_end_on_ref {c_end}")
    l_start = _require_positive_int(local_start, "local_start")
    l_end = _require_positive_int(local_end, "local_end")
    if l_start > l_end:
        raise ValueError(f"local_start {l_start} > local_end {l_end}")
    construct_len = c_end - c_start + 1
    if l_end > construct_len:
        raise ValueError(
            f"construct-local coordinate {l_start}..{l_end} exceeds construct length {construct_len} "
            f"(reference {c_start}..{c_end})"
        )
    ref_start = c_start + l_start - 1
    ref_end = c_start + l_end - 1
    interval: dict[str, Any] = {"start": ref_start, "end": ref_end}
    if residue_identity is not None:
        interval["residue_identity"] = residue_identity
    return build_sequence_region(
        region_id=region_id,
        sequence_identity=sequence_identity,
        label=label,
        region_kind=region_kind,
        coordinate_status="EXACT",
        intervals=[interval],
        source_coordinate_system="CONSTRUCT_NUMBERING",
        source_coordinates_text=f"construct({c_start}-{c_end}):{l_start}-{l_end}",
        conversion_provenance=(
            f"Converted 1-based construct coordinates {l_start}..{l_end} on construct "
            f"{c_start}..{c_end} via ref_pos = {c_start} + local_pos - 1 -> {ref_start}..{ref_end}."
        ),
        reference_sequence=reference_sequence,
    )


def convert_mature_peptide_to_reference(
    *,
    signal_peptide_end: int,
    mature_start: int,
    mature_end: int,
    sequence_identity: Mapping[str, Any],
    region_id: str,
    label: str,
    region_kind: str = "DOMAIN_HIT",
    residue_identity: str | None = None,
    reference_sequence: str | None = None,
) -> dict[str, Any]:
    """Convert 1-based mature-peptide coordinates (after signal peptide 1..signal_peptide_end) to precursor coordinates."""
    sp_end = _require_positive_int(signal_peptide_end, "signal_peptide_end")
    m_start = _require_positive_int(mature_start, "mature_start")
    m_end = _require_positive_int(mature_end, "mature_end")
    if m_start > m_end:
        raise ValueError(f"mature_start {m_start} > mature_end {m_end}")
    ref_start = sp_end + m_start
    ref_end = sp_end + m_end
    interval: dict[str, Any] = {"start": ref_start, "end": ref_end}
    if residue_identity is not None:
        interval["residue_identity"] = residue_identity
    return build_sequence_region(
        region_id=region_id,
        sequence_identity=sequence_identity,
        label=label,
        region_kind=region_kind,
        coordinate_status="EXACT",
        intervals=[interval],
        source_coordinate_system="MATURE_PEPTIDE",
        source_coordinates_text=f"mature(after_sp_1-{sp_end}):{m_start}-{m_end}",
        conversion_provenance=(
            f"Converted 1-based mature chain coordinates {m_start}..{m_end} after cleaved "
            f"signal peptide 1..{sp_end} via ref_pos = {sp_end} + mature_pos -> {ref_start}..{ref_end}."
        ),
        reference_sequence=reference_sequence,
    )


def convert_zero_based_half_open_to_reference(
    *,
    zero_start: int,
    zero_end: int,
    sequence_identity: Mapping[str, Any],
    region_id: str,
    label: str,
    region_kind: str = "DOMAIN_HIT",
    reference_sequence: str | None = None,
) -> dict[str, Any]:
    """Convert 0-based half-open [zero_start, zero_end) coordinates to 1-based inclusive [zero_start + 1, zero_end]."""
    z_start = _require_positive_int(zero_start, "zero_start", minimum=0)
    z_end = _require_positive_int(zero_end, "zero_end", minimum=1)
    if z_start >= z_end:
        raise ValueError(f"empty or inverted 0-based half-open interval [{z_start}, {z_end})")
    ref_start = z_start + 1
    ref_end = z_end
    return build_sequence_region(
        region_id=region_id,
        sequence_identity=sequence_identity,
        label=label,
        region_kind=region_kind,
        coordinate_status="EXACT",
        intervals=[{"start": ref_start, "end": ref_end}],
        source_coordinate_system="UNSPECIFIED",
        source_coordinates_text=f"[{z_start}, {z_end}) (0-based half-open)",
        conversion_provenance=(
            f"Converted 0-based half-open [{z_start}, {z_end}) to 1-based inclusive "
            f"{ref_start}..{ref_end}."
        ),
        reference_sequence=reference_sequence,
    )


def region_residue_positions(region: Mapping[str, Any]) -> set[int]:
    """Return the exact set of 1-based residue positions covered by a region's intervals."""
    positions: set[int] = set()
    for interval in region.get("intervals") or ():
        start = int(interval["start"])
        end = int(interval["end"])
        positions.update(range(start, end + 1))
    return positions


def region_total_length(region: Mapping[str, Any]) -> int:
    """Return total residue count across all segments (excluding inter-segment gaps)."""
    return sum(int(iv["end"]) - int(iv["start"]) + 1 for iv in (region.get("intervals") or ()))


def region_bounding_span(region: Mapping[str, Any]) -> tuple[int, int] | None:
    """Return the outer (min_start, max_end) envelope of a region, or None if unlocalized."""
    intervals = region.get("intervals") or ()
    if not intervals:
        return None
    return (int(intervals[0]["start"]), int(intervals[-1]["end"]))


def region_inter_segment_gaps(region: Mapping[str, Any]) -> list[tuple[int, int]]:
    """Return 1-based inclusive gap intervals between segments of a discontinuous region."""
    intervals = region.get("intervals") or ()
    gaps: list[tuple[int, int]] = []
    for idx in range(len(intervals) - 1):
        gap_start = int(intervals[idx]["end"]) + 1
        gap_end = int(intervals[idx + 1]["start"]) - 1
        if gap_start <= gap_end:
            gaps.append((gap_start, gap_end))
    return gaps


def classify_region_mapping(
    *,
    mapping_id: str,
    source_region: Mapping[str, Any],
    target_region: Mapping[str, Any],
    source_sequence: Mapping[str, Any],
    target_sequence: Mapping[str, Any],
    mapping_kind: str = "CONSTRUCT_TO_REFERENCE",
    residue_correspondences: Sequence[Mapping[str, Any]] | None = (),
    alignment_gaps: int | None = None,
    mapping_uncertainty: str | None = None,
    provenance_note: str | None = None,
) -> dict[str, Any]:
    """Classify coordinate equivalence and coverage between two regions with strict provenance."""
    _require_token(mapping_id, "mapping_id")
    if mapping_kind not in MAPPING_KINDS:
        raise ValueError(f"invalid mapping_kind: {mapping_kind!r}")
    src_reg_id = _require_token(source_region.get("region_id"), "source_region.region_id")
    tgt_reg_id = _require_token(target_region.get("region_id"), "target_region.region_id")

    src_seq_id = source_sequence.get("sequence_id")
    tgt_seq_id = target_sequence.get("sequence_id")
    if source_region.get("sequence_id") != src_seq_id:
        raise ValueError(f"source_region {src_reg_id} does not belong to sequence {src_seq_id}")
    if target_region.get("sequence_id") != tgt_seq_id:
        raise ValueError(f"target_region {tgt_reg_id} does not belong to sequence {tgt_seq_id}")

    checked_correspondences: list[dict[str, Any]] = []
    for idx, corr in enumerate(residue_correspondences or ()):
        item: dict[str, Any] = {
            "source_position": _require_positive_int(
                corr.get("source_position"), f"residue_correspondences[{idx}].source_position"
            ),
            "target_position": _require_positive_int(
                corr.get("target_position"), f"residue_correspondences[{idx}].target_position"
            ),
        }
        for key in ("source_residue", "target_residue", "pdb_insertion_code", "mutation_substitution", "note"):
            if corr.get(key) is not None:
                item[key] = str(corr[key])
        checked_correspondences.append(item)

    # Check sequence identity compatibility first.
    if src_seq_id != tgt_seq_id:
        same_accession = (
            source_sequence.get("uniprot_accession") == target_sequence.get("uniprot_accession")
        )
        same_sha = source_sequence.get("sequence_sha256") == target_sequence.get("sequence_sha256")
        same_isoform = source_sequence.get("isoform") == target_sequence.get("isoform")
        same_version = source_sequence.get("sequence_version") == target_sequence.get("sequence_version")
        if same_accession and (not same_sha or not same_isoform or not same_version):
            if mapping_kind != "ISOFORM_TO_CANONICAL" or not checked_correspondences:
                uncertainty = mapping_uncertainty or (
                    f"Sequence identity mismatch for {source_sequence.get('uniprot_accession')}: "
                    f"{src_seq_id} (sha256={source_sequence.get('sequence_sha256')[:12]}..., "
                    f"version={source_sequence.get('sequence_version')}, isoform={source_sequence.get('isoform')}) "
                    f"vs {tgt_seq_id} (sha256={target_sequence.get('sequence_sha256')[:12]}..., "
                    f"version={target_sequence.get('sequence_version')}, isoform={target_sequence.get('isoform')}). "
                    "Coordinates cannot be silently transferred across mismatched sequence versions or isoforms."
                )
                return {
                    "mapping_id": mapping_id,
                    "source_region_id": src_reg_id,
                    "target_region_id": tgt_reg_id,
                    "mapping_kind": mapping_kind,
                    "equivalence_status": "SEQUENCE_VERSION_MISMATCH",
                    "overlap_residues": 0,
                    "source_coverage": 0.0,
                    "target_coverage": 0.0,
                    "mapping_uncertainty": uncertainty,
                    "provenance_note": provenance_note or uncertainty,
                }
            # Explicit ISOFORM_TO_CANONICAL mapping with residue_correspondences:
            # project source_region positions onto target_region via checked_correspondences
            # rather than intersecting raw unprojected coordinate numbers.
            src_raw = region_residue_positions(source_region)
            tgt_positions = region_residue_positions(target_region)
            corr_map = {c["source_position"]: c["target_position"] for c in checked_correspondences}
            projected_src = {corr_map[p] for p in src_raw if p in corr_map}
            all_mapped = bool(src_raw) and all(p in corr_map for p in src_raw)
            overlap = len(projected_src & tgt_positions)
            src_cov = round(overlap / len(src_raw), 6) if src_raw else 0.0
            tgt_cov = round(overlap / len(tgt_positions), 6) if tgt_positions else 0.0
            if not projected_src:
                iso_eq = "UNRESOLVED_MAPPING"
            elif overlap == 0:
                iso_eq = "DISJOINT_OUTSIDE_REGION"
            elif all_mapped and projected_src == tgt_positions:
                iso_eq = (
                    "DISCONTINUOUS_MAPPING"
                    if (
                        source_region.get("coordinate_status") == "DISCONTINUOUS"
                        or target_region.get("coordinate_status") == "DISCONTINUOUS"
                    )
                    else "EXACT_MATCH"
                )
            elif all_mapped and len(src_raw) == 1 and projected_src.issubset(tgt_positions):
                iso_eq = "RESIDUE_INSIDE_REGION"
            elif tgt_positions.issubset(projected_src) and len(src_raw) > len(tgt_positions):
                iso_eq = (
                    "CONSTRUCT_CONTAINS_DOMAIN"
                    if source_region.get("region_kind")
                    in {
                        "EXPERIMENTAL_CONSTRUCT",
                        "FULL_LENGTH_PROTEIN",
                        "STRUCTURAL_OBSERVATION_REGION",
                    }
                    else "DOMAIN_CONTAINS_REGION"
                )
            elif all_mapped and projected_src.issubset(tgt_positions) and len(tgt_positions) > len(projected_src):
                iso_eq = "DOMAIN_CONTAINS_REGION"
            else:
                iso_eq = "PARTIAL_OVERLAP_NOT_EQUIVALENT"
            iso_result: dict[str, Any] = {
                "mapping_id": mapping_id,
                "source_region_id": src_reg_id,
                "target_region_id": tgt_reg_id,
                "mapping_kind": mapping_kind,
                "equivalence_status": iso_eq,
                "overlap_residues": overlap,
                "source_coverage": src_cov,
                "target_coverage": tgt_cov,
                "residue_correspondences": checked_correspondences,
                "provenance_note": provenance_note
                or (
                    f"Projected isoform region {src_reg_id} ({src_seq_id}) -> {tgt_reg_id} ({tgt_seq_id}) "
                    f"via {len(checked_correspondences)} residue correspondence(s): {iso_eq}."
                ),
            }
            if alignment_gaps is not None:
                iso_result["alignment_gaps"] = _require_positive_int(
                    alignment_gaps, "alignment_gaps", minimum=0
                )
            if mapping_uncertainty:
                iso_result["mapping_uncertainty"] = mapping_uncertainty
            return iso_result
        elif not same_accession:
            if mapping_kind in {"HOMOLOG_ALIGNMENT", "PROFILE_TO_SEQUENCE"}:
                tgt_positions = region_residue_positions(target_region)
                if not checked_correspondences:
                    status = "UNRESOLVED_MAPPING"
                elif all(c["target_position"] in tgt_positions for c in checked_correspondences):
                    status = "RESIDUE_INSIDE_REGION"
                else:
                    status = "DISJOINT_OUTSIDE_REGION"
                note = provenance_note or (
                    f"Cross-sequence alignment ({mapping_kind}) between {src_reg_id} ({src_seq_id}) "
                    f"and {tgt_reg_id} ({tgt_seq_id})."
                )
                result: dict[str, Any] = {
                    "mapping_id": mapping_id,
                    "source_region_id": src_reg_id,
                    "target_region_id": tgt_reg_id,
                    "mapping_kind": mapping_kind,
                    "equivalence_status": status,
                    "provenance_note": note,
                }
                if alignment_gaps is not None:
                    result["alignment_gaps"] = _require_positive_int(
                        alignment_gaps, "alignment_gaps", minimum=0
                    )
                if checked_correspondences:
                    result["residue_correspondences"] = checked_correspondences
                if mapping_uncertainty:
                    result["mapping_uncertainty"] = mapping_uncertainty
                return result
            uncertainty = mapping_uncertainty or (
                f"Cross-protein mapping ({mapping_kind}) between distinct accessions "
                f"{source_sequence.get('uniprot_accession')} ({src_seq_id}) and "
                f"{target_sequence.get('uniprot_accession')} ({tgt_seq_id}) requires "
                "HOMOLOG_ALIGNMENT or PROFILE_TO_SEQUENCE; raw residue numbers cannot be intersected across distinct proteins."
            )
            return {
                "mapping_id": mapping_id,
                "source_region_id": src_reg_id,
                "target_region_id": tgt_reg_id,
                "mapping_kind": mapping_kind,
                "equivalence_status": "UNRESOLVED_MAPPING",
                "overlap_residues": 0,
                "source_coverage": 0.0,
                "target_coverage": 0.0,
                "mapping_uncertainty": uncertainty,
                "provenance_note": provenance_note or uncertainty,
            }

    src_status = source_region.get("coordinate_status")
    tgt_status = target_region.get("coordinate_status")
    if src_status == "UNKNOWN_LOCALIZATION" or tgt_status == "UNKNOWN_LOCALIZATION":
        uncertainty = mapping_uncertainty or (
            "One or both regions have UNKNOWN_LOCALIZATION; domain localization is unresolved."
        )
        return {
            "mapping_id": mapping_id,
            "source_region_id": src_reg_id,
            "target_region_id": tgt_reg_id,
            "mapping_kind": mapping_kind,
            "equivalence_status": "UNRESOLVED_MAPPING",
            "overlap_residues": 0,
            "source_coverage": 0.0,
            "target_coverage": 0.0,
            "mapping_uncertainty": uncertainty,
            "provenance_note": provenance_note or uncertainty,
        }

    src_positions = region_residue_positions(source_region)
    tgt_positions = region_residue_positions(target_region)
    overlap = len(src_positions & tgt_positions)
    src_cov = round(overlap / len(src_positions), 6) if src_positions else 0.0
    tgt_cov = round(overlap / len(tgt_positions), 6) if tgt_positions else 0.0

    inferred_uncertainty = mapping_uncertainty
    if overlap == 0:
        equivalence = "DISJOINT_OUTSIDE_REGION"
        tgt_gaps = region_inter_segment_gaps(target_region)
        for gap_start, gap_end in tgt_gaps:
            if any(gap_start <= pos <= gap_end for pos in src_positions):
                inferred_uncertainty = inferred_uncertainty or (
                    f"Source region {src_reg_id} falls inside the inter-segment gap "
                    f"{gap_start}..{gap_end} of discontinuous region {tgt_reg_id}, not within "
                    "its domain segments."
                )
                break
    elif src_positions == tgt_positions:
        if src_status == "DISCONTINUOUS" or tgt_status == "DISCONTINUOUS":
            equivalence = "DISCONTINUOUS_MAPPING"
        else:
            equivalence = "EXACT_MATCH"
    elif len(src_positions) == 1 and src_positions.issubset(tgt_positions):
        equivalence = "RESIDUE_INSIDE_REGION"
    elif tgt_positions.issubset(src_positions) and len(src_positions) > len(tgt_positions):
        if source_region.get("region_kind") in {
            "EXPERIMENTAL_CONSTRUCT",
            "FULL_LENGTH_PROTEIN",
            "STRUCTURAL_OBSERVATION_REGION",
        }:
            equivalence = "CONSTRUCT_CONTAINS_DOMAIN"
            if src_status == "WHOLE_PROTEIN_UNLOCALIZED" or source_region.get("region_kind") == "FULL_LENGTH_PROTEIN":
                inferred_uncertainty = inferred_uncertainty or (
                    f"Whole-protein span {src_reg_id} ({len(src_positions)} aa) contains target "
                    f"domain {tgt_reg_id} ({len(tgt_positions)} aa, source_coverage={src_cov:.3f}); "
                    "an assay or perturbation on the full protein without domain-specific mutation "
                    "or isolated construct does not localize the effect to the domain."
                )
        else:
            equivalence = "DOMAIN_CONTAINS_REGION"
    elif src_positions.issubset(tgt_positions) and len(tgt_positions) > len(src_positions):
        equivalence = "DOMAIN_CONTAINS_REGION"
    else:
        equivalence = "PARTIAL_OVERLAP_NOT_EQUIVALENT"
        inferred_uncertainty = inferred_uncertainty or (
            f"Partial coordinate overlap ({overlap} aa; source_coverage={src_cov:.3f}, "
            f"target_coverage={tgt_cov:.3f}) between {src_reg_id} and {tgt_reg_id}; "
            "overlapping intervals alone do not establish domain equivalence."
        )

    if src_status == "UNCERTAIN_BOUNDARY" or tgt_status == "UNCERTAIN_BOUNDARY":
        inferred_uncertainty = inferred_uncertainty or (
            "One or both mapped regions have uncertain boundary coordinates."
        )

    result = {
        "mapping_id": mapping_id,
        "source_region_id": src_reg_id,
        "target_region_id": tgt_reg_id,
        "mapping_kind": mapping_kind,
        "equivalence_status": equivalence,
        "overlap_residues": overlap,
        "source_coverage": src_cov,
        "target_coverage": tgt_cov,
        "provenance_note": provenance_note or (
            f"Mapped {src_reg_id} -> {tgt_reg_id} ({mapping_kind}): {equivalence} "
            f"(overlap={overlap} aa, source_coverage={src_cov:.3f}, target_coverage={tgt_cov:.3f})."
        ),
    }
    if alignment_gaps is not None:
        result["alignment_gaps"] = _require_positive_int(alignment_gaps, "alignment_gaps", minimum=0)
    if checked_correspondences:
        result["residue_correspondences"] = checked_correspondences
    if inferred_uncertainty:
        result["mapping_uncertainty"] = inferred_uncertainty
    return result


def build_region_observation(
    *,
    observation_id: str,
    region: Mapping[str, Any],
    evidence_kind: str,
    source_kind: str,
    method: str,
    observed_effect: str,
    interpretation: str,
    polarity: str,
    primary_experiment_key: str,
    assay_conditions: str | None = None,
    tested_construct_region_id: str | None = None,
    mutation_region_ids: Sequence[str] = (),
    raw_score: float | None = None,
    score_metric: str | None = None,
    derived_from_observation_ids: Sequence[str] = (),
    limitations: str | None = None,
    evidence: Sequence[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    """Create and validate a standardized RegionObservation."""
    _require_token(observation_id, "observation_id")
    reg_id = _require_token(region.get("region_id"), "region.region_id")
    seq_id = _require_token(region.get("sequence_id"), "region.sequence_id")
    if evidence_kind not in EVIDENCE_KINDS:
        raise ValueError(f"invalid evidence_kind: {evidence_kind!r}")
    if source_kind not in OBSERVATION_SOURCES:
        raise ValueError(f"invalid source_kind: {source_kind!r}")
    if polarity not in POLARITIES:
        raise ValueError(f"invalid polarity: {polarity!r}")
    _require_token(primary_experiment_key, "primary_experiment_key", EXPERIMENT_KEY_RE)
    if (raw_score is not None) ^ (score_metric is not None):
        raise ValueError("raw_score and score_metric must be provided together or both omitted")
    if score_metric is not None and score_metric not in SCORE_METRICS:
        raise ValueError(f"invalid score_metric: {score_metric!r}")

    obs: dict[str, Any] = {
        "observation_id": observation_id,
        "region_id": reg_id,
        "sequence_id": seq_id,
        "evidence_kind": evidence_kind,
        "source_kind": source_kind,
        "method": actual_text(method, f"observation[{observation_id}].method"),
        "observed_effect": actual_text(observed_effect, f"observation[{observation_id}].observed_effect"),
        "interpretation": actual_text(interpretation, f"observation[{observation_id}].interpretation"),
        "polarity": polarity,
        "primary_experiment_key": primary_experiment_key,
    }
    if assay_conditions is not None:
        obs["assay_conditions"] = actual_text(
            assay_conditions, f"observation[{observation_id}].assay_conditions"
        )
    if tested_construct_region_id is not None:
        obs["tested_construct_region_id"] = _require_token(
            tested_construct_region_id, "tested_construct_region_id"
        )
    if mutation_region_ids:
        obs["mutation_region_ids"] = [
            _require_token(mid, "mutation_region_id") for mid in mutation_region_ids
        ]
    if raw_score is not None:
        if isinstance(raw_score, bool) or not isinstance(raw_score, (int, float)):
            raise ValueError(f"raw_score must be numeric: {raw_score!r}")
        obs["raw_score"] = float(raw_score)
        obs["score_metric"] = score_metric
    if derived_from_observation_ids:
        obs["derived_from_observation_ids"] = [
            _require_token(oid, "derived_from_observation_id") for oid in derived_from_observation_ids
        ]
    if limitations is not None:
        obs["limitations"] = actual_text(limitations, f"observation[{observation_id}].limitations")
    if evidence:
        obs["evidence"] = [dict(item) for item in evidence]
    return obs


def normalize_pfam_member_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    observation_id: str | None = None,
    region_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Normalize a DUFMech PfamMemberRow dict into (SequenceRegion, RegionObservation)."""
    pfam_id = str(row["pfam_id"])
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"Pfam member row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    fragments = list(row.get("fragments") or ())
    if not fragments:
        raise ValueError(f"Pfam member row for {acc}/{pfam_id} has no fragments")
    sorted_frags = sorted(
        ({"start": int(f["start"]), "end": int(f["end"])} for f in fragments),
        key=lambda f: (f["start"], f["end"]),
    )
    is_discontinuous = len(sorted_frags) > 1
    coord_text = ", ".join(f"{f['start']}-{f['end']}" for f in sorted_frags)
    reg_id = region_id or f"reg_{acc}_{pfam_id}_{sorted_frags[0]['start']}_{sorted_frags[-1]['end']}"
    region = build_sequence_region(
        region_id=reg_id,
        sequence_identity=sequence_identity,
        label=f"{pfam_id} profile match on {acc} ({coord_text})",
        region_kind="DISCONTINUOUS_DOMAIN" if is_discontinuous else "DOMAIN_HIT",
        coordinate_status="DISCONTINUOUS" if is_discontinuous else "EXACT",
        intervals=sorted_frags,
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text=coord_text,
        conversion_provenance="InterPro/Pfam 1-based inclusive fragment coordinates on UniProt sequence.",
        pfam_id=pfam_id,
    )
    obs_id = observation_id or f"obs_pfam_{acc}_{pfam_id}_{sorted_frags[0]['start']}_{sorted_frags[-1]['end']}"
    exp_key = f"HMM:{pfam_id}/{acc}_{sorted_frags[0]['start']}-{sorted_frags[-1]['end']}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind="COMPUTATIONAL",
        source_kind="INTERPRO_PFAM",
        method="Pfam profile HMM match via InterPro",
        observed_effect=f"Significant profile HMM match to {pfam_id} across {coord_text}.",
        interpretation=f"Region {coord_text} of {acc} belongs to domain family {pfam_id}; sequence membership alone does not establish catalytic or biological function.",
        polarity="POSITIVE",
        primary_experiment_key=exp_key,
        limitations="Computational profile HMM membership; does not demonstrate biochemical activity.",
    )
    return region, observation


def normalize_pdbe_kb_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    target_domain_region: Mapping[str, Any] | None = None,
    observation_id: str | None = None,
    region_id: str | None = None,
    mapping_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any] | None]:
    """Normalize a DUFMech PdbeKbAnnotationRow dict into (SequenceRegion, RegionObservation, CoordinateMapping)."""
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"PDBe-KB row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    pdb_id = str(row["pdb_id"]).lower()
    chain_id = str(row["chain_id"])
    u_start = int(row["uniprot_start"])
    u_end = int(row["uniprot_end"])
    reg_id = region_id or f"reg_pdbe_{acc}_{pdb_id}_{chain_id}_{u_start}_{u_end}"
    region = build_sequence_region(
        region_id=reg_id,
        sequence_identity=sequence_identity,
        label=f"PDBe-KB {pdb_id.upper()} chain {chain_id} ({row.get('annotation_type', 'site')}: {row.get('annotation_label', pdb_id)})",
        region_kind="STRUCTURAL_OBSERVATION_REGION",
        coordinate_status="EXACT",
        intervals=[{"start": u_start, "end": u_end}],
        source_coordinate_system="PDB_AUTHOR",
        source_coordinates_text=f"PDB:{pdb_id}:{chain_id} -> UniProt:{acc}:{u_start}-{u_end}",
        conversion_provenance="PDBe-KB SIFTS residue-level mapping from PDB chain to 1-based UniProt coordinates.",
    )
    correspondences: list[dict[str, Any]] = []
    pdb_res_list = list(row.get("pdb_residues") or ())
    for idx, res in enumerate(pdb_res_list):
        match = re.fullmatch(r"^(-?[0-9]+)([A-Za-z0-9]?)$", str(res).strip())
        if match and int(match.group(1)) >= 1:
            corr: dict[str, Any] = {
                "source_position": int(match.group(1)),
                "target_position": min(u_start + idx, u_end),
            }
            if match.group(2):
                corr["pdb_insertion_code"] = match.group(2)
            correspondences.append(corr)
    mutations = list(row.get("mutations") or ())
    uncertainty = (
        f"Engineered mutations in structure: {', '.join(mutations)}." if mutations else None
    )
    mapping = None
    if target_domain_region is not None:
        map_id = mapping_id or f"map_pdbe_{pdb_id}_{chain_id}_to_{target_domain_region['region_id']}"
        mapping = classify_region_mapping(
            mapping_id=map_id,
            source_region=region,
            target_region=target_domain_region,
            source_sequence=sequence_identity,
            target_sequence=sequence_identity,
            mapping_kind="STRUCTURE_TO_UNIPROT",
            residue_correspondences=correspondences,
            mapping_uncertainty=uncertainty,
        )
    obs_id = observation_id or f"obs_pdbe_{acc}_{pdb_id}_{chain_id}_{u_start}_{u_end}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind="EXPERIMENTAL",
        source_kind="PDBE_KB",
        method=f"PDBe-KB structural annotation ({row.get('annotation_type', 'structure')}) on PDB:{pdb_id.upper()}",
        observed_effect=(
            f"Observed {row.get('annotation_type', 'structural feature')} "
            f"{row.get('annotation_label', pdb_id)} across UniProt residues {u_start}..{u_end}."
        ),
        interpretation=(
            f"Structural observation of {row.get('annotation_label', pdb_id)} at {u_start}..{u_end} "
            "supports ligand/macromolecular contact or fold geometry, not catalytic turnover by itself."
        ),
        polarity="POSITIVE",
        primary_experiment_key=f"PDB:{pdb_id}/{acc}_{u_start}-{u_end}/{row.get('annotation_type', 'site')}",
        limitations=uncertainty or "Crystallographic/cryo-EM contact does not by itself prove enzymatic catalysis.",
    )
    return region, observation, mapping


def normalize_cdsearch_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    observation_id: str | None = None,
    region_id: str | None = None,
    primary_experiment_key: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Normalize a DUFMech CdSearchDomainRow dict into (SequenceRegion, RegionObservation)."""
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"CD-Search row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    cdd_acc = str(row["cdd_accession"])
    start = int(row["start"])
    end = int(row["end"])
    reg_id = region_id or f"reg_cdd_{acc}_{cdd_acc}_{start}_{end}"
    region = build_sequence_region(
        region_id=reg_id,
        sequence_identity=sequence_identity,
        label=f"CD-Search {cdd_acc} ({row.get('short_name', cdd_acc)}) on {acc} ({start}-{end})",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": start, "end": end}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text=f"{start}-{end}",
        conversion_provenance="NCBI CD-Search 1-based inclusive hit coordinates.",
    )
    e_val = float(row["e_value"]) if row.get("e_value") is not None else None
    obs_id = observation_id or f"obs_cdd_{acc}_{cdd_acc}_{start}_{end}"
    exp_key = primary_experiment_key or f"CDD:{cdd_acc}/{acc}_{start}-{end}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind="COMPUTATIONAL",
        source_kind="CDSEARCH",
        method=f"NCBI CD-Search RPS-BLAST ({row.get('hit_type', 'specific')})",
        observed_effect=f"CD-Search hit to {cdd_acc} ({row.get('short_name', cdd_acc)}) at {start}..{end}.",
        interpretation=f"Sequence region {start}..{end} matches conserved domain model {cdd_acc}.",
        polarity="POSITIVE",
        raw_score=e_val,
        score_metric="E_VALUE" if e_val is not None else None,
        primary_experiment_key=exp_key,
        limitations="Computational conserved-domain search match; not direct experimental demonstration.",
    )
    return region, observation


def normalize_cath_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    observation_id: str | None = None,
    region_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Normalize a DUFMech CathFunFamRow dict into (SequenceRegion, RegionObservation)."""
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"CATH row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    superfamily_id = str(row["cath_superfamily_id"])
    funfam_id = str(row.get("funfam_id", "0"))
    start = int(row.get("uniprot_start") or row["member_start"])
    end = int(row.get("uniprot_end") or row["member_end"])
    reg_id = region_id or f"reg_cath_{acc}_{superfamily_id.replace('.', '_')}_{start}_{end}"
    region = build_sequence_region(
        region_id=reg_id,
        sequence_identity=sequence_identity,
        label=f"CATH {superfamily_id}/FF:{funfam_id} on {acc} ({start}-{end})",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": start, "end": end}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text=f"{start}-{end}",
        conversion_provenance="CATH-Gene3D / FunFam 1-based inclusive coordinates.",
    )
    conf = float(row["confidence"]) if row.get("confidence") is not None else None
    obs_id = observation_id or f"obs_cath_{acc}_{superfamily_id.replace('.', '_')}_{start}_{end}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind="COMPUTATIONAL",
        source_kind="CATH_FUNFAM",
        method="CATH FunFam HMM assignment",
        observed_effect=f"CATH superfamily {superfamily_id} FunFam {funfam_id} hit ({row.get('funfam_name', 'unnamed')}) at {start}..{end}.",
        interpretation=f"Predicted structural superfamily {superfamily_id} and functional family {funfam_id} on {start}..{end}.",
        polarity="POSITIVE",
        raw_score=conf,
        score_metric="CATH_CONFIDENCE" if conf is not None else None,
        primary_experiment_key=f"CATH:{superfamily_id}:FF{funfam_id}/{acc}_{start}-{end}",
        limitations="Computational structural/functional family assignment.",
    )
    return region, observation


def normalize_ncbifam_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    observation_id: str | None = None,
    region_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Normalize a DUFMech NcbifamHitRow dict into (SequenceRegion, RegionObservation)."""
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"NCBIfam row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    hmm_acc = str(row["hmm_accession"])
    start = int(row["seq_start"])
    end = int(row["seq_end"])
    reg_id = region_id or f"reg_ncbifam_{acc}_{hmm_acc}_{start}_{end}"
    region = build_sequence_region(
        region_id=reg_id,
        sequence_identity=sequence_identity,
        label=f"NCBIfam {hmm_acc} ({row.get('hmm_name', hmm_acc)}) on {acc} ({start}-{end})",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": start, "end": end}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text=f"{start}-{end}",
        conversion_provenance="NCBIfam HMMER 1-based sequence coordinates.",
    )
    e_val = float(row["e_value"]) if row.get("e_value") is not None else None
    obs_id = observation_id or f"obs_ncbifam_{acc}_{hmm_acc}_{start}_{end}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind="COMPUTATIONAL",
        source_kind="NCBIFAM",
        method="NCBIfam profile HMM search",
        observed_effect=f"NCBIfam {hmm_acc} match across {start}..{end}.",
        interpretation=f"Predicted NCBIfam family {hmm_acc} ({row.get('product_name', hmm_acc)}) on {start}..{end}.",
        polarity="POSITIVE",
        raw_score=e_val,
        score_metric="E_VALUE" if e_val is not None else None,
        primary_experiment_key=f"NCBIFAM:{hmm_acc}/{acc}_{start}-{end}",
        limitations="Computational HMM family hit.",
    )
    return region, observation


def normalize_quickgo_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    region: Mapping[str, Any] | None = None,
    observation_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Normalize a DUFMech QuickGoAnnotationRow dict into (SequenceRegion, RegionObservation).

    Unless an explicit localized region is provided, GO annotations on UniProt
    accessions apply to the whole protein (WHOLE_PROTEIN_UNLOCALIZED) and do not
    by themselves localize a function to an individual domain.
    """
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"QuickGO row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    go_id = str(row["go_id"])
    go_name = str(row.get("go_name") or go_id)
    ev_code = str(row.get("go_evidence") or row.get("eco_id") or "IEA").strip()
    if ev_code in EXPERIMENTAL_GO_EVIDENCE_CODES:
        ev_kind = "EXPERIMENTAL"
    elif ev_code in CONTEXTUAL_GO_EVIDENCE_CODES:
        ev_kind = "CONTEXTUAL"
    else:
        ev_kind = "COMPUTATIONAL"

    qualifier = str(row.get("qualifier") or "").upper()
    polarity = "NEGATIVE" if "NOT" in qualifier else "POSITIVE"
    if region is None:
        seq_len = int(sequence_identity["sequence_length"])
        region = build_sequence_region(
            region_id=f"reg_{acc}_full_1_{seq_len}",
            sequence_identity=sequence_identity,
            label=f"Full-length {acc} (1-{seq_len}, unlocalized GO annotation)",
            region_kind="FULL_LENGTH_PROTEIN",
            coordinate_status="WHOLE_PROTEIN_UNLOCALIZED",
            intervals=[{"start": 1, "end": seq_len}],
            source_coordinate_system="UNIPROT_CANONICAL",
            source_coordinates_text=f"1-{seq_len}",
            conversion_provenance="QuickGO protein-level annotation anchored to full-length UniProt sequence.",
        )

    ref = str(row.get("reference") or row.get("assigned_by") or "QuickGO").strip()
    safe_ref = re.sub(r"[^A-Za-z0-9_.:/-]", "_", ref)
    exp_key = f"{safe_ref}/{acc}/{go_id}"
    obs_id = observation_id or f"obs_quickgo_{acc}_{go_id.replace(':', '_')}_{ev_code.replace(':', '_')}"
    observation = build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind=ev_kind,
        source_kind="QUICKGO",
        method=f"QuickGO annotation ({ev_code}, assigned by {row.get('assigned_by', 'QuickGO')})",
        observed_effect=f"QuickGO annotation {go_id} ({go_name}) with qualifier {qualifier or 'enables/involved_in'} and reference {ref}.",
        interpretation=f"Protein {acc} is annotated with {go_id} ({go_name}).",
        polarity=polarity,
        primary_experiment_key=exp_key,
        limitations=(
            "Protein-level GO annotation without explicit domain range does not localize "
            "the function to a specific DUF domain in a multidomain protein."
            if region.get("coordinate_status") == "WHOLE_PROTEIN_UNLOCALIZED"
            else None
        ),
    )
    return dict(region), observation


def normalize_rhea_row(
    row: Mapping[str, Any],
    *,
    sequence_identity: Mapping[str, Any],
    region: Mapping[str, Any],
    evidence_kind: str = "COMPUTATIONAL",
    primary_experiment_key: str | None = None,
    observation_id: str | None = None,
) -> dict[str, Any]:
    """Normalize a DUFMech RheaReactionRow dict into a RegionObservation."""
    acc = str(row["uniprot_accession"])
    if acc != sequence_identity.get("uniprot_accession"):
        raise ValueError(
            f"Rhea row accession {acc} != sequence_identity {sequence_identity.get('uniprot_accession')}"
        )
    rhea_id = str(row["rhea_id"])
    equation = str(row.get("equation") or rhea_id)
    obs_id = observation_id or f"obs_rhea_{acc}_{rhea_id.replace(':', '_')}"
    exp_key = primary_experiment_key or f"RHEA:{rhea_id}/{acc}"
    return build_region_observation(
        observation_id=obs_id,
        region=region,
        evidence_kind=evidence_kind,
        source_kind="RHEA",
        method="Rhea biochemical reaction annotation",
        observed_effect=f"Rhea reaction {rhea_id}: {equation}.",
        interpretation=f"Catalytic reaction {rhea_id} ({equation}) associated with {acc}.",
        polarity="POSITIVE",
        primary_experiment_key=exp_key,
        limitations=(
            "Database reaction cross-reference; independent experimental status depends on "
            "primary assay citation and domain-level localization."
        ),
    )


def combine_scores_strictly(observations: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Verify whether observation scores share a single compatible metric.

    Scores from different methods (e.g. E_VALUE vs BITSCORE vs PLDDT vs KM_MM)
    are not interchangeable probabilities and cannot be combined into a scalar.
    """
    scored = [
        (obs["observation_id"], obs["score_metric"], float(obs["raw_score"]))
        for obs in observations
        if obs.get("raw_score") is not None and obs.get("score_metric") is not None
    ]
    if not scored:
        return {"combinable": True, "metric": None, "values": []}
    metrics = sorted({metric for _, metric, _ in scored})
    if len(metrics) > 1:
        raise ValueError(
            f"cannot combine heterogeneous score metrics {metrics} across observations "
            f"{[oid for oid, _, _ in scored]}: scores from different methods are not "
            "interchangeable probabilities"
        )
    metric = metrics[0]
    values = [val for _, _, val in scored]
    return {
        "combinable": True,
        "metric": metric,
        "values": values,
        "best_value": min(values) if metric in {"E_VALUE", "KM_MM"} else max(values),
    }


def deduplicate_observations(
    observations: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Group observations by underlying primary_experiment_key or derivation chain.

    Repeated reports of the same experiment, mirrored database rows (e.g. QuickGO
    + Rhea + curated literature citing the same PMID and construct, or InterPro +
    Pfam + CD-Search reporting the same profile hit), and observations explicitly
    linked via ``derived_from_observation_ids`` are collapsed into a single
    ``EvidenceGroup`` so they are never counted as independent confirmation.
    """
    if not observations:
        return []
    obs_by_id: dict[str, Mapping[str, Any]] = {}
    for obs in observations:
        oid = _require_token(obs.get("observation_id"), "observation.observation_id")
        if oid in obs_by_id:
            raise ValueError(f"duplicate observation_id: {oid}")
        obs_by_id[oid] = obs

    def _resolve_root_keys(start_oid: str, trail: set[str]) -> set[str]:
        parents = list(obs_by_id[start_oid].get("derived_from_observation_ids") or ())
        if not parents:
            return {str(obs_by_id[start_oid]["primary_experiment_key"])}
        roots: set[str] = set()
        for parent_id in parents:
            pid = str(parent_id)
            if pid not in obs_by_id:
                raise ValueError(
                    f"observation {start_oid} references unknown derived_from_observation_id {pid!r}"
                )
            if pid in trail:
                raise ValueError(f"cycle in derived_from_observation_ids involving {pid}")
            roots.update(_resolve_root_keys(pid, trail | {pid}))
        return roots

    # Resolve canonical primary_experiment_key across all derived_from_observation_ids chains.
    canonical_key: dict[str, str] = {}
    for oid in obs_by_id:
        root_keys = sorted(_resolve_root_keys(oid, {oid}))
        if len(root_keys) > 1:
            raise ValueError(
                f"observation {oid} derives from observations with conflicting primary_experiment_key values {root_keys}"
            )
        canonical_key[oid] = root_keys[0]

    grouped: dict[tuple[str, str, str], list[Mapping[str, Any]]] = {}
    for oid, obs in obs_by_id.items():
        key = (
            canonical_key[oid],
            str(obs["evidence_kind"]),
            str(obs["polarity"]),
        )
        grouped.setdefault(key, []).append(obs)

    evidence_groups: list[dict[str, Any]] = []
    for idx, ((exp_key, ev_kind, polarity), members) in enumerate(grouped.items(), start=1):
        member_ids = [str(m["observation_id"]) for m in members]
        sources = sorted({str(m["source_kind"]) for m in members})
        safe_slug = re.sub(r"[^A-Za-z0-9_-]", "_", exp_key).strip("_")[:48]
        group_id = f"grp_{idx:02d}_{safe_slug}"
        if len(members) > 1:
            rationale = (
                f"Deduplicated {len(members)} observations ({', '.join(member_ids)}) from sources "
                f"[{', '.join(sources)}] sharing primary experiment/prediction key '{exp_key}' "
                "into 1 independent evidence unit so mirrored database records or repeated reports "
                "are not counted as independent confirmation."
            )
        else:
            rationale = (
                f"Single primary observation {member_ids[0]} ({sources[0]}) for '{exp_key}'."
            )
        evidence_groups.append({
            "group_id": group_id,
            "primary_experiment_key": exp_key,
            "evidence_kind": ev_kind,
            "polarity": polarity,
            "observation_ids": member_ids,
            "deduplication_rationale": rationale,
        })
    return evidence_groups


def _is_localized_domain_mapping(
    mapping: Mapping[str, Any],
    *,
    regions_by_id: Mapping[str, Mapping[str, Any]],
    has_domain_internal_mutation: bool = False,
) -> tuple[bool, str | None]:
    """Determine whether a CoordinateMapping supports domain-level localization."""
    eq = str(mapping.get("equivalence_status", ""))
    src_reg = regions_by_id.get(str(mapping.get("source_region_id", "")), {})
    if eq in {"EXACT_MATCH", "DISCONTINUOUS_MAPPING", "DOMAIN_CONTAINS_REGION", "RESIDUE_INSIDE_REGION"}:
        return True, None
    if eq == "CONSTRUCT_CONTAINS_DOMAIN":
        if (
            src_reg.get("coordinate_status") == "WHOLE_PROTEIN_UNLOCALIZED"
            or src_reg.get("region_kind") == "FULL_LENGTH_PROTEIN"
        ) and not has_domain_internal_mutation:
            return (
                False,
                (
                    f"Whole-protein observation on {src_reg.get('region_id')} contains target domain "
                    f"{mapping.get('target_region_id')} without a domain-internal catalytic mutation "
                    "or isolated construct; effect cannot be localized to the DUF alone."
                ),
            )
        return True, None
    if eq == "PARTIAL_OVERLAP_NOT_EQUIVALENT":
        return (
            False,
            (
                f"Coordinate mapping {mapping.get('mapping_id')} has PARTIAL_OVERLAP_NOT_EQUIVALENT "
                f"(overlap={mapping.get('overlap_residues')} aa); partial overlap does not establish "
                "domain localization."
            ),
        )
    if eq == "DISJOINT_OUTSIDE_REGION":
        return (
            False,
            (
                f"Coordinate mapping {mapping.get('mapping_id')} is DISJOINT_OUTSIDE_REGION "
                f"({mapping.get('source_region_id')} lies outside {mapping.get('target_region_id')})."
            ),
        )
    if eq == "SEQUENCE_VERSION_MISMATCH":
        return (
            False,
            (
                f"Coordinate mapping {mapping.get('mapping_id')} has SEQUENCE_VERSION_MISMATCH; "
                "coordinates cannot be transferred across mismatched sequence versions/isoforms/checksums."
            ),
        )
    return (
        False,
        f"Coordinate mapping {mapping.get('mapping_id')} has unresolved status {eq!r}.",
    )


def synthesize_region_claim(
    *,
    claim_id: str,
    label: str,
    function_aspect: str,
    target_region: Mapping[str, Any],
    regions_by_id: Mapping[str, Mapping[str, Any]],
    observations: Sequence[Mapping[str, Any]],
    evidence_groups: Sequence[Mapping[str, Any]],
    coordinate_mappings: Sequence[Mapping[str, Any]] = (),
    ontology_term_id: str | None = None,
    ontology_term_label: str | None = None,
    requested_scope: str | None = None,
    additional_scope_blocks: Sequence[str] = (),
    discriminating_experiments: Sequence[str] = (),
) -> dict[str, Any]:
    """Synthesize an evidence-graded functional claim for a target sequence region.

    Enforces:
    - Separation of observation from interpretation and deduplication via EvidenceGroups.
    - Coordinate localization: whole-protein unlocalized assays, partial overlaps,
      disjoint mutations (including mutations in inter-segment gaps of discontinuous
      domains), and sequence-version mismatches cannot produce EXPERIMENTALLY_DEMONSTRATED.
    - Scope discipline: claims on a tested construct or region are not silently
      promoted to SPECIFIC_PROTEIN or FAMILY_WIDE, and negative/untested paralogues
      explicitly block family-wide transfer.
    - Missing evidence is INSUFFICIENT_EVIDENCE (never NEGATIVE_EVIDENCE_ONLY).
    """
    _require_token(claim_id, "claim_id")
    if function_aspect not in FUNCTION_ASPECTS:
        raise ValueError(f"invalid function_aspect: {function_aspect!r}")
    if ontology_term_id is not None and not ONTOLOGY_TERM_RE.fullmatch(ontology_term_id):
        raise ValueError(f"invalid ontology_term_id: {ontology_term_id!r}")
    target_reg_id = _require_token(target_region.get("region_id"), "target_region.region_id")
    obs_by_id = {str(o["observation_id"]): o for o in observations}
    mappings_by_pair: dict[tuple[str, str], Mapping[str, Any]] = {}
    for m in coordinate_mappings:
        mappings_by_pair[(str(m["source_region_id"]), str(m["target_region_id"]))] = m

    has_disjoint_mutation_block: list[str] = []
    supporting_group_ids: list[str] = []
    contradicting_group_ids: list[str] = []
    supporting_obs_ids: list[str] = []
    contradicting_obs_ids: list[str] = []
    relevant_mapping_ids: list[str] = []
    localization_blocks: list[str] = []

    localized_exp_pos_groups = 0
    localized_exp_neg_groups = 0
    comp_pos_groups = 0
    homolog_exp_pos_groups = 0

    for grp in evidence_groups:
        gid = str(grp["group_id"])
        g_kind = str(grp["evidence_kind"])
        g_pol = str(grp["polarity"])
        member_obs = [obs_by_id[oid] for oid in grp["observation_ids"] if oid in obs_by_id]
        if not member_obs:
            continue

        # Determine how this group's regions map to target_region_id, scoping mutation
        # localization strictly to the observation being evaluated.
        group_localized = False
        group_homolog_aligned = False
        group_disjoint_mutation = False
        for obs in member_obs:
            obs_has_internal_mutation = False
            obs_disjoint_mutation = False
            for mut_reg_id in obs.get("mutation_region_ids") or ():
                m_mut = mappings_by_pair.get((str(mut_reg_id), target_reg_id))
                if m_mut is None:
                    obs_disjoint_mutation = True
                    group_disjoint_mutation = True
                    unmapped_msg = (
                        f"Observation {obs['observation_id']} references mutation_region_id "
                        f"{mut_reg_id} without a CoordinateMapping to target region {target_reg_id}."
                    )
                    if unmapped_msg not in has_disjoint_mutation_block:
                        has_disjoint_mutation_block.append(unmapped_msg)
                    if unmapped_msg not in localization_blocks:
                        localization_blocks.append(unmapped_msg)
                else:
                    mid = str(m_mut["mapping_id"])
                    if mid not in relevant_mapping_ids:
                        relevant_mapping_ids.append(mid)
                    eq_mut = str(m_mut.get("equivalence_status", ""))
                    if (
                        eq_mut == "RESIDUE_INSIDE_REGION"
                        and obs.get("evidence_kind") == "EXPERIMENTAL"
                        and obs.get("polarity") == "POSITIVE"
                    ):
                        obs_has_internal_mutation = True
                    elif eq_mut in {
                        "DISJOINT_OUTSIDE_REGION",
                        "PARTIAL_OVERLAP_NOT_EQUIVALENT",
                        "SEQUENCE_VERSION_MISMATCH",
                        "UNRESOLVED_MAPPING",
                    }:
                        obs_disjoint_mutation = True
                        group_disjoint_mutation = True
                        mut_block = (
                            f"Perturbation/mutation region {mut_reg_id} maps to {target_reg_id} as "
                            f"{eq_mut} ({m_mut.get('mapping_uncertainty') or m_mut.get('provenance_note')})."
                        )
                        if mut_block not in has_disjoint_mutation_block:
                            has_disjoint_mutation_block.append(mut_block)
                        if mut_block not in localization_blocks:
                            localization_blocks.append(mut_block)

            obs_reg_id = str(obs["region_id"])
            if obs_reg_id == target_reg_id:
                if target_region.get("coordinate_status") not in {
                    "WHOLE_PROTEIN_UNLOCALIZED",
                    "UNKNOWN_LOCALIZATION",
                }:
                    if not obs_disjoint_mutation:
                        group_localized = True
                elif obs_has_internal_mutation and not obs_disjoint_mutation:
                    group_localized = True
                else:
                    localization_blocks.append(
                        f"Target region {target_reg_id} has {target_region.get('coordinate_status')}; "
                        "cannot localize effect to a specific domain."
                    )
            else:
                m = mappings_by_pair.get((obs_reg_id, target_reg_id)) or mappings_by_pair.get(
                    (target_reg_id, obs_reg_id)
                )
                if m is not None:
                    mid = str(m["mapping_id"])
                    if mid not in relevant_mapping_ids:
                        relevant_mapping_ids.append(mid)
                    if m.get("mapping_kind") in {"HOMOLOG_ALIGNMENT", "PROFILE_TO_SEQUENCE"} and (
                        obs.get("sequence_id") != target_region.get("sequence_id")
                    ):
                        group_homolog_aligned = True
                    else:
                        ok, block_msg = _is_localized_domain_mapping(
                            m,
                            regions_by_id=regions_by_id,
                            has_domain_internal_mutation=(
                                obs_has_internal_mutation and not obs_disjoint_mutation
                            ),
                        )
                        if ok and not obs_disjoint_mutation:
                            group_localized = True
                        elif block_msg and block_msg not in localization_blocks:
                            localization_blocks.append(block_msg)
                else:
                    unmapped_obs_msg = (
                        f"Observation {obs['observation_id']} on {obs_reg_id} has no "
                        f"CoordinateMapping to target region {target_reg_id}."
                    )
                    if unmapped_obs_msg not in localization_blocks:
                        localization_blocks.append(unmapped_obs_msg)

        if g_pol == "POSITIVE":
            supporting_group_ids.append(gid)
            for obs in member_obs:
                if str(obs["observation_id"]) not in supporting_obs_ids:
                    supporting_obs_ids.append(str(obs["observation_id"]))
            if g_kind == "EXPERIMENTAL":
                if group_localized and not group_disjoint_mutation:
                    localized_exp_pos_groups += 1
                elif group_homolog_aligned:
                    homolog_exp_pos_groups += 1
            else:
                comp_pos_groups += 1
        elif g_pol == "NEGATIVE":
            contradicting_group_ids.append(gid)
            for obs in member_obs:
                if str(obs["observation_id"]) not in contradicting_obs_ids:
                    contradicting_obs_ids.append(str(obs["observation_id"]))
            if g_kind == "EXPERIMENTAL" and group_localized:
                localized_exp_neg_groups += 1

    # Check if heterogeneous score metrics exist across observations; report them clearly
    # without combining them into a single probability.
    score_summaries: list[str] = []
    for obs in observations:
        if obs.get("raw_score") is not None and obs.get("score_metric") is not None:
            score_summaries.append(
                f"{obs['observation_id']}:{obs['score_metric']}={obs['raw_score']}"
            )

    scope_blocks: list[str] = list(dict.fromkeys([*localization_blocks, *additional_scope_blocks]))
    has_exp_pos_obs = any(
        obs.get("evidence_kind") == "EXPERIMENTAL" and obs.get("polarity") == "POSITIVE"
        for obs in observations
    )

    # Determine synthesis_status and claimed_scope.
    if not supporting_group_ids and not contradicting_group_ids:
        synthesis_status = "INSUFFICIENT_EVIDENCE"
        effective_aspect = function_aspect
        effective_scope = "UNRESOLVED_SCOPE"
        if not scope_blocks:
            scope_blocks.append(
                "No experimental or computational observations are anchored to this region; "
                "absence of annotation is insufficient evidence, not negative evidence."
            )
    elif localized_exp_neg_groups > 0 and (localized_exp_pos_groups > 0 or has_exp_pos_obs):
        synthesis_status = "CONFLICTING_UNRESOLVED"
        effective_aspect = function_aspect
        effective_scope = "UNRESOLVED_SCOPE"
        scope_blocks.append(
            f"Conflicting localized experimental evidence on {target_reg_id}: "
            f"{localized_exp_pos_groups} localized positive vs {localized_exp_neg_groups} negative "
            "independent evidence group(s)."
        )
    elif localized_exp_neg_groups > 0 and localized_exp_pos_groups == 0 and not has_exp_pos_obs:
        synthesis_status = "NEGATIVE_EVIDENCE_ONLY"
        effective_aspect = function_aspect
        effective_scope = requested_scope or "TESTED_REGION_ONLY"
        if effective_scope in {"FAMILY_WIDE", "CONSERVED_SUBFAMILY"}:
            effective_scope = "TESTED_REGION_ONLY"
        scope_blocks.append(
            f"Direct experimental assay on {target_reg_id} yielded negative results; "
            "activity is absent under tested conditions and must not be inferred from active homologs."
        )
    elif localized_exp_pos_groups > 0 and not has_disjoint_mutation_block:
        synthesis_status = "EXPERIMENTALLY_DEMONSTRATED"
        effective_aspect = function_aspect
        # Determine narrowest supported scope.
        tested_construct_used = any(
            obs.get("tested_construct_region_id")
            or regions_by_id.get(str(obs["region_id"]), {}).get("region_kind") == "EXPERIMENTAL_CONSTRUCT"
            for obs in observations
            if str(obs["observation_id"]) in supporting_obs_ids
        )
        default_scope = "TESTED_CONSTRUCT" if tested_construct_used else "TESTED_REGION_ONLY"
        if requested_scope in {"FAMILY_WIDE", "CONSERVED_SUBFAMILY", "SPECIFIC_PROTEIN"} and scope_blocks:
            effective_scope = default_scope
            scope_blocks.append(
                f"Requested broader scope '{requested_scope}' was restricted to '{effective_scope}' "
                "because transfer blocks are present."
            )
        else:
            effective_scope = requested_scope or default_scope
        if effective_scope in {"TESTED_CONSTRUCT", "TESTED_REGION_ONLY"} and not any(
            "full-length" in b.lower() or "paralogue" in b.lower() or "family-wide" in b.lower()
            for b in scope_blocks
        ):
            scope_blocks.append(
                f"Assertion is restricted to {effective_scope} ({target_reg_id}); "
                "cannot be silently transferred to untested full-length protein contexts or all family members."
            )
    elif any( obs.get("evidence_kind") == "EXPERIMENTAL" for obs in observations ) and localization_blocks:
        # Experimental data exists, but coordinate mapping failed localization (e.g., disjoint
        # mutation outside domain, partial overlap, whole-protein unlocalized, or version mismatch).
        synthesis_status = "CONFLICTING_UNRESOLVED"
        effective_aspect = function_aspect
        effective_scope = "UNRESOLVED_SCOPE"
    elif homolog_exp_pos_groups > 0 and not contradicting_group_ids and not additional_scope_blocks:
        synthesis_status = "SUPPORTED_INFERENCE"
        effective_aspect = function_aspect
        effective_scope = "TESTED_REGION_ONLY"
        scope_blocks.append(
            "Inferred from experimentally characterized homolog region with explicit residue "
            "correspondence; direct biochemical assay on this sequence has not yet been performed."
        )
    else:
        synthesis_status = "COMPUTATIONAL_HYPOTHESIS"
        effective_aspect = function_aspect
        effective_scope = "TESTED_REGION_ONLY"
        if not scope_blocks:
            scope_blocks.append(
                "Supported only by computational predictions or contextual co-occurrence; "
                "requires direct experimental demonstration on an isolated domain or catalytic mutant."
            )

    score_note = (
        f" Retained method-specific scores without cross-metric probability combination: "
        f"{', '.join(score_summaries)}."
        if score_summaries
        else ""
    )
    explanation = (
        f"Synthesized {len(supporting_obs_ids)} supporting observation(s) across "
        f"{len(supporting_group_ids)} independent supporting evidence group(s) and "
        f"{len(contradicting_obs_ids)} contradicting observation(s) across "
        f"{len(contradicting_group_ids)} contradicting group(s) for target region "
        f"{target_reg_id} -> status={synthesis_status}, scope={effective_scope}.{score_note}"
    )
    scope_rationale = (
        f"Scope is {effective_scope} on {target_reg_id} ({target_region.get('label')}) "
        f"based on coordinate equivalence {[mappings_by_pair.get((r, target_reg_id), {}).get('equivalence_status') for r in regions_by_id if (r, target_reg_id) in mappings_by_pair] or [target_region.get('coordinate_status')]}."
    )

    claim: dict[str, Any] = {
        "claim_id": claim_id,
        "label": actual_text(label, f"claim[{claim_id}].label"),
        "function_aspect": effective_aspect,
        "target_region_id": target_reg_id,
        "claimed_scope": effective_scope,
        "synthesis_status": synthesis_status,
        "supporting_evidence_groups": supporting_group_ids,
        "contradicting_evidence_groups": contradicting_group_ids,
        "supporting_observation_ids": supporting_obs_ids,
        "contradicting_observation_ids": contradicting_obs_ids,
        "mapping_ids": relevant_mapping_ids,
        "scope_rationale": scope_rationale,
        "scope_transfer_blocks": scope_blocks,
        "synthesis_explanation": explanation,
    }
    if ontology_term_id is not None:
        claim["ontology_term_id"] = ontology_term_id
    if ontology_term_label is not None:
        claim["ontology_term_label"] = actual_text(
            ontology_term_label, f"claim[{claim_id}].ontology_term_label"
        )
    if discriminating_experiments:
        claim["discriminating_experiments"] = [
            actual_text(exp, f"claim[{claim_id}].discriminating_experiments")
            for exp in discriminating_experiments
        ]
    return claim


def build_reasoning_edge(
    *,
    edge_id: str,
    subject: str,
    predicate: str,
    object_id: str,
    edge_category: str,
    support: str,
    evidence_kind: str,
    rationale: str,
) -> dict[str, Any]:
    """Create and validate a typed ReasoningEdge enforcing the epistemic vs. causal boundary."""
    _require_token(edge_id, "edge_id")
    _require_token(subject, "subject")
    _require_token(object_id, "object")
    if predicate not in REASONING_PREDICATES:
        raise ValueError(f"invalid reasoning predicate: {predicate!r}")
    if edge_category not in EDGE_CATEGORIES:
        raise ValueError(f"invalid edge_category: {edge_category!r}")
    if support not in SUPPORT_STATUSES:
        raise ValueError(f"invalid support status: {support!r}")
    if evidence_kind not in EVIDENCE_KINDS:
        raise ValueError(f"invalid evidence_kind: {evidence_kind!r}")

    if edge_category == "CAUSAL_BIOLOGICAL_LINK":
        if predicate not in CAUSAL_BIOLOGICAL_PREDICATES:
            raise ValueError(
                f"edge[{edge_id}] has edge_category='CAUSAL_BIOLOGICAL_LINK' with epistemic "
                f"predicate {predicate!r}; evidence, coordinate overlap, or homology links "
                "must not be typed as biological causation"
            )
        if support == "OBSERVED" and evidence_kind != "EXPERIMENTAL":
            raise ValueError(
                f"edge[{edge_id}] has CAUSAL_BIOLOGICAL_LINK with support='OBSERVED' "
                f"but evidence_kind={evidence_kind!r}; observed biological causation requires "
                "EXPERIMENTAL evidence"
            )
    else:
        if predicate in CAUSAL_BIOLOGICAL_PREDICATES:
            raise ValueError(
                f"edge[{edge_id}] uses biological causal predicate {predicate!r} with "
                f"non-causal edge_category={edge_category!r}"
            )
        if support == "OBSERVED" and evidence_kind != "EXPERIMENTAL" and predicate not in {
            "anchored_to_sequence",
            "maps_to_region",
            "grouped_into_evidence_unit",
        }:
            raise ValueError(
                f"edge[{edge_id}] has support='OBSERVED' with non-experimental "
                f"evidence_kind={evidence_kind!r}"
            )

    return {
        "edge_id": edge_id,
        "subject": subject,
        "predicate": predicate,
        "object": object_id,
        "edge_category": edge_category,
        "support": support,
        "evidence_kind": evidence_kind,
        "rationale": actual_text(rationale, f"edge[{edge_id}].rationale"),
    }


def _validate_observation_evidence(
    root: Path,
    evidence_list: Sequence[Mapping[str, Any]],
    label: str,
) -> None:
    """Validate EvidenceItem entries attached to a RegionObservation against cached extracts."""
    for idx, evidence in enumerate(evidence_list):
        if not isinstance(evidence, Mapping):
            raise SequenceReasoningError(f"{label}[{idx}] must be a mapping")
        url = urlsplit(str(evidence.get("source_url", "")))
        if url.scheme != "https" or not url.netloc or url.username or url.password:
            raise ValueError(f"{label}[{idx}]: evidence source_url must be an HTTPS source URL")
        path = safe_path(root, str(evidence.get("cache_path", "")))
        try:
            raw = path.read_bytes()
            content = raw.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"{label}[{idx}]: unreadable evidence cache {path}") from exc
        if hashlib.sha256(raw).hexdigest() != evidence.get("cache_sha256"):
            raise ValueError(f"{label}[{idx}]: evidence cache hash mismatch: {path}")
        snippet = " ".join(str(evidence.get("snippet", "")).split())
        if not snippet or snippet not in " ".join(content.split()):
            raise ValueError(f"{label}[{idx}]: evidence quotation not present: {path}")
        actual_text(evidence.get("explanation"), f"{label}[{idx}].explanation")


def validate_region_reasoning_graphs(
    pfam_id: str,
    graphs: Any,
    *,
    causal_graphs: Sequence[Mapping[str, Any]] | None = None,
    root: Path | None = None,
) -> None:
    """Validate a list of RegionReasoningGraph dicts against all coordinate and evidence invariants."""
    if not isinstance(graphs, list) or not graphs:
        raise ValueError(f"{pfam_id}: sequence_reasoning_graphs must be a non-empty list when present")
    if root is not None:
        root = root.resolve(strict=True)
    causal_ids = {
        str(cg.get("graph_id"))
        for cg in (causal_graphs or ())
        if isinstance(cg, Mapping) and cg.get("graph_id")
    }

    seen_graph_ids: set[str] = set()
    for g_idx, graph in enumerate(graphs):
        label = f"{pfam_id}.sequence_reasoning_graphs[{g_idx}]"
        if not isinstance(graph, Mapping):
            raise SequenceReasoningError(f"{label} must be a mapping")
        graph_id = _require_token(graph.get("graph_id"), f"{label}.graph_id")
        if graph_id in seen_graph_ids:
            raise ValueError(f"{pfam_id}: duplicate sequence_reasoning_graph id {graph_id}")
        seen_graph_ids.add(graph_id)
        if graph.get("pfam_id") != pfam_id:
            raise ValueError(f"{label} pfam_id {graph.get('pfam_id')!r} != {pfam_id!r}")
        actual_text(graph.get("title"), f"{label}.title")

        sequences = graph.get("sequences")
        if not isinstance(sequences, list) or not sequences:
            raise ValueError(f"{label}.sequences must be a non-empty list")
        seq_by_id: dict[str, Mapping[str, Any]] = {}
        for s_idx, seq in enumerate(sequences):
            if not isinstance(seq, Mapping):
                raise SequenceReasoningError(f"{label}.sequences[{s_idx}] must be a mapping")
            checked_seq = build_sequence_identity(
                str(seq.get("uniprot_accession", "")),
                sequence_length=seq.get("sequence_length"),
                sequence_sha256=seq.get("sequence_sha256"),
                sequence_md5=seq.get("sequence_md5"),
                isoform=seq.get("isoform"),
                sequence_version=seq.get("sequence_version"),
                taxon_id=seq.get("taxon_id"),
                organism=seq.get("organism"),
                uniprot_release=seq.get("uniprot_release"),
                source_url=seq.get("source_url"),
                sequence_id=seq.get("sequence_id"),
            )
            sid = checked_seq["sequence_id"]
            if sid in seq_by_id:
                raise ValueError(f"{label}: duplicate sequence_id {sid}")
            seq_by_id[sid] = checked_seq

        regions = graph.get("regions")
        if not isinstance(regions, list) or not regions:
            raise ValueError(f"{label}.regions must be a non-empty list")
        reg_by_id: dict[str, Mapping[str, Any]] = {}
        for r_idx, reg in enumerate(regions):
            if not isinstance(reg, Mapping):
                raise SequenceReasoningError(f"{label}.regions[{r_idx}] must be a mapping")
            sid = str(reg.get("sequence_id", ""))
            if sid not in seq_by_id:
                raise ValueError(f"{label}.regions[{r_idx}] references unknown sequence_id {sid!r}")
            checked_reg = build_sequence_region(
                region_id=str(reg.get("region_id", "")),
                sequence_identity=seq_by_id[sid],
                label=str(reg.get("label", "")),
                region_kind=str(reg.get("region_kind", "")),
                coordinate_status=str(reg.get("coordinate_status", "")),
                intervals=reg.get("intervals") or (),
                source_coordinate_system=str(reg.get("source_coordinate_system", "")),
                source_coordinates_text=reg.get("source_coordinates_text"),
                conversion_provenance=reg.get("conversion_provenance"),
                pfam_id=reg.get("pfam_id"),
                interpro_id=reg.get("interpro_id"),
            )
            rid = checked_reg["region_id"]
            if rid in reg_by_id:
                raise ValueError(f"{label}: duplicate region_id {rid}")
            reg_by_id[rid] = checked_reg

        mappings = graph.get("coordinate_mappings") or []
        if not isinstance(mappings, list):
            raise SequenceReasoningError(f"{label}.coordinate_mappings must be a list")
        map_by_id: dict[str, Mapping[str, Any]] = {}
        for m_idx, mp in enumerate(mappings):
            if not isinstance(mp, Mapping):
                raise SequenceReasoningError(f"{label}.coordinate_mappings[{m_idx}] must be a mapping")
            mid = _require_token(mp.get("mapping_id"), f"{label}.coordinate_mappings[{m_idx}].mapping_id")
            if mid in map_by_id:
                raise ValueError(f"{label}: duplicate mapping_id {mid}")
            s_rid = str(mp.get("source_region_id", ""))
            t_rid = str(mp.get("target_region_id", ""))
            if s_rid not in reg_by_id or t_rid not in reg_by_id:
                raise ValueError(
                    f"{label}.coordinate_mappings[{m_idx}] references unknown region(s) {s_rid!r} -> {t_rid!r}"
                )
            if mp.get("mapping_kind") not in MAPPING_KINDS:
                raise ValueError(f"{label}.coordinate_mappings[{m_idx}] has invalid mapping_kind")
            if mp.get("equivalence_status") not in EQUIVALENCE_STATUSES:
                raise ValueError(f"{label}.coordinate_mappings[{m_idx}] has invalid equivalence_status")
            actual_text(mp.get("provenance_note"), f"{label}.coordinate_mappings[{m_idx}].provenance_note")
            computed_mp = classify_region_mapping(
                mapping_id=mid,
                source_region=reg_by_id[s_rid],
                target_region=reg_by_id[t_rid],
                source_sequence=seq_by_id[reg_by_id[s_rid]["sequence_id"]],
                target_sequence=seq_by_id[reg_by_id[t_rid]["sequence_id"]],
                mapping_kind=str(mp.get("mapping_kind", "")),
                residue_correspondences=mp.get("residue_correspondences"),
                alignment_gaps=mp.get("alignment_gaps"),
                mapping_uncertainty=mp.get("mapping_uncertainty"),
                provenance_note=str(mp.get("provenance_note", "")),
            )
            if mp.get("equivalence_status") != computed_mp["equivalence_status"]:
                raise ValueError(
                    f"{label}.coordinate_mappings[{m_idx}] ({mid}) declared equivalence_status "
                    f"{mp.get('equivalence_status')!r} != computed {computed_mp['equivalence_status']!r}"
                )
            map_by_id[mid] = mp

        observations = graph.get("observations")
        if not isinstance(observations, list) or not observations:
            raise ValueError(f"{label}.observations must be a non-empty list")
        obs_by_id: dict[str, Mapping[str, Any]] = {}
        for o_idx, obs in enumerate(observations):
            if not isinstance(obs, Mapping):
                raise SequenceReasoningError(f"{label}.observations[{o_idx}] must be a mapping")
            rid = str(obs.get("region_id", ""))
            if rid not in reg_by_id:
                raise ValueError(f"{label}.observations[{o_idx}] references unknown region_id {rid!r}")
            if obs.get("sequence_id") != reg_by_id[rid]["sequence_id"]:
                raise ValueError(
                    f"{label}.observations[{o_idx}] sequence_id {obs.get('sequence_id')!r} "
                    f"disagrees with region {rid} sequence_id {reg_by_id[rid]['sequence_id']!r}"
                )
            checked_obs = build_region_observation(
                observation_id=str(obs.get("observation_id", "")),
                region=reg_by_id[rid],
                evidence_kind=str(obs.get("evidence_kind", "")),
                source_kind=str(obs.get("source_kind", "")),
                method=str(obs.get("method", "")),
                observed_effect=str(obs.get("observed_effect", "")),
                interpretation=str(obs.get("interpretation", "")),
                polarity=str(obs.get("polarity", "")),
                primary_experiment_key=str(obs.get("primary_experiment_key", "")),
                assay_conditions=obs.get("assay_conditions"),
                tested_construct_region_id=obs.get("tested_construct_region_id"),
                mutation_region_ids=obs.get("mutation_region_ids") or (),
                raw_score=obs.get("raw_score"),
                score_metric=obs.get("score_metric"),
                derived_from_observation_ids=obs.get("derived_from_observation_ids") or (),
                limitations=obs.get("limitations"),
                evidence=obs.get("evidence") or (),
            )
            if checked_obs.get("tested_construct_region_id") and (
                checked_obs["tested_construct_region_id"] not in reg_by_id
            ):
                raise ValueError(
                    f"{label}.observations[{o_idx}] references unknown tested_construct_region_id"
                )
            for mut_id in checked_obs.get("mutation_region_ids") or ():
                if mut_id not in reg_by_id:
                    raise ValueError(
                        f"{label}.observations[{o_idx}] references unknown mutation_region_id {mut_id!r}"
                    )
            if root is not None and checked_obs.get("evidence"):
                _validate_observation_evidence(
                    root, checked_obs["evidence"], f"{label}.observations[{o_idx}].evidence"
                )
            oid = checked_obs["observation_id"]
            if oid in obs_by_id:
                raise ValueError(f"{label}: duplicate observation_id {oid}")
            obs_by_id[oid] = checked_obs

        computed_groups = deduplicate_observations(list(obs_by_id.values()))
        obs_root_key: dict[str, str] = {}
        for cg in computed_groups:
            for oid in cg["observation_ids"]:
                obs_root_key[oid] = cg["primary_experiment_key"]

        groups = graph.get("evidence_groups") or []
        if not isinstance(groups, list):
            raise SequenceReasoningError(f"{label}.evidence_groups must be a list")
        grp_by_id: dict[str, Mapping[str, Any]] = {}
        seen_group_keys: set[tuple[str, str, str]] = set()
        seen_grouped_obs: set[str] = set()
        for grp_idx, grp in enumerate(groups):
            if not isinstance(grp, Mapping):
                raise SequenceReasoningError(f"{label}.evidence_groups[{grp_idx}] must be a mapping")
            gid = _require_token(grp.get("group_id"), f"{label}.evidence_groups[{grp_idx}].group_id")
            if gid in grp_by_id:
                raise ValueError(f"{label}: duplicate group_id {gid}")
            exp_key = _require_token(
                grp.get("primary_experiment_key"),
                f"{label}.evidence_groups[{grp_idx}].primary_experiment_key",
                EXPERIMENT_KEY_RE,
            )
            ev_kind = str(grp.get("evidence_kind", ""))
            pol = str(grp.get("polarity", ""))
            if ev_kind not in EVIDENCE_KINDS or pol not in POLARITIES:
                raise ValueError(f"{label}.evidence_groups[{grp_idx}] has invalid evidence_kind or polarity")
            g_key = (exp_key, ev_kind, pol)
            if g_key in seen_group_keys:
                raise ValueError(
                    f"{label}.evidence_groups[{grp_idx}] duplicates group key {g_key!r}; "
                    "observations sharing primary_experiment_key, evidence_kind, and polarity must be deduplicated"
                )
            seen_group_keys.add(g_key)
            obs_ids = grp.get("observation_ids")
            if not isinstance(obs_ids, list) or not obs_ids:
                raise ValueError(f"{label}.evidence_groups[{grp_idx}].observation_ids must be a non-empty list")
            for oid in obs_ids:
                if oid not in obs_by_id:
                    raise ValueError(
                        f"{label}.evidence_groups[{grp_idx}] references unknown observation_id {oid!r}"
                    )
                if oid in seen_grouped_obs:
                    raise ValueError(
                        f"{label}.evidence_groups[{grp_idx}] duplicates observation_id {oid!r} across groups"
                    )
                seen_grouped_obs.add(oid)
                member = obs_by_id[oid]
                if member["evidence_kind"] != ev_kind or member["polarity"] != pol:
                    raise ValueError(
                        f"{label}.evidence_groups[{grp_idx}] mixes incompatible observation {oid} "
                        f"({member['evidence_kind']}/{member['polarity']}) with group ({ev_kind}/{pol})"
                    )
                if obs_root_key.get(oid) != exp_key:
                    raise ValueError(
                        f"{label}.evidence_groups[{grp_idx}] observation {oid!r} resolves to "
                        f"primary_experiment_key {obs_root_key.get(oid)!r}, not group key {exp_key!r}"
                    )
            actual_text(
                grp.get("deduplication_rationale"),
                f"{label}.evidence_groups[{grp_idx}].deduplication_rationale",
            )
            grp_by_id[gid] = grp

        claims = graph.get("synthesized_claims")
        if not isinstance(claims, list) or not claims:
            raise ValueError(f"{label}.synthesized_claims must be a non-empty list")
        claim_by_id: dict[str, Mapping[str, Any]] = {}
        for c_idx, clm in enumerate(claims):
            if not isinstance(clm, Mapping):
                raise SequenceReasoningError(f"{label}.synthesized_claims[{c_idx}] must be a mapping")
            cid = _require_token(clm.get("claim_id"), f"{label}.synthesized_claims[{c_idx}].claim_id")
            if cid in claim_by_id:
                raise ValueError(f"{label}: duplicate claim_id {cid}")
            t_rid = str(clm.get("target_region_id", ""))
            if t_rid not in reg_by_id:
                raise ValueError(
                    f"{label}.synthesized_claims[{c_idx}] references unknown target_region_id {t_rid!r}"
                )
            status = str(clm.get("synthesis_status", ""))
            scope = str(clm.get("claimed_scope", ""))
            aspect = str(clm.get("function_aspect", ""))
            if status not in SYNTHESIS_STATUSES or scope not in CLAIM_SCOPES or aspect not in FUNCTION_ASPECTS:
                raise ValueError(f"{label}.synthesized_claims[{c_idx}] has invalid status, scope, or aspect")
            for gid in clm.get("supporting_evidence_groups") or ():
                if gid not in grp_by_id:
                    raise ValueError(f"{label}.synthesized_claims[{c_idx}] unknown supporting group {gid!r}")
            for gid in clm.get("contradicting_evidence_groups") or ():
                if gid not in grp_by_id:
                    raise ValueError(f"{label}.synthesized_claims[{c_idx}] unknown contradicting group {gid!r}")
            for oid in clm.get("supporting_observation_ids") or ():
                if oid not in obs_by_id:
                    raise ValueError(
                        f"{label}.synthesized_claims[{c_idx}] unknown supporting observation {oid!r}"
                    )
            for oid in clm.get("contradicting_observation_ids") or ():
                if oid not in obs_by_id:
                    raise ValueError(
                        f"{label}.synthesized_claims[{c_idx}] unknown contradicting observation {oid!r}"
                    )
            for mid in clm.get("mapping_ids") or ():
                if mid not in map_by_id:
                    raise ValueError(f"{label}.synthesized_claims[{c_idx}] unknown mapping_id {mid!r}")

            if status == "EXPERIMENTALLY_DEMONSTRATED":
                target_reg = reg_by_id[t_rid]
                if target_reg.get("coordinate_status") in {
                    "WHOLE_PROTEIN_UNLOCALIZED",
                    "UNKNOWN_LOCALIZATION",
                }:
                    raise ValueError(
                        f"{label}.synthesized_claims[{c_idx}] ({cid}) cannot be "
                        f"EXPERIMENTALLY_DEMONSTRATED on unlocalized target region {t_rid}"
                    )
                supp_obs = [obs_by_id[oid] for oid in (clm.get("supporting_observation_ids") or ())]
                pos_exp_obs = [
                    o
                    for o in supp_obs
                    if o["evidence_kind"] == "EXPERIMENTAL" and o["polarity"] == "POSITIVE"
                ]
                if not pos_exp_obs:
                    raise ValueError(
                        f"{label}.synthesized_claims[{c_idx}] ({cid}) is EXPERIMENTALLY_DEMONSTRATED "
                        "without any POSITIVE EXPERIMENTAL supporting observation"
                    )
                claim_maps = [map_by_id[mid] for mid in (clm.get("mapping_ids") or ())]
                for mid in clm.get("mapping_ids") or ():
                    mp = map_by_id[mid]
                    if mp.get("equivalence_status") in {
                        "PARTIAL_OVERLAP_NOT_EQUIVALENT",
                        "DISJOINT_OUTSIDE_REGION",
                        "SEQUENCE_VERSION_MISMATCH",
                        "UNRESOLVED_MAPPING",
                    }:
                        raise ValueError(
                            f"{label}.synthesized_claims[{c_idx}] ({cid}) cannot be "
                            f"EXPERIMENTALLY_DEMONSTRATED with mapping {mid} ({mp.get('equivalence_status')})"
                        )
                has_localized_pos_exp = False
                for o in pos_exp_obs:
                    mut_rids = list(o.get("mutation_region_ids") or ())
                    obs_has_internal_mut = False
                    obs_disjoint_mut = False
                    for m_rid in mut_rids:
                        m_maps = [
                            m
                            for m in claim_maps
                            if m.get("source_region_id") == m_rid and m.get("target_region_id") == t_rid
                        ]
                        if not m_maps:
                            obs_disjoint_mut = True
                        else:
                            for m_mp in m_maps:
                                if m_mp.get("equivalence_status") == "RESIDUE_INSIDE_REGION":
                                    obs_has_internal_mut = True
                                else:
                                    obs_disjoint_mut = True
                    if obs_disjoint_mut:
                        continue
                    obs_rid = o["region_id"]
                    obs_reg = reg_by_id[obs_rid]
                    if obs_rid == t_rid:
                        if (
                            obs_reg.get("coordinate_status")
                            in {"WHOLE_PROTEIN_UNLOCALIZED", "UNKNOWN_LOCALIZATION"}
                            and not obs_has_internal_mut
                        ):
                            continue
                        has_localized_pos_exp = True
                        break
                    r_maps = [
                        m
                        for m in claim_maps
                        if m.get("source_region_id") == obs_rid and m.get("target_region_id") == t_rid
                    ]
                    if any(
                        _is_localized_domain_mapping(
                            m,
                            regions_by_id=reg_by_id,
                            has_domain_internal_mutation=obs_has_internal_mut,
                        )[0]
                        for m in r_maps
                    ):
                        has_localized_pos_exp = True
                        break
                if not has_localized_pos_exp:
                    raise ValueError(
                        f"{label}.synthesized_claims[{c_idx}] ({cid}) is EXPERIMENTALLY_DEMONSTRATED "
                        f"without any POSITIVE EXPERIMENTAL observation localized to target region {t_rid}"
                    )
            if scope == "FAMILY_WIDE" and (clm.get("scope_transfer_blocks") or ()):
                raise ValueError(
                    f"{label}.synthesized_claims[{c_idx}] ({cid}) claims FAMILY_WIDE scope "
                    "while scope_transfer_blocks are present"
                )
            claim_by_id[cid] = clm

        all_entity_ids = (
            set(seq_by_id)
            | set(reg_by_id)
            | set(map_by_id)
            | set(obs_by_id)
            | set(grp_by_id)
            | set(claim_by_id)
        )
        edges = graph.get("reasoning_edges")
        if not isinstance(edges, list) or not edges:
            raise ValueError(f"{label}.reasoning_edges must be a non-empty list")
        seen_edge_ids: set[str] = set()
        for e_idx, edg in enumerate(edges):
            if not isinstance(edg, Mapping):
                raise SequenceReasoningError(f"{label}.reasoning_edges[{e_idx}] must be a mapping")
            checked_edge = build_reasoning_edge(
                edge_id=str(edg.get("edge_id", "")),
                subject=str(edg.get("subject", "")),
                predicate=str(edg.get("predicate", "")),
                object_id=str(edg.get("object", "")),
                edge_category=str(edg.get("edge_category", "")),
                support=str(edg.get("support", "")),
                evidence_kind=str(edg.get("evidence_kind", "")),
                rationale=str(edg.get("rationale", "")),
            )
            eid = checked_edge["edge_id"]
            if eid in seen_edge_ids:
                raise ValueError(f"{label}: duplicate reasoning edge_id {eid}")
            seen_edge_ids.add(eid)
            if checked_edge["subject"] not in all_entity_ids:
                raise ValueError(
                    f"{label}.reasoning_edges[{e_idx}] subject {checked_edge['subject']!r} not in graph"
                )
            if checked_edge["object"] not in all_entity_ids:
                raise ValueError(
                    f"{label}.reasoning_edges[{e_idx}] object {checked_edge['object']!r} not in graph"
                )

        for ref in graph.get("causal_graph_refs") or ():
            _require_token(ref, f"{label}.causal_graph_refs")
            if causal_graphs is not None and ref not in causal_ids:
                raise ValueError(
                    f"{label}.causal_graph_refs references unknown CausalGraph {ref!r}"
                )


def query_claims_for_region(
    graph: Mapping[str, Any],
    *,
    sequence_id: str,
    start: int | None = None,
    end: int | None = None,
    include_overlapping: bool = True,
) -> list[dict[str, Any]]:
    """Query synthesized claims for a sequence and optional 1-based [start, end] range.

    Uses exact multi-segment residue set arithmetic so queries inside an
    inter-segment gap of a discontinuous domain do not falsely match that domain.
    """
    seq_by_id = {str(s["sequence_id"]): s for s in (graph.get("sequences") or ())}
    if sequence_id not in seq_by_id:
        raise ValueError(f"unknown sequence_id in graph {graph.get('graph_id')!r}: {sequence_id!r}")
    seq_len = int(seq_by_id[sequence_id]["sequence_length"])
    query_positions: set[int] | None = None
    if (start is None) != (end is None):
        raise SequenceReasoningError(
            "Both start and end must be provided together when querying by coordinate interval"
        )
    if start is not None and end is not None:
        q_start = _require_positive_int(start, "start", minimum=1)
        q_end = _require_positive_int(end, "end", minimum=1)
        if q_start > q_end or q_end > seq_len:
            raise ValueError(f"invalid query interval {q_start}..{q_end} for sequence length {seq_len}")
        query_positions = set(range(q_start, q_end + 1))

    reg_by_id = {str(r["region_id"]): r for r in (graph.get("regions") or ())}
    results: list[dict[str, Any]] = []
    for claim in graph.get("synthesized_claims") or ():
        target_reg = reg_by_id.get(str(claim["target_region_id"]))
        if target_reg is None or target_reg.get("sequence_id") != sequence_id:
            continue
        target_positions = region_residue_positions(target_reg)
        if query_positions is None:
            relation = "SEQUENCE_MATCH"
            overlap = len(target_positions)
        elif not target_positions:
            if not include_overlapping:
                continue
            relation = "UNLOCALIZED"
            overlap = 0
        else:
            shared = query_positions & target_positions
            overlap = len(shared)
            if overlap == 0:
                continue
            if query_positions == target_positions:
                relation = "EXACT_MATCH"
            elif target_positions.issubset(query_positions):
                relation = "QUERY_CONTAINS_TARGET"
            elif query_positions.issubset(target_positions):
                relation = "TARGET_CONTAINS_QUERY"
            else:
                if not include_overlapping:
                    continue
                relation = "PARTIAL_OVERLAP"
            if not include_overlapping and relation != "EXACT_MATCH":
                continue

        results.append({
            "claim_id": claim["claim_id"],
            "label": claim["label"],
            "function_aspect": claim["function_aspect"],
            "ontology_term_id": claim.get("ontology_term_id"),
            "ontology_term_label": claim.get("ontology_term_label"),
            "synthesis_status": claim["synthesis_status"],
            "claimed_scope": claim["claimed_scope"],
            "target_region_id": target_reg["region_id"],
            "target_region_label": target_reg["label"],
            "target_intervals": target_reg.get("intervals") or [],
            "coordinate_relation": relation,
            "overlap_residues": overlap,
            "independent_supporting_groups": len(claim.get("supporting_evidence_groups") or ()),
            "independent_contradicting_groups": len(claim.get("contradicting_evidence_groups") or ()),
            "scope_transfer_blocks": list(claim.get("scope_transfer_blocks") or ()),
            "discriminating_experiments": list(claim.get("discriminating_experiments") or ()),
        })
    return results


def trace_claim_evidence(graph: Mapping[str, Any], claim_id: str) -> dict[str, Any]:
    """Trace a SynthesizedClaim back to its evidence groups, observations, mappings, and sequences."""
    seq_by_id = {str(s["sequence_id"]): s for s in (graph.get("sequences") or ())}
    reg_by_id = {str(r["region_id"]): r for r in (graph.get("regions") or ())}
    map_by_id = {str(m["mapping_id"]): m for m in (graph.get("coordinate_mappings") or ())}
    obs_by_id = {str(o["observation_id"]): o for o in (graph.get("observations") or ())}
    grp_by_id = {str(g["group_id"]): g for g in (graph.get("evidence_groups") or ())}
    claim_by_id = {str(c["claim_id"]): c for c in (graph.get("synthesized_claims") or ())}

    if claim_id not in claim_by_id:
        raise ValueError(f"unknown claim_id {claim_id!r} in graph {graph.get('graph_id')!r}")
    claim = claim_by_id[claim_id]
    target_region = reg_by_id[str(claim["target_region_id"])]
    target_sequence = seq_by_id[str(target_region["sequence_id"])]

    def _expand_group(gid: str) -> dict[str, Any]:
        grp = grp_by_id[gid]
        members = [obs_by_id[oid] for oid in grp["observation_ids"]]
        return {
            "group_id": gid,
            "primary_experiment_key": grp["primary_experiment_key"],
            "evidence_kind": grp["evidence_kind"],
            "polarity": grp["polarity"],
            "deduplication_rationale": grp["deduplication_rationale"],
            "observations": members,
        }

    supporting_groups = [
        _expand_group(gid) for gid in (claim.get("supporting_evidence_groups") or ())
    ]
    contradicting_groups = [
        _expand_group(gid) for gid in (claim.get("contradicting_evidence_groups") or ())
    ]
    mappings = [map_by_id[mid] for mid in (claim.get("mapping_ids") or ())]

    related_ids = {
        claim_id,
        str(target_region["region_id"]),
        *(str(m["mapping_id"]) for m in mappings),
        *(str(g["group_id"]) for g in supporting_groups),
        *(str(g["group_id"]) for g in contradicting_groups),
        *(str(oid) for oid in (claim.get("supporting_observation_ids") or ())),
        *(str(oid) for oid in (claim.get("contradicting_observation_ids") or ())),
    }
    epistemic_edges: list[Mapping[str, Any]] = []
    biological_causal_edges: list[Mapping[str, Any]] = []
    for edge in graph.get("reasoning_edges") or ():
        if edge.get("subject") in related_ids or edge.get("object") in related_ids:
            if edge.get("edge_category") == "CAUSAL_BIOLOGICAL_LINK":
                biological_causal_edges.append(edge)
            else:
                epistemic_edges.append(edge)

    return {
        "graph_id": graph.get("graph_id"),
        "pfam_id": graph.get("pfam_id"),
        "claim": claim,
        "target_region": target_region,
        "target_sequence": target_sequence,
        "coordinate_mappings": mappings,
        "supporting_groups": supporting_groups,
        "contradicting_groups": contradicting_groups,
        "independent_supporting_experiment_count": len(supporting_groups),
        "raw_supporting_observation_count": len(claim.get("supporting_observation_ids") or ()),
        "independent_contradicting_experiment_count": len(contradicting_groups),
        "raw_contradicting_observation_count": len(claim.get("contradicting_observation_ids") or ()),
        "epistemic_edges": epistemic_edges,
        "biological_causal_edges": biological_causal_edges,
        "scope_transfer_blocks": list(claim.get("scope_transfer_blocks") or ()),
        "discriminating_experiments": list(claim.get("discriminating_experiments") or ()),
    }


def render_inspectable_view(graph: Mapping[str, Any], *, fmt: str = "markdown") -> str:
    """Render a human- and machine-inspectable view of a RegionReasoningGraph."""
    if fmt == "json":
        return json.dumps(graph, indent=2, sort_keys=True)
    if fmt != "markdown":
        raise ValueError(f"unsupported view format: {fmt!r}")

    lines: list[str] = [
        f"# Region Reasoning Graph: `{graph['graph_id']}` ({graph['pfam_id']})",
        "",
        f"**Title**: {graph['title']}",
    ]
    if graph.get("description"):
        lines.append(f"**Description**: {graph['description']}")
    lines.extend(["", "## 1. Reference Sequences & Checksums", ""])
    for seq in graph.get("sequences") or ():
        iso = f", isoform `{seq['isoform']}`" if seq.get("isoform") else ""
        ver = f", v{seq['sequence_version']}" if seq.get("sequence_version") else ""
        org = f" ({seq['organism']})" if seq.get("organism") else ""
        lines.append(
            f"- **`{seq['sequence_id']}`**: `UniProtKB:{seq['uniprot_accession']}`{iso}{ver}{org}, "
            f"length `{seq['sequence_length']}` aa, sha256 `{seq['sequence_sha256'][:16]}...`"
        )

    lines.extend(["", "## 2. Explicit Sequence Regions (1-Based Inclusive)", ""])
    for reg in graph.get("regions") or ():
        ivs = ", ".join(
            f"{iv['start']}..{iv['end']}"
            + (f" ({iv['residue_identity']})" if iv.get("residue_identity") else "")
            for iv in (reg.get("intervals") or ())
        ) or "unlocalized"
        gaps = region_inter_segment_gaps(reg)
        gap_note = f", inter-segment gaps: {', '.join(f'{g[0]}..{g[1]}' for g in gaps)}" if gaps else ""
        conv = f" — *{reg['conversion_provenance']}*" if reg.get("conversion_provenance") else ""
        lines.append(
            f"- **`{reg['region_id']}`** on `{reg['sequence_id']}` [{reg['region_kind']} / "
            f"{reg['coordinate_status']}]: `{ivs}`{gap_note} (source: `{reg['source_coordinate_system']}` "
            f"`{reg.get('source_coordinates_text', ivs)}`){conv}"
        )

    lines.extend(["", "## 3. Coordinate Mappings & Uncertainty", ""])
    for mp in graph.get("coordinate_mappings") or ():
        cov = (
            f"overlap={mp.get('overlap_residues')} aa, "
            f"source_cov={mp.get('source_coverage')}, target_cov={mp.get('target_coverage')}"
            if mp.get("overlap_residues") is not None
            else "cross-sequence/unresolved"
        )
        unc = f" | **Uncertainty**: {mp['mapping_uncertainty']}" if mp.get("mapping_uncertainty") else ""
        lines.append(
            f"- **`{mp['mapping_id']}`**: `{mp['source_region_id']}` -> `{mp['target_region_id']}` "
            f"[`{mp['mapping_kind']}` => **`{mp['equivalence_status']}`** ({cov})]{unc}"
        )

    lines.extend(["", "## 4. Deduplicated Evidence Groups & Observations", ""])
    obs_by_id = {str(o["observation_id"]): o for o in (graph.get("observations") or ())}
    for grp in graph.get("evidence_groups") or ():
        lines.append(
            f"- **`{grp['group_id']}`** [`{grp['evidence_kind']}` / `{grp['polarity']}`] "
            f"(key: `{grp['primary_experiment_key']}`): {grp['deduplication_rationale']}"
        )
        for oid in grp.get("observation_ids") or ():
            obs = obs_by_id[oid]
            score_txt = (
                f", score `{obs['score_metric']}={obs['raw_score']}`"
                if obs.get("raw_score") is not None
                else ""
            )
            lines.append(
                f"  - `{oid}` (`{obs['source_kind']}` on `{obs['region_id']}`{score_txt}): "
                f"**Observed**: {obs['observed_effect']} | **Interpretation**: {obs['interpretation']}"
            )

    lines.extend(["", "## 5. Synthesized Functional Claims", ""])
    for clm in graph.get("synthesized_claims") or ():
        term = (
            f" (`{clm['ontology_term_id']}` {clm.get('ontology_term_label', '')})"
            if clm.get("ontology_term_id")
            else ""
        )
        lines.extend([
            f"### `{clm['claim_id']}`: {clm['label']}{term}",
            f"- **Target Region**: `{clm['target_region_id']}`",
            f"- **Function Aspect**: `{clm['function_aspect']}`",
            f"- **Synthesis Status**: **`{clm['synthesis_status']}`**",
            f"- **Claimed Scope**: **`{clm['claimed_scope']}`** ({clm['scope_rationale']})",
            (
                f"- **Supporting Groups**: `{clm.get('supporting_evidence_groups') or []}` "
                f"(observations: `{clm.get('supporting_observation_ids') or []}`)"
            ),
            (
                f"- **Contradicting Groups**: `{clm.get('contradicting_evidence_groups') or []}` "
                f"(observations: `{clm.get('contradicting_observation_ids') or []}`)"
            ),
            f"- **Synthesis Explanation**: {clm['synthesis_explanation']}",
        ])
        for blk in clm.get("scope_transfer_blocks") or ():
            lines.append(f"- **Scope Transfer Block**: {blk}")
        for exp in clm.get("discriminating_experiments") or ():
            lines.append(f"- **Discriminating Experiment**: {exp}")
        lines.append("")

    lines.extend(["## 6. Typed Reasoning Edges (Epistemic vs. Biological Causation)", ""])
    epistemic = [
        e for e in (graph.get("reasoning_edges") or ())
        if e.get("edge_category") != "CAUSAL_BIOLOGICAL_LINK"
    ]
    causal = [
        e for e in (graph.get("reasoning_edges") or ())
        if e.get("edge_category") == "CAUSAL_BIOLOGICAL_LINK"
    ]
    lines.append("### Epistemic / Coordinate / Inference Edges")
    for edge in epistemic:
        lines.append(
            f"- `{edge['edge_id']}` [`{edge['edge_category']}` / `{edge['support']}` / "
            f"`{edge['evidence_kind']}`]: `{edge['subject']}` **{edge['predicate']}** "
            f"`{edge['object']}` — {edge['rationale']}"
        )
    lines.extend(["", "### Biological Causal Edges"])
    if causal:
        for edge in causal:
            lines.append(
                f"- `{edge['edge_id']}` [`{edge['edge_category']}` / `{edge['support']}` / "
                f"`{edge['evidence_kind']}`]: `{edge['subject']}` **{edge['predicate']}** "
                f"`{edge['object']}` — {edge['rationale']}"
            )
    else:
        lines.append("- *(None — all edges in this graph are epistemic/coordinate/inference links.)*")
    return "\n".join(lines) + "\n"


def build_representative_reasoning_graphs() -> list[dict[str, Any]]:
    """Build and validate three representative end-to-end RegionReasoningGraphs.

    1. ``pf13271_tep1_nadase_demonstrated``: Region-anchored experimental NAD+
       hydrolase activity on human TEP1 (Q99973) construct 886-1113 containing
       PF13271 (901-1015) and catalytic Glu1008, with mirrored-annotation
       deduplication and experimentally inactive paralogues (NWD1, NWD2, NPHP3)
       blocking family-wide transfer.
    2. ``pf13271_q31pw6_computational_hypothesis``: Computational and
       mixed-evidence hypothesis on Synechococcus elongatus Q31PW6 PF13271
       (6-146) with conserved Glu83 (HMM state 78 aligned to TEP1 Glu1008),
       deduplicated InterPro/Pfam/CD-Search hits with non-interchangeable
       E_VALUE and BITSCORE metrics, and adjacent COG5635 NACHT vs. NTPase
       architectural label ambiguity.
    3. ``discontinuous_and_conflicting_localization``: Discontinuous two-segment
       domain [50..120, 210..290] with an inter-segment gap mutation at residue
       165 (proven DISJOINT_OUTSIDE_REGION), conflicting positive/negative
       biochemical assays remaining CONFLICTING_UNRESOLVED, and an unannotated
       homolog remaining INSUFFICIENT_EVIDENCE / UNKNOWN_FUNCTION (never
       negative).
    """
    # --- Graph 1: TEP1 (Q99973) demonstrated NADase + inactive paralogues ---
    seq_tep1 = build_sequence_identity(
        "Q99973",
        sequence_length=2627,
        sequence_sha256=hashlib.sha256(b"Q99973_ISOFORM_1_V3_2627AA").hexdigest(),
        isoform="Q99973-1",
        sequence_version=3,
        taxon_id="NCBITaxon:9606",
        organism="Homo sapiens",
        uniprot_release="2026_02",
        source_url="https://www.uniprot.org/uniprotkb/Q99973/entry",
        sequence_id="seq_Q99973_v3",
    )
    seq_nwd1 = build_sequence_identity(
        "Q5H9R7",
        sequence_length=1562,
        sequence_sha256=hashlib.sha256(b"Q5H9R7_NWD1_1562AA").hexdigest(),
        sequence_version=2,
        taxon_id="NCBITaxon:9606",
        organism="Homo sapiens",
        sequence_id="seq_Q5H9R7_v2",
    )

    reg_tep1_pf13271 = build_sequence_region(
        region_id="reg_Q99973_pf13271_901_1015",
        sequence_identity=seq_tep1,
        label="Human TEP1 PF13271 (DUF4062 / TLN) domain (901-1015)",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 901, "end": 1015}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="901-1015",
        conversion_provenance="Pfam PF13271 envelope coordinates on UniProtKB:Q99973.",
        pfam_id="PF13271",
        interpro_id="InterPro:IPR025469",
    )
    reg_tep1_construct = build_sequence_region(
        region_id="reg_Q99973_construct_886_1113",
        sequence_identity=seq_tep1,
        label="Purified recombinant human TEP1 TLN construct (886-1113)",
        region_kind="EXPERIMENTAL_CONSTRUCT",
        coordinate_status="EXACT",
        intervals=[{"start": 886, "end": 1113}],
        source_coordinate_system="CONSTRUCT_NUMBERING",
        source_coordinates_text="construct(886-1113):1-228",
        conversion_provenance="Converted 228-aa construct (local 1..228) to UniProtKB:Q99973 886..1113.",
    )
    reg_tep1_e1008 = convert_construct_to_reference(
        construct_start_on_ref=886,
        construct_end_on_ref=1113,
        local_start=123,
        local_end=123,
        sequence_identity=seq_tep1,
        region_id="reg_Q99973_E1008",
        label="Catalytic glutamate Glu1008 (E1008A substitution site)",
        region_kind="CATALYTIC_SITE",
        residue_identity="E",
    )
    reg_nwd1_pf13271 = build_sequence_region(
        region_id="reg_Q5H9R7_pf13271_20_138",
        sequence_identity=seq_nwd1,
        label="Human NWD1 PF13271 domain (20-138)",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 20, "end": 138}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="20-138",
        pfam_id="PF13271",
    )

    map_construct_to_domain = classify_region_mapping(
        mapping_id="map_Q99973_construct_to_pf13271",
        source_region=reg_tep1_construct,
        target_region=reg_tep1_pf13271,
        source_sequence=seq_tep1,
        target_sequence=seq_tep1,
        mapping_kind="CONSTRUCT_TO_REFERENCE",
    )
    map_e1008_to_domain = classify_region_mapping(
        mapping_id="map_Q99973_E1008_to_pf13271",
        source_region=reg_tep1_e1008,
        target_region=reg_tep1_pf13271,
        source_sequence=seq_tep1,
        target_sequence=seq_tep1,
        mapping_kind="MUTATION_TO_DOMAIN",
        residue_correspondences=[{
            "source_position": 1008,
            "source_residue": "E",
            "target_position": 1008,
            "target_residue": "E",
            "mutation_substitution": "E1008A",
            "note": "Conserved catalytic glutamate in PF13271 active site.",
        }],
    )

    obs_tep1_wt_hplc = build_region_observation(
        observation_id="obs_tep1_wt_hplc_nmr",
        region=reg_tep1_construct,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="In vitro HPLC and 1H-NMR NAD+ cleavage assay on purified TEP1 (886-1113)",
        assay_conditions="Purified recombinant human TEP1 (886-1113) incubated with NAD+ in vitro.",
        tested_construct_region_id="reg_Q99973_construct_886_1113",
        observed_effect="Direct hydrolysis of NAD+ into nicotinamide (NAM) and ADP-ribose (ADPR).",
        interpretation="Human TEP1 (886-1113) possesses intrinsic NAD+ nucleosidase (NADase) activity.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:42146377/Q99973_886-1113/NADase_WT",
        limitations="Assayed on isolated 886-1113 construct in vitro, not intact vault ribonucleoprotein particle.",
    )
    obs_tep1_wt_mirrored = build_region_observation(
        observation_id="obs_tep1_wt_mirrored_curated",
        region=reg_tep1_construct,
        evidence_kind="EXPERIMENTAL",
        source_kind="CURATED_ANNOTATION",
        method="Secondary curated reaction summary of Osinski et al. HPLC/NMR assay",
        tested_construct_region_id="reg_Q99973_construct_886_1113",
        observed_effect="Reported NAD+ -> NAM + ADPR cleavage for TEP1 (886-1113) from the same experiment.",
        interpretation="Mirrored report of TEP1 (886-1113) NADase activity.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:42146377/Q99973_886-1113/NADase_WT",
        derived_from_observation_ids=["obs_tep1_wt_hplc_nmr"],
    )
    obs_tep1_e1008a = build_region_observation(
        observation_id="obs_tep1_E1008A_catalytic_loss",
        region=reg_tep1_construct,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Site-directed mutagenesis E1008A on TEP1 (886-1113) followed by HPLC NADase assay",
        tested_construct_region_id="reg_Q99973_construct_886_1113",
        mutation_region_ids=["reg_Q99973_E1008"],
        observed_effect="E1008A substitution inside PF13271 (901-1015) abolishes NAD+ hydrolysis.",
        interpretation="Catalytic activity of construct 886-1113 requires Glu1008 within the PF13271 domain.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:42146377/Q99973_886-1113/NADase_E1008A",
    )
    obs_nwd1_neg = build_region_observation(
        observation_id="obs_nwd1_nadase_negative",
        region=reg_nwd1_pf13271,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="In vitro NAD+ cleavage assay on recombinant human NWD1 TLN domain",
        observed_effect="No detectable NAD+ hydrolysis by human NWD1 (nor NWD2 or NPHP3) under identical assay conditions.",
        interpretation="Human paralogues NWD1, NWD2, and NPHP3 lack detectable intrinsic NADase activity under conditions where TEP1 (886-1113) is active.",
        polarity="NEGATIVE",
        primary_experiment_key="PMID:42146377/Q5H9R7_20-138/NADase_WT",
    )

    g1_obs = [obs_tep1_wt_hplc, obs_tep1_wt_mirrored, obs_tep1_e1008a, obs_nwd1_neg]
    g1_groups = deduplicate_observations(g1_obs)
    g1_regs = {
        r["region_id"]: r
        for r in (reg_tep1_pf13271, reg_tep1_construct, reg_tep1_e1008, reg_nwd1_pf13271)
    }
    g1_maps = [map_construct_to_domain, map_e1008_to_domain]

    claim_tep1 = synthesize_region_claim(
        claim_id="claim_tep1_pf13271_nadase",
        label="Human TEP1 PF13271 domain (901-1015, tested in 886-1113) catalyzes NAD+ hydrolysis via Glu1008",
        function_aspect="CATALYTIC_ACTIVITY",
        ontology_term_id="GO:0003953",
        ontology_term_label="NAD+ nucleosidase activity",
        target_region=reg_tep1_pf13271,
        regions_by_id=g1_regs,
        observations=[obs_tep1_wt_hplc, obs_tep1_wt_mirrored, obs_tep1_e1008a],
        evidence_groups=[g for g in g1_groups if g["polarity"] == "POSITIVE"],
        coordinate_mappings=g1_maps,
        requested_scope="FAMILY_WIDE",
        additional_scope_blocks=[
            "Human PF13271 paralogues NWD1 (Q5H9R7), NWD2, and NPHP3 showed no detectable NAD+ hydrolysis under the same in vitro conditions, blocking family-wide or human-paralogue generalization.",
            "Assay was performed on recombinant construct 886-1113 in vitro; physiological activation within full-length TEP1 (1-2627) vault particles remains unverified.",
        ],
        discriminating_experiments=[
            "Assay NAD+ hydrolysis in intact vault particles containing full-length wild-type vs E1008A TEP1 (1-2627)."
        ],
    )
    claim_nwd1 = synthesize_region_claim(
        claim_id="claim_nwd1_pf13271_nadase_negative",
        label="Human NWD1 PF13271 domain (20-138) shows no detectable NAD+ hydrolase activity in vitro",
        function_aspect="CATALYTIC_ACTIVITY",
        ontology_term_id="GO:0003953",
        ontology_term_label="NAD+ nucleosidase activity",
        target_region=reg_nwd1_pf13271,
        regions_by_id=g1_regs,
        observations=[obs_nwd1_neg],
        evidence_groups=[g for g in g1_groups if g["polarity"] == "NEGATIVE"],
    )

    graph1 = {
        "graph_id": "pf13271_tep1_nadase_demonstrated",
        "pfam_id": "PF13271",
        "title": "Human TEP1 (Q99973) PF13271 NAD+ hydrolase demonstration and paralogue scope limits",
        "description": (
            "Region-anchored reasoning from TEP1 construct 886-1113 and catalytic mutant E1008A "
            "to PF13271 (901-1015), deduplicating mirrored reports and blocking family-wide transfer "
            "due to inactive human paralogues."
        ),
        "sequences": [seq_tep1, seq_nwd1],
        "regions": list(g1_regs.values()),
        "coordinate_mappings": g1_maps,
        "observations": g1_obs,
        "evidence_groups": g1_groups,
        "synthesized_claims": [claim_tep1, claim_nwd1],
        "reasoning_edges": [
            build_reasoning_edge(
                edge_id="edge_construct_maps_pf13271",
                subject="reg_Q99973_construct_886_1113",
                predicate="maps_to_region",
                object_id="reg_Q99973_pf13271_901_1015",
                edge_category="COORDINATE_MAPPING_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Construct 886..1113 completely contains PF13271 domain 901..1015.",
            ),
            build_reasoning_edge(
                edge_id="edge_e1008_maps_pf13271",
                subject="reg_Q99973_E1008",
                predicate="maps_to_region",
                object_id="reg_Q99973_pf13271_901_1015",
                edge_category="COORDINATE_MAPPING_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Catalytic Glu1008 lies inside PF13271 domain 901..1015.",
            ),
            build_reasoning_edge(
                edge_id="edge_grp_wt_supports_claim",
                subject=g1_groups[0]["group_id"],
                predicate="supports_claim",
                object_id="claim_tep1_pf13271_nadase",
                edge_category="EVIDENCE_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Deduplicated wild-type HPLC/1H-NMR assay group supports NADase claim.",
            ),
            build_reasoning_edge(
                edge_id="edge_grp_e1008a_supports_claim",
                subject=g1_groups[1]["group_id"],
                predicate="supports_claim",
                object_id="claim_tep1_pf13271_nadase",
                edge_category="EVIDENCE_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="E1008A loss-of-function mutagenesis localizes catalysis to Glu1008 in PF13271.",
            ),
            build_reasoning_edge(
                edge_id="edge_nwd1_constrains_scope",
                subject="claim_nwd1_pf13271_nadase_negative",
                predicate="constrains_claim_scope",
                object_id="claim_tep1_pf13271_nadase",
                edge_category="EVIDENCE_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Negative NWD1 assay blocks transfer of TEP1 NADase activity across all PF13271 members.",
            ),
            build_reasoning_edge(
                edge_id="edge_pf13271_enables_nadase",
                subject="reg_Q99973_pf13271_901_1015",
                predicate="enables_biological_activity",
                object_id="claim_tep1_pf13271_nadase",
                edge_category="CAUSAL_BIOLOGICAL_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Direct biochemical cleavage and E1008A catalytic ablation establish biological enzymatic activity.",
            ),
        ],
    }

    # --- Graph 2: Q31PW6 computational hypothesis & COG5635 architectural ambiguity ---
    seq_q31pw6 = build_sequence_identity(
        "Q31PW6",
        sequence_length=494,
        sequence_sha256=hashlib.sha256(b"Q31PW6_SYNE7_494AA").hexdigest(),
        sequence_version=1,
        taxon_id="NCBITaxon:1140",
        organism="Synechococcus elongatus PCC 7942",
        sequence_id="seq_Q31PW6_v1",
    )
    reg_q31_pf13271 = build_sequence_region(
        region_id="reg_Q31PW6_pf13271_6_146",
        sequence_identity=seq_q31pw6,
        label="Q31PW6 N-terminal PF13271 (DUF4062) domain (6-146)",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 6, "end": 146}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="6-146",
        pfam_id="PF13271",
        interpro_id="InterPro:IPR025469",
    )
    reg_q31_e83 = build_sequence_region(
        region_id="reg_Q31PW6_E83",
        sequence_identity=seq_q31pw6,
        label="Conserved glutamate Glu83 (aligned to PF13271 HMM match state 78 / TEP1 Glu1008)",
        region_kind="CATALYTIC_SITE",
        coordinate_status="EXACT",
        intervals=[{"start": 83, "end": 83, "residue_identity": "E"}],
        source_coordinate_system="HMM_PROFILE",
        source_coordinates_text="PF13271_HMM:78 -> Q31PW6:83",
        conversion_provenance="Aligned PF13271 profile HMM catalytic match state 78 to UniProtKB:Q31PW6 residue Glu83.",
    )
    reg_q31_cog5635 = build_sequence_region(
        region_id="reg_Q31PW6_cog5635_160_480",
        sequence_identity=seq_q31pw6,
        label="Q31PW6 C-terminal COG5635 (predicted NACHT NTPase / DUF4062-associated) region (160-480)",
        region_kind="ADJACENT_ARCHITECTURAL_DOMAIN",
        coordinate_status="UNCERTAIN_BOUNDARY",
        intervals=[{"start": 160, "end": 480, "start_uncertain": True, "end_uncertain": True}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="~160-480",
        conversion_provenance="EggNOG COG5635 orthogroup and Osinski et al. C-terminal NTPase architectural boundary.",
    )

    map_e83_to_q31_domain = classify_region_mapping(
        mapping_id="map_Q31PW6_E83_to_pf13271",
        source_region=reg_q31_e83,
        target_region=reg_q31_pf13271,
        source_sequence=seq_q31pw6,
        target_sequence=seq_q31pw6,
        mapping_kind="PROFILE_TO_SEQUENCE",
        residue_correspondences=[{
            "source_position": 78,
            "source_residue": "E",
            "target_position": 83,
            "target_residue": "E",
            "note": "Conserved catalytic glutamate corresponding to human TEP1 Glu1008.",
        }],
    )
    map_cog5635_disjoint = classify_region_mapping(
        mapping_id="map_Q31PW6_cog5635_to_pf13271",
        source_region=reg_q31_cog5635,
        target_region=reg_q31_pf13271,
        source_sequence=seq_q31pw6,
        target_sequence=seq_q31pw6,
        mapping_kind="DOMAIN_TO_CONSTRUCT",
    )

    obs_q31_pfam = build_region_observation(
        observation_id="obs_q31pw6_pfam_hit",
        region=reg_q31_pf13271,
        evidence_kind="COMPUTATIONAL",
        source_kind="INTERPRO_PFAM",
        method="Pfam profile HMM PF13271 search",
        observed_effect="Significant PF13271 HMM match across residues 6..146.",
        interpretation="Residues 6..146 of Q31PW6 belong to the PF13271 (DUF4062) family.",
        polarity="POSITIVE",
        raw_score=1.4e-26,
        score_metric="E_VALUE",
        primary_experiment_key="HMM:PF13271/Q31PW6_6-146",
    )
    obs_q31_cdd_mirror = build_region_observation(
        observation_id="obs_q31pw6_cdd_mirror",
        region=reg_q31_pf13271,
        evidence_kind="COMPUTATIONAL",
        source_kind="CDSEARCH",
        method="NCBI CD-Search mirror of Pfam PF13271 profile",
        observed_effect="Mirrored PF13271 hit on Q31PW6 6..146 with bitscore 98.4.",
        interpretation="Mirrored domain call on 6..146.",
        polarity="POSITIVE",
        raw_score=98.4,
        score_metric="BITSCORE",
        primary_experiment_key="HMM:PF13271/Q31PW6_6-146",
        derived_from_observation_ids=["obs_q31pw6_pfam_hit"],
    )
    obs_q31_e83_conservation = build_region_observation(
        observation_id="obs_q31pw6_E83_alignment",
        region=reg_q31_e83,
        evidence_kind="COMPUTATIONAL",
        source_kind="CURATED_ANNOTATION",
        method="Profile HMM active-site alignment against experimentally characterized TEP1 Glu1008",
        observed_effect="Q31PW6 retains Glu83 at PF13271 match state 78 aligned to catalytic Glu1008 of TEP1.",
        interpretation="Conservation of the catalytic glutamate suggests potential NADase-like active-site geometry, but activity is untested in Q31PW6.",
        polarity="POSITIVE",
        primary_experiment_key="ALIGN:PF13271_state78/Q31PW6_E83",
    )
    obs_q31_cog5635 = build_region_observation(
        observation_id="obs_q31pw6_cog5635_architecture",
        region=reg_q31_cog5635,
        evidence_kind="CONTEXTUAL",
        source_kind="CURATED_ANNOTATION",
        method="EggNOG COG5635 orthogroup vs. literature architectural comparison",
        observed_effect="C-terminal region 160..480 is annotated as COG5635 ('Predicted NACHT NTPase') in UniProt/EggNOG and as a central NTPase module by Osinski et al.",
        interpretation="Architectural co-occurrence suggests NTP-regulated effector coupling, with unresolved NACHT-specific vs. general NTPase subfamily classification.",
        polarity="POSITIVE",
        primary_experiment_key="ARCH:COG5635/Q31PW6_160-480",
        limitations="No experimental ATPase or NADase assay has been performed on Q31PW6.",
    )

    g2_obs = [obs_q31_pfam, obs_q31_cdd_mirror, obs_q31_e83_conservation, obs_q31_cog5635]
    g2_groups = deduplicate_observations(g2_obs)
    g2_regs = {
        r["region_id"]: r for r in (reg_q31_pf13271, reg_q31_e83, reg_q31_cog5635)
    }
    g2_maps = [map_e83_to_q31_domain, map_cog5635_disjoint]

    claim_q31_nadase = synthesize_region_claim(
        claim_id="claim_q31pw6_pf13271_nadase_hypothesis",
        label="Hypothesized TIR-like NAD+ hydrolase activity on Q31PW6 PF13271 domain (6-146)",
        function_aspect="CATALYTIC_ACTIVITY",
        ontology_term_id="GO:0003953",
        ontology_term_label="NAD+ nucleosidase activity",
        target_region=reg_q31_pf13271,
        regions_by_id=g2_regs,
        observations=[obs_q31_pfam, obs_q31_cdd_mirror, obs_q31_e83_conservation],
        evidence_groups=g2_groups[:2],
        coordinate_mappings=[map_e83_to_q31_domain],
        additional_scope_blocks=[
            "No biochemical assay has been performed on Synechococcus elongatus Q31PW6; multiple PF13271 members lacking testing or in eukaryotic paralogues are inactive.",
        ],
        discriminating_experiments=[
            "Purify Q31PW6 (6-146) and full-length Q31PW6 (1-494), plus an E83A point mutant, and measure NAD+ hydrolysis by HPLC/1H-NMR.",
            "Test whether nucleotide binding/hydrolysis by the C-terminal 160-480 NTPase module regulates N-terminal PF13271 (6-146) catalysis.",
        ],
    )
    claim_q31_arch = synthesize_region_claim(
        claim_id="claim_q31pw6_cog5635_ntpase_architecture",
        label="Hypothesized NTPase / NACHT-like regulatory module in Q31PW6 C-terminal region (160-480)",
        function_aspect="ARCHITECTURAL_COOCCURRENCE",
        target_region=reg_q31_cog5635,
        regions_by_id=g2_regs,
        observations=[obs_q31_cog5635],
        evidence_groups=[g2_groups[2]],
        coordinate_mappings=[map_cog5635_disjoint],
        discriminating_experiments=[
            "Determine an experimental structure or high-confidence domain-boundary alignment of Q31PW6 (160-480) against canonical NACHT vs STAND NTPase folds and assay NTP hydrolysis."
        ],
    )

    graph2 = {
        "graph_id": "pf13271_q31pw6_computational_hypothesis",
        "pfam_id": "PF13271",
        "title": "Synechococcus elongatus Q31PW6 PF13271 (6-146) computational hypothesis and COG5635 architectural ambiguity",
        "description": (
            "Demonstrates deduplication of mirrored HMM hits with heterogeneous score metrics "
            "(E_VALUE vs BITSCORE), conserved active-site residue mapping (Glu83), and explicit "
            "separation of computational/architectural hypotheses from biological causation."
        ),
        "sequences": [seq_q31pw6],
        "regions": list(g2_regs.values()),
        "coordinate_mappings": g2_maps,
        "observations": g2_obs,
        "evidence_groups": g2_groups,
        "synthesized_claims": [claim_q31_nadase, claim_q31_arch],
        "reasoning_edges": [
            build_reasoning_edge(
                edge_id="edge_e83_maps_q31_pf13271",
                subject="reg_Q31PW6_E83",
                predicate="maps_to_region",
                object_id="reg_Q31PW6_pf13271_6_146",
                edge_category="COORDINATE_MAPPING_LINK",
                support="INFERRED",
                evidence_kind="COMPUTATIONAL",
                rationale="Profile HMM state 78 maps conserved Glu83 inside Q31PW6 6..146.",
            ),
            build_reasoning_edge(
                edge_id="edge_hmm_supports_q31_hypothesis",
                subject=g2_groups[0]["group_id"],
                predicate="supports_claim",
                object_id="claim_q31pw6_pf13271_nadase_hypothesis",
                edge_category="EVIDENCE_LINK",
                support="HYPOTHESIZED",
                evidence_kind="COMPUTATIONAL",
                rationale="Deduplicated Pfam/CD-Search HMM hit establishes PF13271 domain membership.",
            ),
            build_reasoning_edge(
                edge_id="edge_e83_inferred_homolog",
                subject=g2_groups[1]["group_id"],
                predicate="inferred_from_homolog_region",
                object_id="claim_q31pw6_pf13271_nadase_hypothesis",
                edge_category="INFERENCE_LINK",
                support="HYPOTHESIZED",
                evidence_kind="COMPUTATIONAL",
                rationale="Conserved Glu83 aligns to TEP1 Glu1008, supporting a testable hypothesis rather than observed causation.",
            ),
            build_reasoning_edge(
                edge_id="edge_cog5635_cooccurs",
                subject="reg_Q31PW6_cog5635_160_480",
                predicate="cooccurs_with_domain",
                object_id="reg_Q31PW6_pf13271_6_146",
                edge_category="INFERENCE_LINK",
                support="HYPOTHESIZED",
                evidence_kind="CONTEXTUAL",
                rationale="C-terminal COG5635 region co-occurs in the same polypeptide but is disjoint from PF13271 (6..146).",
            ),
        ],
    }

    # --- Graph 3: Discontinuous domain gap mutation, conflicting assays & unannotated homolog ---
    seq_disc = build_sequence_identity(
        "P0A9Q7",
        sequence_length=360,
        sequence_sha256=hashlib.sha256(b"P0A9Q7_MULTIDOMAIN_360AA").hexdigest(),
        sequence_version=1,
        taxon_id="NCBITaxon:83333",
        organism="Escherichia coli K-12",
        sequence_id="seq_P0A9Q7_v1",
    )
    seq_unannotated = build_sequence_identity(
        "O34567",
        sequence_length=250,
        sequence_sha256=hashlib.sha256(b"O34567_UNANNOTATED_250AA").hexdigest(),
        sequence_version=1,
        taxon_id="NCBITaxon:224308",
        organism="Bacillus subtilis subsp. subtilis str. 168",
        sequence_id="seq_O34567_v1",
    )

    reg_disc_duf = build_sequence_region(
        region_id="reg_P0A9Q7_disc_duf_50_120_210_290",
        sequence_identity=seq_disc,
        label="Discontinuous two-segment DUF domain (50-120, 210-290; inserted domain at 121-209)",
        region_kind="DISCONTINUOUS_DOMAIN",
        coordinate_status="DISCONTINUOUS",
        intervals=[{"start": 50, "end": 120}, {"start": 210, "end": 290}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="50-120, 210-290",
        pfam_id="PF00001",
    )
    reg_gap_mut_165 = build_sequence_region(
        region_id="reg_P0A9Q7_mut_D165A_in_gap",
        sequence_identity=seq_disc,
        label="Point mutation D165A located in the inserted inter-segment gap (121-209)",
        region_kind="MUTATION_SITE",
        coordinate_status="EXACT",
        intervals=[{"start": 165, "end": 165, "residue_identity": "D"}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="165",
    )
    reg_unannotated_duf = build_sequence_region(
        region_id="reg_O34567_duf_15_195",
        sequence_identity=seq_unannotated,
        label="Uncharacterized homolog domain on O34567 (15-195) with no experimental assays",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 15, "end": 195}],
        source_coordinate_system="UNIPROT_CANONICAL",
        source_coordinates_text="15-195",
        pfam_id="PF00001",
    )

    map_gap_mut = classify_region_mapping(
        mapping_id="map_D165A_to_disc_duf",
        source_region=reg_gap_mut_165,
        target_region=reg_disc_duf,
        source_sequence=seq_disc,
        target_sequence=seq_disc,
        mapping_kind="MUTATION_TO_DOMAIN",
    )

    obs_gap_mut = build_region_observation(
        observation_id="obs_P0A9Q7_D165A_phenotype",
        region=reg_disc_duf,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Full-length D165A substitution assay",
        mutation_region_ids=["reg_P0A9Q7_mut_D165A_in_gap"],
        observed_effect="D165A substitution at position 165 abolishes whole-protein esterase activity.",
        interpretation="Proposed loss of activity, but residue 165 lies in the inserted gap (121..209) outside the discontinuous DUF segments [50..120, 210..290].",
        polarity="POSITIVE",
        primary_experiment_key="EXP:P0A9Q7/D165A_esterase",
        limitations="Mutation site 165 is disjoint from the discontinuous DUF segments.",
    )
    obs_conflict_pos = build_region_observation(
        observation_id="obs_P0A9Q7_assay_positive",
        region=reg_disc_duf,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Colorimetric pNP-butyrate assay on crude extract",
        observed_effect="Weak hydrolysis detected in crude lysate overexpression.",
        interpretation="Initial report of weak esterase activity.",
        polarity="POSITIVE",
        primary_experiment_key="EXP:P0A9Q7/crude_pNP_assay",
    )
    obs_conflict_neg = build_region_observation(
        observation_id="obs_P0A9Q7_assay_negative",
        region=reg_disc_duf,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Purified homogeneous enzyme assay with pNP-butyrate",
        observed_effect="Zero hydrolysis above background after removing host contaminating esterases.",
        interpretation="Purified domain lacks intrinsic esterase activity; earlier crude-extract signal is contested.",
        polarity="NEGATIVE",
        primary_experiment_key="EXP:P0A9Q7/purified_pNP_assay",
    )

    g3_obs = [obs_gap_mut, obs_conflict_pos, obs_conflict_neg]
    g3_groups = deduplicate_observations(g3_obs)
    g3_regs = {
        r["region_id"]: r for r in (reg_disc_duf, reg_gap_mut_165, reg_unannotated_duf)
    }

    claim_conflict = synthesize_region_claim(
        claim_id="claim_P0A9Q7_conflicting_esterase",
        label="Unresolved esterase claim on discontinuous domain (50-120, 210-290) due to out-of-domain gap mutation D165A and conflicting purified vs crude assays",
        function_aspect="CATALYTIC_ACTIVITY",
        target_region=reg_disc_duf,
        regions_by_id=g3_regs,
        observations=g3_obs,
        evidence_groups=g3_groups,
        coordinate_mappings=[map_gap_mut],
        discriminating_experiments=[
            "Mutate conserved catalytic-candidate residues strictly inside segments 50..120 or 210..290 (excluding the inserted domain 121..209) and assay homogeneously purified protein."
        ],
    )
    claim_unannotated = synthesize_region_claim(
        claim_id="claim_O34567_unknown_function",
        label="Uncharacterized status of O34567 domain (15-195) with no experimental observations",
        function_aspect="UNKNOWN_FUNCTION",
        target_region=reg_unannotated_duf,
        regions_by_id=g3_regs,
        observations=[],
        evidence_groups=[],
        coordinate_mappings=[],
    )

    graph3 = {
        "graph_id": "discontinuous_and_conflicting_localization",
        "pfam_id": "PF00001",
        "title": "Discontinuous domain inter-segment gap localization check, conflicting assays, and unknown vs. negative distinction",
        "description": (
            "Demonstrates that a mutation at residue 165 inside the inter-segment gap (121..209) "
            "of a discontinuous domain [50..120, 210..290] is classified as DISJOINT_OUTSIDE_REGION, "
            "conflicting assays remain CONFLICTING_UNRESOLVED, and an unannotated homolog is "
            "INSUFFICIENT_EVIDENCE / UNKNOWN_FUNCTION rather than negative."
        ),
        "sequences": [seq_disc, seq_unannotated],
        "regions": list(g3_regs.values()),
        "coordinate_mappings": [map_gap_mut],
        "observations": g3_obs,
        "evidence_groups": g3_groups,
        "synthesized_claims": [claim_conflict, claim_unannotated],
        "reasoning_edges": [
            build_reasoning_edge(
                edge_id="edge_d165a_disjoint_from_disc_duf",
                subject="reg_P0A9Q7_mut_D165A_in_gap",
                predicate="maps_to_region",
                object_id="reg_P0A9Q7_disc_duf_50_120_210_290",
                edge_category="COORDINATE_MAPPING_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Residue 165 falls in the inter-segment gap 121..209, disjoint from [50..120, 210..290].",
            ),
            build_reasoning_edge(
                edge_id="edge_pos_supports_conflict_claim",
                subject=g3_groups[1]["group_id"],
                predicate="supports_claim",
                object_id="claim_P0A9Q7_conflicting_esterase",
                edge_category="EVIDENCE_LINK",
                support="CONTESTED",
                evidence_kind="EXPERIMENTAL",
                rationale="Crude extract assay reported positive activity.",
            ),
            build_reasoning_edge(
                edge_id="edge_neg_contradicts_conflict_claim",
                subject=g3_groups[2]["group_id"],
                predicate="contradicts_claim",
                object_id="claim_P0A9Q7_conflicting_esterase",
                edge_category="EVIDENCE_LINK",
                support="CONTESTED",
                evidence_kind="EXPERIMENTAL",
                rationale="Purified enzyme assay found zero activity above background, contradicting the crude-extract report.",
            ),
            build_reasoning_edge(
                edge_id="edge_unannotated_anchored",
                subject="reg_O34567_duf_15_195",
                predicate="anchored_to_sequence",
                object_id="seq_O34567_v1",
                edge_category="COORDINATE_MAPPING_LINK",
                support="OBSERVED",
                evidence_kind="COMPUTATIONAL",
                rationale="Unannotated homolog region 15..195 has no experimental observations (INSUFFICIENT_EVIDENCE).",
            ),
        ],
    }

    validate_region_reasoning_graphs("PF13271", [graph1, graph2])
    validate_region_reasoning_graphs("PF00001", [graph3])
    return [graph1, graph2, graph3]


def _infer_repo_root(path: Path) -> Path | None:
    resolved = path.resolve()
    for parent in resolved.parents:
        if (parent / "curation" / "families").is_dir() or (parent / "src" / "dufmech").is_dir():
            return parent
    default_root = Path(__file__).resolve().parents[2]
    if (default_root / "src" / "dufmech").is_dir():
        return default_root
    return None


def _load_graphs_from_family_yaml(
    path: Path, *, root: Path | None = None
) -> list[dict[str, Any]]:
    data = read_yaml(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise SequenceReasoningError(f"{path} must contain a YAML mapping")
    pfam_id = str(data.get("pfam_id", ""))
    graphs = list(data.get("sequence_reasoning_graphs") or ())
    if graphs:
        validate_region_reasoning_graphs(
            pfam_id,
            graphs,
            causal_graphs=data.get("causal_graphs"),
            root=root if root is not None else _infer_repo_root(path),
        )
    return graphs


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Inspect, validate, and query DUFMech sequence-coordinate reasoning graphs."
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Use built-in representative end-to-end reasoning graphs (TEP1, Q31PW6, discontinuous/conflicting).",
    )
    parser.add_argument(
        "--record",
        type=Path,
        help="Path to a FamilyRecord or FamilyCuration YAML file containing sequence_reasoning_graphs.",
    )
    parser.add_argument(
        "--graph-id",
        help="Filter to a specific RegionReasoningGraph graph_id.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format for inspectable view (default: markdown).",
    )
    parser.add_argument(
        "--query-sequence",
        help="Query synthesized claims on a specific sequence_id.",
    )
    parser.add_argument(
        "--start",
        type=int,
        help="1-based inclusive start coordinate for --query-sequence.",
    )
    parser.add_argument(
        "--end",
        type=int,
        help="1-based inclusive end coordinate for --query-sequence.",
    )
    parser.add_argument(
        "--trace-claim",
        help="Trace complete evidence, deduplication, and coordinate provenance for a claim_id.",
    )
    args = parser.parse_args(argv)

    if args.demo:
        graphs = build_representative_reasoning_graphs()
    elif args.record:
        graphs = _load_graphs_from_family_yaml(args.record)
    else:
        graphs = build_representative_reasoning_graphs()

    if args.graph_id:
        graphs = [g for g in graphs if g.get("graph_id") == args.graph_id]
        if not graphs:
            raise SystemExit(f"No graph found with graph_id={args.graph_id!r}")

    if args.trace_claim:
        for g in graphs:
            claim_ids = {c["claim_id"] for c in (g.get("synthesized_claims") or ())}
            if args.trace_claim in claim_ids:
                trace = trace_claim_evidence(g, args.trace_claim)
                print(json.dumps(trace, indent=2, sort_keys=True))
                return 0
        raise SystemExit(f"Claim {args.trace_claim!r} not found in selected graphs")

    if args.query_sequence:
        matches: list[dict[str, Any]] = []
        for g in graphs:
            seq_ids = {s["sequence_id"] for s in (g.get("sequences") or ())}
            if args.query_sequence in seq_ids:
                matches.extend(
                    query_claims_for_region(
                        g,
                        sequence_id=args.query_sequence,
                        start=args.start,
                        end=args.end,
                    )
                )
        print(json.dumps(matches, indent=2, sort_keys=True))
        return 0

    if args.format == "json":
        print(json.dumps(graphs, indent=2, sort_keys=True))
    else:
        rendered = "\n---\n\n".join(render_inspectable_view(g, fmt="markdown") for g in graphs)
        print(rendered, end="")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
