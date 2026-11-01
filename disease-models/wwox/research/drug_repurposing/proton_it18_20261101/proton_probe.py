#!/usr/bin/env python3
"""IT18 P-PROTON: coverage, minimal scoring path and the pre-registered trial for PROTON on the WWOX needs.

Non-canonical research tool; not medical advice. Computes link-prediction scores from PROTON's released
node embeddings and relation decoder (no checkpoint, no training) and compares them with simple baselines
and with LEGEND's catalogue, as fixed in PRE_REGISTRATION.md next to this file.

Subcommands
  extract       stream NeuroKG edges.csv.zip once (standard library); write compact extracts to --out-dir
  coverage      node/edge coverage of the WWOX entities and of the need targets (standard library)
  run           stage-2 checks + trial (a) and (c); needs torch and numpy (throwaway venv), reads the extracts
  chembl-check  secondary measure (b): plain public GETs to the ChEMBL REST API, cached under --cache-dir

Nothing is written unless a subcommand is given; `--help` has no side effect. Inputs are untrusted downloads:
the decoder pickle is read with an allow-list unpickler (four numpy/codecs globals), embeddings with
torch.load(weights_only=True).
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import os
import pickle
import random
import sys
import time
import urllib.request
import zipfile

DRUG_PROTEIN = ("drug", "drug_protein", "gene/protein")
INDICATION = ("disease", "indication", "drug")
FOCUS_NAMES = {"WWOX": "gene/protein"}
FOCUS_DISEASE_MONDO = {"14533": "DEE28 (WOREE)", "13687": "SCAR12", "100062": "DEE (group term)", "18614": "undetermined early-onset EE"}
EPILEPSY_NODE = 39348
DEE28_NODE = 30298
BD_NODE = 39528
BD_EXPECTED = {"Cholecalciferol": 16, "Alfacalcidol": 102, "Calcitriol": 114}
GROUP_TYPES = {"PROTEIN COMPLEX", "PROTEIN COMPLEX GROUP", "PROTEIN FAMILY", "SELECTIVITY GROUP", "CHIMERIC PROTEIN"}


# ---------------------------------------------------------------- pure helpers (tested without torch)

def leaky_relu(x: float, a: float = 0.01) -> float:
    return x if x >= 0 else a * x


def score_pair(src: list[float], rel: list[float], dst: list[float]) -> float:
    """PROTON bilinear-diagonal decoder: sigmoid(sum(lrelu(src) * rel * lrelu(dst)))."""
    s = sum(leaky_relu(a) * w * leaky_relu(b) for a, w, b in zip(src, rel, dst, strict=True))
    return 1.0 / (1.0 + math.exp(-s))


def relation_index(edge_types: list[tuple[str, str, str]], etype: tuple[str, str, str]) -> int:
    hits = [i for i, e in enumerate(edge_types) if tuple(e) == tuple(etype)]
    if len(hits) != 1:
        raise ValueError(f"edge type {etype} found {len(hits)} times")
    return hits[0]


def percentile_ranks(scores: dict, higher_is_better: bool = True) -> dict:
    """Average-rank percentile in [0, 1); 0 = best. Ties share the mean rank."""
    items = sorted(scores.items(), key=lambda kv: kv[1], reverse=higher_is_better)
    n = len(items)
    out = {}
    i = 0
    while i < n:
        j = i
        while j + 1 < n and items[j + 1][1] == items[i][1]:
            j += 1
        mean_rank0 = (i + j) / 2.0
        for k in range(i, j + 1):
            out[items[k][0]] = mean_rank0 / n
        i = j + 1
    return out


def recall_at(percentiles: list[float], frac: float) -> float | None:
    if not percentiles:
        return None
    return sum(1 for p in percentiles if p <= frac) / len(percentiles)


def sign_test(a: list[float], b: list[float]) -> dict:
    """Two-sided exact sign test on paired values; lower is better. Ties dropped."""
    wins = sum(1 for x, y in zip(a, b, strict=True) if x < y)
    losses = sum(1 for x, y in zip(a, b, strict=True) if x > y)
    n = wins + losses
    if n == 0:
        return {"a_better": 0, "b_better": 0, "ties": len(a), "p": 1.0}
    k = min(wins, losses)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n * 2
    return {"a_better": wins, "b_better": losses, "ties": len(a) - n, "p": min(1.0, p)}


def spearman(x: list[float], y: list[float]) -> float:
    def ranks(v):
        pr = percentile_ranks(dict(enumerate(v)), higher_is_better=True)
        return [pr[i] for i in range(len(v))]
    rx, ry = ranks(x), ranks(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry, strict=True))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


class AllowListUnpickler(pickle.Unpickler):
    """Only the globals a pickled numpy array needs; anything else is refused."""
    ALLOWED = {("numpy.core.multiarray", "_reconstruct"), ("numpy", "ndarray"), ("numpy", "dtype"), ("_codecs", "encode")}

    def find_class(self, module, name):
        if (module, name) not in self.ALLOWED:
            raise pickle.UnpicklingError(f"refused global {module}.{name}")
        if module == "numpy.core.multiarray":
            import numpy
            core = getattr(numpy, "_core", None) or numpy.core
            return core.multiarray._reconstruct
        return super().find_class(module, name)


def load_pickled_array(path: str):
    with zipfile.ZipFile(path) as z:
        names = [n for n in z.namelist() if n.endswith("data.pkl")]
        if len(names) != 1:
            raise ValueError(f"{path}: expected one data.pkl, got {names}")
        return AllowListUnpickler(io.BytesIO(z.read(names[0]))).load()


def need_targets(needs: dict) -> list[dict]:
    rows = []
    for n in needs["needs"]:
        direction = (n.get("intervention_direction") or {}).get("direction")
        for t in n.get("targets", []):
            if t.get("target_kind") == "intervention_target":
                rows.append({"need": n["id"], "symbol": t["symbol"], "hgnc_id": t.get("hgnc_id"), "direction": direction})
    return rows


def catalogue_reference(records, genes: set[str]) -> list[dict]:
    """(drugbank id, gene, stratum, action) from ChEMBL curated, direct, human mechanism rows on the genes."""
    out = []
    for r in records:
        dbs = (r.get("ids") or {}).get("drugbank") or []
        if not dbs:
            continue
        for t in r.get("targets") or []:
            if t.get("source") != "ChEMBL curated mechanism" or t.get("direct_interaction") != 1:
                continue
            if t.get("organism") != "Homo sapiens":
                continue
            stratum = "single_protein" if t.get("target_type") == "SINGLE PROTEIN" else "group_level"
            for g in t.get("gene_symbols") or []:
                if g in genes:
                    for db in dbs:
                        out.append({"drugbank": db, "gene": g, "stratum": stratum, "action": t.get("action_type"),
                                    "chembl": (r.get("ids") or {}).get("chembl"), "target_chembl": t.get("target_id")})
    return out


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def read_nodes(path: str) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- extract (stdlib, one streaming pass)

def cmd_extract(a) -> int:
    nodes = read_nodes(a.nodes)
    needs = json.load(open(a.needs))
    symbols = {t["symbol"] for t in need_targets(needs)}
    gene_idx = {int(r["node_index"]) for r in nodes if r["node_type"] == "gene/protein" and r["node_name"] in symbols}
    focus = set(gene_idx)
    focus |= {int(r["node_index"]) for r in nodes if r["node_type"] == "gene/protein" and r["node_name"] == "WWOX"}
    focus |= {int(r["node_index"]) for r in nodes if r["node_type"] == "disease" and r["node_id"] in FOCUS_DISEASE_MONDO}
    focus |= {EPILEPSY_NODE}
    os.makedirs(a.out_dir, exist_ok=True)
    canon: dict[tuple, int] = {}
    n = 0
    with zipfile.ZipFile(a.edges_zip) as z, \
            open(os.path.join(a.out_dir, "drug_protein.tsv"), "w") as fdp, \
            open(os.path.join(a.out_dir, "focus_edges.tsv"), "w") as ffo, \
            open(os.path.join(a.out_dir, "ppi_targets.tsv"), "w") as fpp:
        with z.open("edges.csv") as raw:
            rd = csv.DictReader(io.TextIOWrapper(raw, newline=""))
            for r in rd:
                n += 1
                key = (r["x_type"], r["relation"], r["y_type"])
                canon[key] = canon.get(key, 0) + 1
                if r["direction"] != "forward":
                    continue
                x, y = int(r["x_index"]), int(r["y_index"])
                if r["relation"] == "drug_protein":
                    fdp.write(f"{x}\t{y}\t{r['display_relation']}\n")
                if r["relation"] == "protein_protein" and (x in gene_idx or y in gene_idx):
                    fpp.write(f"{x}\t{y}\n")
                if x in focus or y in focus:
                    ffo.write(f"{r['relation']}\t{r['display_relation']}\t{x}\t{r['x_type']}\t{y}\t{r['y_type']}\n")
    with open(os.path.join(a.out_dir, "canonical_etypes.json"), "w") as f:
        json.dump({"rows": n, "etypes": [[*k, v] for k, v in sorted(canon.items())]}, f)
    print(json.dumps({"rows": n, "canonical_etypes": len(canon), "target_gene_nodes": len(gene_idx)}))
    return 0


# ---------------------------------------------------------------- coverage (stdlib)

def cmd_coverage(a) -> int:
    nodes = read_nodes(a.nodes)
    by_idx = {int(r["node_index"]): r for r in nodes}
    needs = json.load(open(a.needs))
    tg = need_targets(needs)
    name_to_idx = {}
    for r in nodes:
        if r["node_type"] == "gene/protein":
            name_to_idx.setdefault(r["node_name"], []).append(int(r["node_index"]))
    focus_rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(a.extract_dir, "focus_edges.tsv"))]
    dp = [tuple(map(int, l.split("\t")[:2])) for l in open(os.path.join(a.extract_dir, "drug_protein.tsv"))]
    dp_by_gene: dict[int, int] = {}
    for d, g in dp:
        dp_by_gene[g] = dp_by_gene.get(g, 0) + 1

    def rel_counts(idx):
        c: dict[str, int] = {}
        for rel, _disp, x, _xt, y, _yt in focus_rows:
            if int(x) == idx or int(y) == idx:
                c[rel] = c.get(rel, 0) + 1
        return dict(sorted(c.items()))

    wwox = [int(r["node_index"]) for r in nodes if r["node_type"] == "gene/protein" and r["node_name"] == "WWOX"]
    diseases = {}
    for r in nodes:
        if r["node_type"] == "disease" and r["node_id"] in FOCUS_DISEASE_MONDO:
            idx = int(r["node_index"])
            nb = [(rel, by_idx[int(x) if int(y) == idx else int(y)]["node_name"]) for rel, _d, x, _xt, y, _yt in focus_rows
                  if (int(x) == idx or int(y) == idx) and rel in ("disease_protein", "indication", "off_label_use",
                                                                   "strong_clinical_evidence", "weak_clinical_evidence")]
            diseases[FOCUS_DISEASE_MONDO[r["node_id"]]] = {
                "node_index": idx, "mondo": "MONDO:" + r["node_id"].zfill(7), "node_name": r["node_name"],
                "relations": rel_counts(idx),
                "disease_protein_genes": sorted({n for rel, n in nb if rel == "disease_protein"}),
                "drug_relations": sorted({f"{rel}:{n}" for rel, n in nb if rel != "disease_protein"})}
    wwox_edges = [(rel, by_idx[int(y) if int(x) == wwox[0] else int(x)]) for rel, _d, x, _xt, y, _yt in focus_rows
                  if wwox and (int(x) == wwox[0] or int(y) == wwox[0])]
    targets = []
    for t in tg:
        idx = name_to_idx.get(t["symbol"], [])
        targets.append({**t, "node_index": idx[0] if len(idx) == 1 else idx,
                        "in_neurokg": bool(idx), "drug_protein_edges": sum(dp_by_gene.get(i, 0) for i in idx)})
    out = {
        "nodes_file_sha256": sha256(a.nodes),
        "wwox": {"node_index": wwox, "ncbi_gene": [by_idx[i]["node_id"] for i in wwox], "relations": rel_counts(wwox[0]) if wwox else {},
                 "disease_neighbours": sorted({r["node_name"] for rel, r in wwox_edges if r["node_type"] == "disease"}),
                 "drug_protein_edges": dp_by_gene.get(wwox[0], 0) if wwox else 0},
        "woree_word_as_node_name": any("woree" in r["node_name"].lower() for r in nodes),
        "diseases": diseases,
        "need_targets": targets,
        "need_targets_absent": sorted({t["symbol"] for t in targets if not t["in_neurokg"]}),
    }
    json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
    print(json.dumps({"wwox": out["wwox"]["node_index"], "absent_targets": out["need_targets_absent"],
                      "diseases": {k: v["node_index"] for k, v in diseases.items()}}))
    return 0


# ---------------------------------------------------------------- run (torch path)

def load_artifacts(hf_dir: str):
    import torch  # noqa: PLC0415  (only in the throwaway venv)
    emb = torch.load(os.path.join(hf_dir, "embeddings.pt"), weights_only=True, mmap=True)
    dec = torch.tensor(load_pickled_array(os.path.join(hf_dir, "decoder.pt")))
    et = [tuple(e) for e in torch.load(os.path.join(hf_dir, "edge_types.pt"), weights_only=True)]
    return emb, dec, et


def scores_one_to_many(emb, dec, ridx: int, src: int, dsts: list[int], src_is_x: bool = True):
    import torch
    import torch.nn.functional as F
    s = F.leaky_relu(emb[src].unsqueeze(0))
    d = F.leaky_relu(emb[torch.tensor(dsts)])
    return torch.sigmoid((s * dec[ridx] * d).sum(dim=1)).tolist()


def cmd_run(a) -> int:
    nodes = read_nodes(a.nodes)
    by_idx = {int(r["node_index"]): r for r in nodes}
    drugs = sorted(int(r["node_index"]) for r in nodes if r["node_type"] == "drug")
    db_to_idx = {by_idx[i]["node_id"]: i for i in drugs}
    emb, dec, et = load_artifacts(a.hf_dir)
    canon = json.load(open(os.path.join(a.extract_dir, "canonical_etypes.json")))
    canon_list = [tuple(e[:3]) for e in canon["etypes"]]
    res: dict = {"inputs": {"embeddings_sha256": sha256(os.path.join(a.hf_dir, "embeddings.pt")),
                            "decoder_sha256": sha256(os.path.join(a.hf_dir, "decoder.pt")),
                            "edge_types_sha256": sha256(os.path.join(a.hf_dir, "edge_types.pt")),
                            "nodes_sha256": sha256(a.nodes), "edges_rows": canon["rows"],
                            "embeddings_shape": list(emb.shape), "decoder_shape": list(dec.shape)}}
    # check 1: relation order
    res["check_order"] = {"edge_types": len(et), "canonical_from_edges": len(canon_list),
                          "equal_to_sorted_canonical": et == sorted(canon_list) and et == canon_list}
    # check 2: official BD example
    ind = relation_index(et, INDICATION)
    bd = scores_one_to_many(emb, dec, ind, BD_NODE, drugs)
    order = sorted(range(len(drugs)), key=lambda k: -bd[k])
    rank = {drugs[k]: r + 1 for r, k in enumerate(order)}
    name_idx = {by_idx[i]["node_name"]: i for i in drugs}
    got = {n: rank.get(name_idx.get(n)) for n in BD_EXPECTED}
    res["check_bd"] = {"expected": BD_EXPECTED, "observed": got,
                       "reproduced": all(got[n] is not None and abs(got[n] - BD_EXPECTED[n]) <= 2 for n in BD_EXPECTED)}
    # trial inputs
    needs = json.load(open(a.needs))
    tg = need_targets(needs)
    sym_to_idx = {}
    for r in nodes:
        if r["node_type"] == "gene/protein":
            sym_to_idx.setdefault(r["node_name"], []).append(int(r["node_index"]))
    genes = {s: v[0] for s, v in sym_to_idx.items() if len(v) == 1 and s in {t["symbol"] for t in tg}}
    gene_need = {}
    for t in tg:
        gene_need.setdefault(t["symbol"], set()).add(t["need"])
    need_genes = {}
    for t in tg:
        need_genes.setdefault(t["need"], set()).add(t["symbol"])
    dp = [tuple(map(int, l.split("\t")[:2])) for l in open(os.path.join(a.extract_dir, "drug_protein.tsv"))]
    drug_targets: dict[int, set] = {}
    for d, g in dp:
        drug_targets.setdefault(d, set()).add(g)
    degree = {d: len(drug_targets.get(d, ())) for d in drugs}
    ppi: dict[int, set] = {}
    for l in open(os.path.join(a.extract_dir, "ppi_targets.tsv")):
        x, y = map(int, l.split("\t"))
        ppi.setdefault(x, set()).add(y)
        ppi.setdefault(y, set()).add(x)
    records = (json.loads(l) for l in gzip.open(a.catalogue, "rt"))
    ref_rows = catalogue_reference(records, set(genes))
    ref: dict[tuple, dict] = {}
    unmapped_db = set()
    for r in ref_rows:
        d = db_to_idx.get(r["drugbank"])
        if d is None:
            unmapped_db.add(r["drugbank"])
            continue
        key = (r["gene"], d)
        cur = ref.get(key)
        if cur is None or (cur["stratum"] == "group_level" and r["stratum"] == "single_protein"):
            ref[key] = r
    ridx = relation_index(et, DRUG_PROTEIN)
    per_gene = {}
    pairs = []
    top_rows = []
    auroc_pos, auroc_neg = [], []
    rng = random.Random(18)
    for sym, gi in sorted(genes.items()):
        in_graph = {d for d in drugs if gi in drug_targets.get(d, ())}
        cand = [d for d in drugs if d not in in_graph]
        p_all = scores_one_to_many(emb, dec, ridx, gi, drugs)
        # The decoder row for ('drug','drug_protein','gene/protein') expects src = drug, dst = gene; the product is symmetric
        # in src/dst for a diagonal decoder, so scoring gene against all drugs with the forward row is identical.
        pscore = dict(zip(drugs, p_all))
        b1 = {d: degree[d] for d in cand}
        b2 = {d: (sum(1 for t in drug_targets.get(d, ()) if t != gi and t in ppi.get(gi, ())), degree[d]) for d in cand}
        pr_p = percentile_ranks({d: pscore[d] for d in cand})
        pr_b1 = percentile_ranks(b1)
        pr_b2 = percentile_ranks(b2)
        g_ref = [(d, r) for (s, d), r in ref.items() if s == sym and d not in in_graph]
        n_ref_in_graph = sum(1 for (s, d) in ref if s == sym and d in in_graph)
        siblings = set()
        for nd in gene_need.get(sym, ()):
            siblings |= {genes[x] for x in need_genes[nd] if x in genes and x != sym}
        for d, r in g_ref:
            pairs.append({"gene": sym, "drug": by_idx[d]["node_id"], "drug_name": by_idx[d]["node_name"],
                          "stratum": r["stratum"], "action": r["action"],
                          "sibling_in_graph": bool(drug_targets.get(d, set()) & siblings),
                          "pct_P": round(pr_p[d], 5), "pct_B1": round(pr_b1[d], 5), "pct_B2": round(pr_b2[d], 5)})
        if in_graph:
            neg = rng.sample(cand, min(len(in_graph), len(cand)))
            auroc_pos += [pscore[d] for d in in_graph]
            auroc_neg += [pscore[d] for d in neg]
        unknown = [d for d in cand if (sym, d) not in ref]
        top_p = sorted(unknown, key=lambda d: -pscore[d])[:a.top]
        top_b2 = sorted(unknown, key=lambda d: (-b2[d][0], -b2[d][1], d))[:a.top]
        for meth, lst in (("P", top_p), ("B2", top_b2)):
            for k, d in enumerate(lst, 1):
                top_rows.append({"gene": sym, "needs": ";".join(sorted(gene_need[sym])), "method": meth, "rank": k,
                                 "drugbank": by_idx[d]["node_id"], "drug_name": by_idx[d]["node_name"],
                                 "score_P": round(pscore[d], 4), "b2_ppi_targets": b2[d][0], "degree": degree[d]})
        per_gene[sym] = {"node_index": gi, "in_graph_drugs": len(in_graph), "candidates": len(cand),
                         "ref_not_in_graph": len(g_ref), "ref_in_graph": n_ref_in_graph,
                         "max_P_unknown": round(max((pscore[d] for d in unknown), default=float("nan")), 4),
                         "share_candidates_P_gt_0_5": round(sum(1 for d in cand if pscore[d] > 0.5) / len(cand), 4),
                         "share_candidates_P_gt_0_9": round(sum(1 for d in cand if pscore[d] > 0.9) / len(cand), 4)}
    # AUROC (training-set sanity)
    allv = [(s, 1) for s in auroc_pos] + [(s, 0) for s in auroc_neg]
    pr = percentile_ranks(dict(enumerate(v for v, _ in allv)), higher_is_better=False)
    n1, n0 = len(auroc_pos), len(auroc_neg)
    rsum = sum((pr[i] * len(allv) + 1) for i, (_, lab) in enumerate(allv) if lab == 1)
    ptop = [r for r in top_rows if r["method"] == "P"]
    res["p_top_concentration"] = {"rows": len(ptop), "distinct_drugs": len({r["drugbank"] for r in ptop}),
                                  "median_degree_P_top": sorted(r["degree"] for r in ptop)[len(ptop) // 2] if ptop else None,
                                  "median_degree_all_drugs": sorted(degree.values())[len(degree) // 2]}
    res["check_sanity_auroc_in_graph"] = {"pos": n1, "neg": n0,
                                          "auroc": round((rsum - n1 * (n1 + 1) / 2) / (n1 * n0), 4) if n1 and n0 else None}

    def summarise(sel):
        out = {"pairs": len(sel), "genes": len({p["gene"] for p in sel})}
        for m in ("P", "B1", "B2"):
            v = [p[f"pct_{m}"] for p in sel]
            out[m] = {"recall_at_1pct": recall_at(v, 0.01), "recall_at_5pct": recall_at(v, 0.05),
                      "median_pct": (sorted(v)[len(v) // 2] if v else None)}
        return out
    sp = [p for p in pairs if p["stratum"] == "single_protein"]
    res["trial_a"] = {"all": summarise(pairs), "single_protein": summarise(sp),
                      "group_level": summarise([p for p in pairs if p["stratum"] == "group_level"]),
                      "single_protein_sibling_in_graph": summarise([p for p in sp if p["sibling_in_graph"]]),
                      "single_protein_no_sibling": summarise([p for p in sp if not p["sibling_in_graph"]]),
                      "catalogue_drugbank_ids_not_in_neurokg": len(unmapped_db), "per_gene": per_gene}
    s = res["trial_a"]["single_protein"]
    if s["pairs"] >= 20 and s["genes"] >= 5:
        best = max(("B1", "B2"), key=lambda m: s[m]["recall_at_5pct"])
        st = sign_test([p["pct_P"] for p in sp], [p[f"pct_{best}"] for p in sp])
        gain = s["P"]["recall_at_5pct"] - s[best]["recall_at_5pct"]
        res["trial_a"]["decision"] = {"best_baseline": best, "recall5_gain_points": round(100 * gain, 2), "sign_test": st,
                                      "statement": ("PROTON ranks LEGEND-only relations better than the simple baselines"
                                                    if gain >= 0.10 and st["p"] < 0.05 and st["a_better"] > st["b_better"]
                                                    else "no advantage over the simple baselines measured")}
    else:
        res["trial_a"]["decision"] = {"statement": "fewer than 20 SINGLE PROTEIN pairs over 5 genes: figures only, no statement"}
    # (c) WOREE specificity
    dee28 = scores_one_to_many(emb, dec, ind, DEE28_NODE, drugs)
    sib = [int(r["node_index"]) for r in nodes if r["node_type"] == "disease"
           and r["node_name"].startswith("developmental and epileptic encephalopathy") and int(r["node_index"]) != DEE28_NODE]
    rhos = {}
    for s_idx in sib:
        rhos[by_idx[s_idx]["node_name"]] = round(spearman(dee28, scores_one_to_many(emb, dec, ind, s_idx, drugs)), 4)
    epi = round(spearman(dee28, scores_one_to_many(emb, dec, ind, EPILEPSY_NODE, drugs)), 4)
    vals = sorted(rhos.values())
    med = vals[len(vals) // 2] if vals else None
    order28 = sorted(range(len(drugs)), key=lambda k: -dee28[k])[:a.top * 2]
    res["trial_c"] = {"siblings": len(rhos), "spearman_median": med, "spearman_min": vals[0] if vals else None,
                      "spearman_max": vals[-1] if vals else None, "spearman_epilepsy": epi,
                      "statement": ("DEE28 ranking not shown to be WOREE-specific" if med is not None and med >= 0.9
                                    else "DEE28 ranking differs from its siblings (median Spearman < 0.9)"),
                      "dee28_top_indication": [{"rank": r + 1, "drugbank": by_idx[drugs[k]]["node_id"],
                                                "drug_name": by_idx[drugs[k]]["node_name"], "score": round(dee28[k], 4)}
                                               for r, k in enumerate(order28)]}
    wwox = [int(r["node_index"]) for r in nodes if r["node_type"] == "gene/protein" and r["node_name"] == "WWOX"][0]
    ww = scores_one_to_many(emb, dec, ridx, wwox, drugs)
    ow = sorted(range(len(drugs)), key=lambda k: -ww[k])[:a.top * 2]
    res["wwox_drug_protein_top"] = [{"rank": r + 1, "drugbank": by_idx[drugs[k]]["node_id"],
                                     "drug_name": by_idx[drugs[k]]["node_name"], "score": round(ww[k], 4),
                                     "degree": degree[drugs[k]]} for r, k in enumerate(ow)]
    os.makedirs(a.out_dir, exist_ok=True)
    json.dump(res, open(os.path.join(a.out_dir, "results.json"), "w"), indent=1, sort_keys=True)
    for fn, rows in (("reference_pairs.tsv", pairs), ("top_unknown.tsv", top_rows)):
        with open(os.path.join(a.out_dir, fn), "w", newline="") as f:
            if rows:
                w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
                w.writeheader()
                w.writerows(rows)
    print(json.dumps({k: res[k] for k in ("check_order", "check_bd", "check_sanity_auroc_in_graph")}))
    print(json.dumps(res["trial_a"]["decision"]))
    return 0


# ---------------------------------------------------------------- chembl-check (network, plain GET)

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"


def _get(url: str, cache_dir: str):
    os.makedirs(cache_dir, exist_ok=True)
    fn = os.path.join(cache_dir, hashlib.sha256(url.encode()).hexdigest() + ".json")
    if os.path.exists(fn):
        return json.load(open(fn))
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "legend-research/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            json.dump(data, open(fn, "w"))
            time.sleep(0.3)
            return data
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"GET failed: {url}: {err}")


def directed_genes(needs: dict) -> dict[str, str]:
    out = {}
    for t in need_targets(needs):
        if t["direction"] in ("down", "up"):
            out[t["symbol"]] = t["direction"]
    return out


def cmd_chembl_check(a) -> int:
    needs = json.load(open(a.needs))
    dgenes = directed_genes(needs)
    db_to_chembl = {}
    for l in gzip.open(a.catalogue, "rt"):
        r = json.loads(l)
        ids = r.get("ids") or {}
        for db in ids.get("drugbank") or []:
            db_to_chembl.setdefault(db, ids.get("chembl"))
    top = list(csv.DictReader(open(a.top_tsv), delimiter="\t"))
    rows = []
    target_cache: dict[str, list[str]] = {}
    for t in top:
        if t["gene"] not in dgenes:
            continue
        g = t["gene"]
        if g not in target_cache:
            ttype = "" if a.include_complexes else "&target_type=SINGLE%20PROTEIN"
            js = _get(f"{CHEMBL}/target.json?target_components__target_component_synonyms__component_synonym__iexact={g}"
                      f"&organism=Homo%20sapiens{ttype}&limit=100", a.cache_dir)
            keep = {"SINGLE PROTEIN", "PROTEIN COMPLEX"} if a.include_complexes else {"SINGLE PROTEIN"}
            target_cache[g] = sorted({x["target_chembl_id"] for x in js.get("targets", []) if x.get("target_type") in keep})
        mol = db_to_chembl.get(t["drugbank"])
        status, n = "unmappable", None
        if mol and target_cache[g]:
            n = 0
            for tid in target_cache[g]:
                js = _get(f"{CHEMBL}/activity.json?molecule_chembl_id={mol}&target_chembl_id={tid}&pchembl_value__gte=5&limit=1",
                          a.cache_dir)
                n += js.get("page_meta", {}).get("total_count", 0)
            status = "supported" if n > 0 else "not_supported"
        elif mol:
            status = "no_chembl_target"
        rows.append({"gene": g, "method": t["method"], "rank": t["rank"], "drugbank": t["drugbank"],
                     "drug_name": t["drug_name"], "chembl": mol or "", "targets": ";".join(target_cache[g]),
                     "activities_pchembl_ge5": "" if n is None else n, "status": status})
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    summ = {}
    for r in rows:
        summ.setdefault(r["method"], {}).setdefault(r["status"], 0)
        summ[r["method"]][r["status"]] += 1
    print(json.dumps(summ, sort_keys=True))
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")
    e = sub.add_parser("extract", help="stream edges.csv.zip once; write compact extracts")
    e.add_argument("--nodes", required=True)
    e.add_argument("--edges-zip", required=True)
    e.add_argument("--needs", required=True)
    e.add_argument("--out-dir", required=True)
    c = sub.add_parser("coverage", help="coverage JSON of WWOX entities and need targets")
    c.add_argument("--nodes", required=True)
    c.add_argument("--needs", required=True)
    c.add_argument("--extract-dir", required=True)
    c.add_argument("--out", required=True)
    r = sub.add_parser("run", help="stage-2 checks and trial (a), (c); torch required")
    r.add_argument("--nodes", required=True)
    r.add_argument("--needs", required=True)
    r.add_argument("--catalogue", required=True)
    r.add_argument("--extract-dir", required=True)
    r.add_argument("--hf-dir", required=True)
    r.add_argument("--out-dir", required=True)
    r.add_argument("--top", type=int, default=5)
    k = sub.add_parser("chembl-check", help="secondary measure (b): ChEMBL activities for the top unknown pairs")
    k.add_argument("--needs", required=True)
    k.add_argument("--catalogue", required=True)
    k.add_argument("--top-tsv", required=True)
    k.add_argument("--cache-dir", required=True)
    k.add_argument("--out", required=True)
    k.add_argument("--include-complexes", action="store_true",
                   help="post-hoc sensitivity variant: also PROTEIN COMPLEX targets that contain the gene (not pre-registered)")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help()
        return 0
    return {"extract": cmd_extract, "coverage": cmd_coverage, "run": cmd_run, "chembl-check": cmd_chembl_check}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
