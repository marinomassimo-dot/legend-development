#!/usr/bin/env python3
"""IT9 P3: consolidate P2 candidates into parents, diagnostics, feasibility axis, KNOWN-to-LEGEND matching, clusters and the pre-registered selection (selection_rules.md + Amendments 1, 2).
Usage: consolidate_select_it9_p3.py --work DIR --out DIR   (DIR/work has pool_raw.tsv, identity_map.tsv, chembl_profile.tsv; writes the consolidated tables; HGNC gene groups fetched by symbol only)."""
import argparse, collections, csv, glob, gzip, importlib.util, json, os, re, statistics, sys, time, urllib.parse, urllib.request
from pathlib import Path
H = Path(__file__).resolve().parent; D = H.parent; P2 = D / "generation_it9_p2_20261030"; R = P2 / "results"; RK = D / "ranking_it8_p9_20261029"
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--work", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
W = Path(a.work); OUT = Path(a.out)
def rd(p, gz=False):
    return list(csv.DictReader(gzip.open(p, "rt") if gz else open(p), delimiter="\t"))
def wr(p, rows, cols):
    with open(p, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols)
        for r in rows: w.writerow([("" if r.get(c) is None else str(r.get(c))).replace("\t", " ").replace("\n", " ") for c in cols])
os.environ.setdefault("LEGEND_CATALOG_CACHE", str(D / "catalog" / "cache"))
spec = importlib.util.spec_from_file_location("seed_engine", P2 / "seed_engine.py"); se = importlib.util.module_from_spec(spec); sys.modules["seed_engine"] = se; spec.loader.exec_module(se)
# ---- inputs
pool = rd(W / "pool_raw.tsv")
cand = []
for f in sorted(glob.glob(str(R / "candidates_Q*.tsv"))): cand += rd(f)
idmap = {r["family_id"]: r for r in rd(W / "identity_map.tsv")}
prof = {r["chembl_id"]: r for r in rd(W / "chembl_profile.tsv")}
inv = {r["family_id"]: r for r in rd(RK / "inventory_families.tsv.gz", True)}
fam_t = collections.defaultdict(list)
for r in rd(R / "family_actions.tsv.gz", True): fam_t[r["family_id"]].append(r)
edges = se.read_edges(); degc = collections.Counter()
for e in edges: degc[e[0]] += 1; degc[e[1]] += 1
degs = sorted(degc.values()); HUB = degs[int(0.95 * (len(degs) - 1))]
# catalogue mechanism text per family (for F1 and the profile)
allf = {r["family_id"] for r in pool} | {r["family_id"] for r in cand}
cat = {}
for l in gzip.open(D / "catalog/catalog.jsonl.gz", "rt"):
    r = json.loads(l); fid = "FAM:" + r["id"]
    if fid in allf: cat[fid] = r
# ---- known-to-LEGEND index (family ids and parent ids)
known = collections.defaultdict(set)
for c, v in json.load(open(D / "catalog/card_links.json"))["cards"].items():
    for l in v["links"]: known["FAM:" + l["catalogue_id"]].add("card:" + c)
for r in rd(RK / "unit_members.tsv"):
    if r["family_id"]: known[r["family_id"]].add("unit_member:" + r["unit_id"])
for r in rd(RK / "deepening_queue.tsv"):
    for f in r["family_ids"].split(";"):
        if f.strip(): known[f.strip()].add("deepening_queue:" + r["display_group"])
unit_cards = {}  # unit -> cards
CLASS_UNITS = {"U16", "U17", "U18", "U20", "U21", "U25", "U27"}
CLASS_TARGETS = {"GRIN1", "GRIN2A", "GRIN2B", "GRIN2C", "GRIN2D", "GRIN3A", "GRIN3B", "GRIA1", "GRIA2", "GRIA3", "GRIA4", "CACNA1G", "CACNA1H", "CACNA1I"}
# ---- parent collapse
def info(fid):
    i = idmap.get(fid, {}); cid = i.get("chembl_id", ""); p = prof.get(cid, {})
    return i, cid, p
