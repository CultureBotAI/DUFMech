"""Select UniProtKB example-protein candidates for DUF families that lack one."""

from __future__ import annotations

import csv
import io
import json
import re
import time
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

UNIPROTKB_SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
CANDIDATE_FIELDS = "accession,reviewed,annotation_score,protein_name,organism_name,organism_id,length"
# Highest UniProt annotation score first; reviewed entries usually score highest.
# Accession breaks ties so the selection is reproducible within one UniProt release.
CANDIDATE_SORT = "annotation_score desc,accession asc"
CANDIDATE_QUERY = "xref:pfam-{pfam_id}"
PFAM_ID_RE = re.compile(r"PF\d{5}")

# Why a family needs an example; a family can carry several reasons.
TRAITMECH_NAMED = "traitmech_named_without_protein"
TRAITMECH_RENAMED = "traitmech_named_renamed_family"
PROTEIN_TRAITS_GAP = "protein_traits_trait_without_family_example"

EXAMPLE_CANDIDATE_TSV_FIELDNAMES = [
    "pfam_id",
    "rank",
    "uniprot_accession",
    "reviewed",
    "annotation_score",
    "protein_name",
    "taxon_id",
    "organism",
    "length",
    "family_members",
    "selection_reasons",
    "source_url",
]


class ExampleCandidateError(RuntimeError):
    """Raised when UniProtKB cannot be queried or returns an invalid page."""


@dataclass(frozen=True)
class ExampleCandidateRow:
    """One ranked UniProtKB entry carrying a target Pfam family."""

    pfam_id: str
    rank: int
    uniprot_accession: str
    reviewed: bool | None
    annotation_score: float | None
    protein_name: str
    taxon_id: str
    organism: str
    length: int | None
    family_members: int | None
    selection_reasons: tuple[str, ...]

    @property
    def source_url(self) -> str:
        return f"https://rest.uniprot.org/uniprotkb/{self.uniprot_accession}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["selection_reasons"] = ";".join(self.selection_reasons)
        for key in ("reviewed", "annotation_score", "length", "family_members"):
            value = row[key]
            row[key] = "" if value is None else str(value).lower() if key == "reviewed" else value
        row["source_url"] = self.source_url
        return row


@dataclass
class CandidateRun:
    """Rows plus per-family bookkeeping for the manifest."""

    rows: list[ExampleCandidateRow] = field(default_factory=list)
    families_queried: int = 0
    families_without_members: list[str] = field(default_factory=list)
    uniprot_releases: set[str] = field(default_factory=set)
    families_fetched: int = 0
    families_from_checkpoint: int = 0
    checkpoint_fetch_times: set[str] = field(default_factory=set)


def select_target_families(
    cross_mech_rows: Iterable[Mapping[str, Any]],
    *,
    renamed_traitmech_families: Iterable[str] = (),
) -> dict[str, set[str]]:
    """Return ``{pfam_id: reasons}`` for families that need an example protein.

    - TraitMech names the family in record text, and no TraitMech-cited protein or
      ProteinTraitsMech canonical example carries it.
    - ProteinTraitsMech has a trait record for the family, but none of its canonical
      examples carries the family.
    - ``renamed_traitmech_families``: current Pfam families for names TraitMech cites
      under a former DUF name (resolved separately through Pfam previous identifiers).
    """

    rows = list(cross_mech_rows)
    with_protein = {
        row["pfam_id"]
        for row in rows
        if row["pfam_id"] and row.get("uniprot_accession")
        and row["source_mech"] in {"TraitMech", "ProteinTraitsMech"}
    }
    traitmech_named = {
        row["pfam_id"]
        for row in rows
        if row["source_mech"] == "TraitMech" and row["pfam_id"]
        and row["source_section"] == "record_text"
    }
    trait_records = {
        row["pfam_id"]
        for row in rows
        if row["pfam_id"]
        and row["source_mech"] == "ProteinTraitsMech"
        and row["source_section"] == "trait_identifier"
    }
    own_examples = {
        row["pfam_id"]
        for row in rows
        if row["source_mech"] == "ProteinTraitsMech"
        and row["source_section"] == "canonical_examples"
        and row.get("family_mentioned_in_record")
    }
    targets: dict[str, set[str]] = {}
    for pfam_id in traitmech_named - with_protein:
        targets.setdefault(pfam_id, set()).add(TRAITMECH_NAMED)
    for pfam_id in trait_records - own_examples:
        targets.setdefault(pfam_id, set()).add(PROTEIN_TRAITS_GAP)
    for pfam_id in renamed_traitmech_families:
        if not PFAM_ID_RE.fullmatch(pfam_id):
            raise ValueError(f"not a Pfam family ID: {pfam_id!r}")
        targets.setdefault(pfam_id, set()).add(TRAITMECH_RENAMED)
    return targets


