"""Find DUF/PUF families and proteins already curated in sibling Mech repositories."""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import threading
from collections.abc import Iterable, Iterator, Mapping, Sequence
from dataclasses import asdict, dataclass, field
from pathlib import PurePosixPath
from typing import Any

import httpx
import yaml

UNIPROTKB_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
UNIPROTKB_FIELDS = "accession,id,protein_name,organism_name,organism_id,reviewed,xref_pfam"
GITHUB_ORG_URL = "https://github.com/CultureBotAI"

PROTEIN_TRAITS_MECH = "ProteinTraitsMech"
NOT_IN_WORKLIST = "NOT_IN_WORKLIST"

# Word-bounded identifiers; the guards reject drug codes such as PF07321332 and
# GenBank prefixes such as LIPF01000008.
PFAM_TEXT_RE = re.compile(r"(?<![A-Za-z0-9])(PF\d{5})(?:\.\d+)?(?![0-9])")
# Bare DUF/UPF names only; an underscore-joined name (QueG_DUF1730, DUF3458_C) is a
# different Pfam family and is matched exactly through FamilyIndex.compound_names, which
# also masks the few hyphenated worklist names. Other hyphens are prose
# ("DUF1814-family", "COG5340-DUF1814") and still count as the bare name.
SHORT_NAME_TEXT_RE = re.compile(r"(?<![A-Za-z0-9_])(DUF\d{1,5}|UPF\d{4})(?![0-9]|_[A-Za-z0-9])")
COMPOUND_NAME_RE = re.compile(r"[A-Za-z0-9_-]*(?:DUF\d{1,5}|UPF\d{4})[A-Za-z0-9_-]*")
INTERPRO_TEXT_RE = re.compile(r"(?<![A-Za-z0-9])(IPR\d{6})(?![0-9])")
UNIPROT_TEXT_RE = re.compile(
    r"UniProt(?:KB)?(?:/(?:Swiss-Prot|TrEMBL))?[:\s]\s*"
    r"([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})"
    r"(?![A-Za-z0-9])"
)
TOP_LEVEL_RE = re.compile(r"^(identifier|id|name|label|title):\s*(.+?)\s*$", re.MULTILINE)

CROSS_MECH_TSV_FIELDNAMES = [
    "pfam_id",
    "short_name",
    "unknown_status",
    "source_mech",
    "source_category",
    "source_path",
    "source_record_id",
    "source_record_label",
    "source_section",
    "link_basis",
    "uniprot_accession",
    "protein_label",
    "reviewed",
    "taxon_id",
    "taxon_label",
    "family_mentioned_in_record",
]


class CrossMechError(RuntimeError):
    """Raised when a sibling Mech or UniProtKB cannot be read."""


@dataclass(frozen=True)
class MechSource:
    """One sibling Mech and the curated record directory to scan."""

    name: str
    data_dir: str
    repo_slug: str = ""

    @property
    def github_slug(self) -> str:
        return self.repo_slug or self.name


DEFAULT_MECH_SOURCES = (
    MechSource("AntibioticMech", "data/antibiotics"),
    MechSource("CellStructureMech", "data/structures"),
    MechSource("CommunityMech", "kb/communities"),
    MechSource("CultureMech", "data/normalized_yaml"),
    MechSource("HabitatMech", "data/habitats"),
    MechSource("MediaIngredientMech", "data/ingredients"),
    MechSource("NaturalProductMech", "data/natural_products"),
    MechSource("PathwayMech", "data/pathways"),
    MechSource(PROTEIN_TRAITS_MECH, "data/traits", "proteintraitsmech"),
    MechSource("TaxonMech", "data/taxa"),
    MechSource("TraitMech", "data/traits"),
)


@dataclass(frozen=True)
class WorklistFamily:
    """The worklist fields needed to recognize a DUF/PUF family."""

    pfam_id: str
    short_name: str
    name: str
    interpro_id: str
    unknown_status: str