parent_of = {}
for fid in allf:
    i, cid, p = info(fid)
    parent_of[fid] = p.get("parent_chembl_id") or cid or fid
fams_of = collections.defaultdict(list)
for fid, p in parent_of.items(): fams_of[p].append(fid)
# seed genes per set (for hop-0 target of direct-search rows)
seedgenes = {}
for f in glob.glob(str(P2 / "seeds_p1" / "Q*.tsv")):
    g = set()
    for r in rd(f):
        if r.get("kind") == "process": g |= {x for x in r.get("members", "").split(";") if x}
        elif r.get("gene"): g.add(r["gene"].upper())
    seedgenes[os.path.basename(f)[:-4]] = g
# ---- per (question, set) rows
def qname(s): return s.split("_")[0]
rows_by_parent = collections.defaultdict(list)
for r in pool: rows_by_parent[parent_of[r["family_id"]]].append(dict(src="pool", set=r["set"], q=qname(r["set"]), arm=r["arm"], fid=r["family_id"], zt=float(r["Z_total"]), zi=float(r["Z_indeg"]), tg=r["main_target"], tdeg=int(r["main_target_degree"]), seed=r["top_seed_gene"], sd=r["top_seed_direction"], hop=r["hop"], cond=int(r["conditional"]), own=int(r["seed_own_target"]), specific=1, name=r["name"], seeds=r["seeds_contributing"], guard=r["guard"]))
pool_keys = {(r["set"], r["family_id"]) for r in pool}
for r in cand:
    if (r["seed_set"], r["family_id"]) in pool_keys: continue
    cs = (r["contributing_seed_1"] or "").split("|"); seed = cs[1] if len(cs) > 5 else ""; sd = cs[2] if len(cs) > 5 else ""; hop = cs[3] if len(cs) > 5 else ""; tg = cs[4] if len(cs) > 5 else ""
    if r["arm"] == "direct_search" and not tg:
        hits = sorted({t["target_symbol"] for t in fam_t.get(r["family_id"], [])} & seedgenes.get(r["seed_set"], set()))
        if hits: tg, seed, hop = hits[0], hits[0], "hop0"
    zt = float(r["Z_ind_robust_total_null"]) if r["Z_ind_robust_total_null"] else None; zi = float(r["Z_ind_robust_indeg_null"]) if r["Z_ind_robust_indeg_null"] else None
    rows_by_parent[parent_of[r["family_id"]]].append(dict(src="table", set=r["seed_set"], q=r["question"], arm=r["arm"], fid=r["family_id"], zt=zt, zi=zi, tg=tg, tdeg=degc.get(tg, -1) if tg else -1, seed=seed, sd=sd, hop=hop, cond=int(r["conditional_on_uncertain_seeds"] or 0), own=0, specific=0, name=r["name"], seeds="", guard=r["evaluation_forbidden_on"]))
# ---- HGNC groups for main targets
tg_all = sorted({x["tg"] for rs in rows_by_parent.values() for x in rs if x["tg"]})
hg = {}
cache = W / "hgnc_groups.tsv"
if cache.exists(): hg = {r["symbol"]: r for r in rd(cache)}
for t in tg_all:
    if t in hg: continue
    grp, st = "NO_GROUP", "OK"
    try:
        rq = urllib.request.Request("https://rest.genenames.org/fetch/symbol/" + urllib.parse.quote(t), headers={"Accept": "application/json"})
        with urllib.request.urlopen(rq, timeout=30) as f: d = json.load(f)["response"]
        if d["numFound"] == 0: grp, st = "UNKNOWN", "SYMBOL_NOT_FOUND"
        else:
            g = d["docs"][0].get("gene_group") or []
            grp = g[0] if g else "NO_GROUP"
    except Exception as e: grp, st = "UNKNOWN", "SERVICE_ERROR"
    hg[t] = dict(symbol=t, group=grp, state=st); time.sleep(0.15)
