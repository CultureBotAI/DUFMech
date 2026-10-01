from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from io import StringIO

import httpx

from dufmech.member_snapshot import (
    collect_member_uniref_rows,
    write_member_uniref_snapshot,
)
from dufmech.member_snapshot_cli import main as freeze_member_snapshot
from dufmech.member_uniref import PfamMemberUniRefRow
from dufmech.protein_members import InterProPfamProteinClient
from dufmech.uniprotkb import UniProtKbMetadataClient
from dufmech.uniref import UniProtIdMappingClient


def joined_row(accession: str = "B2BDZ4") -> PfamMemberUniRefRow:
    return PfamMemberUniRefRow(
        pfam_id="PF01519",
        uniprot_accession=accession,
        uniprot_id=f"{accession}_MYCPM",
        reviewed=False,
        name="Uncharacterized protein",
        protein_name="UPF0134 protein MPN_139",
        source_database="unreviewed",
        length=163,
        taxon_id="2104",
        organism="Mycoplasmoides pneumoniae",
        uniprot_taxon_id="2104",
        uniprot_organism="Mycoplasmoides pneumoniae",
        gene="MPN139",
        in_alphafold=True,
        match_count=1,
        match_ranges=("39-154",),
        proteome_ids=("UP000000808",),
        uniref_id="UniRef90_P75259",
        uniref_type="UniRef90",
        uniref_name="Cluster: UPF0134 protein MPN_139",
        uniref_updated="2026-06-10",
        uniref_member_count=2,
        uniref_organism_count=2,
        uniref_common_taxon_id="2104",
        uniref_common_taxon_name="Mycoplasmoides pneumoniae",
        representative_accession="P75259",
        representative_member_id="Y139_MYCPN",
        representative_protein_name="UPF0134 protein MPN_139",
        representative_taxon_id="272634",
        representative_length=163,
        uniref_seed_id="P75259",
        member_source_url=f"https://www.ebi.ac.uk/interpro/protein/UniProt/{accession}/",
        uniprot_source_url=f"https://rest.uniprot.org/uniprotkb/{accession}",
        uniref_source_url="https://rest.uniprot.org/uniref/UniRef90_P75259",
    )


def interpro_protein(accession: str) -> dict:
    return {
        "metadata": {
            "accession": accession,
            "name": "Uncharacterized protein",
            "source_database": "unreviewed",
            "length": 163,
            "source_organism": {
                "taxId": "2104",
                "scientificName": "Mycoplasmoides pneumoniae",
            },
            "gene": "MPN139",
            "in_alphafold": True,
        },
        "entries": [
            {
                "accession": "PF01519",
                "entry_protein_locations": [
                    {
                        "fragments": [{"start": 39, "end": 154}],
                    }
                ],
            }
        ],
    }


def uniprotkb_entry(accession: str) -> dict:
    return {
        "primaryAccession": accession,
        "uniProtkbId": f"{accession}_MYCPM",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "proteinDescription": {
            "recommendedName": {
                "fullName": {"value": "UPF0134 protein MPN_139"},
            },
        },
        "organism": {
            "taxonId": 2104,
            "scientificName": "Mycoplasmoides pneumoniae",
        },
        "uniProtKBCrossReferences": [{"database": "Proteomes", "id": "UP000000808"}],
    }


def uniref_result(accession: str) -> dict:
    return {
        "from": accession,
        "to": {
            "id": f"UniRef90_{accession}",
            "entryType": "UniRef90",
            "name": "Cluster: UPF0134 protein MPN_139",
            "updated": "2026-06-10",
            "memberCount": 2,
            "organismCount": 2,
            "commonTaxon": {
                "scientificName": "Mycoplasmoides pneumoniae",
                "taxonId": 2104,
            },
            "representativeMember": {
                "accessions": [accession],
                "memberId": f"{accession}_MYCPM",
                "proteinName": "UPF0134 protein MPN_139",
                "organismTaxId": 272634,
                "sequenceLength": 163,
            },
            "seedId": accession,
        },
    }


