#!/usr/bin/env python3
"""IT18 P4 controls: popularity (C1) and construction leakage / near-equivalent disease (C2).

Design and decision rules: PRE_REGISTRATION.md (this directory), committed before this script.
Offline: reads local files only; --help and import do nothing else. Labels are read from the locked
../answers.tsv (digest checked against ../answers_lock.json); the universe and the GtoPdb reference
are rebuilt with the unchanged functions of ../matching_task.py. Post hoc on EVAL, descriptive only.

  run --catalog F --needs F --chembl-targets F --gtopdb-dir D --dgidb-interactions F [--out F]
"""
import argparse
import gzip
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
P4 = HERE.parent
sys.path.insert(0, str(P4))


def sha256_text(s):
    return hashlib.sha256(s.encode()).hexdigest()


def percentile_map(values_by_key, population):
    """Mid-rank percentile (0-100) of each key's value within `population` (list of numbers)."""
    pop = sorted(population)
    n = len(pop)
    out = {}
    for k, v in values_by_key.items():
        lo = sum(1 for x in pop if x < v)
        eq = sum(1 for x in pop if x == v)
        out[k] = round(100.0 * (lo + 0.5 * eq) / n, 2) if n else None
    return out


def mw_auc(pos, neg):
    """Probability that a random `pos` value exceeds a random `neg` value (ties count 0.5)."""
    if not pos or not neg:
        return None
    s = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return round(s / (len(pos) * len(neg)), 4)


def popularity_path(rows, pop, k_by_need):
    """Per need, the k most popular rows (ties: lowest sha256 of the parent id). rows: [(need, parent)]."""
    by_need = defaultdict(list)
    for need, parent in rows:
        by_need[need].append(parent)
    out = set()
    for need, parents in by_need.items():
        ranked = sorted(parents, key=lambda c: (-pop.get(c, 0), sha256_text(c)))
        out |= {(need, c) for c in ranked[:k_by_need.get(need, 0)]}
    return out


def jaccard(a, b):
    u = a | b
    return round(len(a & b) / len(u), 4) if u else None


def name_terms(names):
    """Whole-word, case-insensitive terms of at least 4 characters."""
    return sorted({n.strip().lower() for n in names if n and len(n.strip()) >= 4})


def leaked(terms, text):
    """Terms that occur in `text` as whole words (letters/digits not adjacent)."""
    t = text.lower()
    return [w for w in terms if re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", t)]


def precision(sel, truth):
    det = [k for k in sel if truth.get(k) in ("compatible", "opposite")]
    ok = sum(truth[k] == "compatible" for k in det)
    return {"determinate": len(det), "truly_compatible": ok, "precision": round(ok / len(det), 4) if det else None}


def dgidb_pop(interactions_tsv, chembl_ids_by_parent, primary_names_by_parent):
    """Amended pop (PRE_REGISTRATION, dated amendment): distinct DGIdb gene_name per parent, joined by
    drug_concept_id chembl:<id> of the parent or a child, or drug_name equal to a parent/child catalogue name."""
    by_chembl, by_name = defaultdict(set), defaultdict(set)
    with open(interactions_tsv, newline="", encoding="utf-8") as f:
        h = f.readline().rstrip("\n").split("\t")
        ix = {k: h.index(k) for k in ("gene_name", "drug_concept_id", "drug_name")}
        for line in f:
            r = line.rstrip("\n").split("\t")
            g = r[ix["gene_name"]]
            if not g or g == "NULL":
                continue
            cc = r[ix["drug_concept_id"]]
            if cc.lower().startswith("chembl:"):
                by_chembl[cc.split(":", 1)[1].upper()].add(g)
            nm = r[ix["drug_name"]].strip().upper()
            if nm and nm != "NULL":
                by_name[nm].add(g)
    out = {}
    for p in set(chembl_ids_by_parent) | set(primary_names_by_parent):
        gs = set()
        for c in chembl_ids_by_parent.get(p, ()):
            gs |= by_chembl.get(c.upper(), set())
        for n in primary_names_by_parent.get(p, ()):
            gs |= by_name.get(n.strip().upper(), set())
        if gs:
            out[p] = len(gs)
    return out


def catalogue_facts(catalog, dgidb_interactions):
    """-> pop {parent: n distinct DGIdb genes}, atc {parent: set(ATC5)}, names {parent: set(name, synonyms)}."""
    atc, names, primary, cids = defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set)
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            cid = d["ids"].get("chembl")
            if not cid:
                continue
            parent = (d["relations"].get("parent") or "").replace("CAT:", "") or cid
            cids[parent].add(cid)
            for a in d.get("atc") or []:
                code = a if isinstance(a, str) else (a.get("code") or a.get("level5") or "")
                if code:
                    atc[parent].add(code)
            if d.get("name"):
                primary[parent].add(d["name"])
            names[parent].add(d.get("name") or "")
            names[parent].update(d.get("synonyms") or [])
    return dgidb_pop(dgidb_interactions, cids, primary), atc, names


