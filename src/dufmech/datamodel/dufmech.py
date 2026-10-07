# id: https://w3id.org/dufmech/schema
# description: Frozen family identities with separately curated, evidence-backed assertions.
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

metamodel_version = "1.11.0"
version = None

# Namespaces
INTERPRO = CurieNamespace('InterPro', 'https://www.ebi.ac.uk/interpro/entry/InterPro/')
PFAM = CurieNamespace('Pfam', 'https://www.ebi.ac.uk/interpro/entry/pfam/')
DUFMECH = CurieNamespace('dufmech', 'https://w3id.org/dufmech/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MECH_SHARED = CurieNamespace('mech_shared', 'https://w3id.org/kg-microbe/mech-shared/')
DEFAULT_ = DUFMECH


# Types

# Class references
class FamilyRecordId(extended_str):
    pass


@dataclass(repr=False)
class FamilyRecord(YAMLRoot):
    """
    A source-derived family projection; SEEDED is not scientific review.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["FamilyRecord"]
    class_class_curie: ClassVar[str] = "dufmech:FamilyRecord"
    class_name: ClassVar[str] = "FamilyRecord"
    class_model_uri: ClassVar[URIRef] = DUFMECH.FamilyRecord

    id: Union[str, FamilyRecordId] = None
    pfam_id: str = None
    name: str = None
    short_name: str = None
    seed_status: Union[str, "SeedStatus"] = None
    characterization_status: Union[str, "CharacterizationStatus"] = None
    curation_status: Union[str, "CurationStatus"] = None
    source_url: Union[str, URI] = None
    provenance: Union[dict, "SnapshotProvenance"] = None
    interpro_id: Optional[str] = None
    review_id: Optional[str] = None
    curation_history: Optional[str] = None
    curation_events: Optional[Union[Union[dict, "CurationEvent"], list[Union[dict, "CurationEvent"]]]] = empty_list()
    description: Optional[str] = None
    counters: Optional[Union[dict, "FamilyCounters"]] = None
    score_provenance: Optional[Union[dict, "SnapshotProvenance"]] = None
    assertions: Optional[Union[Union[dict, "FunctionalAssertion"], list[Union[dict, "FunctionalAssertion"]]]] = empty_list()
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    cross_corpus_links: Optional[Union[Union[dict, "CrossCorpusLink"], list[Union[dict, "CrossCorpusLink"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyRecordId):
            self.id = FamilyRecordId(self.id)

        if self._is_empty(self.pfam_id):
            self.MissingRequiredField("pfam_id")
        if not isinstance(self.pfam_id, str):
            self.pfam_id = str(self.pfam_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.short_name):
            self.MissingRequiredField("short_name")
        if not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self._is_empty(self.seed_status):
            self.MissingRequiredField("seed_status")
        if not isinstance(self.seed_status, SeedStatus):
            self.seed_status = SeedStatus(self.seed_status)

        if self._is_empty(self.characterization_status):
            self.MissingRequiredField("characterization_status")
        if not isinstance(self.characterization_status, CharacterizationStatus):
            self.characterization_status = CharacterizationStatus(self.characterization_status)

        if self._is_empty(self.curation_status):
            self.MissingRequiredField("curation_status")
        if not isinstance(self.curation_status, CurationStatus):
            self.curation_status = CurationStatus(self.curation_status)

        if self._is_empty(self.source_url):
            self.MissingRequiredField("source_url")
        if not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        if self._is_empty(self.provenance):
            self.MissingRequiredField("provenance")
        if not isinstance(self.provenance, SnapshotProvenance):
            self.provenance = SnapshotProvenance(**as_dict(self.provenance))

        if self.interpro_id is not None and not isinstance(self.interpro_id, str):
            self.interpro_id = str(self.interpro_id)

        if self.review_id is not None and not isinstance(self.review_id, str):
            self.review_id = str(self.review_id)

        if self.curation_history is not None and not isinstance(self.curation_history, str):
            self.curation_history = str(self.curation_history)

        self._normalize_inlined_as_list(slot_name="curation_events", slot_type=CurationEvent, key_name="timestamp", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.counters is not None and not isinstance(self.counters, FamilyCounters):
            self.counters = FamilyCounters(**as_dict(self.counters))

        if self.score_provenance is not None and not isinstance(self.score_provenance, SnapshotProvenance):
            self.score_provenance = SnapshotProvenance(**as_dict(self.score_provenance))

        self._normalize_inlined_as_list(slot_name="assertions", slot_type=FunctionalAssertion, key_name="assertion_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        self._normalize_inlined_as_list(slot_name="cross_corpus_links", slot_type=CrossCorpusLink, key_name="corpus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyCuration(YAMLRoot):
    """
    Human-owned overlay. Imported identity and counters cannot be overridden.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["FamilyCuration"]
    class_class_curie: ClassVar[str] = "dufmech:FamilyCuration"
    class_name: ClassVar[str] = "FamilyCuration"
    class_model_uri: ClassVar[URIRef] = DUFMECH.FamilyCuration

    pfam_id: str = None
    curation_status: Union[str, "CurationStatus"] = None
    review_id: Optional[str] = None
    curation_history: Optional[str] = None
    assertions: Optional[Union[Union[dict, "FunctionalAssertion"], list[Union[dict, "FunctionalAssertion"]]]] = empty_list()
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    cross_corpus_links: Optional[Union[Union[dict, "CrossCorpusLink"], list[Union[dict, "CrossCorpusLink"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pfam_id):
            self.MissingRequiredField("pfam_id")
        if not isinstance(self.pfam_id, str):
            self.pfam_id = str(self.pfam_id)

        if self._is_empty(self.curation_status):
            self.MissingRequiredField("curation_status")
        if not isinstance(self.curation_status, CurationStatus):
            self.curation_status = CurationStatus(self.curation_status)

        if self.review_id is not None and not isinstance(self.review_id, str):
            self.review_id = str(self.review_id)

        if self.curation_history is not None and not isinstance(self.curation_history, str):
            self.curation_history = str(self.curation_history)

        self._normalize_inlined_as_list(slot_name="assertions", slot_type=FunctionalAssertion, key_name="assertion_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        self._normalize_inlined_as_list(slot_name="cross_corpus_links", slot_type=CrossCorpusLink, key_name="corpus", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CurationEvent(YAMLRoot):
    """
    Generated record-level view of a canonical sidecar event; the referenced history record is authoritative.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["CurationEvent"]
    class_class_curie: ClassVar[str] = "dufmech:CurationEvent"
    class_name: ClassVar[str] = "CurationEvent"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CurationEvent

    timestamp: str = None
    curator: str = None
    action: str = None
    outcome: str = None
    summary: str = None
    history_record: str = None
    event_index: int = None
    llm_assisted: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if self._is_empty(self.curator):
            self.MissingRequiredField("curator")
        if not isinstance(self.curator, str):
            self.curator = str(self.curator)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, str):
            self.action = str(self.action)

        if self._is_empty(self.outcome):
            self.MissingRequiredField("outcome")
        if not isinstance(self.outcome, str):
            self.outcome = str(self.outcome)

        if self._is_empty(self.summary):
            self.MissingRequiredField("summary")
        if not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self._is_empty(self.history_record):
            self.MissingRequiredField("history_record")
        if not isinstance(self.history_record, str):
            self.history_record = str(self.history_record)

        if self._is_empty(self.event_index):
            self.MissingRequiredField("event_index")
        if not isinstance(self.event_index, int):
            self.event_index = int(self.event_index)

        if self._is_empty(self.llm_assisted):
            self.MissingRequiredField("llm_assisted")
        if not isinstance(self.llm_assisted, Bool):
            self.llm_assisted = Bool(self.llm_assisted)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyCounters(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["FamilyCounters"]
    class_class_curie: ClassVar[str] = "dufmech:FamilyCounters"
    class_name: ClassVar[str] = "FamilyCounters"
    class_model_uri: ClassVar[URIRef] = DUFMECH.FamilyCounters

    proteins: Optional[int] = None
    matches: Optional[int] = None
    proteomes: Optional[int] = None
    taxa: Optional[int] = None
    structures: Optional[int] = None
    alphafold_models: Optional[int] = None
    domain_architectures: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.proteins is not None and not isinstance(self.proteins, int):
            self.proteins = int(self.proteins)

        if self.matches is not None and not isinstance(self.matches, int):
            self.matches = int(self.matches)

        if self.proteomes is not None and not isinstance(self.proteomes, int):
            self.proteomes = int(self.proteomes)

        if self.taxa is not None and not isinstance(self.taxa, int):
            self.taxa = int(self.taxa)

        if self.structures is not None and not isinstance(self.structures, int):
            self.structures = int(self.structures)

        if self.alphafold_models is not None and not isinstance(self.alphafold_models, int):
            self.alphafold_models = int(self.alphafold_models)

        if self.domain_architectures is not None and not isinstance(self.domain_architectures, int):
            self.domain_architectures = int(self.domain_architectures)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SnapshotProvenance(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["SnapshotProvenance"]
    class_class_curie: ClassVar[str] = "dufmech:SnapshotProvenance"
    class_name: ClassVar[str] = "SnapshotProvenance"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SnapshotProvenance

    snapshot_id: str = None
    path: str = None
    sha256: str = None
    generated_at: str = None
    source_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.snapshot_id):
            self.MissingRequiredField("snapshot_id")
        if not isinstance(self.snapshot_id, str):
            self.snapshot_id = str(self.snapshot_id)

        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, str):
            self.path = str(self.path)

        if self._is_empty(self.sha256):
            self.MissingRequiredField("sha256")
        if not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self._is_empty(self.generated_at):
            self.MissingRequiredField("generated_at")
        if not isinstance(self.generated_at, str):
            self.generated_at = str(self.generated_at)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalAssertion(YAMLRoot):
    """
    Scoped experimental or computational claim, not implied by a DUF name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["FunctionalAssertion"]
    class_class_curie: ClassVar[str] = "dufmech:FunctionalAssertion"
    class_name: ClassVar[str] = "FunctionalAssertion"
    class_model_uri: ClassVar[URIRef] = DUFMECH.FunctionalAssertion

    assertion_id: str = None
    statement: str = None
    evidence_kind: Union[str, "EvidenceKind"] = None
    scope: str = None
    evidence: Union[Union[dict, "ClaimEvidence"], list[Union[dict, "ClaimEvidence"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assertion_id):
            self.MissingRequiredField("assertion_id")
        if not isinstance(self.assertion_id, str):
            self.assertion_id = str(self.assertion_id)

        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self._is_empty(self.evidence_kind):
            self.MissingRequiredField("evidence_kind")
        if not isinstance(self.evidence_kind, EvidenceKind):
            self.evidence_kind = EvidenceKind(self.evidence_kind)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, str):
            self.scope = str(self.scope)

        if self._is_empty(self.evidence):
            self.MissingRequiredField("evidence")
        self._normalize_inlined_as_list(slot_name="evidence", slot_type=ClaimEvidence, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClaimEvidence(YAMLRoot):
    """
    A primary-source quotation retained locally for an independently checkable claim.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["ClaimEvidence"]
    class_class_curie: ClassVar[str] = "dufmech:ClaimEvidence"
    class_name: ClassVar[str] = "ClaimEvidence"
    class_model_uri: ClassVar[URIRef] = DUFMECH.ClaimEvidence

    reference: str = None
    source_url: Union[str, URI] = None
    snippet: str = None
    explanation: str = None
    cache_path: str = None
    cache_sha256: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self._is_empty(self.source_url):
            self.MissingRequiredField("source_url")
        if not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        if self._is_empty(self.snippet):
            self.MissingRequiredField("snippet")
        if not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self._is_empty(self.explanation):
            self.MissingRequiredField("explanation")
        if not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self._is_empty(self.cache_path):
            self.MissingRequiredField("cache_path")
        if not isinstance(self.cache_path, str):
            self.cache_path = str(self.cache_path)

        if self._is_empty(self.cache_sha256):
            self.MissingRequiredField("cache_sha256")
        if not isinstance(self.cache_sha256, str):
            self.cache_sha256 = str(self.cache_sha256)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossCorpusLink(YAMLRoot):
    """
    A directed link from the containing record or sub-object to a record in another Mech corpus. The five field names
    preserve NaturalProductMech's existing link shape. Consumers define allowed relations and evidence requirements;
    this class alone does not verify a target, its version, organism scope, or the scientific basis of the relation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["CrossCorpusLink"]
    class_class_curie: ClassVar[str] = "mech_shared:CrossCorpusLink"
    class_name: ClassVar[str] = "CrossCorpusLink"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CrossCorpusLink

    corpus: str = None
    identifier: str = None
    relation: str = None
    basis: str = None
    source_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.corpus):
            self.MissingRequiredField("corpus")
        if not isinstance(self.corpus, str):
            self.corpus = str(self.corpus)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, str):
            self.relation = str(self.relation)

        if self._is_empty(self.basis):
            self.MissingRequiredField("basis")
        if not isinstance(self.basis, str):
            self.basis = str(self.basis)

        if self.source_version is not None and not isinstance(self.source_version, str):
            self.source_version = str(self.source_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingReference(YAMLRoot):
    """
    A lightweight literature/database citation supporting a Discussion or Dataset. Self-contained (so this module has
    no dependency on each repo's EvidenceItem); carries a verbatim `snippet` so the same anti-hallucination
    snippet-vs-cached-abstract check the Mechs already run can validate it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["SupportingReference"]
    class_class_curie: ClassVar[str] = "mech_shared:SupportingReference"
    class_name: ClassVar[str] = "SupportingReference"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SupportingReference

    reference: str = None
    reference_title: Optional[str] = None
    supports: Optional[Union[str, "SupportLevelEnum"]] = None
    evidence_source: Optional[str] = None
    snippet: Optional[str] = None
    explanation: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        if self.reference_title is not None and not isinstance(self.reference_title, str):
            self.reference_title = str(self.reference_title)

        if self.supports is not None and not isinstance(self.supports, SupportLevelEnum):
            self.supports = SupportLevelEnum(self.supports)

        if self.evidence_source is not None and not isinstance(self.evidence_source, str):
            self.evidence_source = str(self.evidence_source)

        if self.snippet is not None and not isinstance(self.snippet, str):
            self.snippet = str(self.snippet)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Discussion(YAMLRoot):
    """
    A thread-like record of an open question, controversy, curation todo, emerging hypothesis, knowledge gap, or
    interpretation debate attached to a record or one of its sub-objects. Captures the discourse / knowledge-gap layer
    of curation. External thread links (GitHub issues, forum posts) are cited via the `evidence` block, not a separate
    slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["Discussion"]
    class_class_curie: ClassVar[str] = "mech_shared:Discussion"
    class_name: ClassVar[str] = "Discussion"
    class_model_uri: ClassVar[URIRef] = DUFMECH.Discussion

    discussion_id: str = None
    prompt: str = None
    kind: Optional[Union[str, "DiscussionKindEnum"]] = None
    status: Optional[Union[str, "DiscussionStatusEnum"]] = None
    attaches_to: Optional[Union[str, list[str]]] = empty_list()
    rationale: Optional[str] = None
    proposed_experiments: Optional[Union[Union[dict, "ProposedExperiment"], list[Union[dict, "ProposedExperiment"]]]] = empty_list()
    evidence: Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]] = empty_list()
    posed_by: Optional[str] = None
    posed_date: Optional[Union[str, XSDDate]] = None
    resolved_date: Optional[Union[str, XSDDate]] = None
    resolution_note: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.discussion_id):
            self.MissingRequiredField("discussion_id")
        if not isinstance(self.discussion_id, str):
            self.discussion_id = str(self.discussion_id)

        if self._is_empty(self.prompt):
            self.MissingRequiredField("prompt")
        if not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.kind is not None and not isinstance(self.kind, DiscussionKindEnum):
            self.kind = DiscussionKindEnum(self.kind)

        if self.status is not None and not isinstance(self.status, DiscussionStatusEnum):
            self.status = DiscussionStatusEnum(self.status)

        if not isinstance(self.attaches_to, list):
            self.attaches_to = [self.attaches_to] if self.attaches_to is not None else []
        self.attaches_to = [v if isinstance(v, str) else str(v) for v in self.attaches_to]

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        if not isinstance(self.proposed_experiments, list):
            self.proposed_experiments = [self.proposed_experiments] if self.proposed_experiments is not None else []
        self.proposed_experiments = [v if isinstance(v, ProposedExperiment) else ProposedExperiment(**as_dict(v)) for v in self.proposed_experiments]

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=SupportingReference, key_name="reference", keyed=False)

        if self.posed_by is not None and not isinstance(self.posed_by, str):
            self.posed_by = str(self.posed_by)

        if self.posed_date is not None and not isinstance(self.posed_date, XSDDate):
            self.posed_date = XSDDate(self.posed_date)

        if self.resolved_date is not None and not isinstance(self.resolved_date, XSDDate):
            self.resolved_date = XSDDate(self.resolved_date)

        if self.resolution_note is not None and not isinstance(self.resolution_note, str):
            self.resolution_note = str(self.resolution_note)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProposedExperiment(YAMLRoot):
    """
    A lightweight, domain-neutral sketch of an experiment or analysis that could resolve a knowledge gap. Records the
    idea and how its outcome would decide the gap; intentionally simpler than a full study design.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["ProposedExperiment"]
    class_class_curie: ClassVar[str] = "mech_shared:ProposedExperiment"
    class_name: ClassVar[str] = "ProposedExperiment"
    class_model_uri: ClassVar[URIRef] = DUFMECH.ProposedExperiment

    experiment_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    approach: Optional[str] = None
    model_systems: Optional[Union[str, list[str]]] = empty_list()
    perturbations: Optional[Union[str, list[str]]] = empty_list()
    readouts: Optional[Union[str, list[str]]] = empty_list()
    decision_criterion: Optional[str] = None
    would_support: Optional[str] = None
    would_refute: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.experiment_id is not None and not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.approach is not None and not isinstance(self.approach, str):
            self.approach = str(self.approach)

        if not isinstance(self.model_systems, list):
            self.model_systems = [self.model_systems] if self.model_systems is not None else []
        self.model_systems = [v if isinstance(v, str) else str(v) for v in self.model_systems]

        if not isinstance(self.perturbations, list):
            self.perturbations = [self.perturbations] if self.perturbations is not None else []
        self.perturbations = [v if isinstance(v, str) else str(v) for v in self.perturbations]

        if not isinstance(self.readouts, list):
            self.readouts = [self.readouts] if self.readouts is not None else []
        self.readouts = [v if isinstance(v, str) else str(v) for v in self.readouts]

        if self.decision_criterion is not None and not isinstance(self.decision_criterion, str):
            self.decision_criterion = str(self.decision_criterion)

        if self.would_support is not None and not isinstance(self.would_support, str):
            self.would_support = str(self.would_support)

        if self.would_refute is not None and not isinstance(self.would_refute, str):
            self.would_refute = str(self.would_refute)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A reference to a publicly available dataset (omics, sequence, phenotype) relevant to this record. A lightweight
    repository-accession reference, not a full Datasheets-for-Datasets / DCAT description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MECH_SHARED["Dataset"]
    class_class_curie: ClassVar[str] = "mech_shared:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DUFMECH.Dataset

    accession: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    organism: Optional[str] = None
    dataset_type: Optional[Union[str, "DatasetTypeEnum"]] = None
    repository: Optional[Union[str, "DatasetRepositoryEnum"]] = None
    sample_types: Optional[Union[str, list[str]]] = empty_list()
    sample_count: Optional[int] = None
    conditions: Optional[Union[str, list[str]]] = empty_list()
    platform: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    publication: Optional[str] = None
    findings: Optional[str] = None
    evidence: Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]] = empty_list()
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.dataset_type is not None and not isinstance(self.dataset_type, DatasetTypeEnum):
            self.dataset_type = DatasetTypeEnum(self.dataset_type)

        if self.repository is not None and not isinstance(self.repository, DatasetRepositoryEnum):
            self.repository = DatasetRepositoryEnum(self.repository)

        if not isinstance(self.sample_types, list):
            self.sample_types = [self.sample_types] if self.sample_types is not None else []
        self.sample_types = [v if isinstance(v, str) else str(v) for v in self.sample_types]

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, str) else str(v) for v in self.conditions]

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.publication is not None and not isinstance(self.publication, str):
            self.publication = str(self.publication)

        if self.findings is not None and not isinstance(self.findings, str):
            self.findings = str(self.findings)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=SupportingReference, key_name="reference", keyed=False)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations
class SeedStatus(EnumDefinitionImpl):

    UNKNOWN_CANDIDATE = PermissibleValue(text="UNKNOWN_CANDIDATE")
    KNOWN_HISTORICAL_DUF = PermissibleValue(text="KNOWN_HISTORICAL_DUF")
    FALSE_POSITIVE_TEXT_HIT = PermissibleValue(text="FALSE_POSITIVE_TEXT_HIT")

    _defn = EnumDefinition(
        name="SeedStatus",
    )

class CharacterizationStatus(EnumDefinitionImpl):

    UNSCORED = PermissibleValue(text="UNSCORED")
    UNKNOWN_CANDIDATE = PermissibleValue(text="UNKNOWN_CANDIDATE")
    KNOWN_HISTORICAL_DUF = PermissibleValue(text="KNOWN_HISTORICAL_DUF")
    PARTIALLY_CHARACTERIZED = PermissibleValue(text="PARTIALLY_CHARACTERIZED")

    _defn = EnumDefinition(
        name="CharacterizationStatus",
    )

class CurationStatus(EnumDefinitionImpl):

    SEEDED = PermissibleValue(text="SEEDED")
    IN_PROGRESS = PermissibleValue(text="IN_PROGRESS")
    REVIEWED = PermissibleValue(text="REVIEWED")

    _defn = EnumDefinition(
        name="CurationStatus",
    )

class EvidenceKind(EnumDefinitionImpl):

    EXPERIMENTAL = PermissibleValue(text="EXPERIMENTAL")
    COMPUTATIONAL = PermissibleValue(text="COMPUTATIONAL")
    CONTEXTUAL = PermissibleValue(text="CONTEXTUAL")

    _defn = EnumDefinition(
        name="EvidenceKind",
    )

class DiscussionKindEnum(EnumDefinitionImpl):
    """
    Kind of unresolved / in-progress item captured by a Discussion. Knowledge gaps are represented as a discussion
    kind so they reuse the shared pointer, evidence, and lifecycle machinery, while optional proposed experiments
    capture how a gap could be resolved.
    """
    OPEN_QUESTION = PermissibleValue(
        text="OPEN_QUESTION",
        description="An unresolved scientific question posed by curators or experts.")
    KNOWLEDGE_GAP = PermissibleValue(
        text="KNOWLEDGE_GAP",
        description="""A missing causal, evidentiary, model-system, or measurement assertion whose resolution would materially improve the record.""")
    CONTROVERSY = PermissibleValue(
        text="CONTROVERSY",
        description="A live disagreement or competing interpretation between published positions.")
    CURATION_TODO = PermissibleValue(
        text="CURATION_TODO",
        description="A curation task captured inline (e.g. \"ingredient needs CHEBI refinement\").")
    EMERGING_HYPOTHESIS = PermissibleValue(
        text="EMERGING_HYPOTHESIS",
        description="A recently reported hypothesis under active discussion in the community.")
    INTERPRETATION = PermissibleValue(
        text="INTERPRETATION",
        description="A discussion about how to interpret existing evidence or model an edge.")
    HUMAN_MODEL_MISMATCH = PermissibleValue(
        text="HUMAN_MODEL_MISMATCH",
        description="""A gap where evidence exists in one system but its fidelity to the target context is uncertain (e.g. an in-vitro/model result whose transfer to the in-situ or host-associated setting is unverified).""")

    _defn = EnumDefinition(
        name="DiscussionKindEnum",
        description="""Kind of unresolved / in-progress item captured by a Discussion. Knowledge gaps are represented as a discussion kind so they reuse the shared pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved.""",
    )

class DiscussionStatusEnum(EnumDefinitionImpl):
    """
    Lifecycle status for a Discussion.
    """
    OPEN = PermissibleValue(
        text="OPEN",
        description="Posed but not yet under active discussion.")
    UNDER_DISCUSSION = PermissibleValue(
        text="UNDER_DISCUSSION",
        description="Actively being discussed in one or more linked venues.")
    RESOLVED = PermissibleValue(
        text="RESOLVED",
        description="Closed with a documented resolution; kept for provenance.")
    ARCHIVED = PermissibleValue(
        text="ARCHIVED",
        description="No longer active and not resolved (deferred, stale, or superseded).")

    _defn = EnumDefinition(
        name="DiscussionStatusEnum",
        description="Lifecycle status for a Discussion.",
    )

class SupportLevelEnum(EnumDefinitionImpl):
    """
    How a SupportingReference bears on the claim it is attached to (mirrors the supports semantics already used in the
    Mech EvidenceItem models).
    """
    SUPPORT = PermissibleValue(
        text="SUPPORT",
        description="The source supports the claim.")
    REFUTE = PermissibleValue(
        text="REFUTE",
        description="The source contradicts the claim.")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="The source partially supports the claim or supports it with caveats.")
    NO_EVIDENCE = PermissibleValue(
        text="NO_EVIDENCE",
        description="The source is relevant context but does not directly bear on the claim.")
    WRONG_STATEMENT = PermissibleValue(
        text="WRONG_STATEMENT",
        description="The cited statement was found to be incorrect (kept for provenance).")

    _defn = EnumDefinition(
        name="SupportLevelEnum",
        description="""How a SupportingReference bears on the claim it is attached to (mirrors the supports semantics already used in the Mech EvidenceItem models).""",
    )

class DatasetTypeEnum(EnumDefinitionImpl):
    """
    Type of dataset or data resource. Canonical UNION of CultureMech's and CommunityMech's enums plus microbial
    additions. Migration map (old → this): CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS,
    METAGENOME→METAGENOMICS, METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S /
    AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged).
    """
    GENOMICS = PermissibleValue(
        text="GENOMICS",
        description="Isolate / single-organism genome data. (CultureMech GENOMICS; CommunityMech GENOME)")
    METAGENOMICS = PermissibleValue(
        text="METAGENOMICS",
        description="Shotgun metagenome sequencing. (CommunityMech METAGENOME)")
    AMPLICON_16S = PermissibleValue(
        text="AMPLICON_16S",
        description="16S rRNA marker-gene amplicon sequencing.")
    AMPLICON_ITS = PermissibleValue(
        text="AMPLICON_ITS",
        description="ITS marker-gene amplicon sequencing.")
    AMPLICON_OTHER = PermissibleValue(
        text="AMPLICON_OTHER",
        description="Marker-gene amplicon sequencing other than 16S/ITS (e.g. 18S, rpoB).")
    TRANSCRIPTOMICS = PermissibleValue(
        text="TRANSCRIPTOMICS",
        description="Single-organism RNA sequencing / expression.")
    METATRANSCRIPTOMICS = PermissibleValue(
        text="METATRANSCRIPTOMICS",
        description="Community-level RNA sequencing. (CommunityMech METATRANSCRIPTOME)")
    PROTEOMICS = PermissibleValue(
        text="PROTEOMICS",
        description="Single-organism protein expression profiling.")
    METAPROTEOMICS = PermissibleValue(
        text="METAPROTEOMICS",
        description="Community-level proteomics. (CommunityMech METAPROTEOME)")
    METABOLOMICS = PermissibleValue(
        text="METABOLOMICS",
        description="Metabolite profiling.")
    FLUXOMICS = PermissibleValue(
        text="FLUXOMICS",
        description="Metabolic flux profiling.")
    PHENOMICS = PermissibleValue(
        text="PHENOMICS",
        description="High-throughput phenotype profiling.")
    PHENOTYPE = PermissibleValue(
        text="PHENOTYPE",
        description="Phenotype / trait measurement collection (e.g. growth, biochemical).")
    MULTI_OMICS = PermissibleValue(
        text="MULTI_OMICS",
        description="Integrated multi-omics profiling.")
    OTHER = PermissibleValue(
        text="OTHER",
        description="A dataset type not covered by the above.")

    _defn = EnumDefinition(
        name="DatasetTypeEnum",
        description="""Type of dataset or data resource. Canonical UNION of CultureMech's and CommunityMech's enums plus microbial additions. Migration map (old → this): CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS, METAGENOME→METAGENOMICS, METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S / AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged).""",
    )

class DatasetRepositoryEnum(EnumDefinitionImpl):
    """
    Public repository hosting the dataset. Superset of CommunityMech's enum (all values preserved) plus common
    additions; CultureMech datasets have no repository field today and migrate with repository unset / OTHER.
    """
    NCBI_SRA = PermissibleValue(
        text="NCBI_SRA",
        description="NCBI Sequence Read Archive.")
    NCBI_BIOPROJECT = PermissibleValue(
        text="NCBI_BIOPROJECT",
        description="NCBI BioProject.")
    NCBI_GEO = PermissibleValue(
        text="NCBI_GEO",
        description="NCBI Gene Expression Omnibus.")
    NCBI_ASSEMBLY = PermissibleValue(
        text="NCBI_ASSEMBLY",
        description="NCBI Assembly (genome assemblies).")
    ENA = PermissibleValue(
        text="ENA",
        description="European Nucleotide Archive.")
    ARRAYEXPRESS = PermissibleValue(
        text="ARRAYEXPRESS",
        description="EBI ArrayExpress / BioStudies.")
    MGNIFY = PermissibleValue(
        text="MGNIFY",
        description="EBI MGnify metagenomics resource.")
    JGI_GOLD = PermissibleValue(
        text="JGI_GOLD",
        description="JGI Genomes OnLine Database.")
    JGI_IMG = PermissibleValue(
        text="JGI_IMG",
        description="JGI Integrated Microbial Genomes & Microbiomes.")
    NMDC = PermissibleValue(
        text="NMDC",
        description="National Microbiome Data Collaborative.")
    METABOLOMICS_WORKBENCH = PermissibleValue(
        text="METABOLOMICS_WORKBENCH",
        description="NIH Metabolomics Workbench.")
    METABOLIGHTS = PermissibleValue(
        text="METABOLIGHTS",
        description="EBI MetaboLights metabolomics repository.")
    MASSIVE = PermissibleValue(
        text="MASSIVE",
        description="MassIVE mass-spectrometry repository.")
    GNPS = PermissibleValue(
        text="GNPS",
        description="Global Natural Products Social Molecular Networking.")
    PRIDE = PermissibleValue(
        text="PRIDE",
        description="EBI PRIDE proteomics repository.")
    DBGAP = PermissibleValue(
        text="DBGAP",
        description="NCBI database of Genotypes and Phenotypes.")
    GTEX = PermissibleValue(
        text="GTEX",
        description="Genotype-Tissue Expression project.")
    FIGSHARE = PermissibleValue(
        text="FIGSHARE",
        description="Figshare general-purpose research data archive.")
    ZENODO = PermissibleValue(
        text="ZENODO",
        description="Zenodo general-purpose research data archive.")
    BIOMODELS = PermissibleValue(
        text="BIOMODELS",
        description="EBI BioModels repository of computational models.")
    KBASE = PermissibleValue(
        text="KBASE",
        description="DOE Systems Biology Knowledgebase (KBase).")
    OTHER = PermissibleValue(
        text="OTHER",
        description="A repository not covered by the above.")

    _defn = EnumDefinition(
        name="DatasetRepositoryEnum",
        description="""Public repository hosting the dataset. Superset of CommunityMech's enum (all values preserved) plus common additions; CultureMech datasets have no repository field today and migrate with repository unset / OTHER.""",
    )