wr(cache, list(hg.values()), ["symbol", "group", "state"])
# ---- feasibility
def feas(parent, fids):
    i, cid, p = info(fids[0])
    routes = [idmap.get(f, {}).get("identity_route", "unresolved") for f in fids]
    best = next((r for r in ["catalogue_chembl", "reconciliation_chembl", "dgidb_concept_chembl", "name_exact_unique"] if r in routes), "unresolved")
    flags, excl = [], []
    if best == "unresolved" or not p or p.get("state") != "OK":
        if best == "unresolved": excl.append("F4_identity_unresolved")
        else: flags.append("profile_" + (p.get("state", "NO_PROFILE") if p else "NO_PROFILE"))
    atc = (p.get("atc") or "").split(";") if p else []
    mech = " ".join((t.get("mechanism_of_action") or "") for f in fids for t in (cat.get(f, {}).get("targets") or []) if isinstance(t, dict)).lower()
    if any(x.startswith(("L01A", "L01B", "L01C", "L01D", "L01XA")) for x in atc) or re.search(r"topoisomerase|tubulin|dna alkylat|dna synthesis|dna intercalat|dna crosslink|antimetabolite", mech): excl.append("F1_cytotoxic_anticancer")
    elif any(x.startswith("L01") for x in atc): flags.append("oncology_targeted")
    if p and p.get("topical") in ("True", "1") and p.get("oral") not in ("True", "1") and p.get("parenteral") not in ("True", "1"): excl.append("F2_topical_only")
    elif atc and all(x.startswith(("D", "S01", "S02", "S03")) for x in atc): excl.append("F2_topical_only_by_ATC")
    mt = (p.get("molecule_type") if p else "") or ""; mods = {inv.get(f, {}).get("modality", "") for f in fids}
    if (mt and mt != "Small molecule" and mt != "Unknown") or (mods & {"antibody", "other:antibody drug conjugate", "other:vaccine component", "cell_product", "enzyme", "oligonucleotide", "protein_or_peptide", "gene_product"} and not mt == "Small molecule"): excl.append("F3_modality_" + (mt or ",".join(sorted(mods & {"antibody", "other:antibody drug conjugate", "other:vaccine component", "cell_product", "enzyme", "oligonucleotide", "protein_or_peptide", "gene_product"}))).replace(" ", "_"))
    stat = ";".join(sorted({inv.get(f, {}).get("status_class", "") for f in fids}))
    mp = (p.get("max_phase") if p else "") or ""
    try: mpv = float(mp)
    except Exception: mpv = None
    if (mpv is None or mpv < 1) and "approved_any_source" not in stat and "clinical_candidate" not in stat: excl.append("F5_no_human_exposure_statement")
    if p and p.get("withdrawn_flag") in ("True", "1"): excl.append("F6_withdrawn")
    return best, excl, flags, p, stat
def lgnd(fids, parent):
    s = set()
    for f in fids + [("FAM:CAT:" + parent) if parent.startswith("CHEMBL") else parent]: s |= known.get(f, set())
    return sorted(s)
