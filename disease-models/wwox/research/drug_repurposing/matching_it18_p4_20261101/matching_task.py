#!/usr/bin/env python3
"""IT18 P4: does the WWOX need context improve compound matching over a target-only search?

Design and decision rules: PRE_REGISTRATION.md (this directory). Offline: reads local files only;
--help and import do nothing else. Reuses the IT17 direction logic (../evaluation_it17_p3_20261101/direction_task.py).

Paths over one universe (catalogue parent compounds with a direct human ChEMBL mechanism on an
intervention-target gene of a need):
  T target-only   every universe compound is a "candidate"
  X external-only ChEMBL action direction compared with a target prior chosen without WWOX
                  (per-target majority GtoPdb direction among DEV compounds; global DEV majority if unseen or tied)
  L contextual    ChEMBL action direction compared with the need's WWOX direction; abstains when the need
                  direction is not down/up, when an action is partial/mixed/unknown, or when the compound
                  has opposite directions on targets of the same need

Stages (order is part of the design):
  answers --catalog F --needs F --chembl-targets F --gtopdb-dir D --outdir D
        writes priors.tsv (DEV rule table), answers.tsv (T/X/L for every universe compound) and
        answers_lock.json (digests). GtoPdb rows of EVAL compounds are dropped on read and never used.
  dev   (same inputs) scores DEV only, for inspection of the rules before the lock.
  score (same inputs) --card-links F --outdir D [--run-label S] [--l-rule v1|v2]
        refuses unless answers_lock.json matches the files and is committed; joins the full GtoPdb
        reference; scores EVAL once; writes results*.json and cases*.tsv.
"""
import argparse
import csv
import gzip
import hashlib
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "evaluation_it17_p3_20261101"))
import direction_task as dt  # noqa: E402

DEC, INC = dt.DEC, dt.INC
NEED_DIR = {"down": DEC, "up": INC}
OPP = {DEC: INC, INC: DEC}
COMPAT, OPPOS, INDET, CAND = "compatible", "opposite", "indeterminable", "candidate"


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load_needs(path):
    """-> list of {id, direction, targets:[symbol], counter_evidence:[str]} for needs with intervention targets."""
    out = []
    for nd in json.loads(Path(path).read_text(encoding="utf-8"))["needs"]:
        syms = [t["symbol"] for t in nd.get("targets", []) if t.get("target_kind") == "intervention_target"]
        if syms:
            out.append({"id": nd["id"], "direction": nd["intervention_direction"]["direction"], "targets": syms,
                        "certainty": nd["intervention_direction"].get("certainty", ""),
                        "counter_evidence": nd.get("counter_evidence", [])})
    return out


