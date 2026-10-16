"""Project DUFMech family text embeddings to 2D for the interactive corpus map.

Reads data/embeddings/{vectors.npy,ids.json,meta.json} plus the latest worklist
snapshot and writes data/embeddings/corpus_map.json.

Run via:
  uv run --with pacmap python scripts/embed_map.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from embed_records import load_corpus_families

EMB_DIR = ROOT / "data" / "embeddings"

SEED_ORDER = [
    "UNKNOWN_CANDIDATE",
    "EX_DUF",
    "KNOWN_HISTORICAL_DUF",
]
CURATION_ORDER = [
    "IN_PROGRESS",
    "SEEDED",
]
CROSS_MECH_ORDER = [
    "Cross-Mech linked",
    "DUFMech only",
]


def project_pacmap(vecs: np.ndarray, n_neighbors: int, seed: int) -> np.ndarray:
    import pacmap

    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=seed,
    )
    return reducer.fit_transform(vecs, init="pca")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--neighbors", type=int, default=10)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    vecs = np.load(EMB_DIR / "vectors.npy")
    ids: list[str] = json.loads((EMB_DIR / "ids.json").read_text(encoding="utf-8"))
    meta = json.loads((EMB_DIR / "meta.json").read_text(encoding="utf-8"))

    xy = project_pacmap(vecs, args.neighbors, args.seed)
    lo = xy.min(axis=0)
    hi = xy.max(axis=0)
    span = np.where((hi - lo) > 0, hi - lo, 1.0)
    xy = (xy - lo) / span

    families = {str(f["pfam_id"]): f for f in load_corpus_families()}
    seed_index = {name: idx for idx, name in enumerate(SEED_ORDER)}
    cur_index = {name: idx for idx, name in enumerate(CURATION_ORDER)}

    points: list[list] = []
    for idx, pfam_id in enumerate(ids):
        fam = families.get(pfam_id, {})
        seed_status = str(fam.get("unknown_status") or "UNKNOWN_CANDIDATE")
        cur_status = str(fam.get("curation_status") or "SEEDED")
        has_cm = bool(fam.get("cross_mechs"))
        s_idx = seed_index.get(seed_status, 0)
        c_idx = cur_index.get(cur_status, 1)
        cm_idx = 0 if has_cm else 1
        points.append([
            round(float(xy[idx, 0]), 4),
            round(float(xy[idx, 1]), 4),
            pfam_id,
            str(fam.get("short_name") or pfam_id),
            str(fam.get("name") or pfam_id),
            s_idx,
            c_idx,
            cm_idx,
            int(fam.get("proteins") or 0),
            int(fam.get("structures") or 0),
        ])

    payload = {
        "model": meta["model"],
        "dim": meta["dim"],
        "method": "pacmap",
        "neighbors": args.neighbors,
        "n": len(points),
        "seed_statuses": SEED_ORDER,
        "curation_statuses": CURATION_ORDER,
        "cross_mech_bins": CROSS_MECH_ORDER,
        "points": points,
    }
    out = EMB_DIR / "corpus_map.json"
    out.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote {len(points)} points ({out.stat().st_size:,} B) -> {out}")


if __name__ == "__main__":
    main()
