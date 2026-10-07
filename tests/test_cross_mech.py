from __future__ import annotations

import json
import subprocess
from pathlib import Path

import httpx
import pytest
from bs4 import BeautifulSoup

from dufmech.cross_mech import (
    NOT_IN_WORKLIST,
    CrossMechError,
    FamilyIndex,
    MechSource,
    UniProtPfamClient,
    UniProtPfamRow,
    load_uniprot_cache,
    render_cross_mech_tsv,
    render_uniprot_cache,
    scan_mechs,
    uniprot_pfam_rows,
)
from dufmech.cross_mech_snapshot import write_cross_mech_snapshot
from dufmech.pages import render_site
from dufmech.provenance import check_manifest
from tests.test_report import worklist_row

FAMILIES = FamilyIndex.from_rows(
    [
        {**worklist_row("PF06226", proteins=1), "short_name": "DUF1007", "interpro_id": "IPR010412"},
        {**worklist_row("PF04363", proteins=1), "short_name": "DUF496", "interpro_id": "IPR007458"},
        {**worklist_row("PF07321", proteins=1), "short_name": "DUF1000"},
    ]
)

TRAIT_RECORD = """\
id: traitmech:000001
name: Example system
description: >-
  DrmB carries DUF1998, and the effector is a DUF1007 (Pfam:PF06226.5) protein.
evidence:
- reference: UniProtKB:P22041
- reference: UniProtKB:Q99999
"""

DECOY_RECORD = """\
id: antibiotic:nirmatrelvir
synonyms:
- PF07321332
genome_accession: genbank:LIPF01000008.1
"""

PTM_DUF_TRAIT = """\
identifier: Pfam:PF06226
label: Protein of unknown function (DUF1007)
canonical_examples:
- protein_id: UniProtKB:P22041
  protein_label: Uncharacterized 15.5 kDa protein
  reviewed: true
  family_classifications:
  - InterPro:IPR010412
  - Pfam:PF06226
  taxon_id: NCBITaxon:147
  taxon_label: Spirochaeta aurantia
"""

PTM_GO_TRAIT = """\
identifier: GO:0009058
label: biosynthetic process
canonical_examples:
- protein_id: UniProtKB:P0A8M6
  protein_label: Pole-localizer protein TmaR
  reviewed: true
  family_classifications:
  - Pfam:PF04363
  - Pfam:PF00001
- protein_id: UniProtKB:P11111
  family_classifications:
  - Pfam:PF00001
"""

PTM_UNRELATED = """\
identifier: Pfam:PF00001
label: 7 transmembrane receptor
"""

MECHS = (
    MechSource("TraitMech", "data/traits"),
    MechSource("AntibioticMech", "data/antibiotics"),
    MechSource("ProteinTraitsMech", "data/traits", "proteintraitsmech"),
)


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def _repo(root: Path, name: str, files: dict[str, str]) -> Path:
    repo = root / name
    repo.mkdir(parents=True)
    _git(repo, "init", "-q")
    for path, text in files.items():
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    _git(repo, "add", ".")
    _git(
        repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid",
        "commit", "-q", "-m", "seed",
    )
    return repo


@pytest.fixture()
def mechs_root(tmp_path: Path) -> Path:
    root = tmp_path / "Mechs"
    trait = _repo(
        root,
        "TraitMech",
        {
            "data/traits/genomics/example_system.yaml": TRAIT_RECORD,
            "data/traits/notes.txt": "DUF496 outside YAML is ignored",
        },
    )
    # Working-tree edits after the commit must not leak into the scan.
    (trait / "data/traits/genomics/example_system.yaml").write_text(
        "id: changed\ndescription: DUF496\n", encoding="utf-8"
    )
    _repo(root, "AntibioticMech", {"data/antibiotics/antiviral/decoy.yaml": DECOY_RECORD})
    _repo(
        root,
        "ProteinTraitsMech",
        {
            "data/traits/sequence/domain/pfam/duf1007-pf06226.yaml": PTM_DUF_TRAIT,
            "data/traits/function/pathway/go/biosynthetic-process.yaml": PTM_GO_TRAIT,
            "data/traits/sequence/family/pfam/7tm.yaml": PTM_UNRELATED,
        },
    )
    return root


def _lookup(accessions):
    assert accessions == ["P22041", "Q99999"]
    return {
        "P22041": UniProtPfamRow(
            "P22041", "P22041", "Uncharacterized 15.5 kDa protein", True, "147",
            "Spirochaeta aurantia", ("PF00001", "PF06226"),
        ),
        "Q99999": UniProtPfamRow(
            "Q99999", "Q99999", "Unrelated", False, "562", "Escherichia coli", ("PF04363",),
        ),
    }


