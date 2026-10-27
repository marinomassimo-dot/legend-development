#!/usr/bin/env python3
"""Iteration 2 (scientist-d, SD-IT2-LINCS-20261027): offline input-quality table for the declared GSE156243 query sets and
construction of content-matched NULL gene sets, plus entity mapping of the new symbols through the key-less SigCom metadata API.
Seeds and rules are declared in lincs_iteration2_interpretation_20261027.md BEFORE any request was sent.
Usage: lincs_it2_null_sets.py <this directory> <GSE92742_Broad_LINCS_gene_info.txt.gz> [--no-network]
Writes derived/lincs_it2_input_quality.json, derived/query_sets_it2_nulls.json, derived/sigcom_entity_map_it2.json."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 3:
    print(__doc__)
    raise SystemExit(0)
import gzip, json, math, os, random, statistics, urllib.parse, urllib.request
G, geneinfo = _sys.argv[1], _sys.argv[2]
net = "--no-network" not in _sys.argv
q = json.load(open(f"{G}/derived/query_sets.json"))
mp = json.load(open(f"{G}/derived/sigcom_entity_map.json"))["map"]
l1000 = {l.split("\t")[1] for l in gzip.open(geneinfo, "rt").read().splitlines()[1:]}  # 12,328 genes of the L1000 space
cnt = {}
with gzip.open("/home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt") as f:
    h = f.readline().rstrip("\n").split("\t")
    for l in f:
        x = l.rstrip("\n").split("\t"); cnt[x[0]] = [float(v) for v in x[1:]]
tot = [sum(v[i] for v in cnt.values()) for i in range(6)]
# symbol-level expression: the counts file is keyed by symbol (gene column)
lcpm = {g: [math.log2(v[i] / tot[i] * 1e6 + 1) for i in range(6)] for g, v in cnt.items()}
meanl = {g: statistics.mean(v) for g, v in lcpm.items()}
hg = json.load(open("/home/desktop/legend-development/files/geo/GSE156243/hgnc_complete_set_20261022.json"))["response"]["docs"]
approved = {d["symbol"] for d in hg}
uni = sorted(g for g in (l.strip() for l in open(f"{G}/derived/universe_counts_ge10_proxy.tsv")) if g in approved and g in meanl and g != "gene")
# ---- input quality of the existing sets
iq = {}
for k, v in q.items():
    u, d = v["up"], v["down"]
    iq[k] = {"n_up": len(u), "n_down": len(d), "dup_up": len(u) - len(set(u)), "dup_down": len(d) - len(set(d)), "in_both_arms": len(set(u) & set(d)),
             "mapped_up": sum(g in mp for g in u), "mapped_down": sum(g in mp for g in d),
             "entity_collisions": len([g for g in u + d if g in mp]) - len({mp[g] for g in u + d if g in mp}),
             "in_L1000_space_up": sum(g in l1000 for g in u), "in_L1000_space_down": sum(g in l1000 for g in d),
             "median_mean_log2cpm": round(statistics.median(meanl.get(g, float("nan")) for g in u + d if g in meanl), 2)}
# ---- strata: expression decile (over the universe) x in-L1000-space flag
ranked = sorted(uni, key=lambda g: meanl[g]); dec = {g: min(9, i * 10 // len(ranked)) for i, g in enumerate(ranked)}
stratum = lambda g: (dec.get(g, 0), g in l1000)
s1 = q["S1"]; s1genes = set(s1["up"]) | set(s1["down"])
pool = {}
for g in uni:
    if g not in s1genes: pool.setdefault(stratum(g), []).append(g)
def matched(seed):
    rnd = random.Random(seed); used = set(); out = {}
    for arm in ("up", "down"):
        out[arm] = []
        for g in s1[arm]:
            cands = [c for c in pool.get(stratum(g), []) if c not in used]
            c = rnd.choice(cands); used.add(c); out[arm].append(c)
    return out
sets = {f"N{i + 1}": matched(20261101 + i) for i in range(3)}
# ---- pseudo-contrast: split of the four KO libraries 2 v 2 (no condition difference by construction); top genes by Welch t on log2 CPM
def welch(a, b):
    ma, mb = statistics.mean(a), statistics.mean(b); va, vb = statistics.variance(a), statistics.variance(b)
    return (ma - mb) / math.sqrt(va / len(a) + vb / len(b) + 1e-9)
for name, (A, B) in {"K1": ((0, 1), (2, 3)), "K2": ((0, 2), (1, 3))}.items():
    t = {g: welch([lcpm[g][i] for i in A], [lcpm[g][i] for i in B]) for g in uni}
    r = sorted(t, key=lambda g: t[g])
    up = [g for g in reversed(r)][:len(s1["up"])]; down = [g for g in r if g not in set(up)][:len(s1["down"])]
    sets[name] = {"up": up, "down": down}
for k in sets:
    u, d = sets[k]["up"], sets[k]["down"]
    iq[k] = {"n_up": len(u), "n_down": len(d), "dup_up": len(u) - len(set(u)), "dup_down": len(d) - len(set(d)), "in_both_arms": len(set(u) & set(d)),
             "in_L1000_space_up": sum(g in l1000 for g in u), "in_L1000_space_down": sum(g in l1000 for g in d),
             "median_mean_log2cpm": round(statistics.median(meanl[g] for g in u + d), 2), "overlap_with_S1_genes": len(set(u + d) & s1genes)}
json.dump(sets, open(f"{G}/derived/query_sets_it2_nulls.json", "w"), indent=1)
json.dump(iq, open(f"{G}/derived/lincs_it2_input_quality.json", "w"), indent=1)
for k, v in iq.items(): print(k, v)
if net:
    need = sorted({g for s in sets.values() for a in s.values() for g in a} - set(mp))
    B = "https://maayanlab.cloud/sigcom-lincs/metadata-api/entities?filter="; m = {}
    for i in range(0, len(need), 150):
        f = {"where": {"meta.symbol": {"inq": need[i:i + 150]}}, "fields": ["id", "meta.symbol"], "limit": 1000}
        for e in json.load(urllib.request.urlopen(B + urllib.parse.quote(json.dumps(f)), timeout=120)): m[e["meta"]["symbol"]] = e["id"]
    json.dump({"n_requested": len(need), "n_mapped": len(m), "unmapped": [g for g in need if g not in m], "map": m}, open(f"{G}/derived/sigcom_entity_map_it2.json", "w"), indent=0)
    print("new symbols", len(need), "mapped", len(m))