def test_collect_member_uniref_rows_orchestrates_three_clients() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/interpro/api/protein/UniProt/entry/pfam/PF01519/":
            assert request.url.params["page_size"] == "50"
            return httpx.Response(
                200,
                json={
                    "results": [
                        interpro_protein("B2BDZ4"),
                        interpro_protein("B2BDZ3"),
                    ],
                },
            )
        if request.url.path == "/uniprotkb/search":
            return httpx.Response(
                200,
                json={
                    "results": [
                        uniprotkb_entry("B2BDZ4"),
                        uniprotkb_entry("B2BDZ3"),
                    ],
                },
            )
        if request.url.path == "/idmapping/run":
            payload = request.read().decode("utf-8")
            assert "ids=B2BDZ3%2CB2BDZ4" in payload
            return httpx.Response(200, json={"jobId": "job-1"})
        assert request.url.path == "/idmapping/status/job-1"
        return httpx.Response(
            200,
            json={
                "results": [
                    uniref_result("B2BDZ4"),
                    uniref_result("B2BDZ3"),
                ]
            },
        )

    transport = httpx.MockTransport(handler)
    rows = collect_member_uniref_rows(
        ["PF01519"],
        member_client=InterProPfamProteinClient(transport=transport),
        metadata_client=UniProtKbMetadataClient(transport=transport),
        uniref_client=UniProtIdMappingClient(
            poll_interval=0,
            transport=transport,
        ),
        page_size=50,
    )

    assert [(row.pfam_id, row.uniprot_accession) for row in rows] == [
        ("PF01519", "B2BDZ3"),
        ("PF01519", "B2BDZ4"),
    ]
    assert rows[0].uniref_id == "UniRef90_B2BDZ3"
    assert rows[0].uniprot_id == "B2BDZ3_MYCPM"
    assert rows[0].proteome_ids == ("UP000000808",)


def test_write_member_uniref_snapshot_writes_artifacts_and_manifest(tmp_path) -> None:
    manifest = write_member_uniref_snapshot(
        [joined_row("B2BDZ4"), joined_row("B2BDZ3")],
        tmp_path,
        snapshot_date="2026-10-01",
        generated_at=datetime(2026, 10, 1, 3, 4, 5, tzinfo=timezone.utc),
        seed_snapshot_id="interpro-pfam-duf-2026-10-01",
        page_size=50,
    )

    json_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.json"
    tsv_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.tsv"
    manifest_path = tmp_path / "pfam-uniprot-uniref90-2026-10-01.manifest.json"

    assert json_path.is_file()
    assert tsv_path.is_file()
    assert manifest_path.is_file()

    assert manifest == json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["snapshot"] == {
        "id": "pfam-uniprot-uniref90-2026-10-01",
        "date": "2026-10-01",
        "generated_at": "2026-10-01T03:04:05Z",
        "seed_snapshot_id": "interpro-pfam-duf-2026-10-01",
    }
    assert manifest["source"]["uniref_target"] == "UniRef90"
    assert manifest["rows"]["total"] == 2
    assert manifest["rows"]["unique_pfam_families"] == 1
    assert manifest["rows"]["unique_uniprot_accessions"] == 2
    assert manifest["rows"]["unique_uniref_clusters"] == 1
    assert manifest["rows"]["with_proteome_ids"] == 2
    assert manifest["files"]["json"]["sha256"] == hashlib.sha256(
        json_path.read_bytes()
    ).hexdigest()
    assert manifest["files"]["tsv"]["sha256"] == hashlib.sha256(
        tsv_path.read_bytes()
    ).hexdigest()

    json_rows = json.loads(json_path.read_text(encoding="utf-8"))
    tsv_rows = list(
        csv.DictReader(StringIO(tsv_path.read_text(encoding="utf-8")), dialect="excel-tab")
    )
    assert [row["uniprot_accession"] for row in json_rows] == ["B2BDZ3", "B2BDZ4"]
    assert [row["proteome_ids"] for row in tsv_rows] == [
        "UP000000808",
        "UP000000808",
    ]


def test_freeze_member_snapshot_cli_reads_saved_worklist(
    tmp_path,
    monkeypatch,
    capsys,
) -> None:
    def fake_collect(pfam_ids, **kwargs) -> list[PfamMemberUniRefRow]:
        assert pfam_ids == ["PF01519"]
        assert kwargs["limit_members_per_family"] == 1
        return [joined_row()]

    monkeypatch.setattr(
        "dufmech.member_snapshot_cli.collect_member_uniref_rows",
        fake_collect,
    )

    input_path = tmp_path / "interpro-pfam-duf-2026-10-01.json"
    input_path.write_text(json.dumps([{"pfam_id": "PF01519"}]), encoding="utf-8")

    assert (
        freeze_member_snapshot(
            [
                "--input-json",
                str(input_path),
                "--limit-members-per-family",
                "1",
                "--snapshot-date",
                "2026-10-01",
                "--out-dir",
                str(tmp_path / "worklists"),
            ]
        )
        == 0
    )

    assert "wrote pfam-uniprot-uniref90-2026-10-01 (1 rows)" in capsys.readouterr().out
    assert (
        tmp_path
        / "worklists"
        / "pfam-uniprot-uniref90-2026-10-01.manifest.json"
    ).is_file()
