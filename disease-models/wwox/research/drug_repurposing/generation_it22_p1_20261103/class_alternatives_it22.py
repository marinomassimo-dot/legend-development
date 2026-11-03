#!/usr/bin/env python3
"""IT22: compare alternatives inside a drug class ONLY on measured, typed values. 'More potent' and 'less toxic' are not read from similarity.

  class_alternatives_it22.py --targets THRB,THRA [--out FILE]      (LEGEND_CATALOG_CACHE must point at the catalogue cache, third-party data, not in git)

For every Guide-to-Pharmacology ligand with a measured human value at one of the TARGET genes it lists, per measure type (IC50, EC50, Ki, Kd; never pooled or converted):
the value at each target, the most potent OTHER target of the SAME type (selectivity is a same-type ratio, else 'not comparable'), the approval flag of the release, and the
action label. It states what it does not know: no exposure, no brain penetration, no safety, no paediatric data; those need the label, a primary paper or a measurement.
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import argparse, collections, csv, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("attribution_screen_it21", HERE.parent / "generation_it21_p2_20261103" / "attribution_screen_it21.py")
AS = importlib.util.module_from_spec(spec); spec.loader.exec_module(AS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True)
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    tg = [t.strip().upper() for t in a.targets.split(",")]
    lig, typed, _ = AS.load_gtopdb_affinities()
    acts = collections.defaultdict(set)
    for r in AS._rd(AS.cache_dir() / "gtopdb" / "interactions.csv"):
        if r.get("Target Species") == "Human" and r.get("Ligand ID"):
            acts[(r["Ligand ID"], (r.get("Target Gene Symbol") or "").upper())].add(r.get("Action") or r.get("Type") or "")
    by_lig = collections.defaultdict(dict)
    for (lid, sym), v in typed.items():
        by_lig[lid][sym] = v
    rows = []
    for lid, genes in by_lig.items():
        if not any(t in genes for t in tg):
            continue
        l = lig.get(lid, {})
        for t in tg:
            if t not in genes:
                continue
            for typ, e in sorted(genes[t].items()):
                others = [(g, d[typ]) for g, d in genes.items() if g != t and typ in d]
                best = min(others, key=lambda x: x[1]["nm"]) if others else None
                sel = ""
                if best:
                    sel = f"{e['nm'] / best[1]['nm']:.1f}x vs {best[0]} ({typ})" if e["rel"] == "=" and best[1]["rel"] == "=" else "censored value: no ratio"
                else:
                    sel = "no other target with a " + typ + " value: not comparable (values kept)"
                rows.append(dict(ligand_id=lid, ligand=l.get("Name", ""), chembl_id=l.get("ChEMBL ID", ""), approved=l.get("Approved", ""), target=t, measure=typ, nm=round(e["nm"], 3), relation=e["rel"],
                                 assay_class=e["assay"], action="|".join(sorted(acts.get((lid, t), []))), same_type_ratio_to_most_potent_other_target=sel,
                                 other_targets_measured="; ".join(f"{g} {'|'.join(f'{k} {v2['nm']:g}' for k, v2 in sorted(d.items()))}" for g, d in sorted(genes.items()) if g != t)[:240]))
    rows.sort(key=lambda r: (r["target"], r["measure"], r["nm"]))
    w = csv.DictWriter(open(a.out, "w", newline="") if a.out else sys.stdout, fieldnames=list(rows[0]) if rows else ["none"], delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)


if __name__ == "__main__":
    main()