@dataclass(frozen=True)
class FamilyIndex:
    """Lookup tables from Pfam IDs, short names, and InterPro IDs to families."""

    by_pfam: Mapping[str, WorklistFamily]
    by_short_name: Mapping[str, tuple[str, ...]]
    by_interpro: Mapping[str, tuple[str, ...]]
    compound_names: re.Pattern[str] | None = None

    @classmethod
    def from_rows(cls, rows: Iterable[Mapping[str, Any]]) -> FamilyIndex:
        by_pfam: dict[str, WorklistFamily] = {}
        by_short: dict[str, set[str]] = {}
        by_interpro: dict[str, set[str]] = {}
        for row in rows:
            family = WorklistFamily(
                pfam_id=_string(row.get("pfam_id")),
                short_name=_string(row.get("short_name")),
                name=_string(row.get("name")),
                interpro_id=_string(row.get("interpro_id")),
                unknown_status=_string(row.get("unknown_status")),
            )
            if not family.pfam_id:
                continue
            by_pfam[family.pfam_id] = family
            if SHORT_NAME_TEXT_RE.fullmatch(family.short_name) or COMPOUND_NAME_RE.fullmatch(
                family.short_name
            ):
                by_short.setdefault(family.short_name, set()).add(family.pfam_id)
            if family.interpro_id:
                by_interpro.setdefault(family.interpro_id, set()).add(family.pfam_id)
        compounds = sorted(
            (name for name in by_short if not SHORT_NAME_TEXT_RE.fullmatch(name)),
            key=lambda name: (-len(name), name),
        )
        return cls(
            by_pfam=by_pfam,
            by_short_name={key: tuple(sorted(value)) for key, value in by_short.items()},
            by_interpro={key: tuple(sorted(value)) for key, value in by_interpro.items()},
            compound_names=(
                re.compile(
                    r"(?<![A-Za-z0-9_-])("
                    + "|".join(re.escape(name) for name in compounds)
                    + r")(?![A-Za-z0-9_-])"
                )
                if compounds
                else None
            ),
        )

    def _short_names(self, text: str) -> tuple[list[str], str]:
        """Return exact compound-name hits and the text with those hits masked."""

        if self.compound_names is None:
            return [], text
        found = self.compound_names.findall(text)
        return found, self.compound_names.sub(" ", text)

    def text_matches(self, text: str) -> dict[str, set[str]]:
        """Return worklist Pfam IDs mentioned in ``text`` with their link bases."""

        matches: dict[str, set[str]] = {}
        for pfam_id in PFAM_TEXT_RE.findall(text):
            if pfam_id in self.by_pfam:
                matches.setdefault(pfam_id, set()).add("record_mentions_pfam_id")
        compounds, masked = self._short_names(text)
        for short_name in [*compounds, *SHORT_NAME_TEXT_RE.findall(masked)]:
            for pfam_id in self.by_short_name.get(short_name, ()):
                matches.setdefault(pfam_id, set()).add("record_mentions_short_name")
        for interpro_id in INTERPRO_TEXT_RE.findall(text):
            for pfam_id in self.by_interpro.get(interpro_id, ()):
                matches.setdefault(pfam_id, set()).add("record_mentions_interpro_id")
        return matches

    def unlisted_short_names(self, text: str) -> set[str]:
        """Return bare DUF/UPF names in ``text`` that the worklist does not carry.

        DUF names are usually families Pfam renamed after characterization. UPF names
        are UniProt family nomenclature, which the Pfam-derived worklist never carries.
        Both are kept as leads instead of being dropped.
        """

        _, masked = self._short_names(text)
        return {
            name for name in SHORT_NAME_TEXT_RE.findall(masked) if name not in self.by_short_name
        }


@dataclass(frozen=True)
class SourceRecord:
    """One curated YAML record read from a sibling Mech commit."""

    mech: MechSource
    commit: str
    path: str
    text: str

    @property
    def category(self) -> str:
        relative = PurePosixPath(self.path).relative_to(self.mech.data_dir)
        return str(relative.parent) if str(relative.parent) != "." else ""

    def identity(self) -> tuple[str, str]:
        found: dict[str, str] = {}
        for key, value in TOP_LEVEL_RE.findall(self.text):
            found.setdefault(key, value.strip("'\""))
        record_id = found.get("identifier") or found.get("id") or PurePosixPath(self.path).stem
        label = found.get("label") or found.get("name") or found.get("title") or ""
        return record_id, label