# Slots
class slots:
    pass

slots.familyRecord__id = Slot(uri=DUFMECH.id, name="familyRecord__id", curie=DUFMECH.curie('id'),
                   model_uri=DUFMECH.familyRecord__id, domain=None, range=URIRef,
                   pattern=re.compile(r'^Pfam:PF[0-9]{5}$'))

slots.familyRecord__pfam_id = Slot(uri=DUFMECH.pfam_id, name="familyRecord__pfam_id", curie=DUFMECH.curie('pfam_id'),
                   model_uri=DUFMECH.familyRecord__pfam_id, domain=None, range=str,
                   pattern=re.compile(r'^PF[0-9]{5}$'))

slots.familyRecord__name = Slot(uri=DUFMECH.name, name="familyRecord__name", curie=DUFMECH.curie('name'),
                   model_uri=DUFMECH.familyRecord__name, domain=None, range=str)

slots.familyRecord__short_name = Slot(uri=DUFMECH.short_name, name="familyRecord__short_name", curie=DUFMECH.curie('short_name'),
                   model_uri=DUFMECH.familyRecord__short_name, domain=None, range=str)

slots.familyRecord__interpro_id = Slot(uri=DUFMECH.interpro_id, name="familyRecord__interpro_id", curie=DUFMECH.curie('interpro_id'),
                   model_uri=DUFMECH.familyRecord__interpro_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^InterPro:IPR[0-9]{6}$'))

slots.familyRecord__seed_status = Slot(uri=DUFMECH.seed_status, name="familyRecord__seed_status", curie=DUFMECH.curie('seed_status'),
                   model_uri=DUFMECH.familyRecord__seed_status, domain=None, range=Union[str, "SeedStatus"])

slots.familyRecord__characterization_status = Slot(uri=DUFMECH.characterization_status, name="familyRecord__characterization_status", curie=DUFMECH.curie('characterization_status'),
                   model_uri=DUFMECH.familyRecord__characterization_status, domain=None, range=Union[str, "CharacterizationStatus"])

slots.familyRecord__curation_status = Slot(uri=DUFMECH.curation_status, name="familyRecord__curation_status", curie=DUFMECH.curie('curation_status'),
                   model_uri=DUFMECH.familyRecord__curation_status, domain=None, range=Union[str, "CurationStatus"])

slots.familyRecord__review_id = Slot(uri=DUFMECH.review_id, name="familyRecord__review_id", curie=DUFMECH.curie('review_id'),
                   model_uri=DUFMECH.familyRecord__review_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^reports/yaml_record_review/[A-Za-z0-9_.-]+[.]md$'))

slots.familyRecord__curation_history = Slot(uri=DUFMECH.curation_history, name="familyRecord__curation_history", curie=DUFMECH.curie('curation_history'),
                   model_uri=DUFMECH.familyRecord__curation_history, domain=None, range=Optional[str],
                   pattern=re.compile(r'^history/records/PF[0-9]{5}$'))

slots.familyRecord__curation_events = Slot(uri=DUFMECH.curation_events, name="familyRecord__curation_events", curie=DUFMECH.curie('curation_events'),
                   model_uri=DUFMECH.familyRecord__curation_events, domain=None, range=Optional[Union[Union[dict, CurationEvent], list[Union[dict, CurationEvent]]]])

slots.familyRecord__description = Slot(uri=DUFMECH.description, name="familyRecord__description", curie=DUFMECH.curie('description'),
                   model_uri=DUFMECH.familyRecord__description, domain=None, range=Optional[str])

slots.familyRecord__source_url = Slot(uri=DUFMECH.source_url, name="familyRecord__source_url", curie=DUFMECH.curie('source_url'),
                   model_uri=DUFMECH.familyRecord__source_url, domain=None, range=Union[str, URI])

slots.familyRecord__counters = Slot(uri=DUFMECH.counters, name="familyRecord__counters", curie=DUFMECH.curie('counters'),
                   model_uri=DUFMECH.familyRecord__counters, domain=None, range=Optional[Union[dict, FamilyCounters]])

slots.familyRecord__provenance = Slot(uri=DUFMECH.provenance, name="familyRecord__provenance", curie=DUFMECH.curie('provenance'),
                   model_uri=DUFMECH.familyRecord__provenance, domain=None, range=Union[dict, SnapshotProvenance])

slots.familyRecord__score_provenance = Slot(uri=DUFMECH.score_provenance, name="familyRecord__score_provenance", curie=DUFMECH.curie('score_provenance'),
                   model_uri=DUFMECH.familyRecord__score_provenance, domain=None, range=Optional[Union[dict, SnapshotProvenance]])

slots.familyRecord__assertions = Slot(uri=DUFMECH.assertions, name="familyRecord__assertions", curie=DUFMECH.curie('assertions'),
                   model_uri=DUFMECH.familyRecord__assertions, domain=None, range=Optional[Union[Union[dict, FunctionalAssertion], list[Union[dict, FunctionalAssertion]]]])

slots.familyRecord__discussions = Slot(uri=DUFMECH.discussions, name="familyRecord__discussions", curie=DUFMECH.curie('discussions'),
                   model_uri=DUFMECH.familyRecord__discussions, domain=None, range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]])

