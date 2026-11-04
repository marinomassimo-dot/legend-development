#!/usr/bin/env python3
"""IT26 A2: scan the listing-tier DGIdb pairs for gene-symbol alias artefacts of the ZHX2 kind.

  alias_scan_it26.py scan --withheld WITHHELD.tsv.gz --meta META.tsv.gz --actions ACTIONS.tsv.gz --hgnc HGNC.json --ncbi ncbi_alias_listing_genes.json --out OUT.tsv
  alias_scan_it26.py --help

Input is the `--listing-tier tier` run of refresh_actions_it21.py (every listing-only signed row, reason class listing_tier_claim_not_carried).
An NCBI alias of the row's gene that HGNC does not list is suspect when it is a stem of (or equal to) the symbol of a target the SAME compound acts on
from another family row (RAF on ZHX2 vs RAF1, the IT25 case). Output is a pointer list for a source check, never a verdict.
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
    s = sub.add_parser("scan")
    for k in ("withheld", "meta", "actions", "hgnc", "ncbi", "out"):
        s.add_argument("--" + k, required=True)
    a = ap.parse_args()
    rd = lambda p: list(csv.DictReader(gzip.open(p, "rt", encoding="utf-8"), delimiter="\t"))
    rows = scan(rd(a.withheld), rd(a.meta), rd(a.actions), json.load(open(a.hgnc))["response"]["docs"], json.load(open(a.ncbi)))
    with open(a.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["compound", "gene", "claim_source", "ncbi_only_alias", "stem_of_measured_target"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "suspect pairs")


if __name__ == "__main__":
    main()
