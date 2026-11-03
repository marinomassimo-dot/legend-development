#!/usr/bin/env python3
"""IT21 V1: what the P3b path-B lever table does not say about a lever it marks NAMED_ALREADY.

`lever_status = NAMED_ALREADY` is a token match against card text and means 'the thread exists'. It does not say whether the card closed the thread, deferred it
for a stated reason, or left a measurement that no one has run. This view attaches, for each NAMED_ALREADY lever gene, (a) the cards that name the gene as a whole
word, their `state_of_known_roads`, `status_reason` and whether a revival trigger is live; (b) the compounds of the lever whose measured affinity at the gene is
within 10-fold of their best measured target (attribution_screen_it21), i.e. for which the lever is the compound's own action and not an annotation.
It reads existing tables and writes one TSV; it is a view, not a registry, and states nothing about suitability.

  named_already_card_state_v1.py [--out FILE]      (LEGEND_CATALOG_CACHE must point at the shared catalogue cache)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, importlib.util, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def rd(p):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def flat(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from flat(v)
    elif isinstance(o, list):
        for v in o:
            yield from flat(v)
    elif isinstance(o, str):
        yield o


def card_index():
    out = []
    for p in sorted((DR / "cards").glob("*.packet.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        card = d.get("p4_card") or {}
        out.append(dict(id=p.name.split(".")[0], text="\n".join(flat(d)), state=card.get("state_of_known_roads", ""), reason=card.get("status_reason", ""),
                        next=card.get("next_measurement", "")))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "named_already_card_state_v1.tsv"))
    a = ap.parse_args()
    import compound_catalog as cc
    import repurposing_search as rs
    AS = load("attribution_screen_it21", DR / "generation_it21_p2_20261103" / "attribution_screen_it21.py")
    P3B = DR / "qualification_it21_p3b_20261103"
    levers = [r for r in rd(P3B / "pathb_levers_it21.tsv") if r["lever_status"] == "NAMED_ALREADY"]
    comps = collections.defaultdict(list)
    for r in rd(P3B / "pathb_compounds_it21.tsv"):
        comps[r["gene"]].append(r)
    entries = cc.load(DR / "catalog" / "catalog.jsonl.gz")
    fam = rs.families(entries)
    lig, aff, _ = AS.load_gtopdb_affinities()
    br = AS.bridge_claim_name_ligands(entries)
    fl = AS.family_ligands(entries, fam, br, lig)
    cards = card_index()
    rows = []
    for lv in levers:
        g = lv["gene"]
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(g) + r"(?![A-Za-z0-9])")
        named = [c for c in cards if pat.search(c["text"])]
        att, seen = [], set()
        for c in comps[g]:
            if c["family_id"] in seen:
                continue
            seen.add(c["family_id"])
            x = AS.attribution(fl.get(c["family_id"], set()), g, aff)
            if x["state"] == "ATTRIBUTABLE":
                att.append(c["name"])
        rows.append(dict(handle=lv["handle"], gene=g, mechanism=lv["mechanism"], lever_basis=lv["basis"], families_signed=lv["families_signed"],
                         cards_naming_the_gene_as_a_word=";".join(c["id"] for c in named) or "none",
                         state_of_known_roads=" | ".join(sorted({c["state"][:160] for c in named if c["state"]})) or "",
                         revival_trigger_or_next_measurement_on_record=("yes" if any(("revival trigger" in c["text"]) or c["next"] for c in named) else "no"),
                         deferral_reason=" | ".join(sorted({c["reason"][:200] for c in named if c["reason"]})) or "",
                         compounds_attributable_at_gene=len(att), examples="; ".join(sorted(att)[:8])))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "NAMED_ALREADY levers ->", a.out)


if __name__ == "__main__":
    main()
