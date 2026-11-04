#!/usr/bin/env python3
"""IT26 A2: scan the listing-tier DGIdb pairs for gene-symbol alias artefacts of the ZHX2 kind.

  alias_scan_it26.py scan --withheld WITHHELD.tsv.gz --meta META.tsv.gz --actions ACTIONS.tsv.gz --hgnc HGNC.json --ncbi ncbi_alias_listing_genes.json --out OUT.tsv
  alias_scan_it26.py --help

Input is the `--listing-tier tier` run of refresh_actions_it21.py (every listing-only signed row, reason class listing_tier_claim_not_carried).
An NCBI alias of the row's gene that HGNC does not list is suspect when it is a stem of (or equal to) the symbol of a target the SAME compound acts on
from another family row (RAF on ZHX2 vs RAF1, the IT25 case). Output is a pointer list for a source check, never a verdict.

  alias_scan_it26.py collide --molecules molecules.jsonl.gz --out OUT.tsv

`collide` (IT27) is the drug-side counterpart: a code-like synonym (it contains a digit) carried by two ChEMBL molecules that are not the same
substance (different parent AND different InChIKey connectivity block) is a collision pointer (E-3810: rabeprazole and lucitanib). Salts and
free bases share a parent, so they are not flagged. Pointers only: nothing is merged or removed from a single shared code.
Offline and deterministic; standard library only.
"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, gzip, json, re


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", s.upper())


def suspect(alias, own_names, measured, gene):
    """[(alias, measured symbol)] for the NCBI-only aliases of `gene` that stem-match a measured target of the compound."""
    out = []
    for a in alias:
        if a.upper() in own_names:
            continue
        na = norm(a)
        if len(na) < 3:
            continue
        for m in sorted(measured):
            nm = norm(m)
            if m != gene.upper() and (nm.startswith(na) or na.startswith(nm)):
                out.append((a, m))
    return out


def code_like(s):
    n = norm(s)
    return len(n) >= 4 and any(c.isdigit() for c in n) and any(c.isalpha() for c in n)


def collide(molecules):
    """{normalised code: [(parent, skeleton, name)]} for codes shared by two or more distinct substances.
    A substance is a (parent, InChIKey connectivity block) pair; the same parent or the same block is one substance."""
    by = collections.defaultdict(dict)
    for d in molecules:
        h = d.get("molecule_hierarchy") or {}
        parent = h.get("parent_chembl_id") or d["molecule_chembl_id"]
        key = ((d.get("molecule_structures") or {}).get("standard_inchi_key") or "")[:14]
        name = d.get("pref_name") or d["molecule_chembl_id"]
        for syn in {x.get("molecule_synonym") for x in d.get("molecule_synonyms") or [] if x.get("molecule_synonym")}:
            if code_like(syn):
                by[norm(syn)].setdefault(parent, (key, name))
    out = {}
    for code, subs in by.items():
        groups = []                                   # merge parents that share a connectivity block
        for parent, (key, name) in sorted(subs.items()):
            for g in groups:
                if key and key == g["key"]:
                    g["members"].append((parent, name))
                    break
            else:
                groups.append(dict(key=key, members=[(parent, name)]))
        if len(groups) > 1:
            out[code] = [(g["members"][0][0], g["key"], g["members"][0][1]) for g in groups]
    return out


def scan(withheld, meta, actions, hgnc, ncbi):
    own = {d["symbol"].upper(): {x.upper() for x in [d["symbol"]] + d.get("alias_symbol", []) + d.get("prev_symbol", [])} for d in hgnc}
    n2f = collections.defaultdict(list)
    for m in meta:
        n2f[m["name"].upper()].append(m["family_id"])
    act = collections.defaultdict(set)
    for a in actions:
        act[a["family_id"]].add(a["target_symbol"].upper())
    rows, seen = [], set()
    for x in withheld:
        if x["reason_class"] != "listing_tier_claim_not_carried":
            continue
        meas = set().union(*[act[f] for f in n2f.get(x["name"].upper(), [])]) if n2f.get(x["name"].upper()) else set()
        for g in x["genes"].split(";"):
            if not g or (x["name"], g, x["claim_source"]) in seen or g not in ncbi:
                continue
            seen.add((x["name"], g, x["claim_source"]))
            for a, m in suspect(ncbi[g]["alias"], own.get(g.upper(), set()), meas, g):
                rows.append(dict(compound=x["name"], gene=g, claim_source=x["claim_source"], ncbi_only_alias=a, stem_of_measured_target=m))
    return rows


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("collide")
    c.add_argument("--molecules", required=True)
    c.add_argument("--out", required=True)
    s = sub.add_parser("scan")
    for k in ("withheld", "meta", "actions", "hgnc", "ncbi", "out"):
        s.add_argument("--" + k, required=True)
    a = ap.parse_args()
    if a.cmd == "collide":
        res = collide(json.loads(l) for l in gzip.open(a.molecules, "rt", encoding="utf-8"))
        with open(a.out, "w", encoding="utf-8", newline="") as fh:
            fh.write("code\tsubstances\tparents\tnames\n")
            for code in sorted(res):
                r = res[code]
                fh.write("%s\t%d\t%s\t%s\n" % (code, len(r), ";".join(x[0] for x in r), ";".join(x[2] for x in r)))
        print(len(res), "collision pointers")
        return
    rd = lambda p: list(csv.DictReader(gzip.open(p, "rt", encoding="utf-8"), delimiter="\t"))
    rows = scan(rd(a.withheld), rd(a.meta), rd(a.actions), json.load(open(a.hgnc))["response"]["docs"], json.load(open(a.ncbi)))
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["compound", "gene", "claim_source", "ncbi_only_alias", "stem_of_measured_target"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "suspect pairs")


if __name__ == "__main__":
    main()
