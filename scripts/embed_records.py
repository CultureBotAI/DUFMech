"""Embed all DUFMech family records with a local sentence-transformer model.

Writes into data/embeddings/:
  vectors.npy   float32 array of shape (N, D), L2-normalised, row-aligned to ids.json
  ids.json      ordered list of pfam_id strings
  meta.json     model name, dimension, record count, text sha256 per record

Run via:
  uv run --with sentence-transformers --with torch python scripts/embed_records.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from dufmech.cross_mech_snapshot import (
    CROSS_MECH_DIR,
    CROSS_MECH_STEM,
    load_cross_mech_snapshot,
)
from dufmech.report import family_index, latest_snapshot_path, load_latest_rows

OUT_DIR = ROOT / "data" / "embeddings"
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"


def load_corpus_families() -> list[dict]:
    """Load all DUF/Pfam families with seed status, curation status, and cross-Mech links."""
    worklist_rows, score_rows, input_ids = load_latest_rows(ROOT / "data" / "worklists")
    families = family_index(worklist_rows, score_rows)
    curated_ids = {
        p.stem for p in (ROOT / "curation" / "families").glob("*.yaml")
    } if (ROOT / "curation" / "families").is_dir() else set()
    cm_path = latest_snapshot_path(ROOT / CROSS_MECH_DIR, CROSS_MECH_STEM, required=False)
    cm_by_pfam: dict[str, set[str]] = {}
    if cm_path is not None:
        cm_rows, _ = load_cross_mech_snapshot(
            cm_path, worklist_rows=worklist_rows, worklist_snapshot_id=input_ids["worklist"],
        )
        for row in cm_rows:
            pfam_id = row.get("pfam_id") or ""
            source_mech = row.get("source_mech") or ""
            if pfam_id and source_mech:
                cm_by_pfam.setdefault(pfam_id, set()).add(source_mech)
    enriched: list[dict] = []
    for fam in sorted(families, key=lambda item: str(item["pfam_id"])):
        pfam_id = str(fam["pfam_id"])
        item = dict(fam)
        item["curation_status"] = "IN_PROGRESS" if pfam_id in curated_ids else "SEEDED"
        item["cross_mechs"] = sorted(cm_by_pfam.get(pfam_id, set()))
        enriched.append(item)
    return enriched


def record_to_text(fam: dict) -> str:
    """Flatten a DUF/Pfam family record into embedding text."""
    parts: list[str] = []
    pfam_id = fam.get("pfam_id", "")
    short_name = fam.get("short_name", "")
    name = fam.get("name", "")
    interpro_id = fam.get("interpro_id", "")
    parts.append(f"Pfam family: {pfam_id} ({short_name}) — {name} [{interpro_id}]")
    parts.append(f"Seed category: {fam.get('unknown_status', 'UNKNOWN_CANDIDATE')}")
    char_status = fam.get("characterization_status") or "UNSCORED"
    parts.append(f"Characterization status: {char_status}")
    parts.append(f"Curation status: {fam.get('curation_status', 'SEEDED')}")
    reasons = fam.get("candidate_reasons") or []
    if reasons:
        parts.append("Candidate reasons: " + ", ".join(str(r) for r in reasons))
    demotions = fam.get("demotion_reasons") or []
    if demotions:
        parts.append("Demotion reasons: " + ", ".join(str(r) for r in demotions))
    mechs = fam.get("cross_mechs") or []
    if mechs:
        parts.append("Cross-Mech links: " + ", ".join(str(m) for m in mechs))
    desc = (fam.get("description") or "").strip()
    if desc:
        parts.append("Description: " + desc)
    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--batch-size", type=int, default=64)
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer

    families = load_corpus_families()
    ids: list[str] = []
    texts: list[str] = []
    hashes: dict[str, str] = {}
    for fam in families:
        pfam_id = str(fam["pfam_id"])
        txt = record_to_text(fam)
        ids.append(pfam_id)
        texts.append(txt)
        hashes[pfam_id] = hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]

    print(f"Embedding {len(texts)} DUF/Pfam families with {args.model} …")
    model = SentenceTransformer(args.model)
    vecs = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype(np.float32)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.save(OUT_DIR / "vectors.npy", vecs)
    (OUT_DIR / "ids.json").write_text(json.dumps(ids, indent=2) + "\n", encoding="utf-8")
    meta = {
        "model": args.model,
        "dim": int(vecs.shape[1]),
        "count": len(ids),
        "normalized": True,
        "text_sha256_prefix": hashes,
    }
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {vecs.shape} -> {OUT_DIR}")


if __name__ == "__main__":
    main()
