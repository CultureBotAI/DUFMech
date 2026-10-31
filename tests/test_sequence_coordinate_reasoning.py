"""Unit and end-to-end tests for sequence-coordinate-aware reasoning."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest

from dufmech.records import RecordError, validate_record, validator
from dufmech.sequence_reasoning import (
    SequenceReasoningError,
    build_reasoning_edge,
    build_region_observation,
    build_representative_reasoning_graphs,
    build_sequence_identity,
    build_sequence_region,
    classify_region_mapping,
    combine_scores_strictly,
    convert_construct_to_reference,
    convert_mature_peptide_to_reference,
    convert_zero_based_half_open_to_reference,
    deduplicate_observations,
    main,
    normalize_cath_row,
    normalize_cdsearch_row,
    normalize_ncbifam_row,
    normalize_pdbe_kb_row,
    normalize_pfam_member_row,
    normalize_quickgo_row,
    normalize_rhea_row,
    query_claims_for_region,
    region_bounding_span,
    region_inter_segment_gaps,
    region_residue_positions,
    region_total_length,
    render_inspectable_view,
    sequence_identity_from_example_row,
    synthesize_region_claim,
    trace_claim_evidence,
    validate_region_reasoning_graphs,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_canary_vertical_slice_schema_and_synthesis() -> None:
    """Offline end-to-end fixture canary: sequence -> region -> mapping -> deduplication -> claim -> schema."""
    raw_seq = "M" * 50 + "ACDEFGHIKLMNPQRSTVWY" + "G" * 30  # 100 aa, E at position 54
    seq = build_sequence_identity(
        "P12345",
        sequence=raw_seq,
        sequence_version=1,
        taxon_id="NCBITaxon:9606",
        organism="Homo sapiens",
    )
    assert seq["sequence_length"] == 100
    assert seq["sequence_sha256"] == hashlib.sha256(raw_seq.encode("ascii")).hexdigest()

    domain_reg = build_sequence_region(
        region_id="reg_P12345_duf",
        sequence_identity=seq,
        label="Test DUF domain (45-80)",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 45, "end": 80}],
        pfam_id="PF13271",
        reference_sequence=raw_seq,
    )
    site_reg = convert_construct_to_reference(
        construct_start_on_ref=41,
        construct_end_on_ref=90,
        local_start=14,
        local_end=14,
        sequence_identity=seq,
        region_id="reg_P12345_E54",
        label="Catalytic Glu54 (construct residue 14)",
        region_kind="CATALYTIC_SITE",
        residue_identity="E",
        reference_sequence=raw_seq,
    )
    assert site_reg["intervals"] == [{"start": 54, "end": 54, "residue_identity": "E"}]

    mapping = classify_region_mapping(
        mapping_id="map_E54_to_duf",
        source_region=site_reg,
        target_region=domain_reg,
        source_sequence=seq,
        target_sequence=seq,
        mapping_kind="MUTATION_TO_DOMAIN",
    )
    assert mapping["equivalence_status"] == "RESIDUE_INSIDE_REGION"

    obs1 = build_region_observation(
        observation_id="obs_assay_primary",
        region=domain_reg,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Purified domain E54A mutagenesis and hydrolase assay",
        mutation_region_ids=["reg_P12345_E54"],
        observed_effect="Wild-type domain cleaves substrate; E54A abolishes cleavage.",
        interpretation="Domain 45..80 catalyzes hydrolysis dependent on Glu54.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:12345678/P12345_45-80/E54A",
    )
    obs2 = build_region_observation(
        observation_id="obs_assay_mirrored",
        region=domain_reg,
        evidence_kind="EXPERIMENTAL",
        source_kind="QUICKGO",
        method="Mirrored GO IDA annotation from PMID:12345678",
        observed_effect="GO hydrolase annotation citing PMID:12345678.",
        interpretation="Mirrored database record of the same experiment.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:12345678/P12345_45-80/E54A",
        derived_from_observation_ids=["obs_assay_primary"],
    )
    groups = deduplicate_observations([obs1, obs2])
    assert len(groups) == 1
    assert groups[0]["observation_ids"] == ["obs_assay_primary", "obs_assay_mirrored"]

    claim = synthesize_region_claim(
        claim_id="claim_P12345_hydrolase",
        label="Demonstrated hydrolase activity on P12345 (45-80)",
        function_aspect="CATALYTIC_ACTIVITY",
        ontology_term_id="GO:0016787",
        ontology_term_label="hydrolase activity",
        target_region=domain_reg,
        regions_by_id={"reg_P12345_duf": domain_reg, "reg_P12345_E54": site_reg},
        observations=[obs1, obs2],
        evidence_groups=groups,
        coordinate_mappings=[mapping],
    )
    assert claim["synthesis_status"] == "EXPERIMENTALLY_DEMONSTRATED"
    assert claim["claimed_scope"] == "TESTED_REGION_ONLY"

    graph = {
        "graph_id": "canary_graph",
        "pfam_id": "PF13271",
        "title": "Canary vertical slice graph",
        "sequences": [seq],
        "regions": [domain_reg, site_reg],
        "coordinate_mappings": [mapping],
        "observations": [obs1, obs2],
        "evidence_groups": groups,
        "synthesized_claims": [claim],
        "reasoning_edges": [
            build_reasoning_edge(
                edge_id="edge_canary_support",
                subject=groups[0]["group_id"],
                predicate="supports_claim",
                object_id="claim_P12345_hydrolase",
                edge_category="EVIDENCE_LINK",
                support="OBSERVED",
                evidence_kind="EXPERIMENTAL",
                rationale="Deduplicated experimental group supports claim.",
            )
        ],
    }
    validate_region_reasoning_graphs("PF13271", [graph])
    overlay_payload = {
        "pfam_id": "PF13271",
        "curation_status": "IN_PROGRESS",
        "sequence_reasoning_graphs": [graph],
    }
    errors = list(validator("FamilyCuration").iter_errors(overlay_payload))
    assert errors == []


def test_coordinate_conversions_and_bounds_validation() -> None:
    """Verify 1-based inclusive coordinate bounds, residue checks, and coordinate system conversions."""
    raw_seq = "M" * 20 + "ARNDCQEGHILKMFPSTWYV" + "A" * 60  # 100 aa; pos 21='A', 22='R', 23='N', 24='D'
    seq = build_sequence_identity("Q99973", sequence=raw_seq)

    # 0-based or negative start rejected
    with pytest.raises(ValueError, match="must be an integer >= 1"):
        build_sequence_region(
            region_id="bad_zero",
            sequence_identity=seq,
            label="Zero start",
            region_kind="DOMAIN_HIT",
            intervals=[{"start": 0, "end": 10}],
        )

    # Inverted interval start > end rejected
    with pytest.raises(ValueError, match="inverted 1-based interval"):
        build_sequence_region(
            region_id="bad_inverted",
            sequence_identity=seq,
            label="Inverted",
            region_kind="DOMAIN_HIT",
            intervals=[{"start": 50, "end": 40}],
        )

    # Out-of-bounds end > sequence_length rejected
    with pytest.raises(ValueError, match="exceeds sequence_length 100"):
        build_sequence_region(
            region_id="bad_oob",
            sequence_identity=seq,
            label="Out of bounds",
            region_kind="DOMAIN_HIT",
            intervals=[{"start": 80, "end": 101}],
        )

    # Residue mismatch against reference sequence rejected
    with pytest.raises(ValueError, match="residue mismatch at 21..21"):
        build_sequence_region(
            region_id="bad_residue",
            sequence_identity=seq,
            label="Wrong residue",
            region_kind="CATALYTIC_SITE",
            intervals=[{"start": 21, "end": 21, "residue_identity": "W"}],
            reference_sequence=raw_seq,
        )

    # Mature peptide conversion (after signal peptide 1..20, mature position 4 is reference position 24 = 'D')
    mature_reg = convert_mature_peptide_to_reference(
        signal_peptide_end=20,
        mature_start=4,
        mature_end=4,
        sequence_identity=seq,
        region_id="reg_mature_D24",
        label="Mature Asp4 -> Precursor Asp24",
        region_kind="CATALYTIC_SITE",
        residue_identity="D",
        reference_sequence=raw_seq,
    )
    assert mature_reg["intervals"] == [{"start": 24, "end": 24, "residue_identity": "D"}]
    assert mature_reg["source_coordinate_system"] == "MATURE_PEPTIDE"

    # 0-based half-open [20, 40) -> 1-based inclusive 21..40
    bed_reg = convert_zero_based_half_open_to_reference(
        zero_start=20,
        zero_end=40,
        sequence_identity=seq,
        region_id="reg_from_zero_half_open",
        label="Converted from [20, 40)",
    )
    assert bed_reg["intervals"] == [{"start": 21, "end": 40}]
    assert region_total_length(bed_reg) == 20

    # Construct conversion out of construct bounds rejected
    with pytest.raises(ValueError, match="exceeds construct length"):
        convert_construct_to_reference(
            construct_start_on_ref=21,
            construct_end_on_ref=40,
            local_start=25,
            local_end=25,
            sequence_identity=seq,
            region_id="bad_construct_pos",
            label="Exceeds construct",
        )


def test_sequence_version_isoform_and_checksum_mismatch() -> None:
    """Verify that sequence-version, isoform, and SHA-256 mismatches are caught and block transfer."""
    raw_v1 = "M" * 120
    raw_v2 = "M" * 119 + "W"
    with pytest.raises(ValueError, match="sequence_sha256 mismatch"):
        build_sequence_identity(
            "Q99973",
            sequence=raw_v1,
            sequence_sha256=hashlib.sha256(raw_v2.encode("ascii")).hexdigest(),
        )
    with pytest.raises(ValueError, match="does not belong to accession"):
        build_sequence_identity("Q99973", sequence=raw_v1, isoform="P12345-2")

    seq_v1 = build_sequence_identity(
        "Q99973", sequence=raw_v1, isoform="Q99973-1", sequence_version=1, sequence_id="seq_Q99973_v1"
    )
    seq_v2 = build_sequence_identity(
        "Q99973", sequence=raw_v2, isoform="Q99973-2", sequence_version=2, sequence_id="seq_Q99973_v2"
    )
    reg_v1 = build_sequence_region(
        region_id="reg_v1_domain",
        sequence_identity=seq_v1,
        label="Domain on v1",
        region_kind="EXPERIMENTAL_CONSTRUCT",
        intervals=[{"start": 10, "end": 100}],
    )
    reg_v2 = build_sequence_region(
        region_id="reg_v2_domain",
        sequence_identity=seq_v2,
        label="Domain on v2",
        region_kind="DOMAIN_HIT",
        intervals=[{"start": 10, "end": 100}],
    )
    mapping = classify_region_mapping(
        mapping_id="map_v1_to_v2",
        source_region=reg_v1,
        target_region=reg_v2,
        source_sequence=seq_v1,
        target_sequence=seq_v2,
    )
    assert mapping["equivalence_status"] == "SEQUENCE_VERSION_MISMATCH"
    assert "cannot be silently transferred" in mapping["mapping_uncertainty"]

    obs = build_region_observation(
        observation_id="obs_on_v1",
        region=reg_v1,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Biochemical assay on v1",
        observed_effect="Active in v1.",
        interpretation="Catalytic activity.",
        polarity="POSITIVE",
        primary_experiment_key="EXP:v1_assay",
    )
    groups = deduplicate_observations([obs])
    claim = synthesize_region_claim(
        claim_id="claim_on_v2_blocked_by_mismatch",
        label="Transfer to v2 blocked by version mismatch",
        function_aspect="CATALYTIC_ACTIVITY",
        target_region=reg_v2,
        regions_by_id={"reg_v1_domain": reg_v1, "reg_v2_domain": reg_v2},
        observations=[obs],
        evidence_groups=groups,
        coordinate_mappings=[mapping],
    )
    assert claim["synthesis_status"] == "CONFLICTING_UNRESOLVED"
    assert claim["claimed_scope"] == "UNRESOLVED_SCOPE"
    assert any("SEQUENCE_VERSION_MISMATCH" in b for b in claim["scope_transfer_blocks"])


def test_discontinuous_domains_and_inter_segment_gap_mutations() -> None:
    """Verify multi-segment discontinuous domain arithmetic and gap-mutation rejection."""
    seq = build_sequence_identity(
        "P0A9Q7",
        sequence_length=350,
        sequence_sha256=hashlib.sha256(b"P0A9Q7_350").hexdigest(),
    )
    # Discontinuous status with only 1 interval rejected
    with pytest.raises(ValueError, match="requires at least 2 disjoint intervals"):
        build_sequence_region(
            region_id="bad_disc",
            sequence_identity=seq,
            label="Single segment marked discontinuous",
            region_kind="DISCONTINUOUS_DOMAIN",
            coordinate_status="DISCONTINUOUS",
            intervals=[{"start": 10, "end": 50}],
        )
    # Overlapping segments rejected
    with pytest.raises(ValueError, match="overlaps or is not strictly ordered"):
        build_sequence_region(
            region_id="bad_overlap_disc",
            sequence_identity=seq,
            label="Overlapping segments",
            region_kind="DISCONTINUOUS_DOMAIN",
            coordinate_status="DISCONTINUOUS",
            intervals=[{"start": 10, "end": 60}, {"start": 55, "end": 100}],
        )

    disc_reg = build_sequence_region(
        region_id="reg_disc_50_120_210_290",
        sequence_identity=seq,
        label="Discontinuous domain [50..120, 210..290]",
        region_kind="DISCONTINUOUS_DOMAIN",
        coordinate_status="DISCONTINUOUS",
        intervals=[{"start": 50, "end": 120}, {"start": 210, "end": 290}],
    )
    assert region_total_length(disc_reg) == (120 - 50 + 1) + (290 - 210 + 1) == 152
    assert region_bounding_span(disc_reg) == (50, 290)
    assert region_inter_segment_gaps(disc_reg) == [(121, 209)]
    positions = region_residue_positions(disc_reg)
    assert 85 in positions
    assert 250 in positions
    assert 165 not in positions  # Inside the inserted gap 121..209!

    gap_site = build_sequence_region(
        region_id="reg_mut_165_in_gap",
        sequence_identity=seq,
        label="Mutation at 165 inside inter-segment gap",
        region_kind="MUTATION_SITE",
        intervals=[{"start": 165, "end": 165}],
    )
    seg2_site = build_sequence_region(
        region_id="reg_mut_245_in_seg2",
        sequence_identity=seq,
        label="Mutation at 245 inside segment 2",
        region_kind="MUTATION_SITE",
        intervals=[{"start": 245, "end": 245}],
    )
    gap_map = classify_region_mapping(
        mapping_id="map_gap_to_disc",
        source_region=gap_site,
        target_region=disc_reg,
        source_sequence=seq,
        target_sequence=seq,
        mapping_kind="MUTATION_TO_DOMAIN",
    )
    assert gap_map["equivalence_status"] == "DISJOINT_OUTSIDE_REGION"
    assert "inter-segment gap 121..209" in gap_map["mapping_uncertainty"]

    seg2_map = classify_region_mapping(
        mapping_id="map_seg2_to_disc",
        source_region=seg2_site,
        target_region=disc_reg,
        source_sequence=seq,
        target_sequence=seq,
        mapping_kind="MUTATION_TO_DOMAIN",
    )
    assert seg2_map["equivalence_status"] == "RESIDUE_INSIDE_REGION"


def test_mapping_ambiguity_partial_overlap_and_unlocalized_whole_protein() -> None:
    """Verify that partial coordinate overlap and unlocalized whole-protein assays block domain claims."""
    seq = build_sequence_identity(
        "Q99973",
        sequence_length=500,
        sequence_sha256=hashlib.sha256(b"Q99973_500").hexdigest(),
    )
    duf_reg = build_sequence_region(
        region_id="reg_duf_100_200",
        sequence_identity=seq,
        label="DUF domain 100..200",
        region_kind="DOMAIN_HIT",
        intervals=[{"start": 100, "end": 200}],
    )
    partial_construct = build_sequence_region(
        region_id="reg_construct_50_150",
        sequence_identity=seq,
        label="Partially overlapping construct 50..150",
        region_kind="EXPERIMENTAL_CONSTRUCT",
        intervals=[{"start": 50, "end": 150}],
    )
    full_protein = build_sequence_region(
        region_id="reg_full_1_500",
        sequence_identity=seq,
        label="Full-length multidomain protein 1..500",
        region_kind="FULL_LENGTH_PROTEIN",
        coordinate_status="WHOLE_PROTEIN_UNLOCALIZED",
        intervals=[{"start": 1, "end": 500}],
    )

    partial_map = classify_region_mapping(
        mapping_id="map_partial",
        source_region=partial_construct,
        target_region=duf_reg,
        source_sequence=seq,
        target_sequence=seq,
    )
    assert partial_map["equivalence_status"] == "PARTIAL_OVERLAP_NOT_EQUIVALENT"
    assert partial_map["overlap_residues"] == 51

    full_map = classify_region_mapping(
        mapping_id="map_full_unlocalized",
        source_region=full_protein,
        target_region=duf_reg,
        source_sequence=seq,
        target_sequence=seq,
    )
    assert full_map["equivalence_status"] == "CONSTRUCT_CONTAINS_DOMAIN"
    assert "does not localize the effect to the domain" in full_map["mapping_uncertainty"]

    obs_full = build_region_observation(
        observation_id="obs_whole_protein_knockout",
        region=full_protein,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Whole-gene deletion phenotype",
        observed_effect="Deletion of full-length gene (1..500) reduces growth.",
        interpretation="Protein is involved in growth, but domain localization is untested.",
        polarity="POSITIVE",
        primary_experiment_key="EXP:whole_gene_ko",
    )
    groups = deduplicate_observations([obs_full])
    claim = synthesize_region_claim(
        claim_id="claim_unlocalized_blocked",
        label="Attempted domain localization from whole-protein knockout",
        function_aspect="PROCESS_CONTRIBUTION",
        target_region=duf_reg,
        regions_by_id={
            "reg_duf_100_200": duf_reg,
            "reg_full_1_500": full_protein,
        },
        observations=[obs_full],
        evidence_groups=groups,
        coordinate_mappings=[full_map],
    )
    assert claim["synthesis_status"] == "CONFLICTING_UNRESOLVED"
    assert claim["claimed_scope"] == "UNRESOLVED_SCOPE"
    assert any("without a domain-internal catalytic mutation" in b for b in claim["scope_transfer_blocks"])


def test_adapters_for_existing_dufmech_sources_and_score_non_interchangeability() -> None:
    """Test normalization adapters for protein_examples, protein_members, pdbe_kb, cdsearch, cath, ncbifam, quickgo, rhea."""
    raw_seq = "A" * 200
    seq = sequence_identity_from_example_row({
        "uniprot_accession": "Q31PW6",
        "sequence": raw_seq,
        "sequence_length": 200,
        "sequence_sha256": hashlib.sha256(raw_seq.encode("ascii")).hexdigest(),
        "taxon_id": "1140",
        "organism": "Synechococcus elongatus",
        "uniprot_version": "2026_02",
    })
    assert seq["taxon_id"] == "NCBITaxon:1140"

    pfam_reg, pfam_obs = normalize_pfam_member_row(
        {
            "pfam_id": "PF13271",
            "uniprot_accession": "Q31PW6",
            "fragments": [{"start": 6, "end": 146}],
        },
        sequence_identity=seq,
    )
    assert pfam_reg["region_kind"] == "DOMAIN_HIT"
    assert pfam_obs["source_kind"] == "INTERPRO_PFAM"

    _pdbe_reg, pdbe_obs, pdbe_map = normalize_pdbe_kb_row(
        {
            "uniprot_accession": "Q31PW6",
            "pdb_id": "8xyz",
            "chain_id": "A",
            "annotation_type": "ligand_binding",
            "annotation_label": "NAD",
            "uniprot_start": 50,
            "uniprot_end": 90,
            "pdb_residues": ["50A", "83"],
            "mutations": ["E83A"],
        },
        sequence_identity=seq,
        target_domain_region=pfam_reg,
    )
    assert pdbe_obs["evidence_kind"] == "EXPERIMENTAL"
    assert pdbe_map is not None
    assert pdbe_map["equivalence_status"] == "DOMAIN_CONTAINS_REGION"
    assert pdbe_map["residue_correspondences"][0]["pdb_insertion_code"] == "A"
    assert "E83A" in pdbe_map["mapping_uncertainty"]

    _, cdd_obs = normalize_cdsearch_row(
        {
            "uniprot_accession": "Q31PW6",
            "cdd_accession": "cd12345",
            "short_name": "TLN_like",
            "hit_type": "specific",
            "start": 6,
            "end": 146,
            "e_value": 1.2e-20,
        },
        sequence_identity=seq,
    )
    _, cath_obs = normalize_cath_row(
        {
            "uniprot_accession": "Q31PW6",
            "cath_superfamily_id": "3.40.50.10140",
            "funfam_id": "12",
            "funfam_name": "TIR-like NADase",
            "member_start": 6,
            "member_end": 146,
            "confidence": 0.94,
        },
        sequence_identity=seq,
    )
    _, ncbifam_obs = normalize_ncbifam_row(
        {
            "uniprot_accession": "Q31PW6",
            "hmm_accession": "NF012345",
            "hmm_name": "TIR_NADase",
            "product_name": "TIR-like NAD+ hydrolase",
            "seq_start": 6,
            "seq_end": 146,
            "e_value": 3.5e-18,
        },
        sequence_identity=seq,
    )
    qgo_reg, qgo_obs = normalize_quickgo_row(
        {
            "uniprot_accession": "Q31PW6",
            "go_id": "GO:0003953",
            "go_name": "NAD+ nucleosidase activity",
            "go_evidence": "IDA",
            "qualifier": "NOT|enables",
            "reference": "PMID:42146377",
            "assigned_by": "UniProt",
        },
        sequence_identity=seq,
    )
    assert qgo_reg["coordinate_status"] == "WHOLE_PROTEIN_UNLOCALIZED"
    assert qgo_obs["evidence_kind"] == "EXPERIMENTAL"
    assert qgo_obs["polarity"] == "NEGATIVE"

    rhea_obs = normalize_rhea_row(
        {
            "uniprot_accession": "Q31PW6",
            "rhea_id": "Rhea:19189",
            "equation": "NAD+ + H2O = ADP-D-ribose + nicotinamide + H+",
        },
        sequence_identity=seq,
        region=pfam_reg,
    )
    assert rhea_obs["source_kind"] == "RHEA"

    # Homogeneous E_VALUE scores can be compared
    combined = combine_scores_strictly([cdd_obs, ncbifam_obs])
    assert combined["metric"] == "E_VALUE"
    assert combined["best_value"] == 1.2e-20

    # Heterogeneous metrics (E_VALUE vs CATH_CONFIDENCE) cannot be combined as interchangeable probabilities
    with pytest.raises(ValueError, match="not interchangeable probabilities"):
        combine_scores_strictly([cdd_obs, cath_obs])


def test_epistemic_vs_causal_edge_boundary_and_forged_scope_rejection() -> None:
    """Verify that predictions/overlaps cannot use CAUSAL_BIOLOGICAL_LINK and forged FAMILY_WIDE claims fail."""
    # Epistemic predicate with CAUSAL_BIOLOGICAL_LINK rejected
    with pytest.raises(ValueError, match="must not be typed as biological causation"):
        build_reasoning_edge(
            edge_id="bad_causal_overlap",
            subject="reg_a",
            predicate="maps_to_region",
            object_id="reg_b",
            edge_category="CAUSAL_BIOLOGICAL_LINK",
            support="OBSERVED",
            evidence_kind="EXPERIMENTAL",
            rationale="Coordinate overlap is not biological causation.",
        )

    # Biological causal edge with OBSERVED support and COMPUTATIONAL evidence rejected
    with pytest.raises(ValueError, match="observed biological causation requires EXPERIMENTAL evidence"):
        build_reasoning_edge(
            edge_id="bad_comp_observed_causal",
            subject="reg_a",
            predicate="enables_biological_activity",
            object_id="claim_b",
            edge_category="CAUSAL_BIOLOGICAL_LINK",
            support="OBSERVED",
            evidence_kind="COMPUTATIONAL",
            rationale="Computational prediction cannot be OBSERVED biological causation.",
        )

    graphs = build_representative_reasoning_graphs()
    forged = copy.deepcopy(graphs[0])
    forged["synthesized_claims"][0]["claimed_scope"] = "FAMILY_WIDE"
    with pytest.raises(ValueError, match="claims FAMILY_WIDE scope while scope_transfer_blocks are present"):
        validate_region_reasoning_graphs("PF13271", [forged])


def test_representative_end_to_end_graphs_queries_trace_views_and_cli(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Verify the 3 representative end-to-end graphs, region queries, evidence tracing, views, and CLI."""
    graphs = build_representative_reasoning_graphs()
    assert len(graphs) == 3
    g_tep1, g_q31, g_disc = graphs

    # 1. TEP1 (Q99973) demonstrated NADase + NWD1 negative paralogue
    tep1_claims = query_claims_for_region(
        g_tep1, sequence_id="seq_Q99973_v3", start=901, end=1015, include_overlapping=False
    )
    assert len(tep1_claims) == 1
    assert tep1_claims[0]["claim_id"] == "claim_tep1_pf13271_nadase"
    assert tep1_claims[0]["synthesis_status"] == "EXPERIMENTALLY_DEMONSTRATED"
    assert tep1_claims[0]["claimed_scope"] == "TESTED_CONSTRUCT"
    assert tep1_claims[0]["coordinate_relation"] == "EXACT_MATCH"

    trace = trace_claim_evidence(g_tep1, "claim_tep1_pf13271_nadase")
    # 3 raw positive observations (WT HPLC, mirrored WT curated, and E1008A mutant) -> 2 independent groups!
    assert trace["raw_supporting_observation_count"] == 3
    assert trace["independent_supporting_experiment_count"] == 2
    assert len(trace["biological_causal_edges"]) == 1
    assert len(trace["epistemic_edges"]) >= 3

    nwd1_claims = query_claims_for_region(g_tep1, sequence_id="seq_Q5H9R7_v2")
    assert len(nwd1_claims) == 1
    assert nwd1_claims[0]["synthesis_status"] == "NEGATIVE_EVIDENCE_ONLY"

    # 2. Q31PW6 computational hypothesis + COG5635 architectural co-occurrence
    q31_trace = trace_claim_evidence(g_q31, "claim_q31pw6_pf13271_nadase_hypothesis")
    assert q31_trace["claim"]["synthesis_status"] == "COMPUTATIONAL_HYPOTHESIS"
    assert q31_trace["raw_supporting_observation_count"] == 3
    assert q31_trace["independent_supporting_experiment_count"] == 2
    assert q31_trace["biological_causal_edges"] == []

    # 3. Discontinuous domain gap query vs segment query & unknown vs negative
    gap_hits = query_claims_for_region(
        g_disc, sequence_id="seq_P0A9Q7_v1", start=130, end=190
    )
    assert gap_hits == []  # Querying the inter-segment gap 121..209 does NOT match [50..120, 210..290]!

    seg_hits = query_claims_for_region(
        g_disc, sequence_id="seq_P0A9Q7_v1", start=60, end=100
    )
    assert len(seg_hits) == 1
    assert seg_hits[0]["synthesis_status"] == "CONFLICTING_UNRESOLVED"
    assert seg_hits[0]["coordinate_relation"] == "TARGET_CONTAINS_QUERY"

    unann_hits = query_claims_for_region(g_disc, sequence_id="seq_O34567_v1")
    assert len(unann_hits) == 1
    assert unann_hits[0]["synthesis_status"] == "INSUFFICIENT_EVIDENCE"
    assert unann_hits[0]["function_aspect"] == "UNKNOWN_FUNCTION"

    # Markdown and JSON inspectable views
    md_view = render_inspectable_view(g_tep1, fmt="markdown")
    assert "## 1. Reference Sequences & Checksums" in md_view
    assert "## 6. Typed Reasoning Edges (Epistemic vs. Biological Causation)" in md_view
    json_view = json.loads(render_inspectable_view(g_tep1, fmt="json"))
    assert json_view["graph_id"] == "pf13271_tep1_nadase_demonstrated"

    # CLI execution
    assert main(["--demo", "--graph-id", "pf13271_tep1_nadase_demonstrated"]) == 0
    out_md = capsys.readouterr().out
    assert "pf13271_tep1_nadase_demonstrated" in out_md

    assert main(["--demo", "--trace-claim", "claim_tep1_pf13271_nadase"]) == 0
    out_trace = json.loads(capsys.readouterr().out)
    assert out_trace["independent_supporting_experiment_count"] == 2

    assert main(["--demo", "--query-sequence", "seq_P0A9Q7_v1", "--start", "130", "--end", "190"]) == 0
    out_query = json.loads(capsys.readouterr().out)
    assert out_query == []

    # Validate integration with records.validate_record on FamilyCuration
    curation_doc = {
        "pfam_id": "PF13271",
        "curation_status": "IN_PROGRESS",
        "sequence_reasoning_graphs": [g_tep1, g_q31],
    }
    validate_record(curation_doc, REPO_ROOT, target="FamilyCuration")

    bad_curation = copy.deepcopy(curation_doc)
    bad_curation["assertions"] = [{
        "assertion_id": "a1",
        "statement": "Test statement",
        "evidence_kind": "EXPERIMENTAL",
        "scope": "Test scope",
        "region_id": "nonexistent_region",
        "evidence": [{
            "reference": "PMID:42146377",
            "source_url": "https://www.biorxiv.org/content/10.64898/2026.05.01.722283v1",
            "snippet": "TIR-like NADases",
            "explanation": "Test",
            "cache_path": "evidence/PF13271/osinski_2026_biorxiv.txt",
            "cache_sha256": "a" * 64,
        }],
    }]
    with pytest.raises(RecordError, match="references unknown region_id 'nonexistent_region'"):
        validate_record(bad_curation, REPO_ROOT, target="FamilyCuration")


