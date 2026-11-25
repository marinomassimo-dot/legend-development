#!/usr/bin/env python3
"""ADV-287 step 0: stratified random sample of 20 statements (seed 287) from universe_adv287.tsv.
Strata = route 1 (structured field) and route 2 only; proportional allocation, largest remainder; within a stratum a
uniform draw with random.Random(287) over rows sorted by (card, sentence); 6 reserves per stratum in draw order.
Excluded cards and Obeid-mention rows are out of the universe. Run: python3 -P -E sample_adv287.py"""
import csv, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [r for r in csv.DictReader(open(os.path.join(HERE, "universe_adv287.tsv")), delimiter="\t") if not r["card_exclusion"] and not r["obeid_flag"]]
strata = {"route1": [r for r in rows if r["route1"] == "1"], "route2_only": [r for r in rows if r["route1"] == "0"]}
for k in strata: strata[k].sort(key=lambda r: (r["card"], r["sentence"]))
N = 20; tot = sum(len(v) for v in strata.values())
raw = {k: N * len(v) / tot for k, v in strata.items()}
alloc = {k: int(x) for k, x in raw.items()}
for k in sorted(raw, key=lambda k: raw[k] - alloc[k], reverse=True):
    if sum(alloc.values()) < N: alloc[k] += 1
rng = random.Random(287); out = []
for k in sorted(strata):
    order = list(strata[k]); rng.shuffle(order)
    for i, r in enumerate(order[: alloc[k] + 6]):
        out.append((k, "sample" if i < alloc[k] else "reserve", i + 1, r["card"], r["family"], r["field_paths"], r["sentence"]))
# Screen on the sentence alone, before any source is opened (rule frozen in PREREG B): a sampled sentence that carries
# no computed or comparative quantity (only a label such as an age band, or the word "range" or "ratio" without a value)
# is replaced by the next reserve of its stratum and recorded.
SCREEN_OUT = [("P11_magnesium_nmdar_gate", "infants and young children 2 to 24 months", "label (age band), no computed quantity"),
              ("E01_isr_modulators", "Compounds range from research tools", "the word range, no value"),
              ("E02_ldh_inhibition", "the liver-to-plasma ratio was measured 1 h after", "the word ratio, no value")]
def screened(r): return any(r[3] == c and r[6].startswith(t) for c, t, _ in SCREEN_OUT)
final = []; repl = []
for k in sorted(strata):
    rows_k = [r for r in out if r[0] == k]
    keep = [r for r in rows_k if r[1] == "sample" and not screened(r)]
    need = alloc[k] - len(keep)
    for r in rows_k:
        if r[1] == "reserve" and need > 0 and not screened(r):
            keep.append((r[0], "sample(reserve %d)" % r[2], r[2], *r[3:])); need -= 1
    final += keep + [r for r in rows_k if r[1] == "reserve" and not any(r[2] == q[2] for q in keep)]
    repl += [r for r in rows_k if r[1] == "sample" and screened(r)]
with open(os.path.join(HERE, "sample_adv287.tsv"), "w") as f:
    f.write("stratum\trole\tdraw_order\tcard\tfamily\tfield_paths\tsentence\n")
    for r in final: f.write("\t".join(str(x) for x in r) + "\n")
with open(os.path.join(HERE, "sample_screened_out_adv287.tsv"), "w") as f:
    f.write("stratum\tdraw_order\tcard\tsentence\treason\n")
    for r in repl: f.write("\t".join([r[0], str(r[2]), r[3], r[6], [c for cc, t, c in SCREEN_OUT if cc == r[3] and r[6].startswith(t)][0]]) + "\n")
fam = collections.Counter(r[4] for r in final if r[1].startswith("sample"))
print("universe", tot, {k: len(v) for k, v in strata.items()}, "alloc", alloc, "families", len(fam), dict(fam))
