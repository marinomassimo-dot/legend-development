#!/usr/bin/env python3
"""v3 compound-side provenance repair (Amendment 5, filters F2 and F3): catalogue -> family actions resolved by HGNC id, with complex-member, alias-collision and active-moiety handling.

  build_actions_v3.py --out DIR [--catalog PATH]
Writes DIR/family_actions.tsv.gz (family_id, target_symbol = HGNC approved symbol, mean_sign, n_rows, groups, scopes, hgnc_id, flags), DIR/family_meta.tsv.gz,
DIR/family_targets_any.tsv.gz, DIR/family_flags.tsv.gz (prodrug / UNCERTAIN_ACTIVE_MOIETY per family) and DIR/build_funnel_v3.json (what each rule removed). Deterministic, offline
apart from the catalogue and hgnc_lookup.tsv.gz. Rules: PRE_REGISTRATION_V3.md section 1.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, gzip, importlib.util, json, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
V2 = HERE.parent
DRUG = V2.parent
REPO = V2.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))


def load_hgnc(path=HERE / "hgnc_lookup.tsv.gz"):
    byid, approved, alias = {}, {}, collections.defaultdict(set)
    uni = {}
    for r in csv.DictReader(gzip.open(path, "rt", encoding="utf-8"), delimiter="\t"):
        if r["status"] != "Approved":
            continue
        byid[r["hgnc_id"]] = dict(symbol=r["symbol"], name=r["name"], aliases=set(filter(None, r["alias_symbol"].split("|"))), prev=set(filter(None, r["prev_symbol"].split("|"))))
        approved[r["symbol"].upper()] = r["hgnc_id"]
        for a in byid[r["hgnc_id"]]["aliases"] | byid[r["hgnc_id"]]["prev"]:
            alias[a.upper()].add(r["hgnc_id"])
        for u in filter(None, r["uniprot_ids"].split("|")):
            uni[u] = r["hgnc_id"]
    return byid, approved, alias, uni


class Hgnc:
    def __init__(self):
        self.byid, self.approved, self.alias, self.uni = load_hgnc()

    def canon(self, sym):
        """approved symbol for a symbol: itself if approved; the unique owner of an alias or previous symbol; else None."""
        s = (sym or "").strip().upper()
        if s in self.approved:
            return self.byid[self.approved[s]]["symbol"]
        ids = self.alias.get(s, set())
        if len(ids) == 1:
            return self.byid[next(iter(ids))]["symbol"]
        return None

    def sym_to_id(self, sym):
        c = self.canon(sym)
        return self.approved.get(c.upper()) if c else None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--catalog", default=str(DRUG / "catalog" / "catalog.jsonl.gz"))
    a = ap.parse_args()
    import compound_catalog as cc
    import repurposing_search as rs
    spec = importlib.util.spec_from_file_location("usable_census", DRUG / "usable_compounds_it7_p2_20261029" / "usable_census.py")
    uc = importlib.util.module_from_spec(spec); spec.loader.exec_module(uc)
    H = Hgnc()
    entries = cc.load(Path(a.catalog)); idx = rs.Index(entries, rs.load_artefacts()); fam = idx.family
    VERIFIED_CLAIM = {"ChEMBL", "GuideToPharmacology", "ChEMBL curated mechanism"}
    F = collections.Counter()
    rows_by_fam = collections.defaultdict(list)   # family -> list of dict(hgnc_id, sign|None, group, scope, curated, flags)
    meta = {}
    prodrug = collections.defaultdict(bool)
    complex_uncredited = []
    for e in entries:
        f = fam[e["id"]]
        m = meta.setdefault(f, dict(family_id=f, name="", n_records=0, has_structure_key=0, has_chembl=0))
        m["n_records"] += 1
        ids = e.get("ids") or {}
        if ids.get("skeleton_key"): m["has_structure_key"] = 1
        if ids.get("chembl"): m["has_chembl"] = 1
        if not m["name"] or "FAM:" + e["id"] == f: m["name"] = e.get("name") or m["name"]
        if (e.get("chemistry") or {}).get("prodrug") == 1:
            prodrug[f] = True
        for t in e["targets"]:
            u = uc.row_usability(rs, idx, e, t)
            F["rows_total"] += 1
            chembl = t["source"].startswith("ChEMBL")
            signed = bool(u["stated"] and not u["excluded"] and u["sign"] in ("up", "down") and u["stable"])
            sign = (1.0 if u["sign"] == "up" else -1.0) if signed else None
            flags = set()
            hids = []
            if chembl:
                ups = t.get("uniprot") or []
                hids = [H.uni[x] for x in ups if x in H.uni]
                if not hids:
                    hids = [i for i in (H.sym_to_id(s) for s in (t.get("gene_symbols") or [])) if i]
                    if hids: F["chembl_rows_resolved_by_symbol_fallback"] += 1
                if t.get("target_type") in ("PROTEIN COMPLEX", "PROTEIN-PROTEIN INTERACTION") and len(hids) > 1:
                    norm = lambda x: " ".join("".join(c if c.isalnum() else " " for c in (x or "").lower()).split())
                    text = norm((t.get("target_name") or "") + " " + (t.get("mechanism_of_action") or ""))
                    toks = set(text.split())
                    cred = [i for i in hids if H.byid[i]["symbol"].lower() in toks or (norm(H.byid[i]["name"]) and norm(H.byid[i]["name"]) in text)]
                    if cred:
                        for i in hids:
                            if i not in cred:
                                complex_uncredited.append((f, e["name"], H.byid[i]["symbol"], t.get("target_name"), "".join(c for c in (e.get("name") or "").upper() if c.isalnum()), i))
                                if signed: F["complex_member_not_credited_usable_rows"] += 1
                        hids = cred
                        flags.add("COMPLEX_MEMBER_CREDITED_BY_NAME")
                    else:
                        flags.add("COMPLEX_MEMBERS_UNRESOLVED")
                        if signed: F["complex_rows_all_members_credited_unresolved"] += 1
                curated = True
            else:
                gid = (t.get("gene_concept_id") or "").upper().replace("HGNC:", "")
                if gid.isdigit() and ("HGNC:" + gid) in H.byid:
                    hids = ["HGNC:" + gid]
                else:
                    i = H.sym_to_id(t.get("gene") or "")
                    hids = [i] if i else []
                    if hids: F["dgidb_rows_resolved_by_symbol_fallback"] += 1
                dgc = (t.get("claim_source") == "ChEMBL")
                curated = (t.get("claim_source") in VERIFIED_CLAIM) or ((t.get("identity") or {}).get("state") in ("corrected", "verified"))
            if chembl:
                dgc = False
            nm = "".join(c for c in (e.get("name") or "").upper() if c.isalnum())
            if not hids:
                F["rows_no_hgnc_id"] += 1
                if signed: F["usable_rows_no_hgnc_id"] += 1
                continue
            for hid in hids:
                rows_by_fam[f].append(dict(hid=hid, sign=sign, group=u["group"], scope=u["scope"], curated=curated, flags=flags, signed=signed, dgc=dgc, nm=nm))
    UNC = {(c[4], c[5]) for c in complex_uncredited}
    for f in list(rows_by_fam):
        keep = []
        for r in rows_by_fam[f]:
            if r["dgc"] and (r["nm"], r["hid"]) in UNC:
                F["dgidb_rows_dropped_copy_of_uncredited_complex_member"] += 1
                if r["signed"]: F["dgidb_usable_rows_dropped_copy_of_uncredited_complex_member"] += 1
                continue
            keep.append(r)
        rows_by_fam[f] = keep
    # alias collision (F2 ii) and aggregation
    acts = {}; anyt = {}
    dropped_alias = []
    for f, rl in rows_by_fam.items():
        curated_ids = {r["hid"] for r in rl if r["curated"]}
        bad = set()
        for r in rl:
            if r["curated"]:
                continue
            sym = H.byid[r["hid"]]["symbol"].upper()
            for y in curated_ids:
                if y != r["hid"] and (sym in {x.upper() for x in H.byid[y]["aliases"] | H.byid[y]["prev"]}):
                    bad.add(r["hid"]); dropped_alias.append((f, meta[f]["name"], H.byid[r["hid"]]["symbol"], H.byid[y]["symbol"])); break
        for r in rl:
            if r["hid"] in bad and not r["curated"]:
                F["rows_dropped_alias_collision"] += 1
                continue
            sym = H.byid[r["hid"]]["symbol"].upper()
            at = anyt.setdefault(f, collections.Counter()); at[sym] += 1
            if r["signed"]:
                d = acts.setdefault(f, {}).setdefault(sym, dict(signs=[], groups=set(), scopes=set(), flags=set(), hid=r["hid"]))
                d["signs"].append(r["sign"]); d["groups"].add(r["group"]); d["scopes"].add(r["scope"]); d["flags"] |= r["flags"]
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    with gzip.open(out / "family_actions.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family_id", "target_symbol", "mean_sign", "n_rows", "groups", "scopes", "hgnc_id", "flags"])
        for f in sorted(acts):
            for sym in sorted(acts[f]):
                d = acts[f][sym]
                flg = set(d["flags"])
                if prodrug.get(f): flg.add("UNCERTAIN_ACTIVE_MOIETY")
                w.writerow([f, sym, f"{sum(d['signs']) / len(d['signs']):.4f}", len(d["signs"]), ";".join(sorted(d["groups"])), ";".join(sorted(d["scopes"])), d["hid"], ";".join(sorted(flg))])
    with gzip.open(out / "family_targets_any.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["family_id", "target_symbol", "n_rows_any_action"])
        for f in sorted(anyt):
            for sym in sorted(anyt[f]): w.writerow([f, sym, anyt[f][sym]])
    with gzip.open(out / "family_meta.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); cols = ["family_id", "name", "n_records", "has_structure_key", "has_chembl", "mnet_usable", "prodrug"]
        w.writerow(cols)
        for f in sorted(meta):
            m = meta[f]; m["mnet_usable"] = 1 if f in acts else 0; m["prodrug"] = 1 if prodrug.get(f) else 0
            w.writerow([m[c] for c in cols])
    with gzip.open(out / "family_flags.tsv.gz", "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["family_id", "flag"])
        for f in sorted(prodrug):
            if prodrug[f] and f in acts: w.writerow([f, "UNCERTAIN_ACTIVE_MOIETY"])
    F["families_total"] = len(meta); F["families_with_signed_hgnc_target"] = len(acts)
    F["prodrug_families"] = sum(1 for f in prodrug if prodrug[f]); F["prodrug_families_with_signed_target"] = sum(1 for f in prodrug if prodrug[f] and f in acts)
    F["alias_collision_family_gene_pairs"] = len(dropped_alias); F["complex_member_not_credited_pairs"] = len(complex_uncredited)
    json.dump(dict(counts=dict(F), alias_collision=dropped_alias[:200], complex_not_credited=[c[:4] for c in complex_uncredited][:200]), open(out / "build_funnel_v3.json", "w"), indent=1)
    print(json.dumps(dict(F), indent=1))


if __name__ == "__main__":
    main()