def test_adversarial_review_regressions() -> None:
    """Verify fixes for all 7 independent adversarial review findings."""
    # Finding 1: ISOFORM_TO_CANONICAL projects via residue_correspondences (never raw intersection),
    # and cross-accession non-alignment mappings return UNRESOLVED_MAPPING.
    seq_iso2 = build_sequence_identity(
        "P12345",
        sequence_length=180,
        sequence_sha256=hashlib.sha256(b"P12345_ISO2_SPLICE_SHIFTED").hexdigest(),
        isoform="P12345-2",
        sequence_version=1,
        sequence_id="seq_P12345_iso2",
    )
    seq_canon = build_sequence_identity(
        "P12345",
        sequence_length=200,
        sequence_sha256=hashlib.sha256(b"P12345_CANON_200").hexdigest(),
        isoform="P12345-1",
        sequence_version=1,
        sequence_id="seq_P12345_canon",
    )
    reg_iso2_site = build_sequence_region(
        region_id="reg_iso2_site50",
        sequence_identity=seq_iso2,
        label="Isoform-2 residue 50 (shifted to canonical residue 70, outside domain 40..60)",
        region_kind="MUTATION_SITE",
        coordinate_status="EXACT",
        intervals=[{"start": 50, "end": 50, "residue_identity": "E"}],
        source_coordinate_system="UNIPROT_ISOFORM",
        conversion_provenance="Isoform P12345-2 lacks exon 2 (residues 21..40 of canonical).",
    )
    reg_canon_dom = build_sequence_region(
        region_id="reg_canon_dom_40_60",
        sequence_identity=seq_canon,
        label="Canonical domain 40..60",
        region_kind="DOMAIN_HIT",
        coordinate_status="EXACT",
        intervals=[{"start": 40, "end": 60}],
        pfam_id="PF13271",
    )
    iso_map = classify_region_mapping(
        mapping_id="map_iso2_50_to_canon_70",
        source_region=reg_iso2_site,
        target_region=reg_canon_dom,
        source_sequence=seq_iso2,
        target_sequence=seq_canon,
        mapping_kind="ISOFORM_TO_CANONICAL",
        residue_correspondences=[
            {
                "source_position": 50,
                "source_residue": "E",
                "target_position": 70,
                "target_residue": "E",
            }
        ],
    )
    # Raw position 50 is inside 40..60, but projected canonical position 70 is outside 40..60!
    assert iso_map["equivalence_status"] == "DISJOINT_OUTSIDE_REGION"
    assert iso_map["overlap_residues"] == 0

    seq_other = build_sequence_identity(
        "Q99973",
        sequence_length=200,
        sequence_sha256=hashlib.sha256(b"Q99973_OTHER_200").hexdigest(),
        sequence_version=1,
        sequence_id="seq_Q99973_other",
    )
    reg_other = build_sequence_region(
        region_id="reg_other_40_60",
        sequence_identity=seq_other,
        label="Different protein region 40..60",
        region_kind="EXPERIMENTAL_CONSTRUCT",
        coordinate_status="EXACT",
        intervals=[{"start": 40, "end": 60}],
    )
    cross_acc_map = classify_region_mapping(
        mapping_id="map_cross_acc_non_align",
        source_region=reg_other,
        target_region=reg_canon_dom,
        source_sequence=seq_other,
        target_sequence=seq_canon,
        mapping_kind="CONSTRUCT_TO_REFERENCE",
    )
    assert cross_acc_map["equivalence_status"] == "UNRESOLVED_MAPPING"

    # Finding 2: Per-observation mutation localization — a COMPUTATIONAL or NEGATIVE
    # observation with RESIDUE_INSIDE_REGION must NOT localize an unlocalized full-length WT assay,
    # and unmapped mutation_region_ids must block localization.
    reg_full = build_sequence_region(
        region_id="reg_canon_full",
        sequence_identity=seq_canon,
        label="Full-length canonical protein 1..200",
        region_kind="FULL_LENGTH_PROTEIN",
        coordinate_status="WHOLE_PROTEIN_UNLOCALIZED",
        intervals=[{"start": 1, "end": 200}],
    )
    reg_canon_site50 = build_sequence_region(
        region_id="reg_canon_site50",
        sequence_identity=seq_canon,
        label="Conserved site 50 inside 40..60",
        region_kind="CATALYTIC_SITE",
        coordinate_status="EXACT",
        intervals=[{"start": 50, "end": 50, "residue_identity": "E"}],
    )
    map_full_to_dom = classify_region_mapping(
        mapping_id="map_full_to_dom",
        source_region=reg_full,
        target_region=reg_canon_dom,
        source_sequence=seq_canon,
        target_sequence=seq_canon,
        mapping_kind="CONSTRUCT_TO_REFERENCE",
    )
    map_site50_to_dom = classify_region_mapping(
        mapping_id="map_site50_to_dom",
        source_region=reg_canon_site50,
        target_region=reg_canon_dom,
        source_sequence=seq_canon,
        target_sequence=seq_canon,
        mapping_kind="MUTATION_TO_DOMAIN",
    )
    obs_wt_unlocalized = build_region_observation(
        observation_id="obs_wt_full_unlocalized",
        region=reg_full,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Whole-protein WT assay without domain truncation or mutagenesis",
        observed_effect="Full-length protein active.",
        interpretation="Activity somewhere in 1..200.",
        polarity="POSITIVE",
        primary_experiment_key="PMID:11111111/P12345_1-200/WT",
    )
    obs_comp_site = build_region_observation(
        observation_id="obs_comp_site50",
        region=reg_canon_dom,
        evidence_kind="COMPUTATIONAL",
        source_kind="CURATED_ANNOTATION",
        method="Predicted active site at residue 50",
        mutation_region_ids=["reg_canon_site50"],
        observed_effect="Residue 50 is conserved.",
        interpretation="Predicted catalytic site.",
        polarity="POSITIVE",
        primary_experiment_key="ALIGN:P12345/site50",
    )
    leak_groups = deduplicate_observations([obs_wt_unlocalized, obs_comp_site])
    leak_claim = synthesize_region_claim(
        claim_id="claim_no_mutation_leakage",
        label="Unlocalized WT assay + computational site must not be EXPERIMENTALLY_DEMONSTRATED",
        function_aspect="CATALYTIC_ACTIVITY",
        target_region=reg_canon_dom,
        regions_by_id={
            "reg_canon_dom_40_60": reg_canon_dom,
            "reg_canon_full": reg_full,
            "reg_canon_site50": reg_canon_site50,
        },
        observations=[obs_wt_unlocalized, obs_comp_site],
        evidence_groups=leak_groups,
        coordinate_mappings=[map_full_to_dom, map_site50_to_dom],
    )
    assert leak_claim["synthesis_status"] != "EXPERIMENTALLY_DEMONSTRATED"

    # Finding 3: validate_region_reasoning_graphs rejects forged CoordinateMapping.equivalence_status,
    # duplicate EvidenceGroup keys, and unlocalized EXPERIMENTALLY_DEMONSTRATED claims.
    graphs = build_representative_reasoning_graphs()
    bad_map_graph = copy.deepcopy(graphs[2])
    bad_map_graph["coordinate_mappings"][0]["equivalence_status"] = "RESIDUE_INSIDE_REGION"
    with pytest.raises(ValueError, match="declared equivalence_status 'RESIDUE_INSIDE_REGION' != computed 'DISJOINT_OUTSIDE_REGION'"):
        validate_region_reasoning_graphs("PF00001", [bad_map_graph])

    bad_grp_graph = copy.deepcopy(graphs[0])
    dup_grp = copy.deepcopy(bad_grp_graph["evidence_groups"][0])
    dup_grp["group_id"] = "grp_dup_inflated"
    bad_grp_graph["evidence_groups"].append(dup_grp)
    with pytest.raises(ValueError, match="duplicates group key"):
        validate_region_reasoning_graphs("PF13271", [bad_grp_graph])

    bad_unloc_claim_graph = copy.deepcopy(graphs[0])
    bad_unloc_claim_graph["synthesized_claims"][0]["mapping_ids"] = []
    with pytest.raises(
        ValueError,
        match="EXPERIMENTALLY_DEMONSTRATED without any POSITIVE EXPERIMENTAL observation localized",
    ):
        validate_region_reasoning_graphs("PF13271", [bad_unloc_claim_graph])

    # Finding 4: deduplicate_observations checks all entries in derived_from_observation_ids.
    obs_root_a = build_region_observation(
        observation_id="obs_root_a",
        region=reg_canon_dom,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Assay A",
        observed_effect="Effect A",
        interpretation="Interp A",
        polarity="POSITIVE",
        primary_experiment_key="PMID:11111111/A",
    )
    obs_root_b = build_region_observation(
        observation_id="obs_root_b",
        region=reg_canon_dom,
        evidence_kind="EXPERIMENTAL",
        source_kind="LITERATURE_ASSAY",
        method="Assay B",
        observed_effect="Effect B",
        interpretation="Interp B",
        polarity="POSITIVE",
        primary_experiment_key="PMID:22222222/B",
    )
    obs_multi_parent_conflict = build_region_observation(
        observation_id="obs_multi_conflict",
        region=reg_canon_dom,
        evidence_kind="EXPERIMENTAL",
        source_kind="QUICKGO",
        method="Mirrored record citing two different experiments",
        observed_effect="Effect",
        interpretation="Interp",
        polarity="POSITIVE",
        primary_experiment_key="PMID:11111111/A",
        derived_from_observation_ids=["obs_root_a", "obs_root_b"],
    )
    with pytest.raises(ValueError, match="conflicting primary_experiment_key values"):
        deduplicate_observations([obs_root_a, obs_root_b, obs_multi_parent_conflict])

    # Finding 5 & 7: Adapter accession mismatch check and single-bound query_claims_for_region error.
    with pytest.raises(ValueError, match="!= sequence_identity"):
        normalize_pdbe_kb_row(
            {
                "uniprot_accession": "Q99973",
                "pdb_id": "8XYZ",
                "chain_id": "A",
                "uniprot_start": 40,
                "uniprot_end": 60,
                "pdb_residues": [1, 2, 3],
            },
            sequence_identity=seq_canon,
        )
    with pytest.raises(
        SequenceReasoningError,
        match="Both start and end must be provided together when querying by coordinate interval",
    ):
        query_claims_for_region(graphs[0], sequence_id="seq_Q99973_v3", start=901)