def test_text_matches_use_identifier_boundaries() -> None:
    text = "PF07321332 LIPF01000008 Pfam:PF06226.5 IPR007458 DUF1007 DUF1998"
    assert FAMILIES.text_matches(text) == {
        "PF06226": {"record_mentions_pfam_id", "record_mentions_short_name"},
        "PF04363": {"record_mentions_interpro_id"},
    }
    assert FAMILIES.unlisted_short_names(text) == {"DUF1998"}


def test_compound_short_names_match_only_their_own_family() -> None:
    families = FamilyIndex.from_rows(
        [
            {**worklist_row("PF11940", proteins=1), "short_name": "DUF3458"},
            {**worklist_row("PF17432", proteins=1), "short_name": "DUF3458_C"},
            {**worklist_row("PF08331", proteins=1), "short_name": "QueG_DUF1730"},
        ]
    )
    assert families.text_matches("the DUF3458_C domain") == {
        "PF17432": {"record_mentions_short_name"}
    }
    assert families.text_matches("QueG_DUF1730 and DUF3458") == {
        "PF08331": {"record_mentions_short_name"},
        "PF11940": {"record_mentions_short_name"},
    }
    # An unlisted suffixed name is neither its base family nor an unlisted base name.
    assert families.text_matches("DUF1285_N") == {}
    assert families.unlisted_short_names("DUF1285_N DUF3458_C UPF0265") == {"UPF0265"}
    # Hyphens in prose still name the bare family.
    assert families.unlisted_short_names("a DUF1814-family toxin; COG5340-DUF1814") == {"DUF1814"}


def test_scan_reads_committed_yaml_and_links_proteins(mechs_root: Path) -> None:
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS, uniprot_lookup=_lookup)
    rows = {
        (row.source_mech, row.source_section, row.pfam_id or row.short_name, row.uniprot_accession):
        row
        for row in result.rows
    }

    assert set(rows) == {
        ("TraitMech", "record_text", "PF06226", ""),
        ("TraitMech", "record_text", "DUF1998", ""),
        ("TraitMech", "uniprot_accession", "PF06226", "P22041"),
        ("TraitMech", "uniprot_accession", "PF04363", "Q99999"),
        ("ProteinTraitsMech", "trait_identifier", "PF06226", ""),
        ("ProteinTraitsMech", "canonical_examples", "PF06226", "P22041"),
        ("ProteinTraitsMech", "canonical_examples", "PF04363", "P0A8M6"),
    }
    unlisted = rows[("TraitMech", "record_text", "DUF1998", "")]
    assert unlisted.unknown_status == NOT_IN_WORKLIST
    assert unlisted.source_record_id == "traitmech:000001"
    assert rows[("TraitMech", "uniprot_accession", "PF06226", "P22041")].family_mentioned_in_record
    assert not rows[("TraitMech", "uniprot_accession", "PF04363", "Q99999")].family_mentioned_in_record
    go_row = rows[("ProteinTraitsMech", "canonical_examples", "PF04363", "P0A8M6")]
    assert go_row.source_category == "function/pathway/go"
    assert go_row.family_mentioned_in_record is False
    assert result.uniprot_requested == 2
    assert result.mechs["TraitMech"]["records_scanned"] == 1
    assert result.mechs["ProteinTraitsMech"]["repository"].endswith("/proteintraitsmech")


def test_scan_without_lookup_keeps_text_rows(mechs_root: Path) -> None:
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS[:2])
    assert {row.source_section for row in result.rows} == {"record_text"}
    assert result.uniprot_requested == 2
    assert result.uniprot_resolved == 0


def test_scan_rejects_missing_checkout(tmp_path: Path) -> None:
    with pytest.raises(CrossMechError, match="not a git checkout"):
        scan_mechs(tmp_path, FAMILIES, mechs=MECHS[:1])