slots.familyRecord__datasets = Slot(uri=DUFMECH.datasets, name="familyRecord__datasets", curie=DUFMECH.curie('datasets'),
                   model_uri=DUFMECH.familyRecord__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.familyRecord__cross_corpus_links = Slot(uri=DUFMECH.cross_corpus_links, name="familyRecord__cross_corpus_links", curie=DUFMECH.curie('cross_corpus_links'),
                   model_uri=DUFMECH.familyRecord__cross_corpus_links, domain=None, range=Optional[Union[Union[dict, CrossCorpusLink], list[Union[dict, CrossCorpusLink]]]])

slots.familyCuration__pfam_id = Slot(uri=DUFMECH.pfam_id, name="familyCuration__pfam_id", curie=DUFMECH.curie('pfam_id'),
                   model_uri=DUFMECH.familyCuration__pfam_id, domain=None, range=str,
                   pattern=re.compile(r'^PF[0-9]{5}$'))

slots.familyCuration__curation_status = Slot(uri=DUFMECH.curation_status, name="familyCuration__curation_status", curie=DUFMECH.curie('curation_status'),
                   model_uri=DUFMECH.familyCuration__curation_status, domain=None, range=Union[str, "CurationStatus"])

slots.familyCuration__review_id = Slot(uri=DUFMECH.review_id, name="familyCuration__review_id", curie=DUFMECH.curie('review_id'),
                   model_uri=DUFMECH.familyCuration__review_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^reports/yaml_record_review/[A-Za-z0-9_.-]+[.]md$'))

slots.familyCuration__curation_history = Slot(uri=DUFMECH.curation_history, name="familyCuration__curation_history", curie=DUFMECH.curie('curation_history'),
                   model_uri=DUFMECH.familyCuration__curation_history, domain=None, range=Optional[str],
                   pattern=re.compile(r'^history/records/PF[0-9]{5}$'))

slots.familyCuration__assertions = Slot(uri=DUFMECH.assertions, name="familyCuration__assertions", curie=DUFMECH.curie('assertions'),
                   model_uri=DUFMECH.familyCuration__assertions, domain=None, range=Optional[Union[Union[dict, FunctionalAssertion], list[Union[dict, FunctionalAssertion]]]])

slots.familyCuration__discussions = Slot(uri=DUFMECH.discussions, name="familyCuration__discussions", curie=DUFMECH.curie('discussions'),
                   model_uri=DUFMECH.familyCuration__discussions, domain=None, range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]])

