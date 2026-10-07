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
| discussions | Discussion | False |
| datasets | Dataset | False |
| cross_corpus_links | CrossCorpusLink | False |

## FamilyCuration

Human-owned overlay. Imported identity and counters cannot be overridden.

| Field | Type | Required |
| --- | --- | --- |
| pfam_id | string | True |
| curation_status | CurationStatus | True |
| review_id | string | False |
| curation_history | string | False |
| assertions | FunctionalAssertion | False |
| discussions | Discussion | False |
| datasets | Dataset | False |
| cross_corpus_links | CrossCorpusLink | False |

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