# ---- parent table
out = []
for parent, rs in rows_by_parent.items():
    fids = sorted(set(parent_of_f for parent_of_f in fams_of[parent] if parent_of_f in allf))
    route, excl, flags, p, stat = feas(parent, fids)
    nm = (p.get("parent_pref_name") or p.get("pref_name")) if p else ""
    nm = nm or rs[0]["name"]
    sp = [x for x in rs if x["specific"]]
    best = sorted(sp, key=lambda x: -min(abs(x["zt"]), abs(x["zi"])))[0] if sp else None
    arms = sorted({(x["q"] + ":" + x["arm"]) for x in rs}); setarms = sorted({(x["set"] + ":" + x["arm"]) for x in rs}); spq = sorted({(x["q"] + ":" + x["arm"]) for x in sp})
    dirs = {x["arm"] for x in sp if x["arm"] in ("opposes", "mimics")}
    ntg = len({t["target_symbol"] for f in fids for t in fam_t.get(f, [])})
    tg = (best or rs[0])["tg"]; tdeg = (best or rs[0])["tdeg"]
    kn = lgnd(fids, parent)
    allt = {t["target_symbol"] for f in fids for t in fam_t.get(f, [])}
    atc = (p.get("atc") or "") if p else ""
    unitsk = {k.split(":", 1)[1] for k in kn if k.startswith("unit_member:")}
    cls = int(atc.startswith("N03") or ";N03" in atc or bool(allt & CLASS_TARGETS) or bool(unitsk & CLASS_UNITS))
    out.append(dict(parent=parent, name=nm, family_ids=";".join(fids), n_families=len(fids), identity_route=route, chembl_parent=(p.get("parent_chembl_id") if p else ""), max_phase=(p.get("max_phase") if p else ""), atc=atc, status_class=stat,
                    questions=";".join(sorted({x["q"] for x in rs})), q_arms=";".join(arms), sets_arms=";".join(setarms), seed_specific_q_arms=";".join(spq), seed_specific=int(bool(sp)), direction=("opposes" if dirs == {"opposes"} else "mimics" if dirs == {"mimics"} else "CONFLICT" if dirs else "none(direct_search/top-list only)"),
                    best_set=best["set"] if best else "", best_Z_total=round(best["zt"], 2) if best else "", best_Z_indeg=round(best["zi"], 2) if best else "", min_absZ=round(min(abs(best["zt"]), abs(best["zi"])), 2) if best else "",
                    top_seed=(best or rs[0])["seed"], top_seed_direction=(best or rs[0])["sd"], seeds_contributing=(best or {}).get("seeds", ""), conditional=int(any(x["cond"] for x in sp)), hop=(best or rs[0])["hop"], main_target=tg, main_target_degree=tdeg,
                    hub_target=int(tdeg >= HUB), n_signed_targets=ntg, promiscuous=int(ntg >= 5), seed_own_target=int(any(x["own"] for x in rs)), direct_search_hit=int(any(x["arm"] == "direct_search" for x in rs)),
                    guard=";".join(sorted({x["guard"] for x in rs if x["guard"] not in ("", "none")})), mech_group=hg.get(tg, {}).get("group", "NO_TARGET") if tg else "NO_TARGET",
                    known_to_legend=";".join(kn), class_asm_nmdar_tcalcium=cls, feasibility_exclusions=";".join(excl), feasibility_flags=";".join(flags), access_categories=";".join(sorted({inv.get(f, {}).get("access_categories", "") for f in fids})),
                    modality=";".join(sorted({inv.get(f, {}).get("modality", "") for f in fids}))))
# ---- clusters
cl = collections.defaultdict(list)
for r in out:
    if r["seed_specific"] and r["main_target"]: cl[r["main_target"]].append(r)
clrows = []; hubart = set()
for t, rs in sorted(cl.items(), key=lambda kv: -len(kv[1])):
    med = statistics.median(int(x["n_signed_targets"]) for x in rs); hubshare = sum(int(x["hub_target"]) for x in rs) / len(rs)
    ha = int(int(rs[0]["hub_target"]) == 1 and med >= 5)
    if ha: hubart.add(t)
    clrows.append(dict(cluster_main_target=t, mech_group=rs[0]["mech_group"], n_parents=len(rs), questions=";".join(sorted({qa.split(":")[0] for x in rs for qa in x["seed_specific_q_arms"].split(";") if qa})), n_opposes=sum(x["direction"] == "opposes" for x in rs), n_mimics=sum(x["direction"] == "mimics" for x in rs),
                       target_degree=rs[0]["main_target_degree"], hub_target_share=round(hubshare, 2), median_promiscuity=med, hub_artefact_cluster=ha, n_known_to_legend=sum(bool(x["known_to_legend"]) for x in rs), n_feasible=sum(not x["feasibility_exclusions"] for x in rs)))