@dataclass(frozen=True)
class UniProtPfamRow:
    """UniProtKB metadata and Pfam cross-references for one requested accession."""

    requested_accession: str
    uniprot_accession: str
    protein_label: str
    reviewed: bool | None
    taxon_id: str
    taxon_label: str
    pfam_ids: tuple[str, ...]


@dataclass(frozen=True)
class CrossMechRow:
    """One DUF/PUF family or protein example found in another Mech."""

    pfam_id: str
    short_name: str
    unknown_status: str
    source_mech: str
    source_category: str
    source_path: str
    source_record_id: str
    source_record_label: str
    source_section: str
    link_basis: tuple[str, ...]
    uniprot_accession: str = ""
    protein_label: str = ""
    reviewed: bool | None = None
    taxon_id: str = ""
    taxon_label: str = ""
    family_mentioned_in_record: bool | None = None

    def sort_key(self) -> tuple[str, ...]:
        return (
            self.pfam_id,
            self.short_name,
            self.source_mech,
            self.source_path,
            self.source_section,
            self.uniprot_accession,
        )

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["link_basis"] = ";".join(self.link_basis)
        for key in ("reviewed", "family_mentioned_in_record"):
            value = row[key]
            row[key] = "" if value is None else str(value).lower()
        return row


@dataclass
class ScanResult:
    """Rows plus per-Mech scan bookkeeping for the manifest."""

    rows: list[CrossMechRow] = field(default_factory=list)
    mechs: dict[str, dict[str, Any]] = field(default_factory=dict)
    uniprot_requested: int = 0
    uniprot_resolved: int = 0
    uniprot_unresolved: list[str] = field(default_factory=list)
    uniprot_lookup: dict[str, Any] = field(default_factory=dict)


def iter_mech_records(
    mechs_root: Any,
    mech: MechSource,
    *,
    ref: str = "HEAD",
) -> tuple[str, Iterator[SourceRecord]]:
    """Return a Mech commit and its tracked YAML records at ``ref``."""

    repo = mechs_root / mech.name
    if not (repo / ".git").exists():
        raise CrossMechError(f"{repo} is not a git checkout")
    commit = _git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    listing = _git(repo, "ls-tree", "-r", "-z", "--full-tree", commit, "--", mech.data_dir)
    blobs: list[tuple[str, str]] = []
    for entry in listing.split("\0"):
        if not entry:
            continue
        meta, path = entry.split("\t", 1)
        _, kind, sha = meta.split()
        if kind == "blob" and path.endswith((".yaml", ".yml")):
            blobs.append((sha, path))
    return commit, _cat_blobs(repo, commit, mech, sorted(blobs, key=lambda item: item[1]))


def scan_mechs(
    mechs_root: Any,
    families: FamilyIndex,
    *,
    mechs: Sequence[MechSource] = DEFAULT_MECH_SOURCES,
    ref: str = "HEAD",
    uniprot_lookup: Any = None,
) -> ScanResult:
    """Scan sibling Mechs and return DUF/PUF family and protein example rows."""

    result = ScanResult()
    pending: dict[str, list[tuple[SourceRecord, set[str]]]] = {}
    for mech in mechs:
        commit, records = iter_mech_records(mechs_root, mech, ref=ref)
        scanned = 0
        before = len(result.rows)
        for record in records:
            scanned += 1
            if mech.name == PROTEIN_TRAITS_MECH:
                result.rows.extend(protein_traits_rows(record, families))
                continue
            mentioned = families.text_matches(record.text)
            result.rows.extend(family_mention_rows(record, families, mentioned))
            result.rows.extend(unlisted_name_rows(record, families.unlisted_short_names(record.text)))
            for accession in sorted(set(UNIPROT_TEXT_RE.findall(record.text))):
                pending.setdefault(accession, []).append((record, set(mentioned)))
        result.mechs[mech.name] = {
            "commit": commit,
            "data_dir": mech.data_dir,
            "repository": f"{GITHUB_ORG_URL}/{mech.github_slug}",
            "records_scanned": scanned,
            "rows_before_uniprot": len(result.rows) - before,
        }

    result.uniprot_requested = len(pending)
    if pending and uniprot_lookup is not None:
        lookups = uniprot_lookup(sorted(pending))
        result.uniprot_resolved = len(lookups)
        result.uniprot_unresolved = sorted(set(pending) - set(lookups))
        for accession, contexts in sorted(pending.items()):
            lookup = lookups.get(accession)
            if lookup is None:
                continue
            for record, mentioned in contexts:
                result.rows.extend(uniprot_rows(record, families, lookup, mentioned))
    result.rows = _dedupe(result.rows)
    return result


