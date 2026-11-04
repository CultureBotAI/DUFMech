# DUFMech Schema

Generated from `src/dufmech/schema/dufmech.yaml`.

## FamilyRecord

A source-derived family projection; SEEDED is not scientific review.

| Field | Type | Required |
| --- | --- | --- |
| id | string | True |
| pfam_id | string | True |
| name | string | True |
| short_name | string | True |
| interpro_id | string | False |
| seed_status | SeedStatus | True |
| characterization_status | CharacterizationStatus | True |
| curation_status | CurationStatus | True |
| review_id | string | False |
| curation_history | string | False |
| curation_events | CurationEvent | False |
| description | string | False |
| source_url | uri | True |
| counters | FamilyCounters | False |
| provenance | SnapshotProvenance | True |
| score_provenance | SnapshotProvenance | False |
| assertions | FunctionalAssertion | False |
| causal_graphs | CausalGraph | False |
| discussions | Discussion | False |
| datasets | Dataset | False |
| cross_corpus_links | CrossCorpusLink | False |
| sequence_reasoning_graphs | RegionReasoningGraph | False |

## FamilyCuration

Human-owned overlay. Imported identity and counters cannot be overridden.

| Field | Type | Required |
| --- | --- | --- |
| pfam_id | string | True |
| curation_status | CurationStatus | True |
| review_id | string | False |
| curation_history | string | False |
| assertions | FunctionalAssertion | False |
| causal_graphs | CausalGraph | False |
| discussions | Discussion | False |
| datasets | Dataset | False |
| cross_corpus_links | CrossCorpusLink | False |
| sequence_reasoning_graphs | RegionReasoningGraph | False |

## CurationEvent

Generated record-level view of a canonical sidecar event; the referenced history record is authoritative.

| Field | Type | Required |
| --- | --- | --- |
| timestamp | string | True |
| curator | string | True |
| action | string | True |
| outcome | string | True |
| summary | string | True |
| history_record | string | True |
| event_index | integer | True |
| llm_assisted | boolean | True |

## FamilyCounters



| Field | Type | Required |
| --- | --- | --- |
| proteins | integer | False |
| matches | integer | False |
| proteomes | integer | False |
| taxa | integer | False |
| structures | integer | False |
| alphafold_models | integer | False |
| domain_architectures | integer | False |

## SnapshotProvenance



| Field | Type | Required |
| --- | --- | --- |
| snapshot_id | string | True |
| path | string | True |
| sha256 | string | True |
| generated_at | string | True |
| source_url | uri | False |

## FunctionalAssertion

Scoped experimental or computational claim, not implied by a DUF name.

| Field | Type | Required |
| --- | --- | --- |
| assertion_id | string | True |
| statement | string | True |
| evidence_kind | EvidenceKind | True |
| scope | string | True |
| sequence_id | string | False |
| region_id | string | False |
| synthesized_claim_id | string | False |
| evidence | ClaimEvidence | True |

## CausalGraph

A scoped directed mechanism or phenotype graph, not family-wide functional proof.

| Field | Type | Required |
| --- | --- | --- |
| graph_id | string | True |
| title | string | True |
| scope | string | True |
| context | string | True |
| family_mapping | string | True |
| scope_status | CausalScope | True |
| taxon | string | False |
| limitations | string | True |
| feedback_explanation | string | False |
| nodes | CausalNode | True |
| edges | CausalEdge | True |

## CausalNode



| Field | Type | Required |
| --- | --- | --- |
| node_id | string | True |
| label | string | True |
| node_type | CausalNodeType | True |
| grounding | string | False |
| sequence_id | string | False |
| region_id | string | False |

## CausalEdge

Evidence for a directed relation, rather than citations only establishing the endpoints.

| Field | Type | Required |
| --- | --- | --- |
| edge_id | string | True |
| subject | string | True |
| predicate | CausalPredicate | True |
| object | string | True |
| mechanism | string | True |
| directness | CausalDirectness | True |
| support | CausalSupport | True |
| evidence_kind | EvidenceKind | True |
| evidence | ClaimEvidence | True |

## ClaimEvidence

A primary-source quotation retained locally for an independently checkable claim.

| Field | Type | Required |
| --- | --- | --- |
| reference | string | True |
| source_url | uri | True |
| snippet | string | True |
| explanation | string | True |
| cache_path | string | True |
| cache_sha256 | string | True |

## RegionReasoningGraph

Sequence-coordinate-aware reasoning graph connecting reference sequences, explicit 1-based inclusive regions, coordinate mappings, deduplicated observations, and evidence-graded functional claims while separating epistemic evidence links from biological causation.

| Field | Type | Required |
| --- | --- | --- |
| graph_id | string | True |
| pfam_id | string | True |
| title | string | True |
| description | string | False |
| sequences | SequenceIdentity | True |
| regions | SequenceRegion | True |
| coordinate_mappings | CoordinateMapping | False |
| observations | RegionObservation | True |
| evidence_groups | EvidenceGroup | False |
| synthesized_claims | SynthesizedClaim | True |
| reasoning_edges | ReasoningEdge | True |
| causal_graph_refs | string | False |

