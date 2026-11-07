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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uri
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
    causal_graphs: Optional[Union[Union[dict, "CausalGraph"], list[Union[dict, "CausalGraph"]]]] = empty_list()
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    cross_corpus_links: Optional[Union[Union[dict, "CrossCorpusLink"], list[Union[dict, "CrossCorpusLink"]]]] = empty_list()
    sequence_reasoning_graphs: Optional[Union[Union[dict, "RegionReasoningGraph"], list[Union[dict, "RegionReasoningGraph"]]]] = empty_list()

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

        self._normalize_inlined_as_list(slot_name="causal_graphs", slot_type=CausalGraph, key_name="graph_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        self._normalize_inlined_as_list(slot_name="cross_corpus_links", slot_type=CrossCorpusLink, key_name="corpus", keyed=False)

        self._normalize_inlined_as_list(slot_name="sequence_reasoning_graphs", slot_type=RegionReasoningGraph, key_name="graph_id", keyed=False)

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
    causal_graphs: Optional[Union[Union[dict, "CausalGraph"], list[Union[dict, "CausalGraph"]]]] = empty_list()
    discussions: Optional[Union[Union[dict, "Discussion"], list[Union[dict, "Discussion"]]]] = empty_list()
    datasets: Optional[Union[Union[dict, "Dataset"], list[Union[dict, "Dataset"]]]] = empty_list()
    cross_corpus_links: Optional[Union[Union[dict, "CrossCorpusLink"], list[Union[dict, "CrossCorpusLink"]]]] = empty_list()
    sequence_reasoning_graphs: Optional[Union[Union[dict, "RegionReasoningGraph"], list[Union[dict, "RegionReasoningGraph"]]]] = empty_list()

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

        self._normalize_inlined_as_list(slot_name="causal_graphs", slot_type=CausalGraph, key_name="graph_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="discussions", slot_type=Discussion, key_name="discussion_id", keyed=False)

        if not isinstance(self.datasets, list):
            self.datasets = [self.datasets] if self.datasets is not None else []
        self.datasets = [v if isinstance(v, Dataset) else Dataset(**as_dict(v)) for v in self.datasets]

        self._normalize_inlined_as_list(slot_name="cross_corpus_links", slot_type=CrossCorpusLink, key_name="corpus", keyed=False)

        self._normalize_inlined_as_list(slot_name="sequence_reasoning_graphs", slot_type=RegionReasoningGraph, key_name="graph_id", keyed=False)

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
    sequence_id: Optional[str] = None
    region_id: Optional[str] = None
    synthesized_claim_id: Optional[str] = None

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

        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.region_id is not None and not isinstance(self.region_id, str):
            self.region_id = str(self.region_id)

        if self.synthesized_claim_id is not None and not isinstance(self.synthesized_claim_id, str):
            self.synthesized_claim_id = str(self.synthesized_claim_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CausalGraph(YAMLRoot):
    """
    A scoped directed mechanism or phenotype graph, not family-wide functional proof.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["CausalGraph"]
    class_class_curie: ClassVar[str] = "dufmech:CausalGraph"
    class_name: ClassVar[str] = "CausalGraph"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CausalGraph

    graph_id: str = None
    title: str = None
    scope: str = None
    context: str = None
    family_mapping: str = None
    scope_status: Union[str, "CausalScope"] = None
    limitations: str = None
    nodes: Union[Union[dict, "CausalNode"], list[Union[dict, "CausalNode"]]] = None
    edges: Union[Union[dict, "CausalEdge"], list[Union[dict, "CausalEdge"]]] = None
    taxon: Optional[str] = None
    feedback_explanation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.graph_id):
            self.MissingRequiredField("graph_id")
        if not isinstance(self.graph_id, str):
            self.graph_id = str(self.graph_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, str):
            self.scope = str(self.scope)

        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, str):
            self.context = str(self.context)

        if self._is_empty(self.family_mapping):
            self.MissingRequiredField("family_mapping")
        if not isinstance(self.family_mapping, str):
            self.family_mapping = str(self.family_mapping)

        if self._is_empty(self.scope_status):
            self.MissingRequiredField("scope_status")
        if not isinstance(self.scope_status, CausalScope):
            self.scope_status = CausalScope(self.scope_status)

        if self._is_empty(self.limitations):
            self.MissingRequiredField("limitations")
        if not isinstance(self.limitations, str):
            self.limitations = str(self.limitations)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=CausalNode, key_name="node_id", keyed=False)

        if self._is_empty(self.edges):
            self.MissingRequiredField("edges")
        self._normalize_inlined_as_list(slot_name="edges", slot_type=CausalEdge, key_name="edge_id", keyed=False)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.feedback_explanation is not None and not isinstance(self.feedback_explanation, str):
            self.feedback_explanation = str(self.feedback_explanation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CausalNode(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["CausalNode"]
    class_class_curie: ClassVar[str] = "dufmech:CausalNode"
    class_name: ClassVar[str] = "CausalNode"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CausalNode

    node_id: str = None
    label: str = None
    node_type: Union[str, "CausalNodeType"] = None
    grounding: Optional[Union[str, list[str]]] = empty_list()
    sequence_id: Optional[str] = None
    region_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.node_id):
            self.MissingRequiredField("node_id")
        if not isinstance(self.node_id, str):
            self.node_id = str(self.node_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.node_type):
            self.MissingRequiredField("node_type")
        if not isinstance(self.node_type, CausalNodeType):
            self.node_type = CausalNodeType(self.node_type)

        if not isinstance(self.grounding, list):
            self.grounding = [self.grounding] if self.grounding is not None else []
        self.grounding = [v if isinstance(v, str) else str(v) for v in self.grounding]

        if self.sequence_id is not None and not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self.region_id is not None and not isinstance(self.region_id, str):
            self.region_id = str(self.region_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CausalEdge(YAMLRoot):
    """
    Evidence for a directed relation, rather than citations only establishing the endpoints.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["CausalEdge"]
    class_class_curie: ClassVar[str] = "dufmech:CausalEdge"
    class_name: ClassVar[str] = "CausalEdge"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CausalEdge

    edge_id: str = None
    subject: str = None
    predicate: Union[str, "CausalPredicate"] = None
    object: str = None
    mechanism: str = None
    directness: Union[str, "CausalDirectness"] = None
    support: Union[str, "CausalSupport"] = None
    evidence_kind: Union[str, "EvidenceKind"] = None
    evidence: Union[Union[dict, "ClaimEvidence"], list[Union[dict, "ClaimEvidence"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.edge_id):
            self.MissingRequiredField("edge_id")
        if not isinstance(self.edge_id, str):
            self.edge_id = str(self.edge_id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, CausalPredicate):
            self.predicate = CausalPredicate(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self._is_empty(self.mechanism):
            self.MissingRequiredField("mechanism")
        if not isinstance(self.mechanism, str):
            self.mechanism = str(self.mechanism)

        if self._is_empty(self.directness):
            self.MissingRequiredField("directness")
        if not isinstance(self.directness, CausalDirectness):
            self.directness = CausalDirectness(self.directness)

        if self._is_empty(self.support):
            self.MissingRequiredField("support")
        if not isinstance(self.support, CausalSupport):
            self.support = CausalSupport(self.support)

        if self._is_empty(self.evidence_kind):
            self.MissingRequiredField("evidence_kind")
        if not isinstance(self.evidence_kind, EvidenceKind):
            self.evidence_kind = EvidenceKind(self.evidence_kind)

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
class RegionReasoningGraph(YAMLRoot):
    """
    Sequence-coordinate-aware reasoning graph connecting reference sequences, explicit 1-based inclusive regions,
    coordinate mappings, deduplicated observations, and evidence-graded functional claims while separating epistemic
    evidence links from biological causation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["RegionReasoningGraph"]
    class_class_curie: ClassVar[str] = "dufmech:RegionReasoningGraph"
    class_name: ClassVar[str] = "RegionReasoningGraph"
    class_model_uri: ClassVar[URIRef] = DUFMECH.RegionReasoningGraph

    graph_id: str = None
    pfam_id: str = None
    title: str = None
    sequences: Union[Union[dict, "SequenceIdentity"], list[Union[dict, "SequenceIdentity"]]] = None
    regions: Union[Union[dict, "SequenceRegion"], list[Union[dict, "SequenceRegion"]]] = None
    observations: Union[Union[dict, "RegionObservation"], list[Union[dict, "RegionObservation"]]] = None
    synthesized_claims: Union[Union[dict, "SynthesizedClaim"], list[Union[dict, "SynthesizedClaim"]]] = None
    reasoning_edges: Union[Union[dict, "ReasoningEdge"], list[Union[dict, "ReasoningEdge"]]] = None
    description: Optional[str] = None
    coordinate_mappings: Optional[Union[Union[dict, "CoordinateMapping"], list[Union[dict, "CoordinateMapping"]]]] = empty_list()
    evidence_groups: Optional[Union[Union[dict, "EvidenceGroup"], list[Union[dict, "EvidenceGroup"]]]] = empty_list()
    causal_graph_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.graph_id):
            self.MissingRequiredField("graph_id")
        if not isinstance(self.graph_id, str):
            self.graph_id = str(self.graph_id)

        if self._is_empty(self.pfam_id):
            self.MissingRequiredField("pfam_id")
        if not isinstance(self.pfam_id, str):
            self.pfam_id = str(self.pfam_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.sequences):
            self.MissingRequiredField("sequences")
        self._normalize_inlined_as_list(slot_name="sequences", slot_type=SequenceIdentity, key_name="sequence_id", keyed=False)

        if self._is_empty(self.regions):
            self.MissingRequiredField("regions")
        self._normalize_inlined_as_list(slot_name="regions", slot_type=SequenceRegion, key_name="region_id", keyed=False)

        if self._is_empty(self.observations):
            self.MissingRequiredField("observations")
        self._normalize_inlined_as_list(slot_name="observations", slot_type=RegionObservation, key_name="observation_id", keyed=False)

        if self._is_empty(self.synthesized_claims):
            self.MissingRequiredField("synthesized_claims")
        self._normalize_inlined_as_list(slot_name="synthesized_claims", slot_type=SynthesizedClaim, key_name="claim_id", keyed=False)

        if self._is_empty(self.reasoning_edges):
            self.MissingRequiredField("reasoning_edges")
        self._normalize_inlined_as_list(slot_name="reasoning_edges", slot_type=ReasoningEdge, key_name="edge_id", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="coordinate_mappings", slot_type=CoordinateMapping, key_name="mapping_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="evidence_groups", slot_type=EvidenceGroup, key_name="group_id", keyed=False)

        if not isinstance(self.causal_graph_refs, list):
            self.causal_graph_refs = [self.causal_graph_refs] if self.causal_graph_refs is not None else []
        self.causal_graph_refs = [v if isinstance(v, str) else str(v) for v in self.causal_graph_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceIdentity(YAMLRoot):
    """
    Identified reference protein sequence with explicit version or SHA-256 digest and isoform context for coordinate
    validation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["SequenceIdentity"]
    class_class_curie: ClassVar[str] = "dufmech:SequenceIdentity"
    class_name: ClassVar[str] = "SequenceIdentity"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SequenceIdentity

    sequence_id: str = None
    uniprot_accession: str = None
    sequence_length: int = None
    sequence_sha256: str = None
    isoform: Optional[str] = None
    sequence_version: Optional[int] = None
    sequence_md5: Optional[str] = None
    taxon_id: Optional[str] = None
    organism: Optional[str] = None
    uniprot_release: Optional[str] = None
    source_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self._is_empty(self.uniprot_accession):
            self.MissingRequiredField("uniprot_accession")
        if not isinstance(self.uniprot_accession, str):
            self.uniprot_accession = str(self.uniprot_accession)

        if self._is_empty(self.sequence_length):
            self.MissingRequiredField("sequence_length")
        if not isinstance(self.sequence_length, int):
            self.sequence_length = int(self.sequence_length)

        if self._is_empty(self.sequence_sha256):
            self.MissingRequiredField("sequence_sha256")
        if not isinstance(self.sequence_sha256, str):
            self.sequence_sha256 = str(self.sequence_sha256)

        if self.isoform is not None and not isinstance(self.isoform, str):
            self.isoform = str(self.isoform)

        if self.sequence_version is not None and not isinstance(self.sequence_version, int):
            self.sequence_version = int(self.sequence_version)

        if self.sequence_md5 is not None and not isinstance(self.sequence_md5, str):
            self.sequence_md5 = str(self.sequence_md5)

        if self.taxon_id is not None and not isinstance(self.taxon_id, str):
            self.taxon_id = str(self.taxon_id)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.uniprot_release is not None and not isinstance(self.uniprot_release, str):
            self.uniprot_release = str(self.uniprot_release)

        if self.source_url is not None and not isinstance(self.source_url, URI):
            self.source_url = URI(self.source_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceInterval(YAMLRoot):
    """
    Canonical 1-based inclusive interval [start, end] on an identified reference sequence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["SequenceInterval"]
    class_class_curie: ClassVar[str] = "dufmech:SequenceInterval"
    class_name: ClassVar[str] = "SequenceInterval"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SequenceInterval

    start: int = None
    end: int = None
    start_uncertain: Optional[Union[bool, Bool]] = None
    end_uncertain: Optional[Union[bool, Bool]] = None
    residue_identity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.start_uncertain is not None and not isinstance(self.start_uncertain, Bool):
            self.start_uncertain = Bool(self.start_uncertain)

        if self.end_uncertain is not None and not isinstance(self.end_uncertain, Bool):
            self.end_uncertain = Bool(self.end_uncertain)

        if self.residue_identity is not None and not isinstance(self.residue_identity, str):
            self.residue_identity = str(self.residue_identity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceRegion(YAMLRoot):
    """
    An explicit contiguous or discontinuous region, site, construct, or unlocalized whole-protein span on an
    identified sequence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["SequenceRegion"]
    class_class_curie: ClassVar[str] = "dufmech:SequenceRegion"
    class_name: ClassVar[str] = "SequenceRegion"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SequenceRegion

    region_id: str = None
    sequence_id: str = None
    label: str = None
    region_kind: Union[str, "RegionKind"] = None
    coordinate_status: Union[str, "CoordinateStatus"] = None
    source_coordinate_system: Union[str, "CoordinateSystem"] = None
    intervals: Optional[Union[Union[dict, SequenceInterval], list[Union[dict, SequenceInterval]]]] = empty_list()
    source_coordinates_text: Optional[str] = None
    conversion_provenance: Optional[str] = None
    pfam_id: Optional[str] = None
    interpro_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.region_id):
            self.MissingRequiredField("region_id")
        if not isinstance(self.region_id, str):
            self.region_id = str(self.region_id)

        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.region_kind):
            self.MissingRequiredField("region_kind")
        if not isinstance(self.region_kind, RegionKind):
            self.region_kind = RegionKind(self.region_kind)

        if self._is_empty(self.coordinate_status):
            self.MissingRequiredField("coordinate_status")
        if not isinstance(self.coordinate_status, CoordinateStatus):
            self.coordinate_status = CoordinateStatus(self.coordinate_status)

        if self._is_empty(self.source_coordinate_system):
            self.MissingRequiredField("source_coordinate_system")
        if not isinstance(self.source_coordinate_system, CoordinateSystem):
            self.source_coordinate_system = CoordinateSystem(self.source_coordinate_system)

        self._normalize_inlined_as_list(slot_name="intervals", slot_type=SequenceInterval, key_name="start", keyed=False)

        if self.source_coordinates_text is not None and not isinstance(self.source_coordinates_text, str):
            self.source_coordinates_text = str(self.source_coordinates_text)

        if self.conversion_provenance is not None and not isinstance(self.conversion_provenance, str):
            self.conversion_provenance = str(self.conversion_provenance)

        if self.pfam_id is not None and not isinstance(self.pfam_id, str):
            self.pfam_id = str(self.pfam_id)

        if self.interpro_id is not None and not isinstance(self.interpro_id, str):
            self.interpro_id = str(self.interpro_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResidueCorrespondence(YAMLRoot):
    """
    Explicit residue-level correspondence between two coordinate systems or homologous sequences.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["ResidueCorrespondence"]
    class_class_curie: ClassVar[str] = "dufmech:ResidueCorrespondence"
    class_name: ClassVar[str] = "ResidueCorrespondence"
    class_model_uri: ClassVar[URIRef] = DUFMECH.ResidueCorrespondence

    source_position: int = None
    target_position: int = None
    source_residue: Optional[str] = None
    target_residue: Optional[str] = None
    pdb_insertion_code: Optional[str] = None
    mutation_substitution: Optional[str] = None
    note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_position):
            self.MissingRequiredField("source_position")
        if not isinstance(self.source_position, int):
            self.source_position = int(self.source_position)

        if self._is_empty(self.target_position):
            self.MissingRequiredField("target_position")
        if not isinstance(self.target_position, int):
            self.target_position = int(self.target_position)

        if self.source_residue is not None and not isinstance(self.source_residue, str):
            self.source_residue = str(self.source_residue)

        if self.target_residue is not None and not isinstance(self.target_residue, str):
            self.target_residue = str(self.target_residue)

        if self.pdb_insertion_code is not None and not isinstance(self.pdb_insertion_code, str):
            self.pdb_insertion_code = str(self.pdb_insertion_code)

        if self.mutation_substitution is not None and not isinstance(self.mutation_substitution, str):
            self.mutation_substitution = str(self.mutation_substitution)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoordinateMapping(YAMLRoot):
    """
    Explicit mapping between two regions (e.g., construct to domain, structure to UniProt, or homolog alignment)
    retaining coverage, gaps, and uncertainty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["CoordinateMapping"]
    class_class_curie: ClassVar[str] = "dufmech:CoordinateMapping"
    class_name: ClassVar[str] = "CoordinateMapping"
    class_model_uri: ClassVar[URIRef] = DUFMECH.CoordinateMapping

    mapping_id: str = None
    source_region_id: str = None
    target_region_id: str = None
    mapping_kind: Union[str, "CoordinateMappingKind"] = None
    equivalence_status: Union[str, "MappingEquivalenceStatus"] = None
    provenance_note: str = None
    overlap_residues: Optional[int] = None
    source_coverage: Optional[float] = None
    target_coverage: Optional[float] = None
    alignment_gaps: Optional[int] = None
    residue_correspondences: Optional[Union[Union[dict, ResidueCorrespondence], list[Union[dict, ResidueCorrespondence]]]] = empty_list()
    mapping_uncertainty: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mapping_id):
            self.MissingRequiredField("mapping_id")
        if not isinstance(self.mapping_id, str):
            self.mapping_id = str(self.mapping_id)

        if self._is_empty(self.source_region_id):
            self.MissingRequiredField("source_region_id")
        if not isinstance(self.source_region_id, str):
            self.source_region_id = str(self.source_region_id)

        if self._is_empty(self.target_region_id):
            self.MissingRequiredField("target_region_id")
        if not isinstance(self.target_region_id, str):
            self.target_region_id = str(self.target_region_id)

        if self._is_empty(self.mapping_kind):
            self.MissingRequiredField("mapping_kind")
        if not isinstance(self.mapping_kind, CoordinateMappingKind):
            self.mapping_kind = CoordinateMappingKind(self.mapping_kind)

        if self._is_empty(self.equivalence_status):
            self.MissingRequiredField("equivalence_status")
        if not isinstance(self.equivalence_status, MappingEquivalenceStatus):
            self.equivalence_status = MappingEquivalenceStatus(self.equivalence_status)

        if self._is_empty(self.provenance_note):
            self.MissingRequiredField("provenance_note")
        if not isinstance(self.provenance_note, str):
            self.provenance_note = str(self.provenance_note)

        if self.overlap_residues is not None and not isinstance(self.overlap_residues, int):
            self.overlap_residues = int(self.overlap_residues)

        if self.source_coverage is not None and not isinstance(self.source_coverage, float):
            self.source_coverage = float(self.source_coverage)

        if self.target_coverage is not None and not isinstance(self.target_coverage, float):
            self.target_coverage = float(self.target_coverage)

        if self.alignment_gaps is not None and not isinstance(self.alignment_gaps, int):
            self.alignment_gaps = int(self.alignment_gaps)

        self._normalize_inlined_as_list(slot_name="residue_correspondences", slot_type=ResidueCorrespondence, key_name="source_position", keyed=False)

        if self.mapping_uncertainty is not None and not isinstance(self.mapping_uncertainty, str):
            self.mapping_uncertainty = str(self.mapping_uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegionObservation(YAMLRoot):
    """
    Standardized experimental observation, curated annotation, or computational prediction anchored to a sequence
    region, separating observation from interpretation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["RegionObservation"]
    class_class_curie: ClassVar[str] = "dufmech:RegionObservation"
    class_name: ClassVar[str] = "RegionObservation"
    class_model_uri: ClassVar[URIRef] = DUFMECH.RegionObservation

    observation_id: str = None
    region_id: str = None
    sequence_id: str = None
    evidence_kind: Union[str, "EvidenceKind"] = None
    source_kind: Union[str, "ObservationSourceKind"] = None
    method: str = None
    observed_effect: str = None
    interpretation: str = None
    polarity: Union[str, "ObservationPolarity"] = None
    primary_experiment_key: str = None
    assay_conditions: Optional[str] = None
    tested_construct_region_id: Optional[str] = None
    mutation_region_ids: Optional[Union[str, list[str]]] = empty_list()
    raw_score: Optional[float] = None
    score_metric: Optional[Union[str, "ScoreMetricKind"]] = None
    derived_from_observation_ids: Optional[Union[str, list[str]]] = empty_list()
    limitations: Optional[str] = None
    evidence: Optional[Union[Union[dict, ClaimEvidence], list[Union[dict, ClaimEvidence]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_id):
            self.MissingRequiredField("observation_id")
        if not isinstance(self.observation_id, str):
            self.observation_id = str(self.observation_id)

        if self._is_empty(self.region_id):
            self.MissingRequiredField("region_id")
        if not isinstance(self.region_id, str):
            self.region_id = str(self.region_id)

        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, str):
            self.sequence_id = str(self.sequence_id)

        if self._is_empty(self.evidence_kind):
            self.MissingRequiredField("evidence_kind")
        if not isinstance(self.evidence_kind, EvidenceKind):
            self.evidence_kind = EvidenceKind(self.evidence_kind)

        if self._is_empty(self.source_kind):
            self.MissingRequiredField("source_kind")
        if not isinstance(self.source_kind, ObservationSourceKind):
            self.source_kind = ObservationSourceKind(self.source_kind)

        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, str):
            self.method = str(self.method)

        if self._is_empty(self.observed_effect):
            self.MissingRequiredField("observed_effect")
        if not isinstance(self.observed_effect, str):
            self.observed_effect = str(self.observed_effect)

        if self._is_empty(self.interpretation):
            self.MissingRequiredField("interpretation")
        if not isinstance(self.interpretation, str):
            self.interpretation = str(self.interpretation)

        if self._is_empty(self.polarity):
            self.MissingRequiredField("polarity")
        if not isinstance(self.polarity, ObservationPolarity):
            self.polarity = ObservationPolarity(self.polarity)

        if self._is_empty(self.primary_experiment_key):
            self.MissingRequiredField("primary_experiment_key")
        if not isinstance(self.primary_experiment_key, str):
            self.primary_experiment_key = str(self.primary_experiment_key)

        if self.assay_conditions is not None and not isinstance(self.assay_conditions, str):
            self.assay_conditions = str(self.assay_conditions)

        if self.tested_construct_region_id is not None and not isinstance(self.tested_construct_region_id, str):
            self.tested_construct_region_id = str(self.tested_construct_region_id)

        if not isinstance(self.mutation_region_ids, list):
            self.mutation_region_ids = [self.mutation_region_ids] if self.mutation_region_ids is not None else []
        self.mutation_region_ids = [v if isinstance(v, str) else str(v) for v in self.mutation_region_ids]

        if self.raw_score is not None and not isinstance(self.raw_score, float):
            self.raw_score = float(self.raw_score)

        if self.score_metric is not None and not isinstance(self.score_metric, ScoreMetricKind):
            self.score_metric = ScoreMetricKind(self.score_metric)

        if not isinstance(self.derived_from_observation_ids, list):
            self.derived_from_observation_ids = [self.derived_from_observation_ids] if self.derived_from_observation_ids is not None else []
        self.derived_from_observation_ids = [v if isinstance(v, str) else str(v) for v in self.derived_from_observation_ids]

        if self.limitations is not None and not isinstance(self.limitations, str):
            self.limitations = str(self.limitations)

        self._normalize_inlined_as_list(slot_name="evidence", slot_type=ClaimEvidence, key_name="reference", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceGroup(YAMLRoot):
    """
    Deduplicated group of compatible observations sharing a primary experiment or prediction source so mirrored
    records are not counted as independent confirmation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["EvidenceGroup"]
    class_class_curie: ClassVar[str] = "dufmech:EvidenceGroup"
    class_name: ClassVar[str] = "EvidenceGroup"
    class_model_uri: ClassVar[URIRef] = DUFMECH.EvidenceGroup

    group_id: str = None
    primary_experiment_key: str = None
    evidence_kind: Union[str, "EvidenceKind"] = None
    polarity: Union[str, "ObservationPolarity"] = None
    observation_ids: Union[str, list[str]] = None
    deduplication_rationale: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.group_id):
            self.MissingRequiredField("group_id")
        if not isinstance(self.group_id, str):
            self.group_id = str(self.group_id)

        if self._is_empty(self.primary_experiment_key):
            self.MissingRequiredField("primary_experiment_key")
        if not isinstance(self.primary_experiment_key, str):
            self.primary_experiment_key = str(self.primary_experiment_key)

        if self._is_empty(self.evidence_kind):
            self.MissingRequiredField("evidence_kind")
        if not isinstance(self.evidence_kind, EvidenceKind):
            self.evidence_kind = EvidenceKind(self.evidence_kind)

        if self._is_empty(self.polarity):
            self.MissingRequiredField("polarity")
        if not isinstance(self.polarity, ObservationPolarity):
            self.polarity = ObservationPolarity(self.polarity)

        if self._is_empty(self.observation_ids):
            self.MissingRequiredField("observation_ids")
        if not isinstance(self.observation_ids, list):
            self.observation_ids = [self.observation_ids] if self.observation_ids is not None else []
        self.observation_ids = [v if isinstance(v, str) else str(v) for v in self.observation_ids]

        if self._is_empty(self.deduplication_rationale):
            self.MissingRequiredField("deduplication_rationale")
        if not isinstance(self.deduplication_rationale, str):
            self.deduplication_rationale = str(self.deduplication_rationale)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SynthesizedClaim(YAMLRoot):
    """
    Evidence-graded functional claim or aspect of function at supported specificity and sequence scope, retaining
    supporting and contradicting evidence groups.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["SynthesizedClaim"]
    class_class_curie: ClassVar[str] = "dufmech:SynthesizedClaim"
    class_name: ClassVar[str] = "SynthesizedClaim"
    class_model_uri: ClassVar[URIRef] = DUFMECH.SynthesizedClaim

    claim_id: str = None
    label: str = None
    function_aspect: Union[str, "FunctionAspect"] = None
    target_region_id: str = None
    claimed_scope: Union[str, "ClaimScope"] = None
    synthesis_status: Union[str, "SynthesisStatus"] = None
    scope_rationale: str = None
    synthesis_explanation: str = None
    ontology_term_id: Optional[str] = None
    ontology_term_label: Optional[str] = None
    supporting_evidence_groups: Optional[Union[str, list[str]]] = empty_list()
    contradicting_evidence_groups: Optional[Union[str, list[str]]] = empty_list()
    supporting_observation_ids: Optional[Union[str, list[str]]] = empty_list()
    contradicting_observation_ids: Optional[Union[str, list[str]]] = empty_list()
    mapping_ids: Optional[Union[str, list[str]]] = empty_list()
    scope_transfer_blocks: Optional[Union[str, list[str]]] = empty_list()
    discriminating_experiments: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.claim_id):
            self.MissingRequiredField("claim_id")
        if not isinstance(self.claim_id, str):
            self.claim_id = str(self.claim_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.function_aspect):
            self.MissingRequiredField("function_aspect")
        if not isinstance(self.function_aspect, FunctionAspect):
            self.function_aspect = FunctionAspect(self.function_aspect)

        if self._is_empty(self.target_region_id):
            self.MissingRequiredField("target_region_id")
        if not isinstance(self.target_region_id, str):
            self.target_region_id = str(self.target_region_id)

        if self._is_empty(self.claimed_scope):
            self.MissingRequiredField("claimed_scope")
        if not isinstance(self.claimed_scope, ClaimScope):
            self.claimed_scope = ClaimScope(self.claimed_scope)

        if self._is_empty(self.synthesis_status):
            self.MissingRequiredField("synthesis_status")
        if not isinstance(self.synthesis_status, SynthesisStatus):
            self.synthesis_status = SynthesisStatus(self.synthesis_status)

        if self._is_empty(self.scope_rationale):
            self.MissingRequiredField("scope_rationale")
        if not isinstance(self.scope_rationale, str):
            self.scope_rationale = str(self.scope_rationale)

        if self._is_empty(self.synthesis_explanation):
            self.MissingRequiredField("synthesis_explanation")
        if not isinstance(self.synthesis_explanation, str):
            self.synthesis_explanation = str(self.synthesis_explanation)

        if self.ontology_term_id is not None and not isinstance(self.ontology_term_id, str):
            self.ontology_term_id = str(self.ontology_term_id)

        if self.ontology_term_label is not None and not isinstance(self.ontology_term_label, str):
            self.ontology_term_label = str(self.ontology_term_label)

        if not isinstance(self.supporting_evidence_groups, list):
            self.supporting_evidence_groups = [self.supporting_evidence_groups] if self.supporting_evidence_groups is not None else []
        self.supporting_evidence_groups = [v if isinstance(v, str) else str(v) for v in self.supporting_evidence_groups]

        if not isinstance(self.contradicting_evidence_groups, list):
            self.contradicting_evidence_groups = [self.contradicting_evidence_groups] if self.contradicting_evidence_groups is not None else []
        self.contradicting_evidence_groups = [v if isinstance(v, str) else str(v) for v in self.contradicting_evidence_groups]

        if not isinstance(self.supporting_observation_ids, list):
            self.supporting_observation_ids = [self.supporting_observation_ids] if self.supporting_observation_ids is not None else []
        self.supporting_observation_ids = [v if isinstance(v, str) else str(v) for v in self.supporting_observation_ids]

        if not isinstance(self.contradicting_observation_ids, list):
            self.contradicting_observation_ids = [self.contradicting_observation_ids] if self.contradicting_observation_ids is not None else []
        self.contradicting_observation_ids = [v if isinstance(v, str) else str(v) for v in self.contradicting_observation_ids]

        if not isinstance(self.mapping_ids, list):
            self.mapping_ids = [self.mapping_ids] if self.mapping_ids is not None else []
        self.mapping_ids = [v if isinstance(v, str) else str(v) for v in self.mapping_ids]

        if not isinstance(self.scope_transfer_blocks, list):
            self.scope_transfer_blocks = [self.scope_transfer_blocks] if self.scope_transfer_blocks is not None else []
        self.scope_transfer_blocks = [v if isinstance(v, str) else str(v) for v in self.scope_transfer_blocks]

        if not isinstance(self.discriminating_experiments, list):
            self.discriminating_experiments = [self.discriminating_experiments] if self.discriminating_experiments is not None else []
        self.discriminating_experiments = [v if isinstance(v, str) else str(v) for v in self.discriminating_experiments]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReasoningEdge(YAMLRoot):
    """
    Typed edge in a RegionReasoningGraph explicitly distinguishing coordinate mappings, evidence
    support/contradiction, and homology inferences from biological causation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DUFMECH["ReasoningEdge"]
    class_class_curie: ClassVar[str] = "dufmech:ReasoningEdge"
    class_name: ClassVar[str] = "ReasoningEdge"
    class_model_uri: ClassVar[URIRef] = DUFMECH.ReasoningEdge

    edge_id: str = None
    subject: str = None
    predicate: Union[str, "ReasoningPredicate"] = None
    object: str = None
    edge_category: Union[str, "ReasoningEdgeCategory"] = None
    support: Union[str, "CausalSupport"] = None
    evidence_kind: Union[str, "EvidenceKind"] = None
    rationale: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.edge_id):
            self.MissingRequiredField("edge_id")
        if not isinstance(self.edge_id, str):
            self.edge_id = str(self.edge_id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, ReasoningPredicate):
            self.predicate = ReasoningPredicate(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self._is_empty(self.edge_category):
            self.MissingRequiredField("edge_category")
        if not isinstance(self.edge_category, ReasoningEdgeCategory):
            self.edge_category = ReasoningEdgeCategory(self.edge_category)

        if self._is_empty(self.support):
            self.MissingRequiredField("support")
        if not isinstance(self.support, CausalSupport):
            self.support = CausalSupport(self.support)

        if self._is_empty(self.evidence_kind):
            self.MissingRequiredField("evidence_kind")
        if not isinstance(self.evidence_kind, EvidenceKind):
            self.evidence_kind = EvidenceKind(self.evidence_kind)

        if self._is_empty(self.rationale):
            self.MissingRequiredField("rationale")
        if not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

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
class CausalScope(EnumDefinitionImpl):

    MECHANISTIC = PermissibleValue(
        text="MECHANISTIC",
        description="Includes at least one directly observed experimental mechanism step.")
    PHENOTYPIC = PermissibleValue(
        text="PHENOTYPIC",
        description="Includes an experimentally observed effect without claiming a resolved molecular mechanism.")
    HYPOTHETICAL = PermissibleValue(
        text="HYPOTHETICAL",
        description="Proposed directed explanations, not observed causal effects.")

    _defn = EnumDefinition(
        name="CausalScope",
    )

class CausalNodeType(EnumDefinitionImpl):

    STATE = PermissibleValue(text="STATE")
    ACTIVITY = PermissibleValue(text="ACTIVITY")
    PROCESS = PermissibleValue(text="PROCESS")
    PERTURBATION = PermissibleValue(text="PERTURBATION")
    PHENOTYPE = PermissibleValue(text="PHENOTYPE")

    _defn = EnumDefinition(
        name="CausalNodeType",
    )

class CausalPredicate(EnumDefinitionImpl):

    increases = PermissibleValue(text="increases")
    decreases = PermissibleValue(text="decreases")
    required_for = PermissibleValue(text="required_for")
    enables = PermissibleValue(text="enables")
    produces = PermissibleValue(text="produces")
    degrades = PermissibleValue(text="degrades")
    converts_to = PermissibleValue(text="converts_to")

    _defn = EnumDefinition(
        name="CausalPredicate",
    )

class CausalDirectness(EnumDefinitionImpl):

    DIRECT = PermissibleValue(text="DIRECT")
    INDIRECT = PermissibleValue(text="INDIRECT")
    UNRESOLVED = PermissibleValue(text="UNRESOLVED")

    _defn = EnumDefinition(
        name="CausalDirectness",
    )

class CausalSupport(EnumDefinitionImpl):

    OBSERVED = PermissibleValue(text="OBSERVED")
    INFERRED = PermissibleValue(text="INFERRED")
    HYPOTHESIZED = PermissibleValue(text="HYPOTHESIZED")
    CONTESTED = PermissibleValue(text="CONTESTED")

    _defn = EnumDefinition(
        name="CausalSupport",
    )

class SeedStatus(EnumDefinitionImpl):

    UNKNOWN_CANDIDATE = PermissibleValue(text="UNKNOWN_CANDIDATE")
    KNOWN_HISTORICAL_DUF = PermissibleValue(text="KNOWN_HISTORICAL_DUF")
    EX_DUF = PermissibleValue(
        text="EX_DUF",
        description="""Pfam renamed the family away from a DUF/UPF name; its previous identifiers record the former name. Naming history, not experimental evidence.""")
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

class RegionKind(EnumDefinitionImpl):

    DOMAIN_HIT = PermissibleValue(text="DOMAIN_HIT")
    DISCONTINUOUS_DOMAIN = PermissibleValue(text="DISCONTINUOUS_DOMAIN")
    EXPERIMENTAL_CONSTRUCT = PermissibleValue(text="EXPERIMENTAL_CONSTRUCT")
    CATALYTIC_SITE = PermissibleValue(text="CATALYTIC_SITE")
    BINDING_SITE = PermissibleValue(text="BINDING_SITE")
    MUTATION_SITE = PermissibleValue(text="MUTATION_SITE")
    STRUCTURAL_OBSERVATION_REGION = PermissibleValue(text="STRUCTURAL_OBSERVATION_REGION")
    ADJACENT_ARCHITECTURAL_DOMAIN = PermissibleValue(text="ADJACENT_ARCHITECTURAL_DOMAIN")
    FULL_LENGTH_PROTEIN = PermissibleValue(text="FULL_LENGTH_PROTEIN")
    UNKNOWN_LOCALIZATION = PermissibleValue(text="UNKNOWN_LOCALIZATION")

    _defn = EnumDefinition(
        name="RegionKind",
    )

class CoordinateStatus(EnumDefinitionImpl):

    EXACT = PermissibleValue(text="EXACT")
    UNCERTAIN_BOUNDARY = PermissibleValue(text="UNCERTAIN_BOUNDARY")
    DISCONTINUOUS = PermissibleValue(text="DISCONTINUOUS")
    WHOLE_PROTEIN_UNLOCALIZED = PermissibleValue(text="WHOLE_PROTEIN_UNLOCALIZED")
    UNKNOWN_LOCALIZATION = PermissibleValue(text="UNKNOWN_LOCALIZATION")

    _defn = EnumDefinition(
        name="CoordinateStatus",
    )

class CoordinateSystem(EnumDefinitionImpl):

    UNIPROT_CANONICAL = PermissibleValue(text="UNIPROT_CANONICAL")
    UNIPROT_ISOFORM = PermissibleValue(text="UNIPROT_ISOFORM")
    CONSTRUCT_NUMBERING = PermissibleValue(text="CONSTRUCT_NUMBERING")
    MATURE_PEPTIDE = PermissibleValue(text="MATURE_PEPTIDE")
    PDB_SEQRES = PermissibleValue(text="PDB_SEQRES")
    PDB_AUTHOR = PermissibleValue(text="PDB_AUTHOR")
    HMM_PROFILE = PermissibleValue(text="HMM_PROFILE")
    ALIGNMENT_COLUMN = PermissibleValue(text="ALIGNMENT_COLUMN")
    UNSPECIFIED = PermissibleValue(text="UNSPECIFIED")

    _defn = EnumDefinition(
        name="CoordinateSystem",
    )

class CoordinateMappingKind(EnumDefinitionImpl):

    CONSTRUCT_TO_REFERENCE = PermissibleValue(text="CONSTRUCT_TO_REFERENCE")
    DOMAIN_TO_CONSTRUCT = PermissibleValue(text="DOMAIN_TO_CONSTRUCT")
    STRUCTURE_TO_UNIPROT = PermissibleValue(text="STRUCTURE_TO_UNIPROT")
    ISOFORM_TO_CANONICAL = PermissibleValue(text="ISOFORM_TO_CANONICAL")
    HOMOLOG_ALIGNMENT = PermissibleValue(text="HOMOLOG_ALIGNMENT")
    PROFILE_TO_SEQUENCE = PermissibleValue(text="PROFILE_TO_SEQUENCE")
    MUTATION_TO_DOMAIN = PermissibleValue(text="MUTATION_TO_DOMAIN")

    _defn = EnumDefinition(
        name="CoordinateMappingKind",
    )

class MappingEquivalenceStatus(EnumDefinitionImpl):

    EXACT_MATCH = PermissibleValue(text="EXACT_MATCH")
    CONSTRUCT_CONTAINS_DOMAIN = PermissibleValue(text="CONSTRUCT_CONTAINS_DOMAIN")
    DOMAIN_CONTAINS_REGION = PermissibleValue(text="DOMAIN_CONTAINS_REGION")
    RESIDUE_INSIDE_REGION = PermissibleValue(text="RESIDUE_INSIDE_REGION")
    PARTIAL_OVERLAP_NOT_EQUIVALENT = PermissibleValue(text="PARTIAL_OVERLAP_NOT_EQUIVALENT")
    DISJOINT_OUTSIDE_REGION = PermissibleValue(text="DISJOINT_OUTSIDE_REGION")
    DISCONTINUOUS_MAPPING = PermissibleValue(text="DISCONTINUOUS_MAPPING")
    SEQUENCE_VERSION_MISMATCH = PermissibleValue(text="SEQUENCE_VERSION_MISMATCH")
    UNRESOLVED_MAPPING = PermissibleValue(text="UNRESOLVED_MAPPING")

    _defn = EnumDefinition(
        name="MappingEquivalenceStatus",
    )

class ObservationSourceKind(EnumDefinitionImpl):

    LITERATURE_ASSAY = PermissibleValue(text="LITERATURE_ASSAY")
    PDBE_KB = PermissibleValue(text="PDBE_KB")
    INTERPRO_PFAM = PermissibleValue(text="INTERPRO_PFAM")
    CDSEARCH = PermissibleValue(text="CDSEARCH")
    CATH_FUNFAM = PermissibleValue(text="CATH_FUNFAM")
    NCBIFAM = PermissibleValue(text="NCBIFAM")
    QUICKGO = PermissibleValue(text="QUICKGO")
    RHEA = PermissibleValue(text="RHEA")
    ALPHAFOLD = PermissibleValue(text="ALPHAFOLD")
    CURATED_ANNOTATION = PermissibleValue(text="CURATED_ANNOTATION")

    _defn = EnumDefinition(
        name="ObservationSourceKind",
    )

class ObservationPolarity(EnumDefinitionImpl):

    POSITIVE = PermissibleValue(text="POSITIVE")
    NEGATIVE = PermissibleValue(text="NEGATIVE")
    NEUTRAL_OR_UNCHANGED = PermissibleValue(text="NEUTRAL_OR_UNCHANGED")

    _defn = EnumDefinition(
        name="ObservationPolarity",
    )

class ScoreMetricKind(EnumDefinitionImpl):

    E_VALUE = PermissibleValue(text="E_VALUE")
    BITSCORE = PermissibleValue(text="BITSCORE")
    CATH_CONFIDENCE = PermissibleValue(text="CATH_CONFIDENCE")
    PLDDT = PermissibleValue(text="PLDDT")
    KM_MM = PermissibleValue(text="KM_MM")
    KCAT_PER_S = PermissibleValue(text="KCAT_PER_S")
    QUALITATIVE = PermissibleValue(text="QUALITATIVE")

    _defn = EnumDefinition(
        name="ScoreMetricKind",
    )

class FunctionAspect(EnumDefinitionImpl):

    CATALYTIC_ACTIVITY = PermissibleValue(text="CATALYTIC_ACTIVITY")
    SUBSTRATE_SPECIFICITY = PermissibleValue(text="SUBSTRATE_SPECIFICITY")
    COFACTOR_BINDING = PermissibleValue(text="COFACTOR_BINDING")
    LIGAND_BINDING = PermissibleValue(text="LIGAND_BINDING")
    PROTEIN_INTERACTION = PermissibleValue(text="PROTEIN_INTERACTION")
    SUBCELLULAR_LOCALIZATION = PermissibleValue(text="SUBCELLULAR_LOCALIZATION")
    PROCESS_CONTRIBUTION = PermissibleValue(text="PROCESS_CONTRIBUTION")
    STRUCTURAL_ROLE = PermissibleValue(text="STRUCTURAL_ROLE")
    ARCHITECTURAL_COOCCURRENCE = PermissibleValue(text="ARCHITECTURAL_COOCCURRENCE")
    UNKNOWN_FUNCTION = PermissibleValue(text="UNKNOWN_FUNCTION")

    _defn = EnumDefinition(
        name="FunctionAspect",
    )

class ClaimScope(EnumDefinitionImpl):

    TESTED_REGION_ONLY = PermissibleValue(text="TESTED_REGION_ONLY")
    TESTED_CONSTRUCT = PermissibleValue(text="TESTED_CONSTRUCT")
    SPECIFIC_PROTEIN = PermissibleValue(text="SPECIFIC_PROTEIN")
    CONSERVED_SUBFAMILY = PermissibleValue(text="CONSERVED_SUBFAMILY")
    FAMILY_WIDE = PermissibleValue(text="FAMILY_WIDE")
    UNRESOLVED_SCOPE = PermissibleValue(text="UNRESOLVED_SCOPE")

    _defn = EnumDefinition(
        name="ClaimScope",
    )

class SynthesisStatus(EnumDefinitionImpl):

    EXPERIMENTALLY_DEMONSTRATED = PermissibleValue(text="EXPERIMENTALLY_DEMONSTRATED")
    SUPPORTED_INFERENCE = PermissibleValue(text="SUPPORTED_INFERENCE")
    COMPUTATIONAL_HYPOTHESIS = PermissibleValue(text="COMPUTATIONAL_HYPOTHESIS")
    CONFLICTING_UNRESOLVED = PermissibleValue(text="CONFLICTING_UNRESOLVED")
    INSUFFICIENT_EVIDENCE = PermissibleValue(text="INSUFFICIENT_EVIDENCE")
    NEGATIVE_EVIDENCE_ONLY = PermissibleValue(text="NEGATIVE_EVIDENCE_ONLY")

    _defn = EnumDefinition(
        name="SynthesisStatus",
    )

class ReasoningEdgeCategory(EnumDefinitionImpl):

    EVIDENCE_LINK = PermissibleValue(text="EVIDENCE_LINK")
    COORDINATE_MAPPING_LINK = PermissibleValue(text="COORDINATE_MAPPING_LINK")
    INFERENCE_LINK = PermissibleValue(text="INFERENCE_LINK")
    CAUSAL_BIOLOGICAL_LINK = PermissibleValue(text="CAUSAL_BIOLOGICAL_LINK")

    _defn = EnumDefinition(
        name="ReasoningEdgeCategory",
    )

class ReasoningPredicate(EnumDefinitionImpl):

    anchored_to_sequence = PermissibleValue(text="anchored_to_sequence")
    maps_to_region = PermissibleValue(text="maps_to_region")
    observed_on_region = PermissibleValue(text="observed_on_region")
    grouped_into_evidence_unit = PermissibleValue(text="grouped_into_evidence_unit")
    supports_claim = PermissibleValue(text="supports_claim")
    contradicts_claim = PermissibleValue(text="contradicts_claim")
    constrains_claim_scope = PermissibleValue(text="constrains_claim_scope")
    inferred_from_homolog_region = PermissibleValue(text="inferred_from_homolog_region")
    cooccurs_with_domain = PermissibleValue(text="cooccurs_with_domain")
    enables_biological_activity = PermissibleValue(text="enables_biological_activity")
    produces_metabolite = PermissibleValue(text="produces_metabolite")
    degrades_substrate = PermissibleValue(text="degrades_substrate")
    required_for_process = PermissibleValue(text="required_for_process")

    _defn = EnumDefinition(
        name="ReasoningPredicate",
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
                   pattern=re.compile(r'^(reports/yaml_record_review/[A-Za-z0-9_.-]+[.]md|reviews/structured/[A-Za-z0-9][A-Za-z0-9._-]{0,159}/review[.]yaml)$'))

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

slots.familyRecord__causal_graphs = Slot(uri=DUFMECH.causal_graphs, name="familyRecord__causal_graphs", curie=DUFMECH.curie('causal_graphs'),
                   model_uri=DUFMECH.familyRecord__causal_graphs, domain=None, range=Optional[Union[Union[dict, CausalGraph], list[Union[dict, CausalGraph]]]])

slots.familyRecord__discussions = Slot(uri=DUFMECH.discussions, name="familyRecord__discussions", curie=DUFMECH.curie('discussions'),
                   model_uri=DUFMECH.familyRecord__discussions, domain=None, range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]])

slots.familyRecord__datasets = Slot(uri=DUFMECH.datasets, name="familyRecord__datasets", curie=DUFMECH.curie('datasets'),
                   model_uri=DUFMECH.familyRecord__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.familyRecord__cross_corpus_links = Slot(uri=DUFMECH.cross_corpus_links, name="familyRecord__cross_corpus_links", curie=DUFMECH.curie('cross_corpus_links'),
                   model_uri=DUFMECH.familyRecord__cross_corpus_links, domain=None, range=Optional[Union[Union[dict, CrossCorpusLink], list[Union[dict, CrossCorpusLink]]]])

slots.familyRecord__sequence_reasoning_graphs = Slot(uri=DUFMECH.sequence_reasoning_graphs, name="familyRecord__sequence_reasoning_graphs", curie=DUFMECH.curie('sequence_reasoning_graphs'),
                   model_uri=DUFMECH.familyRecord__sequence_reasoning_graphs, domain=None, range=Optional[Union[Union[dict, RegionReasoningGraph], list[Union[dict, RegionReasoningGraph]]]])

slots.familyCuration__pfam_id = Slot(uri=DUFMECH.pfam_id, name="familyCuration__pfam_id", curie=DUFMECH.curie('pfam_id'),
                   model_uri=DUFMECH.familyCuration__pfam_id, domain=None, range=str,
                   pattern=re.compile(r'^PF[0-9]{5}$'))

slots.familyCuration__curation_status = Slot(uri=DUFMECH.curation_status, name="familyCuration__curation_status", curie=DUFMECH.curie('curation_status'),
                   model_uri=DUFMECH.familyCuration__curation_status, domain=None, range=Union[str, "CurationStatus"])

slots.familyCuration__review_id = Slot(uri=DUFMECH.review_id, name="familyCuration__review_id", curie=DUFMECH.curie('review_id'),
                   model_uri=DUFMECH.familyCuration__review_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(reports/yaml_record_review/[A-Za-z0-9_.-]+[.]md|reviews/structured/[A-Za-z0-9][A-Za-z0-9._-]{0,159}/review[.]yaml)$'))

slots.familyCuration__curation_history = Slot(uri=DUFMECH.curation_history, name="familyCuration__curation_history", curie=DUFMECH.curie('curation_history'),
                   model_uri=DUFMECH.familyCuration__curation_history, domain=None, range=Optional[str],
                   pattern=re.compile(r'^history/records/PF[0-9]{5}$'))

slots.familyCuration__assertions = Slot(uri=DUFMECH.assertions, name="familyCuration__assertions", curie=DUFMECH.curie('assertions'),
                   model_uri=DUFMECH.familyCuration__assertions, domain=None, range=Optional[Union[Union[dict, FunctionalAssertion], list[Union[dict, FunctionalAssertion]]]])

slots.familyCuration__causal_graphs = Slot(uri=DUFMECH.causal_graphs, name="familyCuration__causal_graphs", curie=DUFMECH.curie('causal_graphs'),
                   model_uri=DUFMECH.familyCuration__causal_graphs, domain=None, range=Optional[Union[Union[dict, CausalGraph], list[Union[dict, CausalGraph]]]])

slots.familyCuration__discussions = Slot(uri=DUFMECH.discussions, name="familyCuration__discussions", curie=DUFMECH.curie('discussions'),
                   model_uri=DUFMECH.familyCuration__discussions, domain=None, range=Optional[Union[Union[dict, Discussion], list[Union[dict, Discussion]]]])

slots.familyCuration__datasets = Slot(uri=DUFMECH.datasets, name="familyCuration__datasets", curie=DUFMECH.curie('datasets'),
                   model_uri=DUFMECH.familyCuration__datasets, domain=None, range=Optional[Union[Union[dict, Dataset], list[Union[dict, Dataset]]]])

slots.familyCuration__cross_corpus_links = Slot(uri=DUFMECH.cross_corpus_links, name="familyCuration__cross_corpus_links", curie=DUFMECH.curie('cross_corpus_links'),
                   model_uri=DUFMECH.familyCuration__cross_corpus_links, domain=None, range=Optional[Union[Union[dict, CrossCorpusLink], list[Union[dict, CrossCorpusLink]]]])

slots.familyCuration__sequence_reasoning_graphs = Slot(uri=DUFMECH.sequence_reasoning_graphs, name="familyCuration__sequence_reasoning_graphs", curie=DUFMECH.curie('sequence_reasoning_graphs'),
                   model_uri=DUFMECH.familyCuration__sequence_reasoning_graphs, domain=None, range=Optional[Union[Union[dict, RegionReasoningGraph], list[Union[dict, RegionReasoningGraph]]]])

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

slots.functionalAssertion__sequence_id = Slot(uri=DUFMECH.sequence_id, name="functionalAssertion__sequence_id", curie=DUFMECH.curie('sequence_id'),
                   model_uri=DUFMECH.functionalAssertion__sequence_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.functionalAssertion__region_id = Slot(uri=DUFMECH.region_id, name="functionalAssertion__region_id", curie=DUFMECH.curie('region_id'),
                   model_uri=DUFMECH.functionalAssertion__region_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.functionalAssertion__synthesized_claim_id = Slot(uri=DUFMECH.synthesized_claim_id, name="functionalAssertion__synthesized_claim_id", curie=DUFMECH.curie('synthesized_claim_id'),
                   model_uri=DUFMECH.functionalAssertion__synthesized_claim_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.functionalAssertion__evidence = Slot(uri=DUFMECH.evidence, name="functionalAssertion__evidence", curie=DUFMECH.curie('evidence'),
                   model_uri=DUFMECH.functionalAssertion__evidence, domain=None, range=Union[Union[dict, ClaimEvidence], list[Union[dict, ClaimEvidence]]])

slots.causalGraph__graph_id = Slot(uri=DUFMECH.graph_id, name="causalGraph__graph_id", curie=DUFMECH.curie('graph_id'),
                   model_uri=DUFMECH.causalGraph__graph_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.causalGraph__title = Slot(uri=DUFMECH.title, name="causalGraph__title", curie=DUFMECH.curie('title'),
                   model_uri=DUFMECH.causalGraph__title, domain=None, range=str)

slots.causalGraph__scope = Slot(uri=DUFMECH.scope, name="causalGraph__scope", curie=DUFMECH.curie('scope'),
                   model_uri=DUFMECH.causalGraph__scope, domain=None, range=str)

slots.causalGraph__context = Slot(uri=DUFMECH.context, name="causalGraph__context", curie=DUFMECH.curie('context'),
                   model_uri=DUFMECH.causalGraph__context, domain=None, range=str)

slots.causalGraph__family_mapping = Slot(uri=DUFMECH.family_mapping, name="causalGraph__family_mapping", curie=DUFMECH.curie('family_mapping'),
                   model_uri=DUFMECH.causalGraph__family_mapping, domain=None, range=str)

slots.causalGraph__scope_status = Slot(uri=DUFMECH.scope_status, name="causalGraph__scope_status", curie=DUFMECH.curie('scope_status'),
                   model_uri=DUFMECH.causalGraph__scope_status, domain=None, range=Union[str, "CausalScope"])

slots.causalGraph__taxon = Slot(uri=DUFMECH.taxon, name="causalGraph__taxon", curie=DUFMECH.curie('taxon'),
                   model_uri=DUFMECH.causalGraph__taxon, domain=None, range=Optional[str],
                   pattern=re.compile(r'^NCBITaxon:[0-9]+$'))

slots.causalGraph__limitations = Slot(uri=DUFMECH.limitations, name="causalGraph__limitations", curie=DUFMECH.curie('limitations'),
                   model_uri=DUFMECH.causalGraph__limitations, domain=None, range=str)

slots.causalGraph__feedback_explanation = Slot(uri=DUFMECH.feedback_explanation, name="causalGraph__feedback_explanation", curie=DUFMECH.curie('feedback_explanation'),
                   model_uri=DUFMECH.causalGraph__feedback_explanation, domain=None, range=Optional[str])

slots.causalGraph__nodes = Slot(uri=DUFMECH.nodes, name="causalGraph__nodes", curie=DUFMECH.curie('nodes'),
                   model_uri=DUFMECH.causalGraph__nodes, domain=None, range=Union[Union[dict, CausalNode], list[Union[dict, CausalNode]]])

slots.causalGraph__edges = Slot(uri=DUFMECH.edges, name="causalGraph__edges", curie=DUFMECH.curie('edges'),
                   model_uri=DUFMECH.causalGraph__edges, domain=None, range=Union[Union[dict, CausalEdge], list[Union[dict, CausalEdge]]])

slots.causalNode__node_id = Slot(uri=DUFMECH.node_id, name="causalNode__node_id", curie=DUFMECH.curie('node_id'),
                   model_uri=DUFMECH.causalNode__node_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.causalNode__label = Slot(uri=DUFMECH.label, name="causalNode__label", curie=DUFMECH.curie('label'),
                   model_uri=DUFMECH.causalNode__label, domain=None, range=str)

slots.causalNode__node_type = Slot(uri=DUFMECH.node_type, name="causalNode__node_type", curie=DUFMECH.curie('node_type'),
                   model_uri=DUFMECH.causalNode__node_type, domain=None, range=Union[str, "CausalNodeType"])

slots.causalNode__grounding = Slot(uri=DUFMECH.grounding, name="causalNode__grounding", curie=DUFMECH.curie('grounding'),
                   model_uri=DUFMECH.causalNode__grounding, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z][A-Za-z0-9_.-]*:\S+$'))

slots.causalNode__sequence_id = Slot(uri=DUFMECH.sequence_id, name="causalNode__sequence_id", curie=DUFMECH.curie('sequence_id'),
                   model_uri=DUFMECH.causalNode__sequence_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.causalNode__region_id = Slot(uri=DUFMECH.region_id, name="causalNode__region_id", curie=DUFMECH.curie('region_id'),
                   model_uri=DUFMECH.causalNode__region_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.causalEdge__edge_id = Slot(uri=DUFMECH.edge_id, name="causalEdge__edge_id", curie=DUFMECH.curie('edge_id'),
                   model_uri=DUFMECH.causalEdge__edge_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.causalEdge__subject = Slot(uri=DUFMECH.subject, name="causalEdge__subject", curie=DUFMECH.curie('subject'),
                   model_uri=DUFMECH.causalEdge__subject, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.causalEdge__predicate = Slot(uri=DUFMECH.predicate, name="causalEdge__predicate", curie=DUFMECH.curie('predicate'),
                   model_uri=DUFMECH.causalEdge__predicate, domain=None, range=Union[str, "CausalPredicate"])

slots.causalEdge__object = Slot(uri=DUFMECH.object, name="causalEdge__object", curie=DUFMECH.curie('object'),
                   model_uri=DUFMECH.causalEdge__object, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.causalEdge__mechanism = Slot(uri=DUFMECH.mechanism, name="causalEdge__mechanism", curie=DUFMECH.curie('mechanism'),
                   model_uri=DUFMECH.causalEdge__mechanism, domain=None, range=str)

slots.causalEdge__directness = Slot(uri=DUFMECH.directness, name="causalEdge__directness", curie=DUFMECH.curie('directness'),
                   model_uri=DUFMECH.causalEdge__directness, domain=None, range=Union[str, "CausalDirectness"])

slots.causalEdge__support = Slot(uri=DUFMECH.support, name="causalEdge__support", curie=DUFMECH.curie('support'),
                   model_uri=DUFMECH.causalEdge__support, domain=None, range=Union[str, "CausalSupport"])

slots.causalEdge__evidence_kind = Slot(uri=DUFMECH.evidence_kind, name="causalEdge__evidence_kind", curie=DUFMECH.curie('evidence_kind'),
                   model_uri=DUFMECH.causalEdge__evidence_kind, domain=None, range=Union[str, "EvidenceKind"])

slots.causalEdge__evidence = Slot(uri=DUFMECH.evidence, name="causalEdge__evidence", curie=DUFMECH.curie('evidence'),
                   model_uri=DUFMECH.causalEdge__evidence, domain=None, range=Union[Union[dict, ClaimEvidence], list[Union[dict, ClaimEvidence]]])

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

slots.regionReasoningGraph__graph_id = Slot(uri=DUFMECH.graph_id, name="regionReasoningGraph__graph_id", curie=DUFMECH.curie('graph_id'),
                   model_uri=DUFMECH.regionReasoningGraph__graph_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.regionReasoningGraph__pfam_id = Slot(uri=DUFMECH.pfam_id, name="regionReasoningGraph__pfam_id", curie=DUFMECH.curie('pfam_id'),
                   model_uri=DUFMECH.regionReasoningGraph__pfam_id, domain=None, range=str,
                   pattern=re.compile(r'^PF[0-9]{5}$'))

slots.regionReasoningGraph__title = Slot(uri=DUFMECH.title, name="regionReasoningGraph__title", curie=DUFMECH.curie('title'),
                   model_uri=DUFMECH.regionReasoningGraph__title, domain=None, range=str)

slots.regionReasoningGraph__description = Slot(uri=DUFMECH.description, name="regionReasoningGraph__description", curie=DUFMECH.curie('description'),
                   model_uri=DUFMECH.regionReasoningGraph__description, domain=None, range=Optional[str])

slots.regionReasoningGraph__sequences = Slot(uri=DUFMECH.sequences, name="regionReasoningGraph__sequences", curie=DUFMECH.curie('sequences'),
                   model_uri=DUFMECH.regionReasoningGraph__sequences, domain=None, range=Union[Union[dict, SequenceIdentity], list[Union[dict, SequenceIdentity]]])

slots.regionReasoningGraph__regions = Slot(uri=DUFMECH.regions, name="regionReasoningGraph__regions", curie=DUFMECH.curie('regions'),
                   model_uri=DUFMECH.regionReasoningGraph__regions, domain=None, range=Union[Union[dict, SequenceRegion], list[Union[dict, SequenceRegion]]])

slots.regionReasoningGraph__coordinate_mappings = Slot(uri=DUFMECH.coordinate_mappings, name="regionReasoningGraph__coordinate_mappings", curie=DUFMECH.curie('coordinate_mappings'),
                   model_uri=DUFMECH.regionReasoningGraph__coordinate_mappings, domain=None, range=Optional[Union[Union[dict, CoordinateMapping], list[Union[dict, CoordinateMapping]]]])

slots.regionReasoningGraph__observations = Slot(uri=DUFMECH.observations, name="regionReasoningGraph__observations", curie=DUFMECH.curie('observations'),
                   model_uri=DUFMECH.regionReasoningGraph__observations, domain=None, range=Union[Union[dict, RegionObservation], list[Union[dict, RegionObservation]]])

slots.regionReasoningGraph__evidence_groups = Slot(uri=DUFMECH.evidence_groups, name="regionReasoningGraph__evidence_groups", curie=DUFMECH.curie('evidence_groups'),
                   model_uri=DUFMECH.regionReasoningGraph__evidence_groups, domain=None, range=Optional[Union[Union[dict, EvidenceGroup], list[Union[dict, EvidenceGroup]]]])

slots.regionReasoningGraph__synthesized_claims = Slot(uri=DUFMECH.synthesized_claims, name="regionReasoningGraph__synthesized_claims", curie=DUFMECH.curie('synthesized_claims'),
                   model_uri=DUFMECH.regionReasoningGraph__synthesized_claims, domain=None, range=Union[Union[dict, SynthesizedClaim], list[Union[dict, SynthesizedClaim]]])

slots.regionReasoningGraph__reasoning_edges = Slot(uri=DUFMECH.reasoning_edges, name="regionReasoningGraph__reasoning_edges", curie=DUFMECH.curie('reasoning_edges'),
                   model_uri=DUFMECH.regionReasoningGraph__reasoning_edges, domain=None, range=Union[Union[dict, ReasoningEdge], list[Union[dict, ReasoningEdge]]])

slots.regionReasoningGraph__causal_graph_refs = Slot(uri=DUFMECH.causal_graph_refs, name="regionReasoningGraph__causal_graph_refs", curie=DUFMECH.curie('causal_graph_refs'),
                   model_uri=DUFMECH.regionReasoningGraph__causal_graph_refs, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_-]+$'))

slots.sequenceIdentity__sequence_id = Slot(uri=DUFMECH.sequence_id, name="sequenceIdentity__sequence_id", curie=DUFMECH.curie('sequence_id'),
                   model_uri=DUFMECH.sequenceIdentity__sequence_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.sequenceIdentity__uniprot_accession = Slot(uri=DUFMECH.uniprot_accession, name="sequenceIdentity__uniprot_accession", curie=DUFMECH.curie('uniprot_accession'),
                   model_uri=DUFMECH.sequenceIdentity__uniprot_accession, domain=None, range=str,
                   pattern=re.compile(r'^([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$'))

slots.sequenceIdentity__isoform = Slot(uri=DUFMECH.isoform, name="sequenceIdentity__isoform", curie=DUFMECH.curie('isoform'),
                   model_uri=DUFMECH.sequenceIdentity__isoform, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})-[0-9]+$'))

slots.sequenceIdentity__sequence_version = Slot(uri=DUFMECH.sequence_version, name="sequenceIdentity__sequence_version", curie=DUFMECH.curie('sequence_version'),
                   model_uri=DUFMECH.sequenceIdentity__sequence_version, domain=None, range=Optional[int])

slots.sequenceIdentity__sequence_length = Slot(uri=DUFMECH.sequence_length, name="sequenceIdentity__sequence_length", curie=DUFMECH.curie('sequence_length'),
                   model_uri=DUFMECH.sequenceIdentity__sequence_length, domain=None, range=int)

slots.sequenceIdentity__sequence_sha256 = Slot(uri=DUFMECH.sequence_sha256, name="sequenceIdentity__sequence_sha256", curie=DUFMECH.curie('sequence_sha256'),
                   model_uri=DUFMECH.sequenceIdentity__sequence_sha256, domain=None, range=str,
                   pattern=re.compile(r'^[a-f0-9]{64}$'))

slots.sequenceIdentity__sequence_md5 = Slot(uri=DUFMECH.sequence_md5, name="sequenceIdentity__sequence_md5", curie=DUFMECH.curie('sequence_md5'),
                   model_uri=DUFMECH.sequenceIdentity__sequence_md5, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{32}$'))

slots.sequenceIdentity__taxon_id = Slot(uri=DUFMECH.taxon_id, name="sequenceIdentity__taxon_id", curie=DUFMECH.curie('taxon_id'),
                   model_uri=DUFMECH.sequenceIdentity__taxon_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^NCBITaxon:[0-9]+$'))

slots.sequenceIdentity__organism = Slot(uri=DUFMECH.organism, name="sequenceIdentity__organism", curie=DUFMECH.curie('organism'),
                   model_uri=DUFMECH.sequenceIdentity__organism, domain=None, range=Optional[str])

slots.sequenceIdentity__uniprot_release = Slot(uri=DUFMECH.uniprot_release, name="sequenceIdentity__uniprot_release", curie=DUFMECH.curie('uniprot_release'),
                   model_uri=DUFMECH.sequenceIdentity__uniprot_release, domain=None, range=Optional[str])

slots.sequenceIdentity__source_url = Slot(uri=DUFMECH.source_url, name="sequenceIdentity__source_url", curie=DUFMECH.curie('source_url'),
                   model_uri=DUFMECH.sequenceIdentity__source_url, domain=None, range=Optional[Union[str, URI]])

slots.sequenceInterval__start = Slot(uri=DUFMECH.start, name="sequenceInterval__start", curie=DUFMECH.curie('start'),
                   model_uri=DUFMECH.sequenceInterval__start, domain=None, range=int)

slots.sequenceInterval__end = Slot(uri=DUFMECH.end, name="sequenceInterval__end", curie=DUFMECH.curie('end'),
                   model_uri=DUFMECH.sequenceInterval__end, domain=None, range=int)

slots.sequenceInterval__start_uncertain = Slot(uri=DUFMECH.start_uncertain, name="sequenceInterval__start_uncertain", curie=DUFMECH.curie('start_uncertain'),
                   model_uri=DUFMECH.sequenceInterval__start_uncertain, domain=None, range=Optional[Union[bool, Bool]])

slots.sequenceInterval__end_uncertain = Slot(uri=DUFMECH.end_uncertain, name="sequenceInterval__end_uncertain", curie=DUFMECH.curie('end_uncertain'),
                   model_uri=DUFMECH.sequenceInterval__end_uncertain, domain=None, range=Optional[Union[bool, Bool]])

slots.sequenceInterval__residue_identity = Slot(uri=DUFMECH.residue_identity, name="sequenceInterval__residue_identity", curie=DUFMECH.curie('residue_identity'),
                   model_uri=DUFMECH.sequenceInterval__residue_identity, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]+$'))

slots.sequenceRegion__region_id = Slot(uri=DUFMECH.region_id, name="sequenceRegion__region_id", curie=DUFMECH.curie('region_id'),
                   model_uri=DUFMECH.sequenceRegion__region_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.sequenceRegion__sequence_id = Slot(uri=DUFMECH.sequence_id, name="sequenceRegion__sequence_id", curie=DUFMECH.curie('sequence_id'),
                   model_uri=DUFMECH.sequenceRegion__sequence_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.sequenceRegion__label = Slot(uri=DUFMECH.label, name="sequenceRegion__label", curie=DUFMECH.curie('label'),
                   model_uri=DUFMECH.sequenceRegion__label, domain=None, range=str)

slots.sequenceRegion__region_kind = Slot(uri=DUFMECH.region_kind, name="sequenceRegion__region_kind", curie=DUFMECH.curie('region_kind'),
                   model_uri=DUFMECH.sequenceRegion__region_kind, domain=None, range=Union[str, "RegionKind"])

slots.sequenceRegion__coordinate_status = Slot(uri=DUFMECH.coordinate_status, name="sequenceRegion__coordinate_status", curie=DUFMECH.curie('coordinate_status'),
                   model_uri=DUFMECH.sequenceRegion__coordinate_status, domain=None, range=Union[str, "CoordinateStatus"])

slots.sequenceRegion__intervals = Slot(uri=DUFMECH.intervals, name="sequenceRegion__intervals", curie=DUFMECH.curie('intervals'),
                   model_uri=DUFMECH.sequenceRegion__intervals, domain=None, range=Optional[Union[Union[dict, SequenceInterval], list[Union[dict, SequenceInterval]]]])

slots.sequenceRegion__source_coordinate_system = Slot(uri=DUFMECH.source_coordinate_system, name="sequenceRegion__source_coordinate_system", curie=DUFMECH.curie('source_coordinate_system'),
                   model_uri=DUFMECH.sequenceRegion__source_coordinate_system, domain=None, range=Union[str, "CoordinateSystem"])

slots.sequenceRegion__source_coordinates_text = Slot(uri=DUFMECH.source_coordinates_text, name="sequenceRegion__source_coordinates_text", curie=DUFMECH.curie('source_coordinates_text'),
                   model_uri=DUFMECH.sequenceRegion__source_coordinates_text, domain=None, range=Optional[str])

slots.sequenceRegion__conversion_provenance = Slot(uri=DUFMECH.conversion_provenance, name="sequenceRegion__conversion_provenance", curie=DUFMECH.curie('conversion_provenance'),
                   model_uri=DUFMECH.sequenceRegion__conversion_provenance, domain=None, range=Optional[str])

slots.sequenceRegion__pfam_id = Slot(uri=DUFMECH.pfam_id, name="sequenceRegion__pfam_id", curie=DUFMECH.curie('pfam_id'),
                   model_uri=DUFMECH.sequenceRegion__pfam_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^PF[0-9]{5}$'))

slots.sequenceRegion__interpro_id = Slot(uri=DUFMECH.interpro_id, name="sequenceRegion__interpro_id", curie=DUFMECH.curie('interpro_id'),
                   model_uri=DUFMECH.sequenceRegion__interpro_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^InterPro:IPR[0-9]{6}$'))

slots.residueCorrespondence__source_position = Slot(uri=DUFMECH.source_position, name="residueCorrespondence__source_position", curie=DUFMECH.curie('source_position'),
                   model_uri=DUFMECH.residueCorrespondence__source_position, domain=None, range=int)

slots.residueCorrespondence__source_residue = Slot(uri=DUFMECH.source_residue, name="residueCorrespondence__source_residue", curie=DUFMECH.curie('source_residue'),
                   model_uri=DUFMECH.residueCorrespondence__source_residue, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]$'))

slots.residueCorrespondence__target_position = Slot(uri=DUFMECH.target_position, name="residueCorrespondence__target_position", curie=DUFMECH.curie('target_position'),
                   model_uri=DUFMECH.residueCorrespondence__target_position, domain=None, range=int)

slots.residueCorrespondence__target_residue = Slot(uri=DUFMECH.target_residue, name="residueCorrespondence__target_residue", curie=DUFMECH.curie('target_residue'),
                   model_uri=DUFMECH.residueCorrespondence__target_residue, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z]$'))

slots.residueCorrespondence__pdb_insertion_code = Slot(uri=DUFMECH.pdb_insertion_code, name="residueCorrespondence__pdb_insertion_code", curie=DUFMECH.curie('pdb_insertion_code'),
                   model_uri=DUFMECH.residueCorrespondence__pdb_insertion_code, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9]$'))

slots.residueCorrespondence__mutation_substitution = Slot(uri=DUFMECH.mutation_substitution, name="residueCorrespondence__mutation_substitution", curie=DUFMECH.curie('mutation_substitution'),
                   model_uri=DUFMECH.residueCorrespondence__mutation_substitution, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z][0-9]+[A-Z*]$'))

slots.residueCorrespondence__note = Slot(uri=DUFMECH.note, name="residueCorrespondence__note", curie=DUFMECH.curie('note'),
                   model_uri=DUFMECH.residueCorrespondence__note, domain=None, range=Optional[str])

slots.coordinateMapping__mapping_id = Slot(uri=DUFMECH.mapping_id, name="coordinateMapping__mapping_id", curie=DUFMECH.curie('mapping_id'),
                   model_uri=DUFMECH.coordinateMapping__mapping_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.coordinateMapping__source_region_id = Slot(uri=DUFMECH.source_region_id, name="coordinateMapping__source_region_id", curie=DUFMECH.curie('source_region_id'),
                   model_uri=DUFMECH.coordinateMapping__source_region_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.coordinateMapping__target_region_id = Slot(uri=DUFMECH.target_region_id, name="coordinateMapping__target_region_id", curie=DUFMECH.curie('target_region_id'),
                   model_uri=DUFMECH.coordinateMapping__target_region_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.coordinateMapping__mapping_kind = Slot(uri=DUFMECH.mapping_kind, name="coordinateMapping__mapping_kind", curie=DUFMECH.curie('mapping_kind'),
                   model_uri=DUFMECH.coordinateMapping__mapping_kind, domain=None, range=Union[str, "CoordinateMappingKind"])

slots.coordinateMapping__equivalence_status = Slot(uri=DUFMECH.equivalence_status, name="coordinateMapping__equivalence_status", curie=DUFMECH.curie('equivalence_status'),
                   model_uri=DUFMECH.coordinateMapping__equivalence_status, domain=None, range=Union[str, "MappingEquivalenceStatus"])

slots.coordinateMapping__overlap_residues = Slot(uri=DUFMECH.overlap_residues, name="coordinateMapping__overlap_residues", curie=DUFMECH.curie('overlap_residues'),
                   model_uri=DUFMECH.coordinateMapping__overlap_residues, domain=None, range=Optional[int])

slots.coordinateMapping__source_coverage = Slot(uri=DUFMECH.source_coverage, name="coordinateMapping__source_coverage", curie=DUFMECH.curie('source_coverage'),
                   model_uri=DUFMECH.coordinateMapping__source_coverage, domain=None, range=Optional[float])

slots.coordinateMapping__target_coverage = Slot(uri=DUFMECH.target_coverage, name="coordinateMapping__target_coverage", curie=DUFMECH.curie('target_coverage'),
                   model_uri=DUFMECH.coordinateMapping__target_coverage, domain=None, range=Optional[float])

slots.coordinateMapping__alignment_gaps = Slot(uri=DUFMECH.alignment_gaps, name="coordinateMapping__alignment_gaps", curie=DUFMECH.curie('alignment_gaps'),
                   model_uri=DUFMECH.coordinateMapping__alignment_gaps, domain=None, range=Optional[int])

slots.coordinateMapping__residue_correspondences = Slot(uri=DUFMECH.residue_correspondences, name="coordinateMapping__residue_correspondences", curie=DUFMECH.curie('residue_correspondences'),
                   model_uri=DUFMECH.coordinateMapping__residue_correspondences, domain=None, range=Optional[Union[Union[dict, ResidueCorrespondence], list[Union[dict, ResidueCorrespondence]]]])

slots.coordinateMapping__mapping_uncertainty = Slot(uri=DUFMECH.mapping_uncertainty, name="coordinateMapping__mapping_uncertainty", curie=DUFMECH.curie('mapping_uncertainty'),
                   model_uri=DUFMECH.coordinateMapping__mapping_uncertainty, domain=None, range=Optional[str])

slots.coordinateMapping__provenance_note = Slot(uri=DUFMECH.provenance_note, name="coordinateMapping__provenance_note", curie=DUFMECH.curie('provenance_note'),
                   model_uri=DUFMECH.coordinateMapping__provenance_note, domain=None, range=str)

slots.regionObservation__observation_id = Slot(uri=DUFMECH.observation_id, name="regionObservation__observation_id", curie=DUFMECH.curie('observation_id'),
                   model_uri=DUFMECH.regionObservation__observation_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__region_id = Slot(uri=DUFMECH.region_id, name="regionObservation__region_id", curie=DUFMECH.curie('region_id'),
                   model_uri=DUFMECH.regionObservation__region_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__sequence_id = Slot(uri=DUFMECH.sequence_id, name="regionObservation__sequence_id", curie=DUFMECH.curie('sequence_id'),
                   model_uri=DUFMECH.regionObservation__sequence_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__evidence_kind = Slot(uri=DUFMECH.evidence_kind, name="regionObservation__evidence_kind", curie=DUFMECH.curie('evidence_kind'),
                   model_uri=DUFMECH.regionObservation__evidence_kind, domain=None, range=Union[str, "EvidenceKind"])

slots.regionObservation__source_kind = Slot(uri=DUFMECH.source_kind, name="regionObservation__source_kind", curie=DUFMECH.curie('source_kind'),
                   model_uri=DUFMECH.regionObservation__source_kind, domain=None, range=Union[str, "ObservationSourceKind"])

slots.regionObservation__method = Slot(uri=DUFMECH.method, name="regionObservation__method", curie=DUFMECH.curie('method'),
                   model_uri=DUFMECH.regionObservation__method, domain=None, range=str)

slots.regionObservation__assay_conditions = Slot(uri=DUFMECH.assay_conditions, name="regionObservation__assay_conditions", curie=DUFMECH.curie('assay_conditions'),
                   model_uri=DUFMECH.regionObservation__assay_conditions, domain=None, range=Optional[str])

slots.regionObservation__tested_construct_region_id = Slot(uri=DUFMECH.tested_construct_region_id, name="regionObservation__tested_construct_region_id", curie=DUFMECH.curie('tested_construct_region_id'),
                   model_uri=DUFMECH.regionObservation__tested_construct_region_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__mutation_region_ids = Slot(uri=DUFMECH.mutation_region_ids, name="regionObservation__mutation_region_ids", curie=DUFMECH.curie('mutation_region_ids'),
                   model_uri=DUFMECH.regionObservation__mutation_region_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__observed_effect = Slot(uri=DUFMECH.observed_effect, name="regionObservation__observed_effect", curie=DUFMECH.curie('observed_effect'),
                   model_uri=DUFMECH.regionObservation__observed_effect, domain=None, range=str)

slots.regionObservation__interpretation = Slot(uri=DUFMECH.interpretation, name="regionObservation__interpretation", curie=DUFMECH.curie('interpretation'),
                   model_uri=DUFMECH.regionObservation__interpretation, domain=None, range=str)

slots.regionObservation__polarity = Slot(uri=DUFMECH.polarity, name="regionObservation__polarity", curie=DUFMECH.curie('polarity'),
                   model_uri=DUFMECH.regionObservation__polarity, domain=None, range=Union[str, "ObservationPolarity"])

slots.regionObservation__raw_score = Slot(uri=DUFMECH.raw_score, name="regionObservation__raw_score", curie=DUFMECH.curie('raw_score'),
                   model_uri=DUFMECH.regionObservation__raw_score, domain=None, range=Optional[float])

slots.regionObservation__score_metric = Slot(uri=DUFMECH.score_metric, name="regionObservation__score_metric", curie=DUFMECH.curie('score_metric'),
                   model_uri=DUFMECH.regionObservation__score_metric, domain=None, range=Optional[Union[str, "ScoreMetricKind"]])

slots.regionObservation__primary_experiment_key = Slot(uri=DUFMECH.primary_experiment_key, name="regionObservation__primary_experiment_key", curie=DUFMECH.curie('primary_experiment_key'),
                   model_uri=DUFMECH.regionObservation__primary_experiment_key, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:/-]+$'))

slots.regionObservation__derived_from_observation_ids = Slot(uri=DUFMECH.derived_from_observation_ids, name="regionObservation__derived_from_observation_ids", curie=DUFMECH.curie('derived_from_observation_ids'),
                   model_uri=DUFMECH.regionObservation__derived_from_observation_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.regionObservation__limitations = Slot(uri=DUFMECH.limitations, name="regionObservation__limitations", curie=DUFMECH.curie('limitations'),
                   model_uri=DUFMECH.regionObservation__limitations, domain=None, range=Optional[str])

slots.regionObservation__evidence = Slot(uri=DUFMECH.evidence, name="regionObservation__evidence", curie=DUFMECH.curie('evidence'),
                   model_uri=DUFMECH.regionObservation__evidence, domain=None, range=Optional[Union[Union[dict, ClaimEvidence], list[Union[dict, ClaimEvidence]]]])

slots.evidenceGroup__group_id = Slot(uri=DUFMECH.group_id, name="evidenceGroup__group_id", curie=DUFMECH.curie('group_id'),
                   model_uri=DUFMECH.evidenceGroup__group_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.evidenceGroup__primary_experiment_key = Slot(uri=DUFMECH.primary_experiment_key, name="evidenceGroup__primary_experiment_key", curie=DUFMECH.curie('primary_experiment_key'),
                   model_uri=DUFMECH.evidenceGroup__primary_experiment_key, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:/-]+$'))

slots.evidenceGroup__evidence_kind = Slot(uri=DUFMECH.evidence_kind, name="evidenceGroup__evidence_kind", curie=DUFMECH.curie('evidence_kind'),
                   model_uri=DUFMECH.evidenceGroup__evidence_kind, domain=None, range=Union[str, "EvidenceKind"])

slots.evidenceGroup__polarity = Slot(uri=DUFMECH.polarity, name="evidenceGroup__polarity", curie=DUFMECH.curie('polarity'),
                   model_uri=DUFMECH.evidenceGroup__polarity, domain=None, range=Union[str, "ObservationPolarity"])

slots.evidenceGroup__observation_ids = Slot(uri=DUFMECH.observation_ids, name="evidenceGroup__observation_ids", curie=DUFMECH.curie('observation_ids'),
                   model_uri=DUFMECH.evidenceGroup__observation_ids, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.evidenceGroup__deduplication_rationale = Slot(uri=DUFMECH.deduplication_rationale, name="evidenceGroup__deduplication_rationale", curie=DUFMECH.curie('deduplication_rationale'),
                   model_uri=DUFMECH.evidenceGroup__deduplication_rationale, domain=None, range=str)

slots.synthesizedClaim__claim_id = Slot(uri=DUFMECH.claim_id, name="synthesizedClaim__claim_id", curie=DUFMECH.curie('claim_id'),
                   model_uri=DUFMECH.synthesizedClaim__claim_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__label = Slot(uri=DUFMECH.label, name="synthesizedClaim__label", curie=DUFMECH.curie('label'),
                   model_uri=DUFMECH.synthesizedClaim__label, domain=None, range=str)

slots.synthesizedClaim__function_aspect = Slot(uri=DUFMECH.function_aspect, name="synthesizedClaim__function_aspect", curie=DUFMECH.curie('function_aspect'),
                   model_uri=DUFMECH.synthesizedClaim__function_aspect, domain=None, range=Union[str, "FunctionAspect"])

slots.synthesizedClaim__ontology_term_id = Slot(uri=DUFMECH.ontology_term_id, name="synthesizedClaim__ontology_term_id", curie=DUFMECH.curie('ontology_term_id'),
                   model_uri=DUFMECH.synthesizedClaim__ontology_term_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(GO:[0-9]{7}|Rhea:[0-9]+|EC:[0-9]+(\.[0-9-]+){0,3}|CHEBI:[0-9]+|Pfam:PF[0-9]{5}|InterPro:IPR[0-9]{6}|UniProtKB:[A-Z0-9-]+)$'))

slots.synthesizedClaim__ontology_term_label = Slot(uri=DUFMECH.ontology_term_label, name="synthesizedClaim__ontology_term_label", curie=DUFMECH.curie('ontology_term_label'),
                   model_uri=DUFMECH.synthesizedClaim__ontology_term_label, domain=None, range=Optional[str])

slots.synthesizedClaim__target_region_id = Slot(uri=DUFMECH.target_region_id, name="synthesizedClaim__target_region_id", curie=DUFMECH.curie('target_region_id'),
                   model_uri=DUFMECH.synthesizedClaim__target_region_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__claimed_scope = Slot(uri=DUFMECH.claimed_scope, name="synthesizedClaim__claimed_scope", curie=DUFMECH.curie('claimed_scope'),
                   model_uri=DUFMECH.synthesizedClaim__claimed_scope, domain=None, range=Union[str, "ClaimScope"])

slots.synthesizedClaim__synthesis_status = Slot(uri=DUFMECH.synthesis_status, name="synthesizedClaim__synthesis_status", curie=DUFMECH.curie('synthesis_status'),
                   model_uri=DUFMECH.synthesizedClaim__synthesis_status, domain=None, range=Union[str, "SynthesisStatus"])

slots.synthesizedClaim__supporting_evidence_groups = Slot(uri=DUFMECH.supporting_evidence_groups, name="synthesizedClaim__supporting_evidence_groups", curie=DUFMECH.curie('supporting_evidence_groups'),
                   model_uri=DUFMECH.synthesizedClaim__supporting_evidence_groups, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__contradicting_evidence_groups = Slot(uri=DUFMECH.contradicting_evidence_groups, name="synthesizedClaim__contradicting_evidence_groups", curie=DUFMECH.curie('contradicting_evidence_groups'),
                   model_uri=DUFMECH.synthesizedClaim__contradicting_evidence_groups, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__supporting_observation_ids = Slot(uri=DUFMECH.supporting_observation_ids, name="synthesizedClaim__supporting_observation_ids", curie=DUFMECH.curie('supporting_observation_ids'),
                   model_uri=DUFMECH.synthesizedClaim__supporting_observation_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__contradicting_observation_ids = Slot(uri=DUFMECH.contradicting_observation_ids, name="synthesizedClaim__contradicting_observation_ids", curie=DUFMECH.curie('contradicting_observation_ids'),
                   model_uri=DUFMECH.synthesizedClaim__contradicting_observation_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__mapping_ids = Slot(uri=DUFMECH.mapping_ids, name="synthesizedClaim__mapping_ids", curie=DUFMECH.curie('mapping_ids'),
                   model_uri=DUFMECH.synthesizedClaim__mapping_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.synthesizedClaim__scope_rationale = Slot(uri=DUFMECH.scope_rationale, name="synthesizedClaim__scope_rationale", curie=DUFMECH.curie('scope_rationale'),
                   model_uri=DUFMECH.synthesizedClaim__scope_rationale, domain=None, range=str)

slots.synthesizedClaim__scope_transfer_blocks = Slot(uri=DUFMECH.scope_transfer_blocks, name="synthesizedClaim__scope_transfer_blocks", curie=DUFMECH.curie('scope_transfer_blocks'),
                   model_uri=DUFMECH.synthesizedClaim__scope_transfer_blocks, domain=None, range=Optional[Union[str, list[str]]])

slots.synthesizedClaim__synthesis_explanation = Slot(uri=DUFMECH.synthesis_explanation, name="synthesizedClaim__synthesis_explanation", curie=DUFMECH.curie('synthesis_explanation'),
                   model_uri=DUFMECH.synthesizedClaim__synthesis_explanation, domain=None, range=str)

slots.synthesizedClaim__discriminating_experiments = Slot(uri=DUFMECH.discriminating_experiments, name="synthesizedClaim__discriminating_experiments", curie=DUFMECH.curie('discriminating_experiments'),
                   model_uri=DUFMECH.synthesizedClaim__discriminating_experiments, domain=None, range=Optional[Union[str, list[str]]])

slots.reasoningEdge__edge_id = Slot(uri=DUFMECH.edge_id, name="reasoningEdge__edge_id", curie=DUFMECH.curie('edge_id'),
                   model_uri=DUFMECH.reasoningEdge__edge_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.reasoningEdge__subject = Slot(uri=DUFMECH.subject, name="reasoningEdge__subject", curie=DUFMECH.curie('subject'),
                   model_uri=DUFMECH.reasoningEdge__subject, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.reasoningEdge__predicate = Slot(uri=DUFMECH.predicate, name="reasoningEdge__predicate", curie=DUFMECH.curie('predicate'),
                   model_uri=DUFMECH.reasoningEdge__predicate, domain=None, range=Union[str, "ReasoningPredicate"])

slots.reasoningEdge__object = Slot(uri=DUFMECH.object, name="reasoningEdge__object", curie=DUFMECH.curie('object'),
                   model_uri=DUFMECH.reasoningEdge__object, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_.:-]+$'))

slots.reasoningEdge__edge_category = Slot(uri=DUFMECH.edge_category, name="reasoningEdge__edge_category", curie=DUFMECH.curie('edge_category'),
                   model_uri=DUFMECH.reasoningEdge__edge_category, domain=None, range=Union[str, "ReasoningEdgeCategory"])

slots.reasoningEdge__support = Slot(uri=DUFMECH.support, name="reasoningEdge__support", curie=DUFMECH.curie('support'),
                   model_uri=DUFMECH.reasoningEdge__support, domain=None, range=Union[str, "CausalSupport"])

slots.reasoningEdge__evidence_kind = Slot(uri=DUFMECH.evidence_kind, name="reasoningEdge__evidence_kind", curie=DUFMECH.curie('evidence_kind'),
                   model_uri=DUFMECH.reasoningEdge__evidence_kind, domain=None, range=Union[str, "EvidenceKind"])

slots.reasoningEdge__rationale = Slot(uri=DUFMECH.rationale, name="reasoningEdge__rationale", curie=DUFMECH.curie('rationale'),
                   model_uri=DUFMECH.reasoningEdge__rationale, domain=None, range=str)

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