def family_mention_rows(
    record: SourceRecord,
    families: FamilyIndex,
    mentioned: Mapping[str, set[str]],
) -> list[CrossMechRow]:
    """Rows for families named in a record's text, without a protein claim."""

    record_id, label = record.identity()
    return [
        _row(
            families.by_pfam[pfam_id],
            record,
            record_id,
            label,
            section="record_text",
            basis=bases,
        )
        for pfam_id, bases in sorted(mentioned.items())
    ]


def unlisted_name_rows(record: SourceRecord, names: Iterable[str]) -> list[CrossMechRow]:
    """Rows for DUF/UPF names that do not resolve to a worklist family."""

    record_id, label = record.identity()
    unlisted = WorklistFamily("", "", "", "", NOT_IN_WORKLIST)
    return [
        _row(
            unlisted,
            record,
            record_id,
            label,
            section="record_text",
            basis={"record_mentions_unlisted_short_name"},
            short_name=name,
        )
        for name in sorted(set(names))
    ]


def uniprot_rows(
    record: SourceRecord,
    families: FamilyIndex,
    lookup: UniProtPfamRow,
    mentioned: set[str],
) -> list[CrossMechRow]:
    """Rows for a record protein whose UniProtKB entry carries a worklist Pfam."""

    record_id, label = record.identity()
    return [
        _row(
            families.by_pfam[pfam_id],
            record,
            record_id,
            label,
            section="uniprot_accession",
            basis={"uniprot_pfam_xref"},
            accession=lookup.uniprot_accession,
            protein_label=lookup.protein_label,
            reviewed=lookup.reviewed,
            taxon_id=f"NCBITaxon:{lookup.taxon_id}" if lookup.taxon_id else "",
            taxon_label=lookup.taxon_label,
            family_mentioned=pfam_id in mentioned,
        )
        for pfam_id in lookup.pfam_ids
        if pfam_id in families.by_pfam
    ]


def protein_traits_rows(record: SourceRecord, families: FamilyIndex) -> list[CrossMechRow]:
    """Rows for ProteinTraitsMech DUF trait terms and DUF-classified canonical examples."""

    mentioned = {
        pfam_id for pfam_id in PFAM_TEXT_RE.findall(record.text) if pfam_id in families.by_pfam
    }
    own_interpro = {
        interpro_id
        for interpro_id in INTERPRO_TEXT_RE.findall(record.text)
        if interpro_id in families.by_interpro
    }
    if not mentioned and not own_interpro:
        return []
    payload = _load_yaml(record)
    record_id = _string(payload.get("identifier")) or PurePosixPath(record.path).stem
    label = _string(payload.get("label"))
    rows: list[CrossMechRow] = []

    trait_pfams: tuple[str, ...] = ()
    if record_id.startswith("Pfam:") and record_id[5:] in families.by_pfam:
        trait_pfams = (record_id[5:],)
    elif record_id.startswith("InterPro:"):
        trait_pfams = families.by_interpro.get(record_id[9:], ())
    for pfam_id in trait_pfams:
        rows.append(
            _row(
                families.by_pfam[pfam_id],
                record,
                record_id,
                label,
                section="trait_identifier",
                basis={"trait_identifier"},
            )
        )

    examples = payload.get("canonical_examples")
    for example in examples if isinstance(examples, list) else ():
        if not isinstance(example, Mapping):
            continue
        accession = _string(example.get("protein_id")).removeprefix("UniProtKB:")
        classifications = example.get("family_classifications")
        pfams = sorted(
            {
                value[5:]
                for value in (classifications if isinstance(classifications, list) else ())
                if isinstance(value, str)
                and value.startswith("Pfam:")
                and value[5:] in families.by_pfam
            }
        )
        reviewed = example.get("reviewed")
        for pfam_id in pfams:
            rows.append(
                _row(
                    families.by_pfam[pfam_id],
                    record,
                    record_id,
                    label,
                    section="canonical_examples",
                    basis={"canonical_example_family_classification"},
                    accession=accession,
                    protein_label=_string(example.get("protein_label")),
                    reviewed=reviewed if isinstance(reviewed, bool) else None,
                    taxon_id=_string(example.get("taxon_id")),
                    taxon_label=_string(example.get("taxon_label")),
                    family_mentioned=pfam_id in trait_pfams,
                )
            )
    return rows


