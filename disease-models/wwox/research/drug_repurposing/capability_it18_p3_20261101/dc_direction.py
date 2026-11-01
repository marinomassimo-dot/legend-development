#!/usr/bin/env python3
"""IT18 P3: DrugCentral as a third action-direction source, with the origin of each action label kept.

Compares, on the module's human direct ChEMBL mechanism pairs (IT17 construction), today's independent
direction source (GtoPdb, through evaluation_it17_p3_20261101/direction_task.py) with DrugCentral
drug.target.interaction.tsv.gz joined by the UniChem ChEMBL->DrugCentral map (src1src34).
Design and outcome rule: README.md (committed before the run). Offline: reads local files only;
--help and import read and write nothing.

  compare --catalog F --gtopdb-dir D --dc F --unichem F --needs F --out-json F --out-tsv F --out-disc F
"""
import argparse
import csv
import gzip
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "evaluation_it17_p3_20261101"))
import direction_task as dt  # noqa: E402  (IT17 loaders and vocabulary, reused unchanged)

SHARED = {"CHEMBL", "IUPHAR"}
INDEPENDENT = {"DRUG LABEL", "SCIENTIFIC LITERATURE", "KEGG DRUG", "EXPERT CURATOR"}
DISCORDANT_IT17 = [("CHEMBL1420", "P22303"), ("CHEMBL1614652", "P08908"), ("CHEMBL493", "P21917"),
                   ("CHEMBL709", "P25100"), ("CHEMBL709", "P35348"), ("CHEMBL709", "P35368")]


def dc_class(action):
    a = (action or "").strip().upper()
    if a == "GATING INHIBITOR":
        return dt.DEC
    return dt.chembl_class(a)


def origin_of(row):
    return (row.get("MOA_SOURCE") or "").strip() or (row.get("ACT_SOURCE") or "").strip() or "UNKNOWN"


def origin_class(origin):
    return "SHARED" if origin in SHARED else "INDEPENDENT" if origin in INDEPENDENT else "OTHER"


