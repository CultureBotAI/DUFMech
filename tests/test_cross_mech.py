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
    assert uniprot_pfam_rows({"primaryAccession": "X1", "entryType": "Inactive"}, ["X1"]) == {}
    assert load_uniprot_cache(render_uniprot_cache(rows)) == rows


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
    assert by_pfam["PF06226"]["records_by_mech"] == {"ProteinTraitsMech": 2, "TraitMech": 2}
    assert by_pfam["PF06226"]["example_proteins"] == 1
    assert payload["summary"]["cross_mech"]["proteins"] == 3

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
    assert report_main(["--cross-mech-dir", str(out), "--out-dir", str(reports)]) == 0
    assert report_main(["--cross-mech-dir", str(out), "--out-dir", str(reports), "--check"]) == 0
    (reports / "cross-mech-duf-examples-2026-10-05.md").write_text("stale", encoding="utf-8")
    assert report_main(["--cross-mech-dir", str(out), "--out-dir", str(reports), "--check"]) == 1