slots.familyCuration__datasets = Slot(uri=DUFMECH.datasets, name="familyCuration__datasets", curie=DUFMECH.curie('datasets'),
                   model_uri=DUFMECH.familyCuration__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.familyCuration__cross_corpus_links = Slot(uri=DUFMECH.cross_corpus_links, name="familyCuration__cross_corpus_links", curie=DUFMECH.curie('cross_corpus_links'),
                   model_uri=DUFMECH.familyCuration__cross_corpus_links, domain=None, range=Optional[Union[Union[dict, CrossCorpusLink], list[Union[dict, CrossCorpusLink]]]])

slots.curationEvent__timestamp = Slot(uri=DUFMECH.timestamp, name="curationEvent__timestamp", curie=DUFMECH.curie('timestamp'),
                   model_uri=DUFMECH.curationEvent__timestamp, domain=None, range=str,
                   pattern=re.compile(r'^20[0-9]{2}-'))

slots.curationEvent__curator = Slot(uri=DUFMECH.curator, name="curationEvent__curator", curie=DUFMECH.curie('curator'),
                   model_uri=DUFMECH.curationEvent__curator, domain=None, range=str)

slots.curationEvent__action = Slot(uri=DUFMECH.action, name="curationEvent__action", curie=DUFMECH.curie('action'),
                   model_uri=DUFMECH.curationEvent__action, domain=None, range=str)

slots.curationEvent__outcome = Slot(uri=DUFMECH.outcome, name="curationEvent__outcome", curie=DUFMECH.curie('outcome'),
                   model_uri=DUFMECH.curationEvent__outcome, domain=None, range=str)

slots.curationEvent__summary = Slot(uri=DUFMECH.summary, name="curationEvent__summary", curie=DUFMECH.curie('summary'),
                   model_uri=DUFMECH.curationEvent__summary, domain=None, range=str)

slots.curationEvent__history_record = Slot(uri=DUFMECH.history_record, name="curationEvent__history_record", curie=DUFMECH.curie('history_record'),
                   model_uri=DUFMECH.curationEvent__history_record, domain=None, range=str,
                   pattern=re.compile(r'^history/records/PF[0-9]{5}/[A-Za-z0-9_.-]+[.]ya?ml$'))

slots.curationEvent__event_index = Slot(uri=DUFMECH.event_index, name="curationEvent__event_index", curie=DUFMECH.curie('event_index'),
                   model_uri=DUFMECH.curationEvent__event_index, domain=None, range=int)

slots.curationEvent__llm_assisted = Slot(uri=DUFMECH.llm_assisted, name="curationEvent__llm_assisted", curie=DUFMECH.curie('llm_assisted'),
                   model_uri=DUFMECH.curationEvent__llm_assisted, domain=None, range=Union[bool, Bool])

slots.familyCounters__proteins = Slot(uri=DUFMECH.proteins, name="familyCounters__proteins", curie=DUFMECH.curie('proteins'),
                   model_uri=DUFMECH.familyCounters__proteins, domain=None, range=Optional[int])

slots.familyCounters__matches = Slot(uri=DUFMECH.matches, name="familyCounters__matches", curie=DUFMECH.curie('matches'),
                   model_uri=DUFMECH.familyCounters__matches, domain=None, range=Optional[int])

slots.familyCounters__proteomes = Slot(uri=DUFMECH.proteomes, name="familyCounters__proteomes", curie=DUFMECH.curie('proteomes'),
                   model_uri=DUFMECH.familyCounters__proteomes, domain=None, range=Optional[int])

slots.familyCounters__taxa = Slot(uri=DUFMECH.taxa, name="familyCounters__taxa", curie=DUFMECH.curie('taxa'),
                   model_uri=DUFMECH.familyCounters__taxa, domain=None, range=Optional[int])

slots.familyCounters__structures = Slot(uri=DUFMECH.structures, name="familyCounters__structures", curie=DUFMECH.curie('structures'),
                   model_uri=DUFMECH.familyCounters__structures, domain=None, range=Optional[int])

slots.familyCounters__alphafold_models = Slot(uri=DUFMECH.alphafold_models, name="familyCounters__alphafold_models", curie=DUFMECH.curie('alphafold_models'),
                   model_uri=DUFMECH.familyCounters__alphafold_models, domain=None, range=Optional[int])

slots.familyCounters__domain_architectures = Slot(uri=DUFMECH.domain_architectures, name="familyCounters__domain_architectures", curie=DUFMECH.curie('domain_architectures'),
                   model_uri=DUFMECH.familyCounters__domain_architectures, domain=None, range=Optional[int])

slots.snapshotProvenance__snapshot_id = Slot(uri=DUFMECH.snapshot_id, name="snapshotProvenance__snapshot_id", curie=DUFMECH.curie('snapshot_id'),
                   model_uri=DUFMECH.snapshotProvenance__snapshot_id, domain=None, range=str)

slots.snapshotProvenance__path = Slot(uri=DUFMECH.path, name="snapshotProvenance__path", curie=DUFMECH.curie('path'),
                   model_uri=DUFMECH.snapshotProvenance__path, domain=None, range=str,
                   pattern=re.compile(r'^data/worklists/[A-Za-z0-9_-]+[.]json$'))

slots.snapshotProvenance__sha256 = Slot(uri=DUFMECH.sha256, name="snapshotProvenance__sha256", curie=DUFMECH.curie('sha256'),
                   model_uri=DUFMECH.snapshotProvenance__sha256, domain=None, range=str,
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.snapshotProvenance__generated_at = Slot(uri=DUFMECH.generated_at, name="snapshotProvenance__generated_at", curie=DUFMECH.curie('generated_at'),
                   model_uri=DUFMECH.snapshotProvenance__generated_at, domain=None, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}T.*(Z|[+-]\d{2}:\d{2})$'))

slots.snapshotProvenance__source_url = Slot(uri=DUFMECH.source_url, name="snapshotProvenance__source_url", curie=DUFMECH.curie('source_url'),
                   model_uri=DUFMECH.snapshotProvenance__source_url, domain=None, range=Optional[Union[str, URI]])

slots.functionalAssertion__assertion_id = Slot(uri=DUFMECH.assertion_id, name="functionalAssertion__assertion_id", curie=DUFMECH.curie('assertion_id'),
                   model_uri=DUFMECH.functionalAssertion__assertion_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.functionalAssertion__statement = Slot(uri=DUFMECH.statement, name="functionalAssertion__statement", curie=DUFMECH.curie('statement'),
                   model_uri=DUFMECH.functionalAssertion__statement, domain=None, range=str)

slots.functionalAssertion__evidence_kind = Slot(uri=DUFMECH.evidence_kind, name="functionalAssertion__evidence_kind", curie=DUFMECH.curie('evidence_kind'),
                   model_uri=DUFMECH.functionalAssertion__evidence_kind, domain=None, range=Union[str, "EvidenceKind"])

slots.functionalAssertion__scope = Slot(uri=DUFMECH.scope, name="functionalAssertion__scope", curie=DUFMECH.curie('scope'),
                   model_uri=DUFMECH.functionalAssertion__scope, domain=None, range=str)

slots.functionalAssertion__evidence = Slot(uri=DUFMECH.evidence, name="functionalAssertion__evidence", curie=DUFMECH.curie('evidence'),
                   model_uri=DUFMECH.functionalAssertion__evidence, domain=None, range=Union[Union[dict, ClaimEvidence], list[Union[dict, ClaimEvidence]]])

slots.claimEvidence__reference = Slot(uri=DUFMECH.reference, name="claimEvidence__reference", curie=DUFMECH.curie('reference'),
                   model_uri=DUFMECH.claimEvidence__reference, domain=None, range=str,
                   pattern=re.compile(r'^(PMID:[0-9]+|doi:10[.][0-9]{4,9}/\S+|https://\S+)$'))

slots.claimEvidence__source_url = Slot(uri=DUFMECH.source_url, name="claimEvidence__source_url", curie=DUFMECH.curie('source_url'),
                   model_uri=DUFMECH.claimEvidence__source_url, domain=None, range=Union[str, URI])

slots.claimEvidence__snippet = Slot(uri=DUFMECH.snippet, name="claimEvidence__snippet", curie=DUFMECH.curie('snippet'),
                   model_uri=DUFMECH.claimEvidence__snippet, domain=None, range=str)

slots.claimEvidence__explanation = Slot(uri=DUFMECH.explanation, name="claimEvidence__explanation", curie=DUFMECH.curie('explanation'),
                   model_uri=DUFMECH.claimEvidence__explanation, domain=None, range=str)

slots.claimEvidence__cache_path = Slot(uri=DUFMECH.cache_path, name="claimEvidence__cache_path", curie=DUFMECH.curie('cache_path'),
                   model_uri=DUFMECH.claimEvidence__cache_path, domain=None, range=str,
                   pattern=re.compile(r'^evidence/[A-Za-z0-9_./-]+[.]txt$'))

slots.claimEvidence__cache_sha256 = Slot(uri=DUFMECH.cache_sha256, name="claimEvidence__cache_sha256", curie=DUFMECH.curie('cache_sha256'),
                   model_uri=DUFMECH.claimEvidence__cache_sha256, domain=None, range=str,
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.crossCorpusLink__corpus = Slot(uri=MECH_SHARED.corpus, name="crossCorpusLink__corpus", curie=MECH_SHARED.curie('corpus'),
                   model_uri=DUFMECH.crossCorpusLink__corpus, domain=None, range=str)

slots.crossCorpusLink__identifier = Slot(uri=MECH_SHARED.identifier, name="crossCorpusLink__identifier", curie=MECH_SHARED.curie('identifier'),
                   model_uri=DUFMECH.crossCorpusLink__identifier, domain=None, range=str)

slots.crossCorpusLink__relation = Slot(uri=MECH_SHARED.relation, name="crossCorpusLink__relation", curie=MECH_SHARED.curie('relation'),
                   model_uri=DUFMECH.crossCorpusLink__relation, domain=None, range=str)

slots.crossCorpusLink__basis = Slot(uri=MECH_SHARED.basis, name="crossCorpusLink__basis", curie=MECH_SHARED.curie('basis'),
                   model_uri=DUFMECH.crossCorpusLink__basis, domain=None, range=str)

slots.crossCorpusLink__source_version = Slot(uri=MECH_SHARED.source_version, name="crossCorpusLink__source_version", curie=MECH_SHARED.curie('source_version'),
                   model_uri=DUFMECH.crossCorpusLink__source_version, domain=None, range=Optional[str])

slots.supportingReference__reference = Slot(uri=MECH_SHARED.reference, name="supportingReference__reference", curie=MECH_SHARED.curie('reference'),
                   model_uri=DUFMECH.supportingReference__reference, domain=None, range=str)

slots.supportingReference__reference_title = Slot(uri=MECH_SHARED.reference_title, name="supportingReference__reference_title", curie=MECH_SHARED.curie('reference_title'),
                   model_uri=DUFMECH.supportingReference__reference_title, domain=None, range=Optional[str])

slots.supportingReference__supports = Slot(uri=MECH_SHARED.supports, name="supportingReference__supports", curie=MECH_SHARED.curie('supports'),
                   model_uri=DUFMECH.supportingReference__supports, domain=None, range=Optional[Union[str, "SupportLevelEnum"]])

slots.supportingReference__evidence_source = Slot(uri=MECH_SHARED.evidence_source, name="supportingReference__evidence_source", curie=MECH_SHARED.curie('evidence_source'),
                   model_uri=DUFMECH.supportingReference__evidence_source, domain=None, range=Optional[str])

slots.supportingReference__snippet = Slot(uri=MECH_SHARED.snippet, name="supportingReference__snippet", curie=MECH_SHARED.curie('snippet'),
                   model_uri=DUFMECH.supportingReference__snippet, domain=None, range=Optional[str])

slots.supportingReference__explanation = Slot(uri=MECH_SHARED.explanation, name="supportingReference__explanation", curie=MECH_SHARED.curie('explanation'),
                   model_uri=DUFMECH.supportingReference__explanation, domain=None, range=Optional[str])

slots.supportingReference__notes = Slot(uri=MECH_SHARED.notes, name="supportingReference__notes", curie=MECH_SHARED.curie('notes'),
                   model_uri=DUFMECH.supportingReference__notes, domain=None, range=Optional[str])

slots.discussion__discussion_id = Slot(uri=MECH_SHARED.discussion_id, name="discussion__discussion_id", curie=MECH_SHARED.curie('discussion_id'),
                   model_uri=DUFMECH.discussion__discussion_id, domain=None, range=str)

slots.discussion__prompt = Slot(uri=MECH_SHARED.prompt, name="discussion__prompt", curie=MECH_SHARED.curie('prompt'),
                   model_uri=DUFMECH.discussion__prompt, domain=None, range=str)

slots.discussion__kind = Slot(uri=MECH_SHARED.kind, name="discussion__kind", curie=MECH_SHARED.curie('kind'),
                   model_uri=DUFMECH.discussion__kind, domain=None, range=Optional[Union[str, "DiscussionKindEnum"]])

slots.discussion__status = Slot(uri=MECH_SHARED.status, name="discussion__status", curie=MECH_SHARED.curie('status'),
                   model_uri=DUFMECH.discussion__status, domain=None, range=Optional[Union[str, "DiscussionStatusEnum"]])

slots.discussion__attaches_to = Slot(uri=MECH_SHARED.attaches_to, name="discussion__attaches_to", curie=MECH_SHARED.curie('attaches_to'),
                   model_uri=DUFMECH.discussion__attaches_to, domain=None, range=Optional[Union[str, list[str]]])

slots.discussion__rationale = Slot(uri=MECH_SHARED.rationale, name="discussion__rationale", curie=MECH_SHARED.curie('rationale'),
                   model_uri=DUFMECH.discussion__rationale, domain=None, range=Optional[str])

slots.discussion__proposed_experiments = Slot(uri=MECH_SHARED.proposed_experiments, name="discussion__proposed_experiments", curie=MECH_SHARED.curie('proposed_experiments'),
                   model_uri=DUFMECH.discussion__proposed_experiments, domain=None, range=Optional[Union[Union[dict, ProposedExperiment], list[Union[dict, ProposedExperiment]]]])

slots.discussion__evidence = Slot(uri=MECH_SHARED.evidence, name="discussion__evidence", curie=MECH_SHARED.curie('evidence'),
                   model_uri=DUFMECH.discussion__evidence, domain=None, range=Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]])

slots.discussion__posed_by = Slot(uri=MECH_SHARED.posed_by, name="discussion__posed_by", curie=MECH_SHARED.curie('posed_by'),
                   model_uri=DUFMECH.discussion__posed_by, domain=None, range=Optional[str])

slots.discussion__posed_date = Slot(uri=MECH_SHARED.posed_date, name="discussion__posed_date", curie=MECH_SHARED.curie('posed_date'),
                   model_uri=DUFMECH.discussion__posed_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.discussion__resolved_date = Slot(uri=MECH_SHARED.resolved_date, name="discussion__resolved_date", curie=MECH_SHARED.curie('resolved_date'),
                   model_uri=DUFMECH.discussion__resolved_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.discussion__resolution_note = Slot(uri=MECH_SHARED.resolution_note, name="discussion__resolution_note", curie=MECH_SHARED.curie('resolution_note'),
                   model_uri=DUFMECH.discussion__resolution_note, domain=None, range=Optional[str])

slots.discussion__notes = Slot(uri=MECH_SHARED.notes, name="discussion__notes", curie=MECH_SHARED.curie('notes'),
                   model_uri=DUFMECH.discussion__notes, domain=None, range=Optional[str])

slots.proposedExperiment__experiment_id = Slot(uri=MECH_SHARED.experiment_id, name="proposedExperiment__experiment_id", curie=MECH_SHARED.curie('experiment_id'),
                   model_uri=DUFMECH.proposedExperiment__experiment_id, domain=None, range=Optional[str])

slots.proposedExperiment__name = Slot(uri=MECH_SHARED.name, name="proposedExperiment__name", curie=MECH_SHARED.curie('name'),
                   model_uri=DUFMECH.proposedExperiment__name, domain=None, range=Optional[str])

slots.proposedExperiment__description = Slot(uri=MECH_SHARED.description, name="proposedExperiment__description", curie=MECH_SHARED.curie('description'),
                   model_uri=DUFMECH.proposedExperiment__description, domain=None, range=Optional[str])

slots.proposedExperiment__approach = Slot(uri=MECH_SHARED.approach, name="proposedExperiment__approach", curie=MECH_SHARED.curie('approach'),
                   model_uri=DUFMECH.proposedExperiment__approach, domain=None, range=Optional[str])

slots.proposedExperiment__model_systems = Slot(uri=MECH_SHARED.model_systems, name="proposedExperiment__model_systems", curie=MECH_SHARED.curie('model_systems'),
                   model_uri=DUFMECH.proposedExperiment__model_systems, domain=None, range=Optional[Union[str, list[str]]])

slots.proposedExperiment__perturbations = Slot(uri=MECH_SHARED.perturbations, name="proposedExperiment__perturbations", curie=MECH_SHARED.curie('perturbations'),
                   model_uri=DUFMECH.proposedExperiment__perturbations, domain=None, range=Optional[Union[str, list[str]]])

slots.proposedExperiment__readouts = Slot(uri=MECH_SHARED.readouts, name="proposedExperiment__readouts", curie=MECH_SHARED.curie('readouts'),
                   model_uri=DUFMECH.proposedExperiment__readouts, domain=None, range=Optional[Union[str, list[str]]])

slots.proposedExperiment__decision_criterion = Slot(uri=MECH_SHARED.decision_criterion, name="proposedExperiment__decision_criterion", curie=MECH_SHARED.curie('decision_criterion'),
                   model_uri=DUFMECH.proposedExperiment__decision_criterion, domain=None, range=Optional[str])

slots.proposedExperiment__would_support = Slot(uri=MECH_SHARED.would_support, name="proposedExperiment__would_support", curie=MECH_SHARED.curie('would_support'),
                   model_uri=DUFMECH.proposedExperiment__would_support, domain=None, range=Optional[str])

slots.proposedExperiment__would_refute = Slot(uri=MECH_SHARED.would_refute, name="proposedExperiment__would_refute", curie=MECH_SHARED.curie('would_refute'),
                   model_uri=DUFMECH.proposedExperiment__would_refute, domain=None, range=Optional[str])

slots.dataset__accession = Slot(uri=MECH_SHARED.accession, name="dataset__accession", curie=MECH_SHARED.curie('accession'),
                   model_uri=DUFMECH.dataset__accession, domain=None, range=Optional[str])

slots.dataset__title = Slot(uri=MECH_SHARED.title, name="dataset__title", curie=MECH_SHARED.curie('title'),
                   model_uri=DUFMECH.dataset__title, domain=None, range=Optional[str])

slots.dataset__description = Slot(uri=MECH_SHARED.description, name="dataset__description", curie=MECH_SHARED.curie('description'),
                   model_uri=DUFMECH.dataset__description, domain=None, range=Optional[str])

slots.dataset__organism = Slot(uri=MECH_SHARED.organism, name="dataset__organism", curie=MECH_SHARED.curie('organism'),
                   model_uri=DUFMECH.dataset__organism, domain=None, range=Optional[str])

slots.dataset__dataset_type = Slot(uri=MECH_SHARED.dataset_type, name="dataset__dataset_type", curie=MECH_SHARED.curie('dataset_type'),
                   model_uri=DUFMECH.dataset__dataset_type, domain=None, range=Optional[Union[str, "DatasetTypeEnum"]])

slots.dataset__repository = Slot(uri=MECH_SHARED.repository, name="dataset__repository", curie=MECH_SHARED.curie('repository'),
                   model_uri=DUFMECH.dataset__repository, domain=None, range=Optional[Union[str, "DatasetRepositoryEnum"]])

slots.dataset__sample_types = Slot(uri=MECH_SHARED.sample_types, name="dataset__sample_types", curie=MECH_SHARED.curie('sample_types'),
                   model_uri=DUFMECH.dataset__sample_types, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__sample_count = Slot(uri=MECH_SHARED.sample_count, name="dataset__sample_count", curie=MECH_SHARED.curie('sample_count'),
                   model_uri=DUFMECH.dataset__sample_count, domain=None, range=Optional[int])

slots.dataset__conditions = Slot(uri=MECH_SHARED.conditions, name="dataset__conditions", curie=MECH_SHARED.curie('conditions'),
                   model_uri=DUFMECH.dataset__conditions, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__platform = Slot(uri=MECH_SHARED.platform, name="dataset__platform", curie=MECH_SHARED.curie('platform'),
                   model_uri=DUFMECH.dataset__platform, domain=None, range=Optional[str])

slots.dataset__url = Slot(uri=MECH_SHARED.url, name="dataset__url", curie=MECH_SHARED.curie('url'),
                   model_uri=DUFMECH.dataset__url, domain=None, range=Optional[Union[str, URI]])

slots.dataset__publication = Slot(uri=MECH_SHARED.publication, name="dataset__publication", curie=MECH_SHARED.curie('publication'),
                   model_uri=DUFMECH.dataset__publication, domain=None, range=Optional[str])

slots.dataset__findings = Slot(uri=MECH_SHARED.findings, name="dataset__findings", curie=MECH_SHARED.curie('findings'),
                   model_uri=DUFMECH.dataset__findings, domain=None, range=Optional[str])

slots.dataset__evidence = Slot(uri=MECH_SHARED.evidence, name="dataset__evidence", curie=MECH_SHARED.curie('evidence'),
                   model_uri=DUFMECH.dataset__evidence, domain=None, range=Optional[Union[Union[dict, SupportingReference], list[Union[dict, SupportingReference]]]])

slots.dataset__notes = Slot(uri=MECH_SHARED.notes, name="dataset__notes", curie=MECH_SHARED.curie('notes'),
                   model_uri=DUFMECH.dataset__notes, domain=None, range=Optional[str])