def symbol_to_uniprot(chembl_targets, symbols):
    """Human primary GENE_SYMBOL only (never GENE_SYMBOL_OTHER: aliases collide, e.g. GRIN1/GPRIN1)."""
    want, out = set(symbols), defaultdict(set)
    with gzip.open(chembl_targets, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d.get("organism") != "Homo sapiens":
                continue
            for c in d.get("target_components") or []:
                for s in c.get("target_component_synonyms") or []:
                    if s.get("syn_type") == "GENE_SYMBOL" and s.get("component_synonym") in want and c.get("accession"):
                        out[s["component_synonym"]].add(c["accession"])
    return {k: sorted(v) for k, v in out.items()}


def load_catalog_extra(catalog):
    """-> names {parent: name}, ttypes {(parent, uniprot): set(target_type)} for direct human ChEMBL mechanisms."""
    names, ttypes = {}, defaultdict(set)
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            if not cid:
                continue
            parent = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
            if parent == cid or parent not in names:
                names[parent] = d.get("name") or ""
            for t in d.get("targets", []):
                if t.get("source") != "ChEMBL curated mechanism" or t.get("organism") != "Homo sapiens" or t.get("inherited_from_parent"):
                    continue
                for u in t.get("uniprot") or []:
                    ttypes[(parent, u)].add(t.get("target_type") or "")
    return names, ttypes


def load_gtopdb_split(gdir, pmap, keep):
    """GtoPdb human interactions keyed by (parent chembl, uniprot); rows whose parent split is not in `keep` are dropped on read."""
    gdir = Path(gdir)
    lig = {}
    with open(gdir / "ligands.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows)
        h = next(rows)
        for r in rows:
            d = dict(zip(h, r))
            if d["ChEMBL ID"]:
                lig[d["Ligand ID"]] = d["ChEMBL ID"]
    out = {}
    with open(gdir / "interactions.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows)
        h = next(rows)
        for r in rows:
            d = dict(zip(h, r))
            if d["Target Species"] != "Human" or d["Ligand ID"] not in lig:
                continue
            c = lig[d["Ligand ID"]]
            parent = pmap.get(c, c)
            if dt.split_of(parent) not in keep:
                continue
            for u in dt._split_ids(d["Target UniProt ID"]):
                e = out.setdefault((parent, u), {"classes": set(), "raw": set(), "pmids": set()})
                e["classes"].add(dt.gtopdb_class(d["Type"], d["Action"]))
                e["raw"].add((d["Type"], d["Action"]))
                e["pmids"] |= dt._split_ids(d["PubMed ID"])
    return out


def build_priors(module, gt_dev, uniprots):
    """X prior per target uniprot from DEV pairs determinate on both sides (as IT17 B1); global DEV majority on unseen/tie."""
    pairs = [{"key": k, "split": "dev", "gt": gt_dev.get(k), "m": m} for k, m in module.items() if dt.split_of(k[0]) == "dev"]
    det, _ = dt.classify(pairs)
    glob = Counter(p["gc"] for p in det)
    g = DEC if glob[DEC] >= glob[INC] else INC
    per = defaultdict(Counter)
    for p in det:
        per[p["key"][1]][p["gc"]] += 1
    out = {}
    for u in sorted(uniprots):
        c = per.get(u, Counter())
        if c[DEC] > c[INC]:
            out[u] = (DEC, "target_majority", c[DEC], c[INC])
        elif c[INC] > c[DEC]:
            out[u] = (INC, "target_majority", c[DEC], c[INC])
        else:
            out[u] = (g, "global_dev_majority" if not c else "tie_global_dev_majority", c[DEC], c[INC])
    return out, {"dev_determinate_pairs": len(det), "global_dev_majority": g, "dev_DEC": glob[DEC], "dev_INC": glob[INC]}


def build_universe(needs, sym2u, module, rowsets=None):
    """-> list of rows {need, parent, targets: {uniprot: (symbol, class, reason)}}, one per (need, parent)."""
    by_parent_u = defaultdict(dict)
    for (c, u), e in module.items():
        by_parent_u[u][c] = e
    rows = []
    module_u = frozenset(u for nd in needs for s in nd["targets"] for u in sym2u.get(s, []))
    for nd in needs:
        u2s = {u: s for s in nd["targets"] for u in sym2u.get(s, [])}
        comp = defaultdict(dict)
        for u, s in u2s.items():
            for c, e in by_parent_u.get(u, {}).items():
                cls, why = dt.single(e)
                comp[c][u] = (s, cls, why, "|".join(sorted(x or "NONE" for x in e["raw"])))
        for c in sorted(comp):
            rs = set()
            for u in comp[c]:
                rs |= (rowsets or {}).get((c, u), set())
            rows.append({"need": nd["id"], "need_direction": nd["direction"], "parent": c, "split": dt.split_of(c), "targets": comp[c],
                         "module_uniprots": module_u, "rowsets": rs})
    return rows


def action_check(row):
    """Shared by X and L: None when the ChEMBL action is usable; else the abstention reason."""
    t = row["targets"].values()
    if any(why == "conflict" for _, _, why, _ in t):
        return "action_conflict_within_target"
    if any(cls is None for _, cls, _, _ in t):
        return "action_partial_or_unknown"
    if len({cls for _, cls, _, _ in t}) > 1:
        return "opposite_directions_across_targets"
    return None


def label_x(row, priors):
    why = action_check(row)
    if why:
        return INDET, why
    agree = [cls == priors[u][0] for u, (_, cls, _, _) in row["targets"].items()]
    if all(agree):
        return COMPAT, "matches_target_prior"
    if not any(agree):
        return OPPOS, "reverses_target_prior"
    return INDET, "mixed_against_target_prior"


def label_l(row, rule="v1"):
    if row["need_direction"] not in NEED_DIR:
        return INDET, "need_direction_" + row["need_direction"]
    if rule == "v2" and row.get("rowsets") and all(len(rs & row["module_uniprots"]) / len(rs) < 0.5 for rs in row["rowsets"]):
        # dated second rule (README, run2): every ChEMBL record that reaches the need is a group-level record whose
        # components lie mostly outside the module's declared intervention targets (all needs), so the action is
        # not resolved to the target family the needs name (e.g. a 26-component voltage-gated calcium channel group)
        return INDET, "group_record_mostly_outside_module_targets"
    why = action_check(row)
    if why:
        return INDET, why
    cls = next(iter(row["targets"].values()))[1]
    return (COMPAT, "matches_need_direction") if cls == NEED_DIR[row["need_direction"]] else (OPPOS, "reverses_need_direction")


def mechanism_rowsets(catalog):
    """-> {(parent, uniprot): set(frozenset(uniprots of the ChEMBL record))} for direct human ChEMBL mechanisms."""
    out = defaultdict(set)
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            if not cid:
                continue
            parent = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
            for t in d.get("targets", []):
                if t.get("source") != "ChEMBL curated mechanism" or t.get("organism") != "Homo sapiens" or t.get("inherited_from_parent"):
                    continue
                us = frozenset(t.get("uniprot") or [])
                for u in us:
                    out[(parent, u)].add(us)
    return out


def write_tsv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def answers_rows(universe, priors):
    out = []
    for r in universe:
        x, xw = label_x(r, priors)
        l, lw = label_l(r)
        l2, lw2 = label_l(r, "v2")
        tg = ";".join("%s:%s:%s" % (s, u, cls or "NONE") for u, (s, cls, _, _) in sorted(r["targets"].items(), key=lambda kv: (kv[1][0], kv[0])))
        out.append([r["need"], r["need_direction"], r["parent"], r["split"], CAND, x, xw, l, lw, l2, lw2, tg])
    return out


ANS_HEADER = ["need_id", "need_direction", "parent_chembl_id", "split", "T", "X", "X_reason", "L", "L_reason", "L_v2", "L_v2_reason", "chembl_class_per_target"]


def load_common(a):
    needs = load_needs(a.needs)
    sym2u = symbol_to_uniprot(a.chembl_targets, {s for n in needs for s in n["targets"]})
    module = dt.load_module(a.catalog)
    pmap = dt.parent_map(a.catalog)
    universe = build_universe(needs, sym2u, module, mechanism_rowsets(a.catalog))
    return needs, sym2u, module, pmap, universe


def truth(row, gt, need_uniprots):
    """Reference category for one (need, compound) on a directed need, over all the need's target uniprots."""
    ents = {u: gt[(row["parent"], u)] for u in need_uniprots if (row["parent"], u) in gt}
    if not ents:
        return "unknown_no_counterpart", ents
    det = set()
    for e in ents.values():
        c, _ = dt.single(e)
        if c:
            det.add(c)
    if not det:
        return "no_direction", ents
    d = NEED_DIR[row["need_direction"]]
    if d in det and OPP[d] not in det:
        return COMPAT, ents
    if det == {OPP[d]}:
        return OPPOS, ents
    return "mixed", ents


def score_split(rows, labels, gt, need_u, split):
    """Precision of compatible labels per path on directed needs, plus base rate, coverage, abstentions, errors."""
    directed = [r for r in rows if r["need_direction"] in NEED_DIR and r["split"] == split]
    tr = {}
    for r in directed:
        tr[(r["need"], r["parent"])] = truth(r, gt, need_u[r["need"]])[0]
    detset = [r for r in directed if tr[(r["need"], r["parent"])] in (COMPAT, OPPOS)]
    k_t = sum(tr[(r["need"], r["parent"])] == COMPAT for r in detset)
    res = {"directed_universe_need_compound": len(directed),
           "directed_unique_compounds": len({r["parent"] for r in directed}),
           "reference_category_counts": dict(Counter(tr.values())),
           "coverage_share_no_counterpart": round(sum(v == "unknown_no_counterpart" for v in tr.values()) / len(directed), 4) if directed else None,
           "T": {"n_determinate": len(detset), "truly_compatible": k_t,
                 "base_rate": round(k_t / len(detset), 4) if detset else None, "ci95": dt.wilson(k_t, len(detset))}}
    for p in ("X", "L"):
        lab = {(r["need"], r["parent"]): labels[p][(r["need"], r["parent"])] for r in directed}
        comp = [r for r in detset if lab[(r["need"], r["parent"])][0] == COMPAT]
        k = sum(tr[(r["need"], r["parent"])] == COMPAT for r in comp)
        opp_as_comp = sorted(r["parent"] for r in comp if tr[(r["need"], r["parent"])] == OPPOS)
        comp_as_opp = sorted(r["parent"] for r in detset if lab[(r["need"], r["parent"])][0] == OPPOS and tr[(r["need"], r["parent"])] == COMPAT)
        labelled_det = [r for r in detset if lab[(r["need"], r["parent"])][0] != INDET]
        right = sum(lab[(r["need"], r["parent"])][0] == tr[(r["need"], r["parent"])] for r in labelled_det)
        res[p] = {"label_counts": dict(Counter(v[0] for v in lab.values())),
                  "abstention_rate": round(sum(v[0] == INDET for v in lab.values()) / len(lab), 4) if lab else None,
                  "abstention_reasons": dict(Counter(v[1] for v in lab.values() if v[0] == INDET)),
                  "compatible_determinate": len(comp), "compatible_truly_compatible": k,
                  "precision_compatible": round(k / len(comp), 4) if comp else None, "precision_ci95": dt.wilson(k, len(comp)),
                  "truly_opposite_labelled_compatible": opp_as_comp, "truly_compatible_labelled_opposite": comp_as_opp,
                  "labelled_determinate": len(labelled_det), "labelled_correct": right,
                  "abstained_with_determinate_reference": len(detset) - len(labelled_det)}
    lx = {(r["need"], r["parent"]): labels["X"][(r["need"], r["parent"])][0] for r in detset}
    ll = {(r["need"], r["parent"]): labels["L"][(r["need"], r["parent"])][0] for r in detset}
    differ = [k for k in lx if lx[k] != ll[k]]
    b = sum(ll[k] == tr[k] and lx[k] != tr[k] for k in differ)
    c = sum(lx[k] == tr[k] and ll[k] != tr[k] for k in differ)
    res["X_vs_L"] = {"directed_rows_labels_differ_all": sum(labels["X"][(r["need"], r["parent"])][0] != labels["L"][(r["need"], r["parent"])][0] for r in directed),
                     "determinate_rows_labels_differ": len(differ), "L_right_X_wrong": b, "X_right_L_wrong": c,
                     "paired_sign_p": round(dt.sign_p(b, c), 6)}
    return res, tr


def decide(ev):
    out = {}
    L, T = ev["L"], ev["T"]
    n, lo = L["compatible_determinate"], (L["precision_ci95"] or [None])[0]
    if n < 40:
        out["L_vs_T"] = "fewer than 40 determinate EVAL compounds labelled compatible by L (n=%d): figure reported with interval, no improvement statement" % n
    elif T["base_rate"] is not None and lo is not None and lo >= T["base_rate"] + 0.05:
        out["L_vs_T"] = "L improves matching over T (lower Wilson bound %.4f >= base rate %.4f + 0.05, n=%d)" % (lo, T["base_rate"], n)
    else:
        out["L_vs_T"] = "no advantage over target-only measured"
    xl = ev["X_vs_L"]
    if xl["directed_rows_labels_differ_all"] == 0:
        out["L_vs_X"] = "no measured WWOX contribution to accuracy on directed needs (L = X on every directed row)"
    elif xl["L_right_X_wrong"] > xl["X_right_L_wrong"] and xl["paired_sign_p"] < 0.05:
        out["L_vs_X"] = "WWOX knowledge improves accuracy over X (sign p=%s)" % xl["paired_sign_p"]
    else:
        out["L_vs_X"] = "L and X differ on directed needs but no significant accuracy difference (sign p=%s)" % xl["paired_sign_p"]
    return out


def need_uniprots(needs, sym2u):
    return {n["id"]: sorted({u for s in n["targets"] for u in sym2u.get(s, [])}) for n in needs}


def git_committed(path):
    try:
        rel = subprocess.run(["git", "-C", str(path.parent), "ls-files", "--error-unmatch", path.name], capture_output=True, text=True)
        dirty = subprocess.run(["git", "-C", str(path.parent), "diff", "--quiet", "HEAD", "--", path.name], capture_output=True)
        return rel.returncode == 0 and dirty.returncode == 0
    except OSError:
        return False


CASE_HEADER = ["case", "contrast", "rule", "need_id", "parent_chembl_id", "name", "split", "chembl_class_per_target",
               "chembl_target_types", "X", "L", "reference", "card_linked", "contrast_count_available"]


def select_cases(universe, labels, gt, need_u, names, ttypes, card_parents):
    """Rule-selected cases (never by outcome): for each contrast, the members with the lowest sha256(parent id)."""
    h = lambda c: hashlib.sha256(c.encode()).hexdigest()
    directed = [r for r in universe if r["need_direction"] in NEED_DIR]
    key = lambda r: (r["need"], r["parent"])
    out = []

    def emit(contrast, rule, rows, available):
        for r in rows:
            ref = truth(r, gt, need_u[r["need"]])[0] if r["need_direction"] in NEED_DIR else "not_scored_uncertain_need"
            tg = ";".join("%s:%s" % (s, cls or "NONE(" + raw + ")") for u, (s, cls, _, raw) in sorted(r["targets"].items(), key=lambda kv: kv[1][0]))
            tt = "|".join(sorted({t for u in r["targets"] for t in ttypes.get((r["parent"], u), set())}))
            out.append([0, contrast, rule, r["need"], r["parent"], names.get(r["parent"], ""), r["split"], tg, tt,
                        labels["X"][key(r)][0], labels["L"][key(r)][0], ref, int(r["parent"] in card_parents), available])

    # 1 same target, opposite action
    by_u = defaultdict(lambda: {DEC: [], INC: []})
    for r in directed:
        for u, (s, cls, _, _) in r["targets"].items():
            if cls:
                by_u[(r["need"], s)][cls].append(r)
    pairs1 = sorted(k for k, v in by_u.items() if v[DEC] and v[INC])
    for k in pairs1[:2]:
        emit("1 same target, opposite action", "gene %s in %s: lowest-hash DECREASE and INCREASE compound" % (k[1], k[0]),
             [min(by_u[k][DEC], key=lambda r: h(r["parent"])), min(by_u[k][INC], key=lambda r: h(r["parent"]))], len(pairs1))
    # 2 same compound, different actions across targets of one need
    c2 = sorted((r for r in directed if len({cls for _, cls, _, _ in r["targets"].values()}) > 1), key=lambda r: h(r["parent"]))
    emit("2 same compound, different actions across targets of one need", "lowest-hash members", c2[:2], len(c2))
    # 3 same family, different pharmacology: subunit-level SINGLE PROTEIN versus complex/family-level mechanism
    single_only = [r for r in directed if all(ttypes.get((r["parent"], u), set()) == {"SINGLE PROTEIN"} for u in r["targets"])]
    complex_only = [r for r in directed if all("SINGLE PROTEIN" not in ttypes.get((r["parent"], u), set()) for u in r["targets"])]
    for nid in sorted({r["need"] for r in directed}):
        s = sorted((r for r in single_only if r["need"] == nid), key=lambda r: h(r["parent"]))
        c = sorted((r for r in complex_only if r["need"] == nid), key=lambda r: h(r["parent"]))
        if s and c:
            emit("3 same family, subunit-level versus complex-level mechanism", "%s: lowest-hash single-protein and lowest-hash complex/family" % nid,
                 [s[0], c[0]], "%d single / %d complex" % (len(s), len(c)))
    # 4 partial/ambiguous action versus clean action
    c4 = sorted((r for r in directed if any(cls is None for _, cls, _, _ in r["targets"].values())), key=lambda r: h(r["parent"]))
    clean = sorted((r for r in directed if all(cls for _, cls, _, _ in r["targets"].values())), key=lambda r: h(r["parent"]))
    emit("4 partial/ambiguous action versus clean action", "lowest-hash ambiguous then lowest-hash clean", c4[:2] + clean[:1], "%d ambiguous / %d clean" % (len(c4), len(clean)))
    # 5 ChEMBL record only, no GtoPdb counterpart on any need target
    c5 = sorted((r for r in directed if truth(r, gt, need_u[r["need"]])[0] == "unknown_no_counterpart"), key=lambda r: h(r["parent"]))
    emit("5 ChEMBL only, reference unknown (kept unknown, not negative)", "lowest-hash members", c5[:2], len(c5))
    # 6 card-linked (documented in a module card) versus not
    c6 = sorted((r for r in universe if r["parent"] in card_parents), key=lambda r: (r["need_direction"] not in NEED_DIR, h(r["parent"])))
    nc6 = sorted((r for r in directed if r["parent"] not in card_parents), key=lambda r: h(r["parent"]))
    emit("6 card-linked versus not card-linked", "all card-linked universe rows (directed first) then lowest-hash non-card directed row", c6 + nc6[:1],
         "%d card-linked rows / %d not" % (len(c6), len(universe) - len(c6)))
    for i, row in enumerate(out, 1):
        row[0] = "C%02d" % i
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    for name in ("answers", "dev", "score"):
        s = sub.add_parser(name)
        s.add_argument("--catalog", required=True)
        s.add_argument("--needs", required=True)
        s.add_argument("--chembl-targets", required=True)
        s.add_argument("--gtopdb-dir", required=True)
        s.add_argument("--outdir", default=str(HERE))
        if name == "score":
            s.add_argument("--card-links", required=True)
            s.add_argument("--run-label", default="run1")
            s.add_argument("--l-rule", choices=("v1", "v2"), default="v1")
            s.add_argument("--allow-uncommitted-lock", action="store_true", help="tests only")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    out = Path(a.outdir)
    needs, sym2u, module, pmap, universe = load_common(a)
    nu = need_uniprots(needs, sym2u)
    all_u = {u for v in nu.values() for u in v}
    if a.cmd in ("answers", "dev"):
        gt_dev = load_gtopdb_split(a.gtopdb_dir, pmap, {"dev"})
        priors, pinfo = build_priors(module, gt_dev, all_u)
        if a.cmd == "dev":
            labels = {"X": {}, "L": {}}
            for r in universe:
                labels["X"][(r["need"], r["parent"])] = label_x(r, priors)
                labels["L"][(r["need"], r["parent"])] = label_l(r)
            res, tr = score_split(universe, labels, gt_dev, nu, "dev")
            print(json.dumps({"prior_info": pinfo, "symbol_to_uniprot": sym2u, "dev": res}, indent=1, sort_keys=True))
            return 0
        u2s = {u: s for n in needs for s in n["targets"] for u in sym2u.get(s, [])}
        write_tsv(out / "priors.tsv", ["uniprot", "symbol", "dev_gtopdb_DECREASE", "dev_gtopdb_INCREASE", "X_prior", "basis"],
                  [[u, u2s[u], v[2], v[3], v[0], v[1]] for u, v in sorted(priors.items(), key=lambda kv: (u2s[kv[0]], kv[0]))])
        write_tsv(out / "answers.tsv", ANS_HEADER, answers_rows(universe, priors))
        lock = {"written_utc_note": "written before the GtoPdb reference of EVAL compounds was read",
                "script_sha256": sha256(__file__), "direction_task_sha256": sha256(dt.__file__),
                "priors_tsv_sha256": sha256(out / "priors.tsv"), "answers_tsv_sha256": sha256(out / "answers.tsv"),
                "catalog_sha256": sha256(a.catalog), "needs_sha256": sha256(a.needs),
                "chembl_targets_sha256": sha256(a.chembl_targets), "prior_info": pinfo, "symbol_to_uniprot": sym2u,
                "universe_rows": len(universe), "universe_unique_compounds": len({r["parent"] for r in universe})}
        (out / "answers_lock.json").write_text(json.dumps(lock, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(lock, indent=1, sort_keys=True))
        return 0
    # score
    lockp = out / "answers_lock.json"
    lock = json.loads(lockp.read_text(encoding="utf-8"))
    checks = {"priors_tsv_sha256": sha256(out / "priors.tsv"), "answers_tsv_sha256": sha256(out / "answers.tsv"),
              "catalog_sha256": sha256(a.catalog), "needs_sha256": sha256(a.needs), "direction_task_sha256": sha256(dt.__file__)}
    bad = [k for k, v in checks.items() if lock.get(k) != v]
    if bad:
        print("REFUSED: lock digests differ for " + ", ".join(bad), file=sys.stderr)
        return 2
    if not a.allow_uncommitted_lock and not (git_committed(lockp) and git_committed(out / "answers.tsv")):
        print("REFUSED: answers_lock.json / answers.tsv are not committed and clean", file=sys.stderr)
        return 2
    # labels are read back from the locked file; --l-rule v2 takes the L_v2 column (locked too), reported as a separate dated run
    lcol = "L_v2" if a.l_rule == "v2" else "L"
    labels = {"X": {}, "L": {}}
    with open(out / "answers.tsv", newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f, delimiter="\t"):
            labels["X"][(d["need_id"], d["parent_chembl_id"])] = (d["X"], d["X_reason"])
            labels["L"][(d["need_id"], d["parent_chembl_id"])] = (d[lcol], d[lcol + "_reason"])
    gt = load_gtopdb_split(a.gtopdb_dir, pmap, {"dev", "eval"})
    ev, tr = score_split(universe, labels, gt, nu, "eval")
    dv, _ = score_split(universe, labels, gt, nu, "dev")
    # (b) information effect on non-directed needs: X labels, L abstains on the need's direction
    info = {}
    for n in needs:
        if n["direction"] in NEED_DIR:
            continue
        rows = [r for r in universe if r["need"] == n["id"]]
        xl = [r["parent"] for r in rows if labels["X"][(r["need"], r["parent"])][0] in (COMPAT, OPPOS)
              and labels["L"][(r["need"], r["parent"])][1].startswith("need_direction_")]
        info[n["id"]] = {"need_direction": n["direction"], "certainty": n["certainty"], "universe_compounds": len(rows),
                         "X_compatible": sum(labels["X"][(r["need"], r["parent"])][0] == COMPAT for r in rows),
                         "X_opposite": sum(labels["X"][(r["need"], r["parent"])][0] == OPPOS for r in rows),
                         "X_labelled_L_abstains_on_need_direction": len(xl),
                         "counter_evidence_items": len(n["counter_evidence"]),
                         "counter_evidence_first": (n["counter_evidence"][0][:240] if n["counter_evidence"] else "")}
    links = json.loads(Path(a.card_links).read_text(encoding="utf-8"))
    card_chembl = {(l.get("chembl_id") or l.get("catalogue_id", "").replace("CAT:", "")) for c in links["cards"].values() for l in c.get("links", [])} - {""}
    card_parents = {pmap.get(c, c) for c in card_chembl}
    names, ttypes = load_catalog_extra(a.catalog)
    cases = select_cases(universe, labels, gt, nu, names, ttypes, card_parents)
    shared = sum(1 for r in universe if r["need_direction"] in NEED_DIR and r["split"] == "eval"
                 and any(module[(r["parent"], u)]["pmids"] & gt[(r["parent"], u)]["pmids"] for u in r["targets"] if (r["parent"], u) in gt))
    res = {"run_label": a.run_label, "l_rule": a.l_rule, "lock_sha256": sha256(lockp), "script_sha256": sha256(__file__),
           "gtopdb_files_sha256": {f: sha256(Path(a.gtopdb_dir) / f) for f in ("interactions.csv", "ligands.csv")},
           "universe_rows": len(universe), "universe_unique_compounds": len({r["parent"] for r in universe}),
           "universe_rows_by_need": dict(Counter(r["need"] for r in universe)),
           "eval_directed": ev, "dev_directed_descriptive": dv, "decision": decide(ev),
           "eval_directed_rows_sharing_a_pmid_between_chembl_and_gtopdb": shared,
           "wwox_contribution_b_information_effect": info,
           "card_linked_parents_in_universe": sorted({r["parent"] for r in universe if r["parent"] in card_parents})}
    sfx = "" if a.run_label == "run1" else "_" + a.run_label
    (out / ("results%s.json" % sfx)).write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    write_tsv(out / ("cases%s.tsv" % sfx), CASE_HEADER, cases)
    write_tsv(out / ("reference%s.tsv" % sfx), ["need_id", "parent_chembl_id", "split", "reference_category"],
              [[k[0], k[1], "eval", v] for k, v in sorted(tr.items())])
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
