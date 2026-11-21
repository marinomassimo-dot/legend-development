import sys, itertools, statistics as S
sys.path.insert(0, ".")
import lin2025_xls_min as xls_min
wb = xls_min.read(sys.argv[1])

def col(sheet, r0, r1, c):
    cl = wb[sheet]; return [cl[(r, c)] for r in range(r0, r1) if isinstance(cl.get((r, c)), float)]

def perm_p(a, b):
    allv = a + b; n = len(a); obs = abs(S.mean(a) - S.mean(b)); cnt = 0; tot = 0
    for idx in itertools.combinations(range(len(allv)), n):
        s = set(idx); x = [allv[i] for i in s]; y = [allv[i] for i in range(len(allv)) if i not in s]
        tot += 1
        if abs(S.mean(x) - S.mean(y)) >= obs - 1e-12: cnt += 1
    return cnt / tot

def line(label, a, b):
    ma, mb = S.mean(a), S.mean(b)
    print("%-52s n=%d vs %d  mean %.4g vs %.4g  ratio(b/a)=%s diff=%.4g  exact perm p=%.3f" % (label, len(a), len(b), ma, mb, ('%.3f' % (mb / ma) if abs(ma) > 0.2 else 'n/a'), mb - ma, perm_p(a, b)))

out = {}
# 7B free cholesterol: spinal cord rows 2-8 (r1..r7) cols 0..3 ; cerebellum rows 14..20
for tissue, r0 in (("spinal cord", 2), ("cerebellum", 16)):
    g = {k: col("Fig. 7B", r0, r0 + 7, c) for k, c in (("WTm", 0), ("WTw", 1), ("Nm", 2), ("Nw", 3))}
    print("--- 7B free cholesterol,", tissue, {k: len(v) for k, v in g.items()})
    line("genotype (maintained): N208Y vs WT", g["WTm"], g["Nm"])
    line("withdrawn vs maintained within N208Y", g["Nm"], g["Nw"])
    line("withdrawn vs maintained within WT", g["WTm"], g["WTw"])
    line("N208Y withdrawn vs WT withdrawn", g["WTw"], g["Nw"])
    out["7B " + tissue] = g
# 7F deuterium labelled cholesterol
for tissue, r0 in (("spinal cord", 2), ("cerebellum", 10)):
    g = {k: col("Fig. 7F", r0, r0 + 4, c) for k, c in (("WTm", 0), ("WTw", 1), ("Nm", 2), ("Nw", 3))}
    print("--- 7F D2O-labelled cholesterol,", tissue, {k: len(v) for k, v in g.items()})
    line("genotype (maintained): N208Y vs WT", g["WTm"], g["Nm"])
    line("withdrawn vs maintained within N208Y", g["Nm"], g["Nw"])
    line("withdrawn vs maintained within WT", g["WTm"], g["WTw"])
# 7G transcript z-scores, rows: cerebellum r2, spinal cord r3
cl = wb["Fig. 7G"]
spans = {"WTm": range(1, 4), "WTw": range(5, 9), "Nm": range(9, 12), "Nw": range(13, 17)}
for tissue, r in (("cerebellum", 1), ("spinal cord", 2), ("kidney", 3), ("lung", 4), ("muscle", 5), ("liver", 6), ("spleen", 7)):
    g = {k: [cl[(r, c)] for c in sp if isinstance(cl.get((r, c)), float)] for k, sp in spans.items()}
    print("--- 7G cholesterol-synthesis gene z-score,", tissue, {k: len(v) for k, v in g.items()})
    line("genotype (maintained): N208Y vs WT", g["WTm"], g["Nm"])
    line("withdrawn vs maintained within N208Y", g["Nm"], g["Nw"])
    line("withdrawn vs maintained within WT", g["WTm"], g["WTw"])
# 7D and 7E MEF
d = {"WTm": col("Fig. 7D", 10, 13, 0), "WTw": col("Fig. 7D", 10, 13, 1), "Nm": col("Fig. 7D", 10, 13, 2), "Nw": col("Fig. 7D", 10, 13, 3)}
print("--- 7D MEF cholesterol-synthesis z", {k: len(v) for k, v in d.items()})
line("genotype (maintained)", d["WTm"], d["Nm"]); line("withdrawn vs maintained within N208Y", d["Nm"], d["Nw"]); line("withdrawn vs maintained within WT", d["WTm"], d["WTw"])
e = {"WTm": col("Fig. 7E", 1, 4, 0), "Nm": col("Fig. 7E", 1, 4, 1), "WTw": col("Fig. 7E", 1, 4, 2), "Nw": col("Fig. 7E", 1, 4, 3)}
print("--- 7E MEF D2O-labelled cholesterol", {k: len(v) for k, v in e.items()})
line("genotype (maintained)", e["WTm"], e["Nm"]); line("withdrawn vs maintained within N208Y", e["Nm"], e["Nw"]); line("withdrawn vs maintained within WT", e["WTm"], e["WTw"])