def test_uniprot_rows_map_secondary_accessions_and_skip_inactive() -> None:
    entry = {
        "primaryAccession": "P0A8M6",
        "secondaryAccessions": ["P76345"],
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "proteinDescription": {"recommendedName": {"fullName": {"value": "TmaR"}}},
        "organism": {"taxonId": 83333, "scientificName": "Escherichia coli"},
        "uniProtKBCrossReferences": [
            {"database": "Pfam", "id": "PF04363"},
            {"database": "PDB", "id": "1ABC"},
        ],
    }
    rows = uniprot_pfam_rows(entry, ["P76345", "Q00000"])
    assert list(rows) == ["P76345"]
    assert rows["P76345"].uniprot_accession == "P0A8M6"
    assert rows["P76345"].reviewed is True
    assert rows["P76345"].pfam_ids == ("PF04363",)
    # UniProt answers a merged secondary accession with an inactive stub, not the successor.
    merged = {
        "primaryAccession": "Q15086",
        "entryType": "Inactive",
        "inactiveReason": {"inactiveReasonType": "MERGED", "mergeDemergeTo": ["P04637"]},
    }
    assert uniprot_pfam_rows(merged, ["Q15086"]) == {}
    assert rows["P76345"].resolution == "secondary"
    assert load_uniprot_cache(render_uniprot_cache(rows)) == {"P76345": (rows["P76345"],)}


def test_uniprot_client_batches_and_follows_pages() -> None:
    seen: list[httpx.URL] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.url)
        if "cursor" not in str(request.url):
            assert request.url.params["fields"].endswith("xref_pfam")
            return httpx.Response(
                200,
                json={"results": [{"primaryAccession": "P1", "entryType": "reviewed"}]},
                headers={"Link": '<https://rest.uniprot.org/uniprotkb/search?cursor=2>; rel="next"'},
            )
        return httpx.Response(200, json={"results": [{"primaryAccession": "P2"}]})

    client = UniProtPfamClient(transport=httpx.MockTransport(handler), batch_size=5)
    assert set(client(["P1", "P2"])) == {"P1", "P2"}
    assert len(seen) == 2


def test_uniprot_client_reports_bad_payload() -> None:
    client = UniProtPfamClient(transport=httpx.MockTransport(lambda _: httpx.Response(200, json={})))
    with pytest.raises(CrossMechError, match="no results list"):
        client(["P1"])


def test_snapshot_manifest_validates(mechs_root: Path, tmp_path: Path) -> None:
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS, uniprot_lookup=_lookup)
    out = tmp_path / "cross_mech"
    manifest = write_cross_mech_snapshot(
        result,
        out,
        worklist_snapshot_id="interpro-pfam-duf-2026-10-01",
        source_ref="HEAD",
        snapshot_date="2026-10-05",
    )

    assert check_manifest(out / "cross-mech-duf-examples-2026-10-05.manifest.json") == []
    assert manifest["rows"]["total"] == len(result.rows)
    assert manifest["rows"]["unique_pfam_ids"] == 2
    assert manifest["rows"]["unlisted_short_names"] == 1
    assert manifest["snapshot"]["input_snapshot_ids"]["worklist"] == "interpro-pfam-duf-2026-10-01"
    header = render_cross_mech_tsv(result.rows).splitlines()[0].split("\t")
    assert header == manifest["schema"]["tsv_fieldnames"]


def test_dashboard_lists_cross_mech_links(mechs_root: Path, tmp_path: Path) -> None:
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS, uniprot_lookup=_lookup)
    rows = json.loads(
        json.dumps([{**row.tsv_row(), "link_basis": list(row.link_basis)} for row in result.rows])
    )
    for row in rows:
        for key in ("reviewed", "family_mentioned_in_record"):
            row[key] = {"true": True, "false": False}.get(row[key])
    out = tmp_path / "pages"
    render_site(
        [
            {**worklist_row("PF06226", proteins=5), "short_name": "DUF1007"},
            {**worklist_row("PF04363", proteins=3), "short_name": "DUF496"},
        ],
        [],
        input_ids={"worklist": "interpro-pfam-duf-2026-10-01"},
        out_dir=out,
        cross_mech_rows=rows,
        cross_mech_sources=result.mechs,
    )
    payload = json.loads((out / "index.json").read_text(encoding="utf-8"))
    by_pfam = {family["pfam_id"]: family["cross_mech"] for family in payload["families"]}
    assert by_pfam["PF06226"]["records_by_mech"] == {"ProteinTraitsMech": 1, "TraitMech": 1}
    assert by_pfam["PF06226"]["example_proteins"] == 1
    assert payload["summary"]["cross_mech"]["proteins"] == 3
    # Trait-record-only links are a flag, not a per-Mech count or a headline family.
    assert payload["summary"]["cross_mech"]["families"] == 2
    assert by_pfam["PF06226"]["protein_traits_record"] is True

    soup = BeautifulSoup((out / "index.html").read_text(encoding="utf-8"), "html.parser")
    curated = soup.select("section")[1]
    assert "DUF1998" in curated.get_text()
    assert "not in worklist" in curated.get_text()
    assert "ProteinTraitsMech" not in curated.select_one("tbody").get_text()
    links = [link["href"] for link in curated.select("tbody a")]
    assert any("/TraitMech/blob/" in link for link in links)
    assert "https://rest.uniprot.org/uniprotkb/P22041" in links