def load_unichem(path):
    """-> {drugcentral struct id: set of ChEMBL ids}. File: header line, then 'CHEMBLxxx<TAB>struct_id'."""
    m = defaultdict(set)
    with gzip.open(path, "rt", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 2 and parts[0].startswith("CHEMBL"):
                m[parts[1].strip()].add(parts[0].strip())
    return m


def augment_with_inchikey(uc, inchikey_tsv, catalog):
    """Amendment: add struct -> ChEMBL ids by exact full standard InChIKey equality with catalogue records.
    Never by skeleton (first block) alone: stereoisomers are not interchangeable. UniChem entries are kept;
    a struct whose InChIKey points to other ChEMBL ids than UniChem's is counted, and UniChem's answer wins."""
    by_key = defaultdict(set)
    with gzip.open(catalog, "rt", encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            if d["ids"].get("chembl") and d["ids"].get("inchikey"):
                by_key[d["ids"]["inchikey"]].add(d["ids"]["chembl"])
    out = {k: set(v) for k, v in uc.items()}
    st = Counter()
    with open(inchikey_tsv, encoding="utf-8") as f:
        next(f)
        for line in f:
            sid, key = (line.rstrip("\n").split("\t") + [""])[:2]
            if not key:
                st["inchikey_missing"] += 1
                continue
            hit = by_key.get(key, set())
            if not hit:
                continue
            if sid in out:
                st["inchikey_agrees_with_unichem" if hit & out[sid] else "inchikey_differs_from_unichem_kept_unichem"] += 1
                continue
            out[sid] = set(hit)
            st["structs_added_by_inchikey"] += 1
    return out, dict(st)


def load_dc(dc_path, uc, pmap):
    """-> (pairs {(parent, uniprot): [entry]}, by_parent_gene {(parent, GENE): [entry]}, stats)."""
    pairs, by_gene, st = defaultdict(list), defaultdict(list), Counter()
    with gzip.open(dc_path, "rt", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            st["rows"] += 1
            if row["ORGANISM"] != "Homo sapiens":
                continue
            st["human_rows"] += 1
            act = (row["ACTION_TYPE"] or "").strip()
            if not act:
                continue
            st["human_rows_with_action"] += 1
            chembl = uc.get(row["STRUCT_ID"].strip(), set())
            if not chembl:
                st["action_rows_struct_not_in_unichem"] += 1
                continue
            parents = {pmap[c] for c in chembl if c in pmap}
            if not parents:
                st["action_rows_struct_not_in_catalogue"] += 1
                continue
            if len(parents) > 1:
                st["action_rows_struct_to_several_parents"] += 1
            o = origin_of(row)
            e = {"class": dc_class(act), "raw": act.upper(), "origin": o, "oclass": origin_class(o)}
            for p in parents:
                for u in dt._split_ids(row["ACCESSION"]):
                    pairs[(p, u)].append(e)
                for g in dt._split_ids(row["GENE"]):
                    by_gene[(p, g.upper())].append(e)
    return pairs, by_gene, st


def resolve(entries, oclasses=None):
    """-> (class or None, reason) over the entries whose origin class is in oclasses (all when None)."""
    es = [e for e in entries if oclasses is None or e["oclass"] in oclasses]
    if not es:
        return None, "absent"
    return dt.single({"classes": {e["class"] for e in es}})


def module_universe(catalog, needs_path):
    """-> {(parent, need_id): group} for compounds with a direct human ChEMBL mechanism on an intervention-target gene."""
    needs = json.loads(Path(needs_path).read_text(encoding="utf-8"))["needs"]
    need_genes, group = {}, {}
    for n in needs:
        g = {t["symbol"].upper() for t in n.get("targets") or []
             if t.get("target_kind") == "intervention_target" and t.get("symbol")}
        if g:
            need_genes[n["id"]] = g
            d = (n.get("intervention_direction") or {}).get("direction")
            group[n["id"]] = "directed" if d in ("down", "up") else "uncertain"
    out = {}
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
                syms = {s.upper() for s in t.get("gene_symbols") or []}
                for nid, g in need_genes.items():
                    if syms & g:
                        out[(parent, nid)] = group[nid]
    return out, need_genes


def compare(a):
    pmap = dt.parent_map(a.catalog)
    module = dt.load_module(a.catalog)
    gt = dt.load_gtopdb(a.gtopdb_dir)
    pairs = dt.join(module, gt, pmap)
    uc = load_unichem(a.unichem)
    join_stats = {"unichem_structs": len(uc)}
    if a.inchikeys:
        uc, extra = augment_with_inchikey(uc, a.inchikeys, a.catalog)
        join_stats.update(extra)
    dcp, dcg, st = load_dc(a.dc, uc, pmap)
    st.update(join_stats)

    rows, c = [], Counter()
    for p in pairs:
        k = p["key"]
        mc, mr = dt.single(p["m"])
        gc, gr = dt.single(p["gt"]) if p["gt"] else (None, "absent")
        ents = dcp.get(k, [])
        ac, ar = resolve(ents)
        ic, ir = resolve(ents, {"INDEPENDENT"})
        sc, _ = resolve(ents, {"SHARED"})
        c["pairs"] += 1
        c["module_determinate"] += mc is not None
        c["gtopdb_counterpart"] += p["gt"] is not None
        c["gtopdb_determinate"] += gc is not None
        c["dc_counterpart"] += bool(ents)
        c["dc_determinate_any"] += ac is not None
        c["dc_determinate_independent"] += ic is not None
        c["dc_conflict_any"] += ar == "conflict"
        if mc is not None:
            if gc is not None:
                c["mg_n"] += 1
                c["mg_agree"] += mc == gc
            if ac is not None:
                c["ma_n"] += 1
                c["ma_agree"] += mc == ac
            if ic is not None:
                c["mi_n"] += 1
                c["mi_agree"] += mc == ic
                if gc is None:
                    c["mi_new_n"] += 1
                    c["mi_new_agree"] += mc == ic
                else:
                    c["mig_n"] += 1
                    c["mig_all_three_agree"] += mc == ic == gc
            if ac is not None and gc is None:
                c["ma_new_n"] += 1
                c["ma_new_agree"] += mc == ac
            if sc is not None:
                c["ms_n"] += 1
                c["ms_agree"] += mc == sc
        if mc is not None and ic is not None and mc != ic:
            rows.append({"split": p["split"], "parent_chembl_id": k[0], "uniprot": k[1], "module_class": mc,
                         "gtopdb_class": gc or "", "dc_independent_class": ic,
                         "dc_independent_labels": "|".join(sorted({e["raw"] + "@" + e["origin"] for e in ents if e["oclass"] == "INDEPENDENT"}))})

    disc = []
    for k in DISCORDANT_IT17:
        ents = dcp.get(k, [])
        disc.append({"parent_chembl_id": k[0], "uniprot": k[1], "module_class": dt.INC, "gtopdb_class": dt.DEC,
                     "dc_any": resolve(ents)[0] or resolve(ents)[1],
                     "dc_independent": resolve(ents, {"INDEPENDENT"})[0] or resolve(ents, {"INDEPENDENT"})[1],
                     "dc_labels": "|".join(sorted({e["raw"] + "@" + e["origin"] for e in ents})) or "none"})

    uni, need_genes = module_universe(a.catalog, a.needs)
    u = Counter()
    for (parent, nid), grp in uni.items():
        ents = [e for g in need_genes[nid] for e in dcg.get((parent, g), [])]
        u[grp + "_units"] += 1
        u[grp + "_dc_any_determinate"] += resolve(ents)[0] is not None
        u[grp + "_dc_independent_determinate"] += resolve(ents, {"INDEPENDENT"})[0] is not None
    u["compounds"] = len({p for p, _ in uni})

    def frac(k, n):
        return {"k": c[k], "n": c[n], "rate": round(c[k] / c[n], 4) if c[n] else None, "wilson95": dt.wilson(c[k], c[n])}

    res = {
        "join": "unichem+inchikey" if a.inchikeys else "unichem (registered)",
        "inputs_sha256": {"catalog": dt.sha256(a.catalog), "drugcentral": dt.sha256(a.dc), "unichem_src1src34": dt.sha256(a.unichem),
                          "needs": dt.sha256(a.needs), "gtopdb_interactions": dt.sha256(Path(a.gtopdb_dir) / "interactions.csv"),
                          "gtopdb_ligands": dt.sha256(Path(a.gtopdb_dir) / "ligands.csv")},
        "script_sha256": dt.sha256(__file__),
        "drugcentral_load": dict(st),
        "dc_origin_of_joined_entries": dict(Counter(e["origin"] for es in dcp.values() for e in es)),
        "counts": dict(c),
        "agreement": {"module_vs_gtopdb": frac("mg_agree", "mg_n"), "module_vs_dc_any": frac("ma_agree", "ma_n"),
                      "module_vs_dc_independent": frac("mi_agree", "mi_n"), "module_vs_dc_shared": frac("ms_agree", "ms_n"),
                      "module_vs_dc_independent_on_pairs_without_gtopdb_direction": frac("mi_new_agree", "mi_new_n"),
                      "module_vs_dc_any_on_pairs_without_gtopdb_direction": frac("ma_new_agree", "ma_new_n"),
                      "all_three_agree_where_all_determinate": frac("mig_all_three_agree", "mig_n")},
        "it17_discordant_pairs": disc,
        "matching_universe_counts_only": dict(u),
    }
    Path(a.out_json).write_text(json.dumps(res, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    with open(a.out_disc, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["split"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r["parent_chembl_id"], r["uniprot"])))
    with open(a.out_tsv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["measure", "today_gtopdb", "drugcentral_any_origin", "drugcentral_independent_origin", "note"])
        w.writerow(["module pairs (human direct ChEMBL mechanisms)", c["pairs"], c["pairs"], c["pairs"], "same universe for both routes"])
        w.writerow(["pairs with a counterpart row", c["gtopdb_counterpart"], c["dc_counterpart"], "", "DrugCentral counts rows carrying ACTION_TYPE only"])
        w.writerow(["pairs with a determinate direction", c["gtopdb_determinate"], c["dc_determinate_any"], c["dc_determinate_independent"], ""])
        w.writerow(["module determinate and source determinate", c["mg_n"], c["ma_n"], c["mi_n"], ""])
        w.writerow(["agreement with module direction", c["mg_agree"], c["ma_agree"], c["mi_agree"], "Wilson intervals in results.json"])
        w.writerow(["new determinate pairs (no GtoPdb direction)", "", c["ma_new_n"], c["mi_new_n"], "coverage the current path lacks"])
        w.writerow(["agreement on the new pairs", "", c["ma_new_agree"], c["mi_new_agree"], ""])
        w.writerow(["IT17 discordant pairs with a determinate label", "6 (by construction)",
                    sum(1 for d in disc if d["dc_any"] in (dt.INC, dt.DEC)), sum(1 for d in disc if d["dc_independent"] in (dt.INC, dt.DEC)), "see results.json"])
        for grp in ("directed", "uncertain"):
            w.writerow([f"matching universe {grp} compound x need units", u[grp + "_units"], u[grp + "_dc_any_determinate"],
                        u[grp + "_dc_independent_determinate"], "first column: units in the universe (no GtoPdb label read here)"])
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    c = sub.add_parser("compare", help="offline comparison; writes the three outputs")
    for k in ("catalog", "gtopdb-dir", "dc", "unichem", "needs", "out-json", "out-tsv", "out-disc"):
        c.add_argument("--" + k, required=True)
    c.add_argument("--inchikeys", help="amendment: struct_id<TAB>inchikey TSV from dc_inchikeys.py; adds an exact full-key join")
    a = ap.parse_args(argv)
    if a.cmd != "compare":
        ap.print_help()
        return 0
    res = compare(a)
    print(json.dumps({"counts": res["counts"], "agreement": res["agreement"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
