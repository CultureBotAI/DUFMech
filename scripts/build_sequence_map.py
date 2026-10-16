"""Build the DUFMech 2D ESM-2 protein sequence embedding map (PaCMAP).

Selects representative protein examples from data/protein_examples/, reuses vectors
from ProteinTraitsMech's ESM-2 cache and /tmp/cross-mech-esm2-cache, embeds any
uncached sequences with facebook/esm2_t33_650M_UR50D on MPS, projects with PaCMAP,
and writes data/embeddings/sequence_map.json.

Run via:
  uv run --with torch --with transformers --with pacmap python scripts/build_sequence_map.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from embed_records import load_corpus_families

from dufmech.protein_examples import latest_protein_snapshot
from dufmech.report import load_json_rows

OUT_PATH = ROOT / "data" / "embeddings" / "sequence_map.json"

PTM_CACHE_DIR = (
    ROOT.parent / "ProteinTraitsMech" / "data" / "embeddings" / "esm2"
)
SHARED_CACHE_DIR = Path("/tmp/cross-mech-esm2-cache")

MODEL_ID = "facebook/esm2_t33_650M_UR50D"
MODEL_REV = "08e4846e537177426273712802403f7ba8261b6c"
MAX_RESIDUES = 1022
POOLING = "mean_residue_l2"
NEIGHBORS = 10
RANDOM_SEED = 42

SEED_ORDER = [
    "UNKNOWN_CANDIDATE",
    "EX_DUF",
    "KNOWN_HISTORICAL_DUF",
]
CURATION_ORDER = [
    "IN_PROGRESS",
    "SEEDED",
]
LENGTH_BINS = [
    "<= 200 aa",
    "201-500 aa",
    "501-1,022 aa",
    "> 1,022 aa",
]


def cache_tag() -> str:
    spec = json.dumps(
        {
            "model": MODEL_ID,
            "revision": MODEL_REV,
            "max_residues": MAX_RESIDUES,
            "pooling": POOLING,
        },
        sort_keys=True,
    )
    return hashlib.sha256(spec.encode()).hexdigest()[:12]


def length_bin(length: int) -> str:
    if length <= 200:
        return "<= 200 aa"
    if length <= 500:
        return "201-500 aa"
    if length <= 1022:
        return "501-1,022 aa"
    return "> 1,022 aa"


def load_caches(tag: str) -> dict[str, np.ndarray]:
    cached: dict[str, np.ndarray] = {}
    for cdir in (PTM_CACHE_DIR, SHARED_CACHE_DIR):
        idx_path = cdir / f"cache_{tag}.json"
        vec_path = cdir / f"cache_{tag}.f32.npy"
        if not idx_path.exists() or not vec_path.exists():
            continue
        meta = json.loads(idx_path.read_text(encoding="utf-8"))
        hashes: list[str] = meta.get("hashes", [])
        vecs = np.load(vec_path)
        if len(hashes) != vecs.shape[0]:
            continue
        for h, v in zip(hashes, vecs):
            cached[h] = v
    return cached


def save_shared_cache(tag: str, cache: dict[str, np.ndarray]) -> None:
    SHARED_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    hashes = sorted(cache.keys())
    vecs = np.stack([cache[h] for h in hashes], axis=0).astype(np.float32)
    idx_path = SHARED_CACHE_DIR / f"cache_{tag}.json"
    vec_path = SHARED_CACHE_DIR / f"cache_{tag}.f32.npy"
    idx_path.write_text(
        json.dumps(
            {
                "meta": {
                    "model": MODEL_ID,
                    "revision": MODEL_REV,
                    "max_residues": MAX_RESIDUES,
                    "pooling": POOLING,
                    "dim": int(vecs.shape[1]),
                },
                "hashes": hashes,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    np.save(vec_path, vecs)


def embed_uncached(sequences: dict[str, str], cached: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    missing = [(h, seq) for h, seq in sequences.items() if h not in cached]
    if not missing:
        print(f"All {len(sequences)} sequences found in ESM-2 cache!", flush=True)
        return cached

    print(
        f"Embedding {len(missing)} uncached sequences ({len(sequences) - len(missing)} cached)...",
        flush=True,
    )
    import torch
    from transformers import AutoModel, AutoTokenizer

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, revision=MODEL_REV)
    model = AutoModel.from_pretrained(MODEL_ID, revision=MODEL_REV).to(device)
    model.eval()

    missing.sort(key=lambda item: len(item[1]))
    token_budget = 4096
    batch: list[tuple[str, str]] = []
    batch_tokens = 0

    def flush(items: list[tuple[str, str]]) -> None:
        if not items:
            return
        hashes = [h for h, _ in items]
        seqs = [s[:MAX_RESIDUES] for _, s in items]
        enc = tokenizer(
            seqs,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_RESIDUES + 2,
        )
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)
        with torch.no_grad():
            out = model(input_ids=input_ids, attention_mask=attention_mask)
            hidden = out.last_hidden_state
            lengths = attention_mask.sum(dim=1)
            mask = attention_mask.clone()
            mask[:, 0] = 0
            for row_idx, seq_len in enumerate(lengths.tolist()):
                if seq_len > 1:
                    mask[row_idx, seq_len - 1] = 0
            mask_f = mask.unsqueeze(-1).to(hidden.dtype)
            denom = mask_f.sum(dim=1).clamp(min=1.0)
            pooled = (hidden * mask_f).sum(dim=1) / denom
            norms = pooled.norm(p=2, dim=1, keepdim=True).clamp(min=1e-12)
            normed = (pooled / norms).cpu().numpy().astype(np.float32)
        for h, v in zip(hashes, normed):
            cached[h] = v

    done = 0
    for h, seq in missing:
        eff_len = min(len(seq), MAX_RESIDUES) + 2
        if batch and (batch_tokens + eff_len > token_budget or len(batch) >= 16):
            flush(batch)
            done += len(batch)
            if done % 100 == 0 or done == len(missing):
                print(f"  embedded {done}/{len(missing)}", flush=True)
            batch = []
            batch_tokens = 0
        batch.append((h, seq))
        batch_tokens += eff_len
    if batch:
        flush(batch)
        done += len(batch)
        print(f"  embedded {done}/{len(missing)}", flush=True)

    return cached


def main() -> None:
    tag = cache_tag()
    cached = load_caches(tag)
    print(f"Loaded {len(cached)} vectors from ESM-2 caches (tag={tag})", flush=True)

    families = {str(f["pfam_id"]): f for f in load_corpus_families()}
    pe_path = latest_protein_snapshot(ROOT / "data" / "protein_examples")
    if pe_path is None:
        raise RuntimeError("No protein_examples snapshot found")
    pe_rows = load_json_rows(pe_path)

    proteins_by_acc: dict[str, dict[str, Any]] = {}
    sequences_by_hash: dict[str, str] = {}
    n_mentions = 0
    family_ids_covered: set[str] = set()

    for row in pe_rows:
        pfam_id = str(row["pfam_id"])
        fam = families.get(pfam_id, {})
        exs = row.get("examples") or []
        if not exs:
            continue
        seed_status = str(fam.get("unknown_status") or "UNKNOWN_CANDIDATE")
        cur_status = str(fam.get("curation_status") or "SEEDED")
        for idx, ex in enumerate(exs):
            seq = (ex.get("sequence") or "").strip()
            sh = (ex.get("sequence_sha256") or "").strip()
            acc = (ex.get("uniprot_accession") or "").strip()
            if not seq or not sh or not acc:
                continue
            is_cached = sh in cached
            is_ptm_primary = idx == 0 and ex.get("sequence_origin") == "PTM_REGISTRY_MIRROR"
            is_curated_primary = idx == 0 and cur_status != "SEEDED"
            if not (is_cached or is_ptm_primary or is_curated_primary):
                continue

            sequences_by_hash[sh] = seq
            family_ids_covered.add(pfam_id)
            n_mentions += 1
            pid = f"UniProtKB:{acc}"
            entry = proteins_by_acc.get(pid)
            rec_item = {
                "id": pfam_id,
                "short_name": str(fam.get("short_name") or pfam_id),
                "label": str(fam.get("name") or pfam_id),
                "seed_status": seed_status,
                "curation_status": cur_status,
                "page": f"families/{pfam_id}.html",
            }
            if entry is None:
                seq_len = int(ex.get("sequence_length") or len(seq))
                proteins_by_acc[pid] = {
                    "id": pid,
                    "uniprot_accession": acc,
                    "label": str(ex.get("protein_name") or acc),
                    "organism": str(ex.get("organism") or ""),
                    "taxon_id": str(ex.get("taxon_id") or ""),
                    "length": seq_len,
                    "length_bin": length_bin(seq_len),
                    "truncated": seq_len > MAX_RESIDUES,
                    "sequence_sha256": sh,
                    "sequence_origin": str(ex.get("sequence_origin") or "UNIPROT_FETCH"),
                    "reviewed": bool(ex.get("reviewed")),
                    "seed_statuses": [seed_status],
                    "curation_statuses": [cur_status],
                    "records": [rec_item],
                }
            else:
                if seed_status not in entry["seed_statuses"]:
                    entry["seed_statuses"].append(seed_status)
                if cur_status not in entry["curation_statuses"]:
                    entry["curation_statuses"].append(cur_status)
                if not any(r["id"] == pfam_id for r in entry["records"]):
                    entry["records"].append(rec_item)

    print(
        f"Selected {len(proteins_by_acc)} unique proteins ({len(sequences_by_hash)} unique "
        f"sequences) across {len(family_ids_covered)} DUF/Pfam families.",
        flush=True,
    )

    cached = embed_uncached(sequences_by_hash, cached)
    save_shared_cache(tag, cached)

    ordered_pids = sorted(proteins_by_acc.keys())
    X = np.stack(
        [cached[proteins_by_acc[pid]["sequence_sha256"]] for pid in ordered_pids],
        axis=0,
    ).astype(np.float32)

    X_centered = X - X.mean(axis=0, keepdims=True)
    norms = np.linalg.norm(X_centered, axis=1, keepdims=True)
    Z = X_centered / np.clip(norms, 1e-12, None)

    import pacmap

    n_neighbors = min(NEIGHBORS, max(2, len(ordered_pids) - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        apply_pca=False,
        random_state=RANDOM_SEED,
    )
    coords = reducer.fit_transform(Z, init="pca")
    mins = coords.min(axis=0)
    maxs = coords.max(axis=0)
    span = np.where((maxs - mins) > 1e-9, maxs - mins, 1.0)
    xy = (coords - mins) / span

    proteins_out: list[dict[str, Any]] = []
    channels_seen: set[str] = set()
    for idx, pid in enumerate(ordered_pids):
        p = proteins_by_acc[pid]
        origin = p["sequence_origin"]
        channels_seen.add(origin)
        primary_seed = p["seed_statuses"][0]
        primary_cur = (
            "IN_PROGRESS" if "IN_PROGRESS" in p["curation_statuses"] else p["curation_statuses"][0]
        )
        proteins_out.append(
            {
                "id": p["id"],
                "uniprot_accession": p["uniprot_accession"],
                "label": p["label"],
                "organism": p["organism"],
                "taxon_id": p["taxon_id"],
                "length": p["length"],
                "length_bin": p["length_bin"],
                "truncated": p["truncated"],
                "x": round(float(xy[idx, 0]), 4),
                "y": round(float(xy[idx, 1]), 4),
                "primary_seed_status": primary_seed,
                "primary_curation_status": primary_cur,
                "seed_statuses": p["seed_statuses"],
                "curation_statuses": p["curation_statuses"],
                "sequence_origin": origin,
                "reviewed": p["reviewed"],
                "records": p["records"],
            }
        )

    payload = {
        "model": MODEL_ID,
        "revision": MODEL_REV[:12],
        "dim": int(X.shape[1]),
        "pooling": POOLING,
        "max_residues": MAX_RESIDUES,
        "method": "PaCMAP",
        "neighbors": n_neighbors,
        "n_proteins": len(proteins_out),
        "n_records": len(family_ids_covered),
        "n_mentions": n_mentions,
        "seed_statuses": SEED_ORDER,
        "curation_statuses": CURATION_ORDER,
        "channels": sorted(channels_seen),
        "length_bins": LENGTH_BINS,
        "proteins": proteins_out,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes, "
        f"{len(proteins_out)} proteins across {len(family_ids_covered)} families)",
        flush=True,
    )


if __name__ == "__main__":
    main()
