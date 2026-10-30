#!/usr/bin/env python3
"""IT9 P4c-D: apply SELECTION_NOTE.md Part 1 (pre-written rules) to the v3 Q5/Q4 expression seed-specific lists.
  select_p4c_d.py --help        this text
  select_p4c_d.py reselect [--out DIR]   offline: re-applies the selection rules to the saved selection_pool.tsv (no network)
  select_p4c_d.py run [--out DIR]   fetches ChEMBL molecule records (ChEMBL ids and exact compound names only) and HGNC groups (gene symbols only);
                                    writes selection_pool.tsv, selection_clusters.tsv, selected_p4c_d.tsv, excluded_selection_p4c_d.tsv, selection_service_log.tsv
No key, no e-mail, no operator identity is sent. Standard library only. Not medical advice."""
import argparse, collections, csv, datetime, gzip, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
V3 = D / "generation_it9_p2_20261030/v3/results"; RK = D / "ranking_it8_p9_20261029"; P3 = D / "exploration_it9_p3_20261030/inputs_fetched"
ROUND1 = ["curcumin", "belnacasan", "fosfestrol", "balsalazide", "ramelteon", "belzutifan", "ceperognastat", "implitapide", "harmine", "pomalidomide", "lenalidomide", "defosbarasertib", "barasertib", "at9283", "at-9283", "pinometostat", "sirolimus", "ar-12", "dichloroacetate", "felbamate", "memantine", "thalidomide"]
LOG = []
def get(url, hdr=None, tries=4):
    err = None
    for t in range(tries):
        try:
            rq = urllib.request.Request(url, headers=hdr or {})
            with urllib.request.urlopen(rq, timeout=60) as r:
                LOG.append([datetime.datetime.utcnow().isoformat(timespec="seconds"), url[:160], r.status, t + 1]); return json.load(r)
        except urllib.error.HTTPError as e:
            LOG.append([datetime.datetime.utcnow().isoformat(timespec="seconds"), url[:160], e.code, t + 1]); err = e
            if e.code == 404: return None
        except Exception as e:
            LOG.append([datetime.datetime.utcnow().isoformat(timespec="seconds"), url[:160], type(e).__name__, t + 1]); err = e
        time.sleep(2 + 4 * t)
    return "ERR"
def rd(p, gz=False):
    return list(csv.DictReader(gzip.open(p, "rt") if gz else open(p), delimiter="\t"))
def wr(p, rows, cols):
    with open(p, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols)
        for r in rows: w.writerow([("" if r.get(c) is None else str(r.get(c))).replace("\t", " ").replace("\n", " ") for c in cols])
