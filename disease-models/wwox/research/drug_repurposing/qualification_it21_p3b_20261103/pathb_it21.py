#!/usr/bin/env python3
"""IT21 P3b, Path B: compound -> WWOX possibilities, bidirectional discovery of levers absent from the target list.

Question fixed before the table was read: for each mechanism handle (handles_it21.tsv: a gene with a stated basis and a pointer), which catalogue compounds
have a documented, signed action on that gene under the IT21 guards (generation_it21_p2 actions), and is the gene already a named target of a need or a card?
A gene that is not named and is reached by a compound is a LEVER FOUND, never a qualified target: this script writes no status other than the closed
vocabulary below, and `lever_status` is never 'qualified'.

  python3 pathb_it21.py run        writes pathb_levers_it21.tsv and pathb_compounds_it21.tsv
  python3 pathb_it21.py profile G  prints every signed target of the families that act on gene G (opposite effects, other needs)
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, json, re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
ACT = DR / "generation_it21_p2_20261103/results/actions"
LEVER_STATUS = ("LEVER_FOUND_NOT_A_TARGET", "NAMED_ALREADY", "NO_SIGNED_COMPOUND")


def rd_gz(p):
    with gzip.open(p, "rt", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def symbols_in_json(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("symbol", "gene", "hgnc_symbol") and isinstance(v, str):
                out.add(v.upper())
            symbols_in_json(v, out)
    elif isinstance(o, list):
        for v in o:
            symbols_in_json(v, out)


def named_set(universe):
    """Genes named by a need (any target kind) or by target_roles, plus HGNC-like tokens in card text that exist in the action universe."""
    named = set()
    symbols_in_json(json.load(open(DR / "needs/needs.json")), named)
    for r in csv.DictReader(open(DR / "coverage/target_roles.tsv"), delimiter="\t"):
        named.add(r["symbol"].upper())
    card_tokens = set()
    for p in sorted((DR / "cards").glob("*.card.json")):
        card_tokens |= set(re.findall(r"(?<![A-Za-z0-9])([A-Z][A-Z0-9]{2,9})(?![A-Za-z0-9])", p.read_text()))
    named_from_cards = card_tokens & universe
    return named, named_from_cards


def load():
    act = rd_gz(ACT / "family_actions.tsv.gz")
    meta = {r["family_id"]: r for r in rd_gz(ACT / "family_meta.tsv.gz")}
    return act, meta


def run():
    act, meta = load()
    universe = {a["target_symbol"] for a in act}
    named_needs, named_cards = named_set(universe)
    handles = list(csv.DictReader(open(HERE / "handles_it21.tsv"), delimiter="\t"))
    by_gene = defaultdict(list)
    for a in act:
        by_gene[a["target_symbol"]].append(a)
    lev, comp = [], []
    seen = set()
    for h in handles:
        g = h["gene"]
        rows = by_gene.get(g, [])
        fams = {}
        for a in rows:
            s = float(a["mean_sign"])
            if s == 0:
                continue
            fams[a["family_id"]] = a
        down = [f for f, a in fams.items() if float(a["mean_sign"]) < 0]
        up = [f for f, a in fams.items() if float(a["mean_sign"]) > 0]
        chembl = [f for f in fams if meta[f]["has_chembl"] == "1"]
        single = [f for f in fams if "single_protein" in fams[f]["scopes"].split(";")[0] or fams[f]["scopes"].startswith("single_protein")]
        in_needs = g in named_needs
        in_cards = g in named_cards
        status = "NO_SIGNED_COMPOUND" if not fams else ("NAMED_ALREADY" if (in_needs or in_cards) else "LEVER_FOUND_NOT_A_TARGET")
        assert status in LEVER_STATUS
        names = sorted({meta[f]["name"] for f in chembl})
        lev.append({"handle": h["handle"], "mechanism": h["mechanism"], "gene": g, "basis": h["basis"], "in_needs": int(in_needs), "in_cards_text": int(in_cards),
                    "lever_status": status, "families_signed": len(fams), "families_chembl": len(chembl), "families_single_protein": len(single),
                    "down": len(down), "up": len(up), "example_chembl_names": "; ".join(names[:8]), "pointer": h["pointer"]})
        for f, a in fams.items():
            key = (g, f)
            if key in seen:
                continue
            seen.add(key)
            m = meta[f]
            comp.append({"handle": h["handle"], "gene": g, "family_id": f, "name": m["name"], "sign": a["mean_sign"], "n_rows": a["n_rows"], "groups": a["groups"],
                         "scopes": a["scopes"], "flags": a["flags"], "has_chembl": m["has_chembl"], "prodrug": m["prodrug"], "lever_status": status})
    w = lambda p, rows: (lambda f: (lambda wr: (wr.writeheader(), wr.writerows(rows)))(csv.DictWriter(f, rows[0].keys(), delimiter="\t")))(open(p, "w", newline=""))
    w(HERE / "pathb_levers_it21.tsv", lev)
    w(HERE / "pathb_compounds_it21.tsv", comp)
    from collections import Counter
    print(Counter(r["lever_status"] for r in lev), "genes", len(lev), "compound rows", len(comp))


def profile(g):
    act, meta = load()
    fams = {a["family_id"] for a in act if a["target_symbol"] == g and float(a["mean_sign"]) != 0}
    by = defaultdict(list)
    for a in act:
        if a["family_id"] in fams and float(a["mean_sign"]) != 0:
            by[a["family_id"]].append(a)
    for f in sorted(by, key=lambda x: meta[x]["name"]):
        print(meta[f]["name"], f, "chembl" if meta[f]["has_chembl"] == "1" else "dgidb-only", "n_signed_targets=%d" % len(by[f]))
        print("   ", ", ".join("%s%s" % (a["target_symbol"], "+" if float(a["mean_sign"]) > 0 else "-") for a in sorted(by[f], key=lambda x: x["target_symbol"])[:40]))


if sys.argv[1] == "run":
    run()
elif sys.argv[1] == "profile":
    profile(sys.argv[2])
else:
    print(__doc__)