for r in out: r["hub_artefact_cluster"] = int(r["main_target"] in hubart)
# ---- selection
def feasible(r): return not r["feasibility_exclusions"]
def key_fn(r, sel):
    groups = {x["mech_group"] for x in sel}; seeds = {(x["best_set"].split("_")[0], x["top_seed"]) for x in sel}
    return (int(r["mech_group"] in groups), int((r["best_set"].split("_")[0], r["top_seed"]) in seeds), int(bool(r["known_to_legend"])), int(r["hub_target"]), -min(r["_z"], 20), r["parent"])
for r in out: r["_z"] = float(r["min_absZ"]) if r["min_absZ"] != "" else 0.0
C = [r for r in out if r["seed_specific"] and r["direction"] in ("opposes", "mimics") and feasible(r) and not r["seed_own_target"] and not r["promiscuous"] and not r["hub_artefact_cluster"] and r["best_set"]]
sel = []; why = {}
def qset(r): return r["best_set"]
def pick(cands, reason):
    cands = [c for c in cands if c not in sel]
    if not cands: return None
    c = min(cands, key=lambda r: key_fn(r, sel)); sel.append(c); why[c["parent"]] = reason; return c
# references first (they never fill quotas): up to 5, one per unit, ranked: seed-specific pool member, else direct-search hit
refs = []
cand_refs = [r for r in out if any(k.startswith(("card:", "unit_member:", "deepening_queue:")) for k in r["known_to_legend"].split(";")) and r["parent"] not in {x["parent"] for x in refs}]
def unit_of(r):
    us = sorted({k.split(":", 1)[1] for k in r["known_to_legend"].split(";") if k.startswith("unit_member:")}) or sorted({k for k in r["known_to_legend"].split(";")})
    return us[0] if us else r["parent"]
def ref_rank(r):
    k = r["known_to_legend"]; lv = 0 if "card:" in k else 1 if "unit_member:" in k else 2
    qs = {"Q2": 0, "Q3": 1, "Q4": 2, "Q5": 3, "Q6": 4, "Q7": 5, "Q1": 6}; qo = min((qs.get(x.split(":")[0], 9) for x in r["q_arms"].split(";")), default=9)
    return (-r["seed_specific"], lv, qo, r["parent"])
cand_refs.sort(key=ref_rank)
used_units = set()
for r in cand_refs:
    u = unit_of(r)
    if u in used_units: continue
    refs.append(r); used_units.add(u)
    if len(refs) >= 5: break
for r in refs: sel.append(r); why[r["parent"]] = "reference"
slots = [("Q2", "opposes"), ("Q2", "mimics"), ("Q4", None), ("Q4", None), ("Q5", None), ("Q5", None), ("Q5", None), ("Q6", None), ("Q6", None)]
for q, arm in slots:
    cs = [r for r in C if r["best_set"].startswith(q + "_") and (arm is None or r["direction"] == arm)]
    pick(cs, "slot:%s%s" % (q, "" if arm is None else ":" + arm))
for arm in ("opposes", "mimics"):
    while sum(1 for x in sel if why[x["parent"]] != "reference" and x["direction"] == arm) < 4:
        cs = [r for r in C if r["direction"] == arm and not (r["best_set"].startswith("Q6_") and sum(1 for x in sel if x["best_set"].startswith("Q6_")) >= 4)]
        if not pick(cs, "slot:overall_" + arm): break
def q6n(): return sum(1 for x in sel if x["best_set"].startswith("Q6_") and why[x["parent"]] != "reference")
while len(sel) < 18:  # 20 total minus the 2 places reserved for artefact controls
    groups = {x["mech_group"] for x in sel}
    cs = [r for r in C if r["mech_group"] not in groups and not (r["best_set"].startswith("Q6_") and q6n() >= 4)]
    if not pick(cs, "fill:new_mechanism_group"): break
