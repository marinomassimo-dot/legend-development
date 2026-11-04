"""IT27 verifier P1b: convergence of the four descriptive KO contrasts (T1: separated, |cLFC|>=0.585, TPM>=1) and its chance expectation.
Usage: python3 -I v_p1b_convergence.py <p1b_own_contrasts...tsv> <p1b_summary.json> <out.json> <out_genes.tsv>"""
import sys, json, csv, itertools
rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t")); S = json.load(open(sys.argv[2]))
C = ["H_S", "H_N", "H_null", "C_S"]; calls = {c: {} for c in C}; sym = {}
for r in rows:
    calls[r["contrast"]][r["ensembl"].split(".")[0]] = (1 if float(r["cLFC"]) > 0 else -1, r["also_in_ctl_vs_ctl_0.585"]); sym[r["ensembl"].split(".")[0]] = r["symbol"]
univ = {c: S["contrasts"][c]["cLFC>=0.585"] for c in C}
nexp = {c: S["contrasts"][c]["n_expr"] for c in C}
p = {c: len(calls[c]) / nexp[c] for c in C}
genes = set().union(*[set(calls[c]) for c in C]); out = {"call_rate_per_expressed_gene": p, "n_calls": {c: len(calls[c]) for c in C}}
N = min(nexp.values())  # approximate common universe size
def exp_k(k):  # expected number of genes called in exactly >=k contrasts if calls independent (Poisson-binomial)
    import itertools as it
    tot = 0.0
    for sub in it.combinations(C, k):
        pr = 1.0
        for c in C: pr *= p[c] if c in sub else 1 - p[c]
        tot += pr
    return tot
def cnt(k):
    return sum(1 for g in genes if sum(g in calls[c] for c in C) == k)
out["observed_exactly_k_of_4"] = {k: cnt(k) for k in (1, 2, 3, 4)}
out["expected_exactly_k_of_4_if_independent_x_universe"] = {k: round(exp_k(k) * N, 1) for k in (2, 3, 4)}
cons = []
for g in genes:
    inc = [c for c in C if g in calls[c]]
    if len(inc) >= 3:
        dirs = {calls[c][g][0] for c in inc}; flag = any(calls[c][g][1] == "1" for c in inc)
        cons.append((g, sym[g], len(inc), "same" if len(dirs) == 1 else "mixed", flag, "".join("+" if calls[c].get(g, (0,))[0] > 0 else "-" if g in calls[c] else "." for c in C)))
out["genes_in_ge3_of_4"] = len(cons); out["of_which_same_direction"] = sum(1 for x in cons if x[3] == "same"); out["of_which_same_dir_and_no_ctl_flag"] = sum(1 for x in cons if x[3] == "same" and not x[4])
out["genes_in_4_of_4_same_dir"] = sum(1 for x in cons if x[2] == 4 and x[3] == "same")
json.dump(out, open(sys.argv[3], "w"), indent=1)
with open(sys.argv[4], "w") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["ensembl", "symbol", "n_contrasts_called", "direction_consistency", "any_control_vs_control_flag", "H_S,H_N,H_null,C_S"])
    for x in sorted(cons, key=lambda x: (-x[2], x[3], x[1])): w.writerow(x)
print(json.dumps(out, indent=1))