class UniProtPfamClient:
    """Fetch UniProtKB Pfam cross-references for accessions, anonymously."""

    def __init__(
        self,
        *,
        timeout: float = 60.0,
        transport: httpx.BaseTransport | None = None,
        batch_size: int = 100,
    ) -> None:
        self.timeout = timeout
        self.transport = transport
        self.batch_size = batch_size

    def __call__(self, accessions: Sequence[str]) -> dict[str, UniProtPfamRow]:
        found: dict[str, UniProtPfamRow] = {}
        with httpx.Client(
            timeout=self.timeout, follow_redirects=True, transport=self.transport
        ) as client:
            for offset in range(0, len(accessions), self.batch_size):
                batch = list(accessions[offset : offset + self.batch_size])
                params: dict[str, str] | None = {
                    "query": " OR ".join(f"accession:{accession}" for accession in batch),
                    "fields": UNIPROTKB_FIELDS,
                    "format": "json",
                    "size": "500",
                }
                next_url: str | None = UNIPROTKB_SEARCH_URL
                while next_url:
                    response = client.get(next_url, params=params)
                    try:
                        response.raise_for_status()
                        payload = response.json()
                    except (httpx.HTTPError, ValueError) as exc:
                        raise CrossMechError(f"could not fetch UniProtKB page {next_url}") from exc
                    results = payload.get("results") if isinstance(payload, Mapping) else None
                    if not isinstance(results, list):
                        raise CrossMechError(f"UniProtKB page {next_url} had no results list")
                    for entry in results:
                        if isinstance(entry, Mapping):
                            found.update(uniprot_pfam_rows(entry, batch))
                    next_link = response.links.get("next")
                    next_url = next_link.get("url") if isinstance(next_link, Mapping) else None
                    params = None
        return found


def uniprot_pfam_rows(
    entry: Mapping[str, Any], requested: Iterable[str]
) -> dict[str, UniProtPfamRow]:
    """Map an active UniProtKB entry back to each requested accession it answers.

    UniProt answers a merged, demerged, or deleted accession with an ``Inactive`` stub
    rather than the successor entry, so those accessions are not mapped here; the
    snapshot manifest lists them as unresolved. ``secondaryAccessions`` is still
    honored when an active entry carries a requested accession there.
    """

    primary = _string(entry.get("primaryAccession"))
    if not primary or "inactive" in _string(entry.get("entryType")).lower():
        return {}
    secondary = entry.get("secondaryAccessions")
    aliases = {primary, *(secondary if isinstance(secondary, list) else ())}
    organism = _mapping(entry.get("organism"))
    entry_type = _string(entry.get("entryType")).lower()
    reviewed = None
    if "unreviewed" in entry_type:
        reviewed = False
    elif "reviewed" in entry_type:
        reviewed = True
    references = entry.get("uniProtKBCrossReferences")
    pfam_ids = tuple(
        sorted(
            {
                _string(reference.get("id"))
                for reference in (references if isinstance(references, list) else ())
                if isinstance(reference, Mapping) and reference.get("database") == "Pfam"
            }
            - {""}
        )
    )
    row_args = {
        "uniprot_accession": primary,
        "protein_label": _protein_name(entry.get("proteinDescription")),
        "reviewed": reviewed,
        "taxon_id": _string(organism.get("taxonId")),
        "taxon_label": _string(organism.get("scientificName")),
        "pfam_ids": pfam_ids,
    }
    return {
        accession: UniProtPfamRow(requested_accession=accession, **row_args)
        for accession in requested
        if accession in aliases
    }