class UniProtExampleClient:
    """Query UniProtKB for the top-ranked members of one Pfam family, anonymously."""

    def __init__(
        self,
        *,
        per_family: int = 3,
        timeout: float = 60.0,
        transport: httpx.BaseTransport | None = None,
        retries: int = 4,
        backoff: float = 2.0,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        if not 1 <= per_family <= 25:
            raise ValueError("per_family must be between 1 and 25")
        self.per_family = per_family
        self.timeout = timeout
        self.transport = transport
        self.retries = retries
        self.backoff = backoff
        self.sleep = sleep

    @property
    def settings(self) -> dict[str, Any]:
        """Query settings a checkpointed response must share to be reused."""

        return {
            "query": CANDIDATE_QUERY,
            "fields": CANDIDATE_FIELDS,
            "sort": CANDIDATE_SORT,
            "per_family": self.per_family,
        }

    def collect(
        self,
        targets: Mapping[str, Iterable[str]],
        *,
        progress: Callable[[int, int], None] | None = None,
        checkpoint: Path | None = None,
    ) -> CandidateRun:
        """Query every target family.

        With ``checkpoint``, each family's raw response is appended as one JSON line as
        soon as it arrives, and families already in the file with the same query
        settings are not queried again, so an interrupted run resumes where it stopped.
        A run whose responses span more than one UniProt release is refused.
        """

        run = CandidateRun()
        done = _load_checkpoint(checkpoint, self.settings) if checkpoint is not None else {}
        sink = None
        if checkpoint is not None:
            checkpoint.parent.mkdir(parents=True, exist_ok=True)
            sink = checkpoint.open("a", encoding="utf-8")
        try:
            with httpx.Client(
                timeout=self.timeout, follow_redirects=True, transport=self.transport
            ) as client:
                for index, pfam_id in enumerate(sorted(targets), start=1):
                    if pfam_id in done:
                        response = done[pfam_id]
                        run.families_from_checkpoint += 1
                        run.checkpoint_fetch_times.add(response.get("fetched_at") or "")
                    else:
                        payload, headers = self._get(client, pfam_id)
                        if not isinstance(payload.get("results"), list):
                            raise ExampleCandidateError(
                                f"UniProtKB page for {pfam_id} had no results list"
                            )
                        run.families_fetched += 1
                        response = {
                            "pfam_id": pfam_id,
                            "settings": self.settings,
                            "fetched_at": _now(),
                            "release": headers.get("x-uniprot-release", ""),
                            "total": _int(headers.get("x-total-results")),
                            "results": payload["results"],
                        }
                        if sink is not None:
                            sink.write(json.dumps(response, sort_keys=True) + "\n")
                            sink.flush()
                    self._record(run, pfam_id, tuple(sorted(targets[pfam_id])), response)
                    if progress is not None:
                        progress(index, len(targets))
        finally:
            if sink is not None:
                sink.close()
        if len(run.uniprot_releases) > 1:
            raise ExampleCandidateError(
                f"responses span UniProt releases {sorted(run.uniprot_releases)}; "
                "use a fresh checkpoint"
            )
        return run

    @staticmethod
    def _record(
        run: CandidateRun, pfam_id: str, reasons: tuple[str, ...], response: Mapping[str, Any]
    ) -> None:
        run.families_queried += 1
        release = response.get("release") or ""
        if release:
            run.uniprot_releases.add(release)
        total = response.get("total")
        results = response.get("results")
        if not isinstance(results, list):
            raise ExampleCandidateError(f"UniProtKB page for {pfam_id} had no results list")
        rows = [
            row
            for rank, entry in enumerate(results, start=1)
            if isinstance(entry, Mapping)
            for row in [candidate_row(entry, pfam_id, rank, total, reasons)]
            if row is not None
        ]
        if not rows:
            run.families_without_members.append(pfam_id)
        run.rows.extend(rows)

    def _get(self, client: httpx.Client, pfam_id: str) -> tuple[Mapping[str, Any], httpx.Headers]:
        params = {
            "query": CANDIDATE_QUERY.format(pfam_id=pfam_id),
            "fields": CANDIDATE_FIELDS,
            "sort": CANDIDATE_SORT,
            "size": str(self.per_family),
            "format": "json",
        }
        for attempt in range(self.retries + 1):
            try:
                response = client.get(UNIPROTKB_SEARCH_URL, params=params)
                if response.status_code in {429, 500, 502, 503, 504} and attempt < self.retries:
                    self.sleep(self.backoff * 2**attempt)
                    continue
                response.raise_for_status()
                payload = response.json()
            except (httpx.TransportError, ValueError) as exc:
                if attempt < self.retries:
                    self.sleep(self.backoff * 2**attempt)
                    continue
                raise ExampleCandidateError(f"could not query UniProtKB for {pfam_id}") from exc
            except httpx.HTTPStatusError as exc:
                raise ExampleCandidateError(f"UniProtKB query for {pfam_id} failed") from exc
            if not isinstance(payload, Mapping):
                raise ExampleCandidateError(f"UniProtKB page for {pfam_id} was not an object")
            return payload, response.headers
        raise ExampleCandidateError(f"could not query UniProtKB for {pfam_id}")


def candidate_row(
    entry: Mapping[str, Any],
    pfam_id: str,
    rank: int,
    family_members: int | None,
    reasons: Sequence[str],
) -> ExampleCandidateRow | None:
    """Normalize one UniProtKB search result, or ``None`` if it has no accession."""

    accession = _string(entry.get("primaryAccession"))
    if not accession:
        return None
    entry_type = _string(entry.get("entryType")).lower()
    reviewed = False if "unreviewed" in entry_type else True if "reviewed" in entry_type else None
    organism = entry.get("organism") if isinstance(entry.get("organism"), Mapping) else {}
    sequence = entry.get("sequence") if isinstance(entry.get("sequence"), Mapping) else {}
    score = entry.get("annotationScore")
    return ExampleCandidateRow(
        pfam_id=pfam_id,
        rank=rank,
        uniprot_accession=accession,
        reviewed=reviewed,
        annotation_score=float(score) if isinstance(score, (int, float)) else None,
        protein_name=_protein_name(entry.get("proteinDescription")),
        taxon_id=f"NCBITaxon:{organism['taxonId']}" if organism.get("taxonId") else "",
        organism=_string(organism.get("scientificName")),
        length=_int(sequence.get("length")),
        family_members=family_members,
        selection_reasons=tuple(reasons),
    )


def render_candidates_tsv(rows: Iterable[ExampleCandidateRow]) -> str:
    """Render candidate rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out, fieldnames=EXAMPLE_CANDIDATE_TSV_FIELDNAMES, dialect="excel-tab", lineterminator="\n"
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_candidates_json(rows: Iterable[ExampleCandidateRow]) -> str:
    """Render candidate rows as stable JSON."""

    return json.dumps(
        [
            {**asdict(row), "selection_reasons": list(row.selection_reasons),
             "source_url": row.source_url}
            for row in rows
        ],
        indent=2,
        sort_keys=True,
    )


def _load_checkpoint(path: Path, settings: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    """Load completed family responses made with identical query ``settings``.

    A torn final line from a crash is removed from the file so later appends start on
    a clean line; any other unreadable line is an error. Lines from other settings
    (including legacy lines without settings) are kept but never reused.
    """

    done: dict[str, Mapping[str, Any]] = {}
    if not path.is_file():
        return done
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        # Keep only complete lines; the torn tail never parsed into a usable response.
        data = data[: data.rfind(b"\n") + 1]
        with path.open("r+b") as handle:
            handle.truncate(len(data))
    for number, line in enumerate(data.decode("utf-8").splitlines(), start=1):
        try:
            item = json.loads(line)
        except ValueError:
            raise ExampleCandidateError(f"corrupt checkpoint line {number} in {path}") from None
        if (
            isinstance(item, Mapping)
            and isinstance(item.get("pfam_id"), str)
            and item.get("settings") == dict(settings)
            and isinstance(item.get("results"), list)
        ):
            done[item["pfam_id"]] = item
    return done


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _protein_name(value: object) -> str:
    description = value if isinstance(value, Mapping) else {}
    for key in ("recommendedName",):
        name = (description.get(key) or {}).get("fullName", {}).get("value")
        if isinstance(name, str) and name.strip():
            return name.strip()
    for submission in description.get("submissionNames") or ():
        name = (submission or {}).get("fullName", {}).get("value")
        if isinstance(name, str) and name.strip():
            return name.strip()
    return ""


def _int(value: object) -> int | None:
    try:
        return int(value) if value is not None and value != "" else None
    except (TypeError, ValueError):
        return None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""