if len(sel) < 12:
    while len(sel) < 12:
        cs = [r for r in C if not (r["best_set"].startswith("Q6_") and q6n() >= 4)]
        if not pick(cs, "fill:any"): break
# artefact controls: up to 2 from hub-artefact clusters or promiscuous, feasible, seed-specific, highest min|Z| (capped)
ctrl = [r for r in out if r["seed_specific"] and r["direction"] in ("opposes", "mimics") and feasible(r) and (r["hub_artefact_cluster"] or r["promiscuous"]) and r["parent"] not in {x["parent"] for x in sel}]
ctrl.sort(key=lambda r: (-min(r["_z"], 20), r["parent"]))
seen_g = set()
for r in ctrl:
    if sum(1 for x in sel if why[x["parent"]] == "artefact_control") >= 2: break
    if r["main_target"] in seen_g: continue
    seen_g.add(r["main_target"]); sel.append(r); why[r["parent"]] = "artefact_control"
# class cap 25 percent
dropped = {}
def share(): return sum(x["class_asm_nmdar_tcalcium"] for x in sel) / max(len(sel), 1)
while sel and share() > 0.25:
    cs = [x for x in sel if x["class_asm_nmdar_tcalcium"]]
    worst = sorted(cs, key=lambda x: (why[x["parent"]] == "reference", -x["_z"]))[0] if cs else None
    if why[worst["parent"]] != "reference" and False: pass
    sel.remove(worst); dropped[worst["parent"]] = "class_cap"
selp = {x["parent"] for x in sel}
for r in out:
    if r["parent"] in selp: r["disposition"] = "selected:" + why[r["parent"]]
    elif r["parent"] in dropped: r["disposition"] = "excluded:class_cap"
    elif r["feasibility_exclusions"] and r["seed_specific"]: r["disposition"] = "excluded:" + r["feasibility_exclusions"].split(";")[0]
    elif r["seed_specific"] and r["seed_own_target"]: r["disposition"] = "not_taken:seed_own_target"
    elif r["seed_specific"] and r["promiscuous"]: r["disposition"] = "not_taken:promiscuous(>=5 targets)"
    elif r["seed_specific"] and r["hub_artefact_cluster"]: r["disposition"] = "not_taken:hub_artefact_cluster"
    elif r["seed_specific"]: r["disposition"] = "not_taken:not_best_by_selection_key"
    elif r["feasibility_exclusions"]: r["disposition"] = "not_seed_specific(" + ("direct_search" if r["direct_search_hit"] else "top-list") + ");feasibility:" + r["feasibility_exclusions"].split(";")[0]
    else: r["disposition"] = "not_seed_specific(" + ("direct_search_arm" if r["direct_search_hit"] else "top-list_only") + ")"
    r["selection_reason"] = why.get(r["parent"], "")
for r in out: r.pop("_z", None)
OUT.mkdir(parents=True, exist_ok=True)
cols = list(out[0]); 
out.sort(key=lambda r: (not r["disposition"].startswith("selected"), r["disposition"], r["parent"]))
wr(OUT / "candidates_consolidated.tsv", out, cols)
wr(OUT / "clusters.tsv", clrows, list(clrows[0]))
wr(OUT / "selected_core.tsv", [r for r in out if r["disposition"].startswith("selected")], cols)
wr(OUT / "excluded.tsv", [r for r in out if r["disposition"].startswith("excluded") or (r["seed_specific"] and r["disposition"].startswith("not_taken") and r["disposition"] != "not_taken:not_best_by_selection_key")], cols)
print("parents", len(out), "seed-specific", sum(r["seed_specific"] for r in out), "selected", len(sel), "hub threshold", HUB, "class share %.2f" % share(), file=sys.stderr)