def analyse(rows, labels, truth, pop, atc, names, need_text, all_pop_values):
    """rows: directed (need, parent, split). Pure function over prepared inputs; returns the result dict."""
    keys = [(n, c) for n, c, _ in rows]
    lcomp = {k for k in keys if labels[k] == "compatible"}
    pct = percentile_map({c: pop.get(c, 0) for _, c in keys}, all_pop_values)
    med = lambda ks: median([pct[c] for _, c in ks]) if ks else None  # noqa: E731
    k_by_need = Counter(n for n, _ in lcomp)
    psel = popularity_path(keys, pop, k_by_need)
    per_need = {}
    for need in sorted({n for n, _ in keys}):
        a = {k for k in lcomp if k[0] == need}
        b = {k for k in psel if k[0] == need}
        per_need[need] = {"T_rows": sum(1 for k in keys if k[0] == need), "k_L_compatible": len(a), "jaccard_P_L": jaccard(a, b)}
    det = [k for k in keys if truth[k] in ("compatible", "opposite")]
    rest = [k for k in keys if k not in det]
    t_med, l_med = med(keys), med(sorted(lcomp))
    c1 = {
        "popularity_definition": "amended (PRE_REGISTRATION dated amendment): distinct DGIdb gene_name joined by chembl concept id or exact parent/child catalogue name; percentile among catalogue parents with >= 1 DGIdb gene",
        "directed_rows_with_pop_zero": sum(1 for _, c in keys if not pop.get(c)),
        "directed_rows": len(keys), "L_compatible_rows": len(lcomp),
        "median_pop_percentile": {"T": t_med, "L_compatible": l_med, "L_not_compatible": med([k for k in keys if k not in lcomp])},
        "median_pop_raw": {"T": median([pop.get(c, 0) for _, c in keys]) if keys else None,
                           "L_compatible": median([pop.get(c, 0) for _, c in lcomp]) if lcomp else None},
        "median_atc5_codes": {"T": median([len(atc.get(c, ())) for _, c in keys]) if keys else None,
                              "L_compatible": median([len(atc.get(c, ())) for _, c in lcomp]) if lcomp else None},
        "P_popularity_path": {"jaccard_P_L_pooled": jaccard(lcomp, psel), "per_need": per_need},
        "precision_on_determinate": {"T": precision(keys, truth), "L": precision(lcomp, truth), "P": precision(psel, truth)},
        "reference_bias": {"determinate_rows": len(det), "auc_pop_determinate_vs_rest": mw_auc([pop.get(c, 0) for _, c in det], [pop.get(c, 0) for _, c in rest]),
                           "determinate": sorted([[n, c, pop.get(c, 0), round(pct[c], 1)] for n, c in det])},
    }
    diff = (l_med - t_med) if (l_med is not None and t_med is not None) else None
    c1["decision_selection"] = ("L selects popular compounds beyond T" if diff is not None and diff >= 10
                                else "L adds no popularity selection over T (median percentile difference %s)" % (round(diff, 2) if diff is not None else "n/a"))
    auc = c1["reference_bias"]["auc_pop_determinate_vs_rest"]
    c1["decision_reference_bias"] = ("the scoreable set is the popular end of the candidates; reference-scored P4 figures do not transfer to less-studied candidates"
                                     if len(det) >= 5 and auc is not None and auc >= 0.70
                                     else "no popularity bias of the reference measured at this denominator (determinate rows %d, AUC %s)" % (len(det), auc))
    pr = c1["precision_on_determinate"]
    if pr["T"]["determinate"] and pr["T"]["truly_compatible"] == pr["T"]["determinate"]:
        c1["decision_discrimination"] = "every determinate row is compatible: popularity and L cannot be discriminated by this reference; not a result for either"
    else:
        c1["decision_discrimination"] = "see precision_on_determinate"
    # C2
    lk = {}
    for n, c, s in rows:
        hit = leaked(name_terms(names.get(c, ())), need_text[n])
        if hit:
            lk[(n, c)] = {"split": s, "terms": hit, "L": labels[(n, c)], "reference": truth[(n, c)]}
    det_leaked = [k for k in lk if truth[k] in ("compatible", "opposite")]
    n03 = {k for k in keys if any(a.startswith("N03") for a in atc.get(k[1], ()))}
    c2 = {"leaked_rows": [[k[0], k[1], v["split"], ";".join(v["terms"]), v["L"], v["reference"]] for k, v in sorted(lk.items())],
          "leaked_row_count": len(lk), "leaked_determinate": len(det_leaked),
          "L_precision_without_leaked": precision(lcomp - set(lk), truth),
          "N03_rows_L_compatible_per_need": dict(Counter(n for n, _ in (lcomp & n03))),
          "N03_rows_T": len(n03), "L_compatible_not_N03": len(lcomp - n03)}
    c2["decision"] = ("the reference-scored figure contains a circular row; figure without it is L_precision_without_leaked"
                      if det_leaked else "leakage is a construction fact the reference cannot see (no leaked row has a determinate reference)")
    return {"C1_popularity": c1, "C2_leakage_and_indication_shortcut": c2}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("run")
    for x in ("--catalog", "--needs", "--chembl-targets", "--gtopdb-dir", "--dgidb-interactions"):
        s.add_argument(x, required=True)
    s.add_argument("--out", default=str(HERE / "controls_result.json"))
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    import csv
    import matching_task as m
    lock = json.loads((P4 / "answers_lock.json").read_text(encoding="utf-8"))
    if m.sha256(P4 / "answers.tsv") != lock["answers_tsv_sha256"]:
        print("REFUSED: answers.tsv differs from answers_lock.json", file=sys.stderr)
        return 2
    labels = {}
    with open(P4 / "answers.tsv", newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f, delimiter="\t"):
            labels[(d["need_id"], d["parent_chembl_id"])] = d["L"]
    needs, sym2u, module, pmap, universe = m.load_common(a)
    nu = m.need_uniprots(needs, sym2u)
    gt = m.load_gtopdb_split(a.gtopdb_dir, pmap, {"dev", "eval"})
    directed = [r for r in universe if r["need_direction"] in m.NEED_DIR]
    truth = {(r["need"], r["parent"]): m.truth(r, gt, nu[r["need"]])[0] for r in directed}
    assert all((r["need"], r["parent"]) in labels for r in universe), "universe and answers.tsv differ"
    pop, atc, names = catalogue_facts(a.catalog, a.dgidb_interactions)
    raw = {nd["id"]: json.dumps(nd, ensure_ascii=False) for nd in json.loads(Path(a.needs).read_text(encoding="utf-8"))["needs"]}
    rows = [(r["need"], r["parent"], r["split"]) for r in directed]
    res = analyse(rows, labels, truth, pop, atc, names, raw, list(pop.values()))
    res.update({"run_label": "controls_it18_20261101", "post_hoc_on_eval": True, "l_rule": "v1 (registered)",
                "answers_lock_sha256": m.sha256(P4 / "answers_lock.json"), "script_sha256": m.sha256(__file__),
                "preregistration_sha256": m.sha256(HERE / "PRE_REGISTRATION.md"),
                "catalog_sha256": m.sha256(a.catalog), "needs_sha256": m.sha256(a.needs),
                "dgidb_interactions_sha256": m.sha256(a.dgidb_interactions),
                "split_counts": dict(Counter(s for _, _, s in rows))})
    Path(a.out).write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
