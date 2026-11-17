"""Scores PREDICTIONS_6_GABA_SCAFFOLD_FROZEN_BEFORE_TABLES_SCI.md against snuc6_a_genes.tsv and snuc6_b_genes.tsv (nats). Reads the frozen tables from the markdown itself.
    python3 score_6.py run   (from the folder holding the files)"""
import sys, csv, math, re, json
if sys.argv[1:] != ["run"]:
    print(__doc__); raise SystemExit(0)
md = open("PREDICTIONS_6_GABA_SCAFFOLD_FROZEN_BEFORE_TABLES_SCI.md").read()
def table(title):
    seg = md.split(title)[1].split("###")[0]; out = {}
    for l in seg.splitlines():
        p = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(p) == 3 and p[0] not in ("Gene", "---"):
            for k, cell in zip(("excitatory", "inhibitory"), p[1:]):
                if "not scored" in cell: continue
                v = [float(x) for x in cell.split("/")]
                out[(p[0].replace(" (LOO)", ""), k, "LOO" if "(LOO)" in p[0] else "default")] = v
    return out
NAIVE_R, NAIVE_B = 0.75, {"LOW": 0.10, "MID": 0.80, "HIGH": 0.10}
def binof(c): return "LOW" if c < -0.4 else ("HIGH" if c > 0.4 else "MID")
def run(name, title, path, ccol, rdcol):
    pred = table(title); rows = {}
    for r in csv.DictReader(open(path), delimiter="\t"):
        rows[(r["gene"], r["class"], r["classification"])] = r
    mine = nv = 0.0; lines = []
    for key, v in pred.items():
        r = rows.get(key)
        readable = bool(r) and r[rdcol] == "yes"
        pr = v[0]; mine += math.log(pr if readable else 1 - pr); nv += math.log(NAIVE_R if readable else 1 - NAIVE_R)
        b = None; c = None
        if readable:
            c = float(r[ccol]); b = binof(c)
            mine += math.log({"LOW": v[1], "MID": v[2], "HIGH": v[3]}[b]); nv += math.log(NAIVE_B[b])
        lines.append((key, readable, c, b, v))
    return mine, nv, lines, rows
res = {}
for name, title, path, ccol, rdcol in (("a", "### (a) S-line", "snuc6_a_genes.tsv", "C_log2_KO_over_ctrl", "readable_detection(>=30 each)"),
                                        ("b", "### (b) PV-Scn1a", "snuc6_b_genes.tsv", "C_per_animal_mean(mut-ctrl log2)", "readable(>=30 each)")):
    md2 = md
    seg_title = title
    mine, nv, lines, rows = run(name, seg_title, path, ccol, rdcol)
    print("=== (%s) scored rows %d  mine %.3f  naive %.3f  diff %+.3f nats" % (name, len(lines), mine, nv, mine - nv))
    for key, rd, c, b, v in lines:
        print("%-9s %-11s %-8s readable=%-5s C=%s bin=%s  (P_read %.2f, LMH %s)" % (key[0], key[1], key[2], rd, "NA" if c is None else "%+.2f" % c, b, v[0], v[1:]))
    res[name] = {"mine": mine, "naive": nv, "rows": len(lines)}
json.dump(res, open("score6.json", "w"), indent=1)