def nn(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
def choose(rows):
    """Selection per SELECTION_NOTE.md 1.3 and 1.5. Representative of a cluster: highest max_phase, then higher min|z| (capped 20), then LOWEST catalogue family id (the first run used -len(family_ids) here, a deviation from the note; corrected offline, see README)."""
    for r in rows:
        r["min_abs_z_capped20"] = float(r["min_abs_z_capped20"])
    cl = collections.defaultdict(list)
    for r in rows: cl[(r["main_target"], r["arm"])].append(r)
    crow = []
    for (mt, arm), rs in sorted(cl.items()):
        el = [r for r in rs if not r["exclusions"]]
        crow.append(dict(main_target=mt, arm=arm, question=rs[0]["q"], seed=rs[0]["seed"], mech_group=rs[0]["mech_group"], n_parents=len(rs), n_eligible=len(el), exclusion_counts=";".join("%s=%d" % kv for kv in sorted(collections.Counter(e.split("_")[0] for r in rs for e in r["exclusions"].split(";") if e).items())), best_min_abs_z=max(r["min_abs_z_capped20"] for r in rs)))
    sel = []
    elig = {}
    for k, rs in cl.items():
        el = [r for r in rs if not r["exclusions"]]
        if el: elig[k] = sorted(el, key=lambda r: (-(float(r["max_phase"]) if r["max_phase"] not in ("", None) else -1), -r["min_abs_z_capped20"], min(r["family_ids"].split(";"))))[0]
    def classknown(r): return int(bool(r["known_to_legend"]) or bool(r["target_named_in_cards"]))
    def key(k, sel):
        r = elig[k]; groups = {x["mech_group"] for x in sel}; seeds = {x["seed"] for x in sel}
        return (int(r["mech_group"] in groups), int(r["seed"] in seeds), classknown(r), -r["min_abs_z_capped20"], r["family_ids"])
    why = {}
    def add(k, reason):
        sel.append(elig[k]); why[(elig[k]["parent"], elig[k]["main_target"])] = reason
    # reserved axes (1.5)
    for axis, tg in (("BET axis", "BRD4"), ("HMGB1 axis", "HMGB1")):
        ks = [k for k in elig if k[0] == tg and k[1] == "opposes"] or [k for k in elig if k[0] == tg]
        if ks: add(ks[0], "reserved:" + axis)
    def nsel(q): return sum(1 for x in sel if x["q"] == q)
    if nsel("Q4") == 0:
        ks = [k for k in elig if elig[k]["q"] == "Q4" and elig[k]["parent"] not in {x["parent"] for x in sel}]
        if ks: add(min(ks, key=lambda k: key(k, sel)), "slot:Q4_expression")
    while len(sel) < 6:
        ks = [k for k in elig if elig[k]["parent"] not in {x["parent"] for x in sel} and (elig[k]["main_target"], elig[k]["arm"]) not in {(x["main_target"], x["arm"]) for x in sel} and elig[k]["mech_group"] not in {x["mech_group"] for x in sel}]
        if not ks: break
        add(min(ks, key=lambda k: key(k, sel)), "order:a-e")
    return sel, why, crow, cl, elig

def finish(out, rows):
    sel, why, crow, cl, elig = choose(rows)
    for r in rows:
        r["disposition"] = "selected:" + why[(r["parent"], r["main_target"])] if r in sel else ("excluded:" + r["exclusions"].split(";")[0] if r["exclusions"] else ("not_taken:cluster_member_not_representative" if elig.get((r["main_target"], r["arm"])) is not None and elig[(r["main_target"], r["arm"])]["parent"] != r["parent"] else "not_taken:ordering_cap_6"))
    rows.sort(key=lambda r: (not r["disposition"].startswith("selected"), r["disposition"], r["main_target"], r["name"]))
    cols = list(rows[0])
    wr(out / "selection_pool.tsv", rows, cols)
    wr(out / "selection_clusters.tsv", crow, list(crow[0]))
    wr(out / "selected_p4c_d.tsv", [r for r in rows if r["disposition"].startswith("selected")], cols)
    wr(out / "excluded_selection_p4c_d.tsv", [r for r in rows if r["disposition"].startswith("excluded")], cols)
    if LOG: wr(out / "selection_service_log.tsv", [dict(zip(["utc", "url", "status", "attempt"], l)) for l in LOG], ["utc", "url", "status", "attempt"])
    print("parents x cluster", len(rows), "clusters", len(cl), "clusters with eligible", len(elig), "selected", len(sel), file=sys.stderr)

def main(out):
    out.mkdir(exist_ok=True)
    pool = [r for r in rd(V3 / "v3_seed_specific_all_nulls.tsv") if r["question"] in ("Q5", "Q4") and r["arm"] in ("opposes", "mimics")]
    meta = {r["family_id"]: r for r in rd(V3 / "actions/family_meta.tsv.gz", True)}
    nsig = collections.defaultdict(set)
    for r in rd(V3 / "actions/family_actions.tsv.gz", True):
        if r["mean_sign"] not in ("0", "0.0000"): nsig[r["family_id"]].add(r["target_symbol"])
    flags = collections.defaultdict(set)
    for r in rd(V3 / "actions/family_flags.tsv.gz", True): flags[r["family_id"]].add(r["flag"])
    allf = {r["family_id"] for r in pool}
    cat = {}
    for l in gzip.open(D / "catalog/catalog.jsonl.gz", "rt"):
        r = json.loads(l); fid = "FAM:" + r["id"]
        if fid in allf: cat[fid] = r
    recon = {r["candidate"]: r for r in rd(D / "catalog/ligand_reconciliation.tsv")}
    p3map = {r["family_id"]: r for r in rd(P3 / "identity_map.tsv")}
    inv = {r["family_id"]: r for r in rd(RK / "inventory_families.tsv.gz", True)}
    # ---- identity routes
    idm = {}; todo = {}
    for fid in sorted(allf):
        r = cat.get(fid); name = (r or {}).get("name") or meta.get(fid, {}).get("name", ""); route, cid, note = "unresolved", "", ""
        m = re.match(r"FAM:CAT:(CHEMBL\d+)$", fid)
        if m: route, cid = "catalogue_chembl", m.group(1)
        elif r:
            rc = recon.get(fid[4:]); ids = r.get("ids", {})
            if rc and rc["chembl_ref"] and rc["decision"] in ("merged", "out_of_selection") and rc.get("structure_check"): route, cid, note = "reconciliation_chembl", rc["chembl_ref"], "structure_check=" + rc["structure_check"]
            elif ids.get("chembl_from_dgidb_concept_not_enumerated"): route, cid = "dgidb_concept_chembl", ids["chembl_from_dgidb_concept_not_enumerated"][0]
            elif fid in p3map and p3map[fid]["identity_route"] != "unresolved": route, cid, note = p3map[fid]["identity_route"], p3map[fid]["chembl_id"], "from P3 identity map; " + p3map[fid]["note"]
            elif name and not re.search(r"\[|\bcompound\b|inhibitor|antagonist|agonist|antibody|vaccine|\bpmid\b|\bexample\b", name, re.I): todo[fid] = ((r.get("ids") or {}).get("dgidb_drug_name") or name)
            else: note = "name pattern not looked up (code name / class name / paper compound)"
        idm[fid] = dict(name=name, route=route, cid=cid, note=note)
    for fid, nme in todo.items():
        hits = set(); err = False
        for fld in ("pref_name__iexact", "molecule_synonyms__molecule_synonym__iexact"):
            d = get("https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit=5&only=molecule_chembl_id,molecule_hierarchy&" + fld + "=" + urllib.parse.quote(nme))
            if d == "ERR": err = True; break
            hits |= {(x.get("molecule_hierarchy") or {}).get("parent_chembl_id") or x["molecule_chembl_id"] for x in (d or {}).get("molecules", [])}
        if err: idm[fid]["note"] = "SERVICE_ERROR on name lookup"
        elif len(hits) == 1: idm[fid].update(route="name_exact_unique", cid=sorted(hits)[0], note="identity UNVERIFIED (no structure check)")
        elif hits: idm[fid]["note"] = "name matches %d ChEMBL parents" % len(hits)
        else: idm[fid]["note"] = "no exact name match"
    # ---- ChEMBL molecule profile (id -> parent)
    ids = sorted({v["cid"] for v in idm.values() if v["cid"]}); rec = {}
    def fetch(batch):
        d = get("https://www.ebi.ac.uk/chembl/api/data/molecule.json?limit=100&molecule_chembl_id__in=" + ",".join(batch))
        if d == "ERR" or d is None: return False
        for x in d["molecules"]: rec[x["molecule_chembl_id"]] = x
        return True
    failed = set()
    for i in range(0, len(ids), 40):
        if not fetch(ids[i:i + 40]): failed |= set(ids[i:i + 40])
    parents = sorted({(x.get("molecule_hierarchy") or {}).get("parent_chembl_id") for x in rec.values()} - {None} - set(rec))
    for i in range(0, len(parents), 40):
        if not fetch(parents[i:i + 40]): failed |= set(parents[i:i + 40])
    def prof(cid):
        x = rec.get(cid)
        if not x: return None
        pid = (x.get("molecule_hierarchy") or {}).get("parent_chembl_id") or cid; p = rec.get(pid, x)
        mp = p.get("max_phase")
        return dict(parent=pid, pname=p.get("pref_name") or x.get("pref_name") or "", max_phase=mp if mp is not None else "", mtype=p.get("molecule_type") or x.get("molecule_type") or "", oral=x.get("oral"), parenteral=x.get("parenteral"), topical=x.get("topical"),
                    withdrawn=x.get("withdrawn_flag"), atc=";".join(p.get("atc_classifications") or x.get("atc_classifications") or []), bbw=x.get("black_box_warning"), prodrug=x.get("prodrug"))
    # ---- HGNC groups
    clusters = collections.defaultdict(list)
    for r in pool:
        mt = r["edge_chain_main_target_to_seed_1"].split(" -")[0].strip(); r["main_target"] = mt
        clusters[(mt, r["arm"])].append(r)
    hg = {}
    for t in sorted({k[0] for k in clusters}):
        d = get("https://rest.genenames.org/fetch/symbol/" + urllib.parse.quote(t), {"Accept": "application/json"})
        if d == "ERR": hg[t] = ("UNKNOWN", "SERVICE_ERROR")
        elif not d or d["response"]["numFound"] == 0:
            d2 = get("https://rest.genenames.org/search/alias_symbol/" + urllib.parse.quote(t), {"Accept": "application/json"}) if False else None
            hg[t] = ("UNKNOWN", "SYMBOL_NOT_FOUND")
        else:
            g = d["response"]["docs"][0].get("gene_group") or []; hg[t] = ((g[0] if g else "NO_GROUP:" + t), "OK")
        time.sleep(0.2)
    # ---- known to LEGEND
    known = collections.defaultdict(set)
    for c, v in json.load(open(D / "catalog/card_links.json"))["cards"].items():
        for l in v["links"]: known["FAM:" + l["catalogue_id"]].add("card:" + c)
    for r in rd(RK / "unit_members.tsv"):
        if r["family_id"]: known[r["family_id"]].add("unit_member:" + r["unit_id"])
    for r in rd(RK / "deepening_queue.tsv"):
        for f in r["family_ids"].split(";"):
            if f.strip(): known[f.strip()].add("deepening_queue:" + r["display_group"])
    cardtxt = {p.name: p.read_text(errors="ignore") for p in (D / "cards").glob("*.card.json")}
    def cardhit(word):
        w = re.compile(r"(?<![A-Za-z0-9])" + re.escape(word) + r"(?![A-Za-z0-9])", re.I)
        return sorted(n.split(".")[0] for n, t in cardtxt.items() if w.search(t))
    # ---- per parent rows
    byparent = collections.defaultdict(list)
    for r in pool:
        fid = r["family_id"]; i = idm[fid]; p = prof(i["cid"]) if i["cid"] else None
        pk = p["parent"] if p else (i["cid"] or fid)
        byparent[(pk, r["main_target"], r["arm"])].append((r, i, p))
    rows = []
    for (pk, mt, arm), items in byparent.items():
        r0, i0, p0 = items[0]
        fids = sorted({x[0]["family_id"] for x in items})
        routes = [idm[f]["route"] for f in fids]
        best = next((r for r in ["catalogue_chembl", "reconciliation_chembl", "dgidb_concept_chembl", "name_exact_unique"] if r in routes), "unresolved")
        p = next((x[2] for x in items if x[2]), None)
        excl, fl = [], []
        names = sorted({x[0]["name"] for x in items}, key=str.lower)
        pname = (p["pname"] if p and p["pname"] else names[0])
        if best == "unresolved": excl.append("E5_identity_unresolved")
        elif pk in failed or p is None: fl.append("profile_NOT_RETURNED_or_SERVICE_ERROR")
        atc = (p["atc"].split(";") if p and p["atc"] else [])
        mech = " ".join((t.get("mechanism_of_action") or "") for f in fids for t in (cat.get(f, {}).get("targets") or []) if isinstance(t, dict)).lower()
        if any(a.startswith(("L01A", "L01B", "L01C", "L01D", "L01XA")) for a in atc) or re.search(r"topoisomerase|tubulin|dna alkylat|dna synthesis|dna intercalat|dna crosslink|antimetabolite", mech): excl.append("E2_cytotoxic_anticancer")
        elif any(a.startswith("L01") for a in atc) or any(a.startswith("L04") for a in atc) and False: fl.append("oncology_targeted")
        if p and p["topical"] in (True, "True", 1) and p["oral"] not in (True, "True", 1) and p["parenteral"] not in (True, "True", 1): excl.append("E3_topical_only")
        elif atc and all(a.startswith(("D", "S01", "S02", "S03")) for a in atc): excl.append("E3_topical_only_by_ATC")
        mt_ = (p["mtype"] if p else "")
        mods = {inv.get(f, {}).get("modality", "") for f in fids}
        if (mt_ and mt_ not in ("Small molecule", "Unknown")) or (mods & {"antibody", "other:antibody drug conjugate", "other:vaccine component", "cell_product", "enzyme", "oligonucleotide", "protein_or_peptide", "gene_product"} and mt_ != "Small molecule"): excl.append("E4_modality_" + (mt_ or ",".join(sorted(mods))).replace(" ", "_"))
        stat = ";".join(sorted({inv.get(f, {}).get("status_class", "") for f in fids}))
        try: mpv = float(p["max_phase"]) if p and p["max_phase"] != "" else None
        except Exception: mpv = None
        if (mpv is None or mpv < 1) and "approved_any_source" not in stat and "clinical_candidate" not in stat: excl.append("E6_no_human_exposure_statement")
        if p and p["withdrawn"] in (True, "True", 1): excl.append("E7_withdrawn")
        nsg = max((len(nsig.get(f, ())) for f in fids), default=0)
        if nsg >= 5: excl.append("E8_promiscuous_%d_signed_targets" % nsg)
        nmset = {nn(pname)} | {nn(x) for x in names}
        if any(nn(rn) in nm for rn in ROUND1 for nm in nmset if nm and nn(rn)): excl.append("E1_round1_qualified")
        kn = sorted(set().union(*[known.get(f, set()) for f in fids]) | ({"card_text:" + c for c in cardhit(pname)} if len(pname) > 4 else set()))
        tg_cards = cardhit(mt)
        zs = [min(min(abs(float(x[0][c])) if x[0][c] else 0 for c in ("Z_ind_robust_total_null", "Z_ind_robust_indeg_null", "Z_ind_robust_adm_null")), 20) for x in items]
        rows.append(dict(parent=pk, name=pname, q=r0["question"], arm=arm, main_target=mt, mech_group=hg.get(mt, ("UNKNOWN",))[0], hgnc_state=hg.get(mt, ("", ""))[1], seed=r0["contributing_seed_1"].split("|")[1] if "|" in r0["contributing_seed_1"] else "",
                         chain=r0["edge_chain_main_target_to_seed_1"][:200], min_abs_z_capped20=round(min(zs), 2), family_ids=";".join(fids), n_families=len(fids), identity_route=best, max_phase=("" if mpv is None else mpv), molecule_type=mt_, atc=";".join(atc),
                         oral=p["oral"] if p else "", parenteral=p["parenteral"] if p else "", topical=p["topical"] if p else "", status_class=stat, n_signed_targets=nsg, prodrug_flag=int(any("UNCERTAIN_ACTIVE_MOIETY" in flags.get(f, ()) for f in fids)),
                         known_to_legend=";".join(kn), target_named_in_cards=";".join(tg_cards), exclusions=";".join(excl), flags=";".join(fl), member_names="; ".join(names)[:300]))
    print('pool rows', len(pool), 'failed ids', len(failed), file=sys.stderr)
    finish(out, rows)
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("cmd", nargs="?", choices=["run", "reselect"]); ap.add_argument("--out", default=str(HERE))
a = ap.parse_args()
if a.cmd == "run": main(Path(a.out))
elif a.cmd == "reselect": finish(Path(a.out), rd(Path(a.out) / "selection_pool.tsv"))
else: ap.print_help()