def load_uniprot_cache(text: str) -> dict[str, UniProtPfamRow]:
    """Load a cached accession lookup written by :func:`render_uniprot_cache`."""

    payload = json.loads(text)
    if not isinstance(payload, list):
        raise CrossMechError("UniProt cache must be a JSON list")
    rows = {}
    for item in payload:
        item = dict(item)
        item["pfam_ids"] = tuple(item.get("pfam_ids", ()))
        row = UniProtPfamRow(**item)
        rows[row.requested_accession] = row
    return rows


def render_uniprot_cache(rows: Mapping[str, UniProtPfamRow]) -> str:
    """Render accession lookups as stable JSON for offline re-runs."""

    return json.dumps(
        [asdict(rows[key]) for key in sorted(rows)], indent=2, sort_keys=True
    )


def render_cross_mech_tsv(rows: Iterable[CrossMechRow]) -> str:
    """Render cross-Mech rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=CROSS_MECH_TSV_FIELDNAMES,
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_cross_mech_json(rows: Iterable[CrossMechRow]) -> str:
    """Render cross-Mech rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "link_basis": list(row.link_basis)} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _row(
    family: WorklistFamily,
    record: SourceRecord,
    record_id: str,
    label: str,
    *,
    section: str,
    basis: Iterable[str],
    accession: str = "",
    protein_label: str = "",
    reviewed: bool | None = None,
    taxon_id: str = "",
    taxon_label: str = "",
    family_mentioned: bool | None = None,
    short_name: str = "",
) -> CrossMechRow:
    return CrossMechRow(
        pfam_id=family.pfam_id,
        short_name=short_name or family.short_name,
        unknown_status=family.unknown_status,
        source_mech=record.mech.name,
        source_category=record.category,
        source_path=record.path,
        source_record_id=record_id,
        source_record_label=label,
        source_section=section,
        link_basis=tuple(sorted(basis)),
        uniprot_accession=accession,
        protein_label=protein_label,
        reviewed=reviewed,
        taxon_id=taxon_id,
        taxon_label=taxon_label,
        family_mentioned_in_record=family_mentioned,
    )


def _dedupe(rows: Iterable[CrossMechRow]) -> list[CrossMechRow]:
    unique: dict[tuple[str, ...], CrossMechRow] = {}
    for row in rows:
        unique.setdefault(row.sort_key(), row)
    return [unique[key] for key in sorted(unique)]


def _cat_blobs(
    repo: Any,
    commit: str,
    mech: MechSource,
    blobs: Sequence[tuple[str, str]],
) -> Iterator[SourceRecord]:
    if not blobs:
        return
    process = subprocess.Popen(
        ["git", "-C", str(repo), "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    assert process.stdin is not None and process.stdout is not None
    stdin = process.stdin

    def feed() -> None:
        # Stream every request up front; a per-blob round trip is ~20x slower on large Mechs.
        try:
            for sha, _ in blobs:
                stdin.write(f"{sha}\n".encode())
        except BrokenPipeError:
            pass
        finally:
            stdin.close()

    feeder = threading.Thread(target=feed, daemon=True)
    feeder.start()
    try:
        for _, path in blobs:
            header = process.stdout.readline().split()
            if len(header) != 3:
                raise CrossMechError(f"could not read {mech.name}:{path}")
            data = process.stdout.read(int(header[2]))
            process.stdout.read(1)
            yield SourceRecord(mech, commit, path, data.decode("utf-8", errors="replace"))
    finally:
        process.stdout.close()
        process.wait()
        feeder.join()


def _git(repo: Any, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=False
    )
    if completed.returncode:
        raise CrossMechError(f"git {' '.join(args)} failed in {repo}: {completed.stderr.strip()}")
    return completed.stdout


def _load_yaml(record: SourceRecord) -> Mapping[str, Any]:
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    try:
        payload = yaml.load(record.text, Loader=loader)
    except yaml.YAMLError as exc:
        raise CrossMechError(f"invalid YAML in {record.mech.name}:{record.path}") from exc
    return payload if isinstance(payload, Mapping) else {}


def _protein_name(value: object) -> str:
    description = _mapping(value)
    name = _string(_mapping(_mapping(description.get("recommendedName")).get("fullName")).get("value"))
    if name:
        return name
    for submission in description.get("submissionNames") or ():
        name = _string(_mapping(_mapping(submission).get("fullName")).get("value"))
        if name:
            return name
    return ""


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _string(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    return ""
