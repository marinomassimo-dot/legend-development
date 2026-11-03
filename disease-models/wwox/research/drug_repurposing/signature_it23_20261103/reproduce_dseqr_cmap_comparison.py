#!/usr/bin/env python3
"""IT23 P2/P5: one circumscribed, key-less LINCS query comparison for ONE signature (the GSE156243 organoid KO-vs-WT list S1),
under explicit scenarios for the unknown role of the genes assigned to composition/maturation. Not medical advice. A mimic/reverse
score is a prompt for a hypothesis, not evidence of benefit; nothing here is WWOX evidence.

Why this script exists: dseqr (MIT) was evaluated as a route to CMap/LINCS queries. Its own data route is dead (see README), so the
comparison runs through the SigCom LINCS public API that LEGEND used before (no key, no account, no e-mail, gene symbols only).

Usage
  reproduce_dseqr_cmap_comparison.py --help
  reproduce_dseqr_cmap_comparison.py run  <repo_root> <geo_files_dir> <scratch_dir> <out_dir>   (live: 4 SigCom requests, ~60 PubChem property calls)
  reproduce_dseqr_cmap_comparison.py analyse <repo_root> <geo_files_dir> <scratch_dir> <out_dir>  (offline, from the stored responses in scratch)

<repo_root>      the worktree root (contains disease-models/...)
<geo_files_dir>  the shared gitignored files/geo (GSE150123 RAW tar + series matrix, GSE92742 gene_info and pert_info)
<scratch_dir>    receives raw service responses (NOT committed; digests are recorded in assets.tsv by the run)
<out_dir>        receives scenarios.tsv, overlap.tsv, coverage.json, compound tables, composition_class.tsv
Standard library only (no numpy). Deterministic given the same service answers.
Declared BEFORE the run (analyst choices, not data-derived): composition class = declared markers (marker_sets_declared.tsv) UNION maturation-consistent
genes, i.e. S1 genes with |Spearman rho| >= 0.6 between log2(CPM+1) and log10(day) over the 62 GSE150123 samples AND a KO-vs-WT direction equal to
'less mature' (KO up where rho < 0, KO down where rho > 0). Top-N = 20 compounds (a compound = one skeleton InChIKey; best signature kept).
"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 6 or _sys.argv[1] not in ("run", "analyse"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, hashlib, io, json, math, os, re, tarfile, time, datetime, urllib.parse, urllib.request

MODE, REPO, GEO, SCR, OUT = _sys.argv[1:6]
DR = f"{REPO}/disease-models/wwox/research/drug_repurposing"
G = f"{DR}/gse156243"
P4 = f"{DR}/generation_it22_p1_20261103/results_p4"
os.makedirs(SCR, exist_ok=True); os.makedirs(OUT, exist_ok=True)
TOPN, RHO_MIN, LIMIT = 20, 0.6, 300
API = "https://data-api.sigcom-lincs.k8s.maayanlab.cloud/v1/api/v1/enrich/ranktwosided"
META = "https://maayanlab.cloud/sigcom-lincs/metadata-api/"
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def tsv(path): return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))
def write_tsv(path, rows, cols):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(cols)
        for r in rows: w.writerow([r.get(c, "") for c in cols])
def sha(b): return hashlib.sha256(b).hexdigest()

# ---------------------------------------------------------------- signature, landmark coverage, composition class
S1 = json.load(open(f"{G}/derived/query_sets.json"))["S1"]
UP, DN = list(S1["up"]), list(S1["down"])
L2 = {r["symbol"]: float(r["log2FoldChange"]) for r in tsv(f"{G}/derived/list_padj_le_0.05.tsv")}
gi = list(csv.DictReader(gzip.open(f"{GEO}/GSE92742/GSE92742_Broad_LINCS_gene_info.txt.gz", "rt"), delimiter="\t"))
LM = {r["pr_gene_symbol"] for r in gi if r["pr_is_lm"] == "1"}
SPACE = {r["pr_gene_symbol"] for r in gi if r["pr_is_lm"] == "1" or r["pr_is_bing"] == "1"}
decl = set()
for r in tsv(f"{G}/marker_sets_declared.tsv"): decl |= set(r["genes"].split(","))
decl &= set(UP) | set(DN)

def spearman(x, y):
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
            for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    a, b = rk(x), rk(y); ma, mb = sum(a) / len(a), sum(b) / len(b)
    sa = math.sqrt(sum((u - ma) ** 2 for u in a)); sb = math.sqrt(sum((u - mb) ** 2 for u in b))
    return sum((u - ma) * (v - mb) for u, v in zip(a, b)) / (sa * sb) if sa and sb else 0.0

def maturation_class():
    meta = gzip.open(f"{GEO}/GSE150123/GSE150123_series_matrix.txt.gz", "rt").read().splitlines()
    gsm = next(l for l in meta if l.startswith("!Sample_geo_accession")).split("\t")[1:]
    day = next(l for l in meta if "differentiation day" in l).split("\t")[1:]
    day = {g.strip('"'): float(d.strip('"').split(": ")[1]) for g, d in zip(gsm, day)}
    cols = {}; tf = tarfile.open(f"{GEO}/GSE150123/GSE150123_RAW.tar")
    for m in tf.getmembers():
        g = m.name.split("_")[0]
        rows = list(csv.reader(io.TextIOWrapper(gzip.open(tf.extractfile(m), "r"), "utf-8")))[1:]
        cols[g] = {r[0]: float(r[1]) for r in rows}
    samples = sorted(cols); tot = {s: sum(cols[s].values()) for s in samples}
    ens = {r["symbol"]: r["ensg"] for r in tsv(f"{G}/derived/list_padj_le_0.05.tsv")}
    out = {}
    for sym in UP + DN:
        e = ens.get(sym)
        if not e or any(e not in cols[s] for s in samples): continue
        y = [math.log2(cols[s][e] / tot[s] * 1e6 + 1) for s in samples]
        if sum(cols[s][e] for s in samples) / len(samples) < 5: continue
        out[sym] = spearman([math.log10(day[s]) for s in samples], y)
    return out, len(samples)

RHO, NS = maturation_class()
mat = {g for g, r in RHO.items() if abs(r) >= RHO_MIN and ((g in UP and r < 0) or (g in DN and r > 0))}
COMP = decl | mat
# SENSITIVITY class (declared in the same file, run as a second wave after seeing that the primary class holds only 26 genes): declared markers UNION every S1 gene with |rho| >= 0.4 in either direction
BROAD = decl | {g for g, r in RHO.items() if abs(r) >= 0.4}
ROWS = []
for g in UP + DN:
    ROWS.append({"symbol": g, "ko_direction": "up" if g in UP else "down", "log2fc": L2.get(g, ""),
                 "in_declared_markers": int(g in decl), "broad_class_abs_rho_ge_0.4": int(g in BROAD), "rho_vs_log10_day": f"{RHO[g]:.3f}" if g in RHO else "",
                 "maturation_consistent": int(g in mat), "composition_class": int(g in COMP),
                 "in_L1000_12328_space": int(g in SPACE), "landmark_978": int(g in LM)})
write_tsv(f"{OUT}/composition_class.tsv", ROWS, list(ROWS[0]))

# ---------------------------------------------------------------- scenario queries (4 requests; both tails of each are read)
def sub(genes): return [g for g in genes]
QUERIES = {
    "QA_all": (UP, DN),
    "QC_minus_declared": ([g for g in UP if g not in decl], [g for g in DN if g not in decl]),
    "QD_minus_composition": ([g for g in UP if g not in COMP], [g for g in DN if g not in COMP]),
    "QF_minus_broad_maturation": ([g for g in UP if g not in BROAD], [g for g in DN if g not in BROAD]),
    # composition genes flipped: reversing this query reverses the non-composition genes and MIMICS the composition genes
    "QE_composition_flipped": ([g for g in UP if g not in COMP] + [g for g in DN if g in COMP], [g for g in DN if g not in COMP] + [g for g in UP if g in COMP]),
}
SCEN = [  # name, query, tail, role assigned to the composition class, role assigned to the rest
    ("S1_reverse_all", "QA_all", "reversers", "reverse", "reverse"),
    ("S2_mimic_all", "QA_all", "mimickers", "mimic", "mimic"),
    ("S3_ignore_declared_markers_reverse", "QC_minus_declared", "reversers", "ignore (27 declared markers only)", "reverse"),
    ("S4_ignore_composition_reverse", "QD_minus_composition", "reversers", "ignore", "reverse"),
    ("S5_ignore_composition_mimic", "QD_minus_composition", "mimickers", "ignore", "mimic"),
    ("S8_ignore_broad_class_reverse", "QF_minus_broad_maturation", "reversers", "ignore (broad class)", "reverse"),
    ("S9_ignore_broad_class_mimic", "QF_minus_broad_maturation", "mimickers", "ignore (broad class)", "mimic"),
    ("S6_mimic_composition_reverse_rest", "QE_composition_flipped", "reversers", "mimic", "reverse"),
    ("S7_reverse_composition_mimic_rest", "QE_composition_flipped", "mimickers", "reverse", "mimic"),
]

def http_json(url, body=None, timeout=600):
    req = urllib.request.Request(url, json.dumps(body).encode() if body is not None else None, {"Content-Type": "application/json"} if body is not None else {})
    r = urllib.request.urlopen(req, timeout=timeout); raw = r.read(); return raw, dict(r.headers), r.status

def run_live():
    genes = sorted({g for q in QUERIES.values() for arm in q for g in arm})
    emap, raw_all = {}, []
    for i in range(0, len(genes), 150):
        f = {"where": {"meta.symbol": {"inq": genes[i:i + 150]}}, "fields": ["id", "meta.symbol"], "limit": 1000}
        raw, _, _ = http_json(META + "entities?filter=" + urllib.parse.quote(json.dumps(f)))
        for e in json.loads(raw): emap[e["meta"]["symbol"]] = e["id"]
    json.dump(emap, open(f"{SCR}/entity_map.json", "w"))
    log("entities mapped", len(emap), "of", len(genes))
    for n, (name, (u, d)) in enumerate(QUERIES.items()):
        if os.path.exists(f"{SCR}/resp_{name}.meta.json") and json.load(open(f"{SCR}/resp_{name}.meta.json"))["status"] == 200: continue   # answered once, never re-asked
        if n: time.sleep(15)
        body = {"up_entities": [emap[g] for g in u if g in emap], "down_entities": [emap[g] for g in d if g in emap], "limit": LIMIT, "database": "l1000_cp"}
        t0 = datetime.datetime.now(datetime.timezone.utc).isoformat()
        try: raw, hdr, st = http_json(API, body)
        except Exception as e: raw, hdr, st = repr(e).encode(), {}, -1   # recorded, not retried
        open(f"{SCR}/resp_{name}.json", "wb").write(raw)
        json.dump({"utc": t0, "status": st, "bytes": len(raw), "sha256": sha(raw), "content_range": hdr.get("Content-Range"), "n_up": len(body["up_entities"]),
                   "n_down": len(body["down_entities"]), "limit": LIMIT}, open(f"{SCR}/resp_{name}.meta.json", "w"))
        log(name, st, len(raw), hdr.get("Content-Range"))
        if st != 200: raise SystemExit(f"query {name} failed: {raw[:300]!r}")
    ids = set()
    for name in QUERIES: ids |= {x["uuid"] for x in json.load(open(f"{SCR}/resp_{name}.json"))["results"]}
    ids = sorted(ids); meta = []
    for i in range(0, len(ids), 100):
        f = {"where": {"id": {"inq": ids[i:i + 100]}}, "limit": 200}
        raw, _, _ = http_json(META + "signatures?filter=" + urllib.parse.quote(json.dumps(f))); meta += json.loads(raw)
    json.dump(meta, open(f"{SCR}/signature_meta.json", "w")); log("signature metadata", len(meta))
    cids = sorted({str(m["meta"]["pubchem_id"]) for m in meta if m["meta"].get("pubchem_id")}); ik = {}
    for i in range(0, len(cids), 100):
        raw, _, _ = http_json("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + ",".join(cids[i:i + 100]) + "/property/InChIKey/JSON")
        for p in json.loads(raw)["PropertyTable"]["Properties"]: ik[str(p["CID"])] = p["InChIKey"]
        time.sleep(0.4)
    json.dump(ik, open(f"{SCR}/pubchem_inchikey.json", "w")); log("pubchem inchikeys", len(ik), "of", len(cids))

if MODE == "run": run_live()

# ---------------------------------------------------------------- analysis (offline)
meta = {m["id"]: m["meta"] for m in json.load(open(f"{SCR}/signature_meta.json"))}
PC = json.load(open(f"{SCR}/pubchem_inchikey.json"))
# GSE92742 pert_info: BRD -> inchi_key for compounds without a PubChem id (2021 library members are mostly absent here)
BRD_IK = {}
for r in csv.DictReader(gzip.open(f"{GEO}/GSE92742/GSE92742_Broad_LINCS_pert_info.txt.gz", "rt"), delimiter="\t"):
    if r.get("inchi_key") and r["inchi_key"] != "-666": BRD_IK[r["pert_id"]] = r["inchi_key"]
def brd(m):
    mm = re.search(r"(BRD-[A-Z]\d{8})", m.get("cmap_id", "") or ""); return mm.group(1) if mm else ""
def identity(m):
    b = brd(m); cid = str(m.get("pubchem_id", "") or "")
    if cid in PC: return PC[cid], "pubchem_cid"
    if b in BRD_IK: return BRD_IK[b], "GSE92742_pert_info_brd"
    return "", "unresolved"

CAT = {}; CATIK = {}
for l in gzip.open(f"{DR}/catalog/catalog.jsonl.gz", "rt"):
    d = json.loads(l); k = d["ids"].get("inchikey")
    if k: CATIK.setdefault(k, d["id"]); CAT.setdefault(k.split("-")[0], d["id"])
CATNAME = {}
LEGNAMES = {}
for l in gzip.open(f"{DR}/catalog/catalog.jsonl.gz", "rt"):
    d = json.loads(l); CATNAME[d["id"]] = d["name"]

# LEGEND list: proposals for the questions whose seeds came from the organoid transcript contrast (Q2, Q4, Q8: all seed sets are organoid-origin expression tiers)
PROP = [r for r in tsv(f"{P4}/proposals_it21.tsv") if r["question"] in ("Q2", "Q4", "Q8")]
HAND = {r["proposal_id"] for r in tsv(f"{P4}/handoff_it21.tsv")}
def leg_key(r):
    m = re.match(r"FAM:(CAT:CHEMBL\d+)$", r["family_id"])
    if not m: return "", ""
    cid = m.group(1); ik = next((k for k, v in CATIK.items() if v == cid), "")
    return cid, ik
LEG = []
for r in PROP:
    cid, ik = leg_key(r)
    LEG.append({"proposal_id": r["proposal_id"], "question": r["question"], "arm": r["hypothesis"], "status": r["status"], "compound": r["compound"], "catalogue_id": cid or r["family_id"],
                "inchikey": ik, "z_total": float(r["z_total"] or 0), "handoff": int(r["proposal_id"] in HAND), "identity_resolved": int(bool(ik))})
for x in LEG:
    if not x["identity_resolved"]: LEGNAMES.setdefault(re.sub(r"[^a-z0-9]", "", x["compound"].lower()), []).append(x["proposal_id"])
LEG_BY_IK = {}
for x in LEG:
    if x["inchikey"]: LEG_BY_IK.setdefault(x["inchikey"].split("-")[0], []).append(x)

def compounds(name, tail):
    res = [x for x in json.load(open(f"{SCR}/resp_{name}.json"))["results"] if x["type"] == tail]
    res.sort(key=lambda x: x["z-sum"], reverse=(tail == "mimickers")); best = {}
    for x in res:
        m = meta.get(x["uuid"], {}); ik, via = identity(m)
        key = ik.split("-")[0] if ik else "UNRES:" + (brd(m) or (m.get("pert_name") or "").lower())
        c = best.setdefault(key, {"key": key, "inchikey": ik, "identity_via": via, "pert_name": m.get("pert_name", ""), "brd": brd(m), "z_sum": x["z-sum"], "cell_line": m.get("cell_line", ""),
                                  "tissue": m.get("tissue", ""), "disease": m.get("disease", ""), "dose": m.get("pert_dose", ""), "time": m.get("pert_time", ""), "library": m.get("cmap_id", "")[:12], "lines": set(), "n_sigs": 0})
        c["lines"].add(m.get("cell_line", "")); c["n_sigs"] += 1
    out = list(best.values()); return out, len(res)

SCEN_TOP, TAB = {}, []
for sc, q, tail, comp_role, rest_role in SCEN:
    cs, n_sig = compounds(q, tail); top = cs[:TOPN]; SCEN_TOP[sc] = [c["key"] for c in top]
    arm = "H_HARM" if tail == "reversers" and q != "QE_composition_flipped" else ("H_PROTECT" if q != "QE_composition_flipped" else "mixed")
    for i, c in enumerate(cs[:TOPN], 1):
        ik = c["inchikey"]; sk = ik.split("-")[0] if ik else ""
        cat_id = CATIK.get(ik) or (CAT.get(sk) if sk else None)
        hit = LEG_BY_IK.get(sk, [])
        TAB.append({"scenario": sc, "query": q, "tail": tail, "composition_class_role": comp_role, "rest_role": rest_role, "rank": i, "pert_name": c["pert_name"], "brd_id": c["brd"],
                    "inchikey": ik, "identity_via": c["identity_via"], "z_sum_best_signature": f"{c['z_sum']:.2f}", "cell_line": c["cell_line"], "tissue": c["tissue"], "disease": c["disease"],
                    "dose_best": c["dose"], "time_best": c["time"], "library_best": c["library"], "n_signatures_in_tail": c["n_sigs"], "n_cell_lines": len(c["lines"]),
                    "in_legend_catalogue": ("exact_inchikey" if ik in CATIK else ("skeleton_only_stereo_differs" if sk in CAT else "no")) if ik else "identity_unresolved",
                    "catalogue_id": cat_id or "", "name_coincidence_with_unresolved_legend_rows_NOT_IDENTITY": ";".join(LEGNAMES.get(re.sub(r"[^a-z0-9]", "", c["pert_name"].lower()), [])) if c["pert_name"] else "",
                    "in_legend_Q2Q4Q8_proposals": ";".join(sorted({f"{h['proposal_id']}({h['arm']})" for h in hit})) if hit else ("not_comparable_identity_unresolved" if not ik else "no")})
cols = ["scenario", "query", "tail", "composition_class_role", "rest_role", "rank", "pert_name", "brd_id", "inchikey", "identity_via", "z_sum_best_signature", "cell_line", "tissue", "disease", "dose_best", "time_best",
        "library_best", "n_signatures_in_tail", "n_cell_lines", "in_legend_catalogue", "catalogue_id", "in_legend_Q2Q4Q8_proposals", "name_coincidence_with_unresolved_legend_rows_NOT_IDENTITY"]
write_tsv(f"{OUT}/scenarios.tsv", TAB, cols)

# ---------------------------------------------------------------- overlap: scenarios among themselves and with LEGEND's list
def jac(a, b): a, b = set(a), set(b); return (len(a & b) / len(a | b)) if (a | b) else float("nan")
LEG_TOP = {}
for arm in ("H_HARM", "H_PROTECT"):
    rows = sorted([x for x in LEG if x["arm"] == arm and x["identity_resolved"]], key=lambda x: -x["z_total"])
    seen, top = set(), []
    for x in rows:
        k = x["inchikey"].split("-")[0]
        if k not in seen: seen.add(k); top.append(k)
    LEG_TOP[arm] = top[:TOPN]
LEG_ALL = {arm: {x["inchikey"].split("-")[0] for x in LEG if x["arm"] == arm and x["identity_resolved"]} for arm in ("H_HARM", "H_PROTECT")}
OV = []
names = [s[0] for s in SCEN]
for i, a in enumerate(names):
    for b in names[i + 1:]:
        OV.append({"set_a": a, "set_b": b, "n_a": len(SCEN_TOP[a]), "n_b": len(SCEN_TOP[b]), "intersection": len(set(SCEN_TOP[a]) & set(SCEN_TOP[b])), "jaccard_top20": f"{jac(SCEN_TOP[a], SCEN_TOP[b]):.3f}", "kind": "scenario_vs_scenario"})
for a in names:
    for arm in ("H_HARM", "H_PROTECT"):
        top = [k for k in SCEN_TOP[a] if not k.startswith("UNRES:")]
        OV.append({"set_a": a, "set_b": f"LEGEND_{arm}_top20_by_z_total(identity_resolved_only)", "n_a": len(SCEN_TOP[a]), "n_b": len(LEG_TOP[arm]), "intersection": len(set(top) & set(LEG_TOP[arm])),
                   "jaccard_top20": f"{jac(top, LEG_TOP[arm]):.3f}", "kind": "scenario_vs_LEGEND_top20"})
        OV.append({"set_a": a, "set_b": f"LEGEND_{arm}_all_resolved_Q2Q4Q8", "n_a": len(SCEN_TOP[a]), "n_b": len(LEG_ALL[arm]), "intersection": len(set(top) & LEG_ALL[arm]),
                   "jaccard_top20": f"{jac(top, LEG_ALL[arm]):.3f}", "kind": "scenario_vs_LEGEND_all"})
write_tsv(f"{OUT}/overlap.tsv", OV, ["set_a", "set_b", "n_a", "n_b", "intersection", "jaccard_top20", "kind"])

# ---------------------------------------------------------------- coverage and run facts
def cov(u, d):
    s = set(u) | set(d)
    return {"genes_in_query": len(s), "up": len(u), "down": len(d), "in_L1000_12328_space": len(s & SPACE), "landmark_978_measured": len(s & LM), "inferred_not_landmark": len((s & SPACE) - LM),
            "not_in_space": len(s - SPACE)}
facts = {"signature": "GSE156243 KO v WT organoid, S1 (padj<=0.01, |log2FC|>=0.26)", "composition_class": {"broad_class_size": len(BROAD), "declared_markers_in_S1": len(decl), "maturation_consistent": len(mat), "union": len(COMP),
         "gse150123_samples": NS, "rho_threshold": RHO_MIN, "genes_with_rho": len(RHO)},
         "coverage": {k: cov(*v) for k, v in QUERIES.items()},
         "legend_Q2Q4Q8": {"rows": len(LEG), "identity_resolved_rows": sum(x["identity_resolved"] for x in LEG), "dgidb_only_unresolved_rows": sum(1 - x["identity_resolved"] for x in LEG)},
         "responses": {n: json.load(open(f"{SCR}/resp_{n}.meta.json")) for n in QUERIES}}
for sc in names:
    r = [t for t in TAB if t["scenario"] == sc]
    facts.setdefault("scenario_counts", {})[sc] = {"top_n": len(r), "identity_resolved": sum(1 for t in r if t["inchikey"]), "in_catalogue": sum(1 for t in r if t["in_legend_catalogue"].startswith(("exact", "skeleton"))),
                                                  "in_legend_Q2Q4Q8_by_identity": sum(1 for t in r if t["in_legend_Q2Q4Q8_proposals"] not in ("no", "not_comparable_identity_unresolved"))}
json.dump(facts, open(f"{OUT}/run_facts.json", "w"), indent=1, sort_keys=True)
log("done", json.dumps(facts["scenario_counts"]))

# ---------------------------------------------------------------- depth check: LEGEND compounds (identity resolved) anywhere in the 300 returned signatures per tail
DEEP = []
for q in QUERIES:
    allr = json.load(open(f"{SCR}/resp_{q}.json"))["results"]
    for tail in ("reversers", "mimickers"):
        res = sorted([x for x in allr if x["type"] == tail], key=lambda x: x["z-sum"], reverse=(tail == "mimickers"))
        for rk, x in enumerate(res, 1):
            m = meta.get(x["uuid"], {}); ik, _ = identity(m); h = LEG_BY_IK.get(ik.split("-")[0], []) if ik else []
            for l in h:
                DEEP.append({"query": q, "tail": tail, "signature_rank_in_tail": rk, "z_sum": f"{x['z-sum']:.2f}", "pert_name": m.get("pert_name", ""), "inchikey": ik, "cell_line": m.get("cell_line", ""),
                             "dose": m.get("pert_dose", ""), "time": m.get("pert_time", ""), "legend_proposal": l["proposal_id"], "legend_question": l["question"], "legend_arm": l["arm"], "legend_compound": l["compound"]})
write_tsv(f"{OUT}/legend_compounds_in_returned_depth.tsv", DEEP, ["query", "tail", "signature_rank_in_tail", "z_sum", "pert_name", "inchikey", "cell_line", "dose", "time", "legend_proposal", "legend_question", "legend_arm", "legend_compound"])
log("legend compounds found in the returned depth:", len(DEEP))
