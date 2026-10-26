#!/usr/bin/env python3
"""Same output as matrix_scores_extract.py, from locally downloaded parquet shards (the route that worked when the
datasets-server `filter` endpoint kept answering 5xx on 2026-10-26).

Needs `duckdb` (run it inside a throw-away venv: `uv venv v && uv pip install --python v/bin/python duckdb`).
The shards are 11 files of about 346 MB under
https://huggingface.co/datasets/everycure/matrix-scores/resolve/main/data/scores/train-NNNNN-of-00011.parquet
Keep them OUTSIDE the repository: the dataset card declares no licence, so nothing but small aggregates is committed.

A BASELINE is also written (meta.baseline): for each requested node, the Spearman rho of its `untransformed_treat_score`
vector against that of 100 other disease nodes drawn deterministically (lowest hash(target)), and the top-50 overlap. It
shows how much of any agreement between two related nodes is a property of the DRUG axis (some drugs score high for
everything) rather than of the disease.

Usage: matrix_scores_from_shards.py <shard_dir> <outdir> <dataset_commit_sha> <MONDO:id> [<MONDO:id> ...]
"""
import datetime
import glob
import hashlib
import json
import sys


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    r, i = [0.0] * len(v), 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def rho(a, b):
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    return cov / (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5


def baseline(con, files, rows, n=100):
    others = [r[0] for r in con.execute(
        "select target from (select distinct target from read_parquet(?)) where target not in (select unnest(?)) "
        "order by hash(target) limit ?", [files, list(rows), n]).fetchall()]
    vec = {}
    for t, s, v in con.execute("select target, source, untransformed_treat_score from read_parquet(?) where target in (select unnest(?))",
                               [files, others]).fetchall():
        if v is not None:
            vec.setdefault(t, {})[s] = v
    out = {"n_other_nodes": len(vec), "per_node": {}}
    for t, rs in rows.items():
        mine = {r["source"]: r["untransformed_treat_score"] for r in rs if r["untransformed_treat_score"] is not None}
        rr, ov = [], []
        for o, d in vec.items():
            common = sorted(set(mine) & set(d))
            if len(common) < 1000:
                continue
            rr.append(rho([mine[s] for s in common], [d[s] for s in common]))
            top = lambda m: set(sorted(common, key=lambda s: -m[s])[:50])
            ov.append(len(top(mine) & top(d)))
        rr.sort(), ov.sort()
        q = lambda x, f: x[int(f * (len(x) - 1))]
        out["per_node"][t] = {"n_compared": len(rr), "rho_min_median_max": [round(rr[0], 3), round(q(rr, .5), 3), round(rr[-1], 3)],
                              "top50_overlap_min_median_max": [ov[0], q(ov, .5), ov[-1]]}
    return out


def main(shard_dir, outdir, commit, targets):
    import duckdb  # imported late so --help works without it

    files = sorted(glob.glob(f"{shard_dir}/*.parquet"))
    con = duckdb.connect()
    rows = {}
    for t in targets:
        cur = con.execute("select * from read_parquet(?) where target = ?", [files, t])
        cols = [c[0] for c in cur.description]
        rows[t] = [dict(zip(cols, r)) for r in cur.fetchall()]
        print(t, len(rows[t]), flush=True)
    meta = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "dataset": "everycure/matrix-scores",
            "route": "local parquet shards", "dataset_commit_sha": commit,
            "num_rows_total": {t: len(r) for t, r in rows.items()},
            "shard_sha256": {f.split("/")[-1]: sha256(f) for f in files}, "baseline": baseline(con, files, rows)}
    json.dump({"meta": meta, "rows": rows}, open(f"{outdir}/matrix_scores_raw.json", "w"))


if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        raise SystemExit(0)
    if len(sys.argv) < 5:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