def test_report_lists_curated_rows_and_reuse_gaps(mechs_root: Path, tmp_path: Path) -> None:
    from dufmech.cross_mech_report import main as report_main
    from dufmech.cross_mech_report import render_cross_mech_report

    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS, uniprot_lookup=_lookup)
    out = tmp_path / "cross_mech"
    manifest = write_cross_mech_snapshot(
        result,
        out,
        worklist_snapshot_id="interpro-pfam-duf-2026-10-01",
        source_ref="origin/main",
        snapshot_date="2026-10-05",
    )
    rows = json.loads((out / "cross-mech-duf-examples-2026-10-05.json").read_text("utf-8"))
    text = render_cross_mech_report(rows, manifest)

    assert "1 names do not match a current worklist short name: DUF1998" in text
    assert "| PF06226 | P22041 |" in text
    assert "| DUF496 (PF04363) | Q99999 Unrelated | TraitMech |" in text
    assert "P22041 Uncharacterized" not in text.split("### ProteinTraitsMech")[1].split("###")[0]
    assert "| GO:0009058 biosynthetic process | DUF496 | P0A8M6 |" in text

    reports = tmp_path / "reports"
    args = ["--cross-mech-dir", str(out), "--out-dir", str(reports), "--worklist-json",
            str(REPO_WORKLISTS / "interpro-pfam-duf-2026-10-01.json")]
    assert report_main(args) == 0
    assert report_main([*args, "--check"]) == 0
    (reports / "cross-mech-duf-examples-2026-10-05.md").write_text("stale", encoding="utf-8")
    assert report_main([*args, "--check"]) == 1



REPO_WORKLISTS = Path(__file__).resolve().parents[1] / "data" / "worklists"


def test_render_from_paths_validates_cross_mech_snapshot(mechs_root: Path, tmp_path: Path) -> None:
    import shutil

    from dufmech.pages import render_from_paths
    from dufmech.report import ReportError

    worklists = tmp_path / "worklists"
    shutil.copytree(REPO_WORKLISTS, worklists)
    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS, uniprot_lookup=_lookup)
    cross = tmp_path / "cross_mech"
    write_cross_mech_snapshot(
        result, cross, worklist_snapshot_id="interpro-pfam-duf-1999-01-01",
        source_ref="HEAD", snapshot_date="2026-10-05",
    )
    with pytest.raises(ReportError, match="regenerate the cross-Mech snapshot"):
        render_from_paths(out_dir=tmp_path / "pages", worklists_dir=worklists, cross_mech_dir=cross)

    cross = tmp_path / "matching_cross_mech"
    write_cross_mech_snapshot(
        result, cross, worklist_snapshot_id="interpro-pfam-duf-2026-10-01",
        source_ref="HEAD", snapshot_date="2026-10-05",
    )
    render_from_paths(
        out_dir=tmp_path / "pages", worklists_dir=worklists, cross_mech_dir=cross,
        worklist_json=worklists / "interpro-pfam-duf-2026-10-01.json",
    )
    payload = json.loads((tmp_path / "pages" / "index.json").read_text(encoding="utf-8"))
    assert payload["inputs"]["cross_mech"] == "cross-mech-duf-examples-2026-10-05"


def test_dashboard_rejects_cross_mech_family_absent_from_worklist(tmp_path: Path) -> None:
    from dufmech.report import ReportError

    row = {
        "pfam_id": "PF99999", "short_name": "DUF9", "source_mech": "TraitMech",
        "source_section": "record_text", "uniprot_accession": "",
    }
    with pytest.raises(ReportError, match="absent from worklist: PF99999"):
        render_site(
            [worklist_row("PF00001", proteins=1)], [], input_ids={}, out_dir=tmp_path / "p",
            cross_mech_rows=[row],
        )