## SequenceIdentity

Identified reference protein sequence with explicit version or SHA-256 digest and isoform context for coordinate validation.

| Field | Type | Required |
| --- | --- | --- |
| sequence_id | string | True |
| uniprot_accession | string | True |
| isoform | string | False |
| sequence_version | integer | False |
| sequence_length | integer | True |
| sequence_sha256 | string | True |
| sequence_md5 | string | False |
| taxon_id | string | False |
| organism | string | False |
| uniprot_release | string | False |
| source_url | uri | False |

## SequenceInterval

Canonical 1-based inclusive interval [start, end] on an identified reference sequence.

| Field | Type | Required |
| --- | --- | --- |
| start | integer | True |
| end | integer | True |
| start_uncertain | boolean | False |
| end_uncertain | boolean | False |
| residue_identity | string | False |

## SequenceRegion

An explicit contiguous or discontinuous region, site, construct, or unlocalized whole-protein span on an identified sequence.

| Field | Type | Required |
| --- | --- | --- |
| region_id | string | True |
| sequence_id | string | True |
| label | string | True |
| region_kind | RegionKind | True |
| coordinate_status | CoordinateStatus | True |
| intervals | SequenceInterval | False |
| source_coordinate_system | CoordinateSystem | True |
| source_coordinates_text | string | False |
| conversion_provenance | string | False |
| pfam_id | string | False |
| interpro_id | string | False |

## ResidueCorrespondence

Explicit residue-level correspondence between two coordinate systems or homologous sequences.

| Field | Type | Required |
| --- | --- | --- |
| source_position | integer | True |
| source_residue | string | False |
| target_position | integer | True |
| target_residue | string | False |
| pdb_insertion_code | string | False |
| mutation_substitution | string | False |
| note | string | False |

## CoordinateMapping

Explicit mapping between two regions (e.g., construct to domain, structure to UniProt, or homolog alignment) retaining coverage, gaps, and uncertainty.

| Field | Type | Required |
| --- | --- | --- |
| mapping_id | string | True |
| source_region_id | string | True |
| target_region_id | string | True |
| mapping_kind | CoordinateMappingKind | True |
| equivalence_status | MappingEquivalenceStatus | True |
| overlap_residues | integer | False |
| source_coverage | float | False |
| target_coverage | float | False |
| alignment_gaps | integer | False |
| residue_correspondences | ResidueCorrespondence | False |
| mapping_uncertainty | string | False |
| provenance_note | string | True |

## RegionObservation

Standardized experimental observation, curated annotation, or computational prediction anchored to a sequence region, separating observation from interpretation.

| Field | Type | Required |
| --- | --- | --- |
| observation_id | string | True |
| region_id | string | True |
| sequence_id | string | True |
| evidence_kind | EvidenceKind | True |
| source_kind | ObservationSourceKind | True |
| method | string | True |
| assay_conditions | string | False |
| tested_construct_region_id | string | False |
| mutation_region_ids | string | False |
| observed_effect | string | True |
| interpretation | string | True |
| polarity | ObservationPolarity | True |
| raw_score | float | False |
| score_metric | ScoreMetricKind | False |
| primary_experiment_key | string | True |
| derived_from_observation_ids | string | False |
| limitations | string | False |
| evidence | ClaimEvidence | False |

## EvidenceGroup

Deduplicated group of compatible observations sharing a primary experiment or prediction source so mirrored records are not counted as independent confirmation.

| Field | Type | Required |
| --- | --- | --- |
| group_id | string | True |
| primary_experiment_key | string | True |
| evidence_kind | EvidenceKind | True |
| polarity | ObservationPolarity | True |
| observation_ids | string | True |
| deduplication_rationale | string | True |

## SynthesizedClaim

Evidence-graded functional claim or aspect of function at supported specificity and sequence scope, retaining supporting and contradicting evidence groups.

| Field | Type | Required |
| --- | --- | --- |
| claim_id | string | True |
| label | string | True |
| function_aspect | FunctionAspect | True |
| ontology_term_id | string | False |
| ontology_term_label | string | False |
| target_region_id | string | True |
| claimed_scope | ClaimScope | True |
| synthesis_status | SynthesisStatus | True |
| supporting_evidence_groups | string | False |
| contradicting_evidence_groups | string | False |
| supporting_observation_ids | string | False |
| contradicting_observation_ids | string | False |
| mapping_ids | string | False |
| scope_rationale | string | True |
| scope_transfer_blocks | string | False |
| synthesis_explanation | string | True |
| discriminating_experiments | string | False |

## ReasoningEdge

Typed edge in a RegionReasoningGraph explicitly distinguishing coordinate mappings, evidence support/contradiction, and homology inferences from biological causation.

| Field | Type | Required |
| --- | --- | --- |
| edge_id | string | True |
| subject | string | True |
| predicate | ReasoningPredicate | True |
| object | string | True |
| edge_category | ReasoningEdgeCategory | True |
| support | CausalSupport | True |
| evidence_kind | EvidenceKind | True |
| rationale | string | True |