def test_cli_records_uniprot_cache_provenance(
    mechs_root: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import shutil

    from dufmech import cross_mech_snapshot_cli as cli

    calls: list[list[str]] = []

    class FakeClient:
        def __call__(self, accessions):
            calls.append(list(accessions))
            return {key: value for key, value in _lookup(["P22041", "Q99999"]).items()
                    if key in accessions}

    monkeypatch.setattr(cli, "UniProtPfamClient", FakeClient)
    worklists = tmp_path / "worklists"
    shutil.copytree(REPO_WORKLISTS, worklists)
    cache = tmp_path / "raw" / "uniprot.json"
    args = [
        "--mechs-root", str(mechs_root), "--worklists-dir", str(worklists),
        "--mech", "TraitMech", "--uniprot-cache", str(cache), "--snapshot-date", "2026-10-05",
    ]
    out = tmp_path / "cross_mech"
    manifest_path = out / "cross-mech-duf-examples-2026-10-05.manifest.json"

    assert cli.main([*args, "--out-dir", str(out)]) == 0
    first = json.loads(manifest_path.read_text(encoding="utf-8"))["source"]
    assert calls == [["P22041", "Q99999"]]
    assert first["uniprotkb_lookup"]["mode"] == "cache"
    assert first["uniprotkb_lookup"]["fetched_accessions"] == 2
    assert first["uniprotkb_accessions_unresolved"] == []

    replay = tmp_path / "replay"
    assert cli.main([*args, "--out-dir", str(replay)]) == 0
    replay_manifest = json.loads((replay / manifest_path.name).read_text(encoding="utf-8"))
    second = replay_manifest["source"]["uniprotkb_lookup"]
    assert len(calls) == 1
    assert second["cache_hits"] == 2
    assert "fetched_at" not in second
    assert second["cache_sha256"] == first["uniprotkb_lookup"]["cache_sha256"]


def _entry(accession: str, pfams: tuple[str, ...]) -> dict:
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "proteinDescription": {"submissionNames": [{"fullName": {"value": f"Protein {accession}"}}]},
        "organism": {"taxonId": 562, "scientificName": "Escherichia coli"},
        "uniProtKBCrossReferences": [{"database": "Pfam", "id": pfam} for pfam in pfams],
    }


def _stub(accession: str, kind: str, targets: list[str]) -> dict:
    reason = {"inactiveReasonType": kind}
    if targets:
        reason["mergeDemergeTo"] = targets
    return {"primaryAccession": accession, "entryType": "Inactive", "inactiveReason": reason}


def test_uniprot_client_follows_merged_and_demerged_successors() -> None:
    entries = {
        "P24247": _stub("P24247", "DEMERGED", ["P0AF13", "P0AF12"]),
        "Q15086": _stub("Q15086", "MERGED", ["P04637"]),
        "A0A045J7I4": _stub("A0A045J7I4", "DELETED", []),
        "P0AF12": _entry("P0AF12", ("PF04363",)),
        "P0AF13": _entry("P0AF13", ("PF04363", "PF00001")),
        "P04637": _entry("P04637", ("PF06226",)),
    }
    queries: list[list[str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        wanted = [part.split(":", 1)[1] for part in request.url.params["query"].split(" OR ")]
        queries.append(wanted)
        return httpx.Response(200, json={"results": [entries[a] for a in wanted if a in entries]})

    client = UniProtPfamClient(transport=httpx.MockTransport(handler))
    resolved = client(["A0A045J7I4", "P24247", "Q15086"])

    assert queries[1] == ["P04637", "P0AF12", "P0AF13"]
    assert set(resolved) == {"P24247", "Q15086"}
    assert [row.uniprot_accession for row in resolved["P24247"]] == ["P0AF12", "P0AF13"]
    assert {row.resolution for row in resolved["P24247"]} == {"demerged"}
    assert {row.requested_accession for row in resolved["P24247"]} == {"P24247"}
    assert resolved["Q15086"][0].resolution == "merged"
    assert load_uniprot_cache(render_uniprot_cache(resolved)) == resolved


def test_scan_rows_keep_cited_accession_for_successors(mechs_root: Path) -> None:
    def lookup(accessions):
        return {
            "P22041": (
                UniProtPfamRow("P22041", "P0AF12", "Successor A", False, "562", "E. coli",
                               ("PF04363",), resolution="demerged"),
                UniProtPfamRow("P22041", "P0AF13", "Successor B", False, "562", "E. coli",
                               ("PF04363",), resolution="demerged"),
            ),
        }

    result = scan_mechs(mechs_root, FAMILIES, mechs=MECHS[:1], uniprot_lookup=lookup)
    rows = [row for row in result.rows if row.source_section == "uniprot_accession"]

    assert [(row.uniprot_accession, row.cited_uniprot_accession) for row in rows] == [
        ("P0AF12", "P22041"),
        ("P0AF13", "P22041"),
    ]
    assert all("uniprot_demerged_successor" in row.link_basis for row in rows)
    assert result.uniprot_unresolved == ["Q99999"]
    header = render_cross_mech_tsv(rows).splitlines()[0].split("\t")
    assert header[-1] == "cited_uniprot_accession"
