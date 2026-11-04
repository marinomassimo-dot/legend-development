#!/usr/bin/env python3
"""IT23 P3: scenario x premise x intervention Boolean simulation of a 21-node (plus 9 drug switches) Q5 (cytokine) network with mpbn
(the engine NORDic's drug scoring uses). Boolean, qualitative, NO probabilities. Not medical advice.
Closeness to the healthy attractor is NOT evidence of functional benefit: MYELIN_OL is a scenario premise, not a measurement.

Two intervention encodings are kept apart:
  PHARM  = an explicit drug-switch input D_x = 1 in phase 2 only (rule modification; acts on the ACTIVITY layer of its target)
  GENETIC= node clamped to 0 in phase 1 AND phase 2 (what NORDic DS does for any 'drug': f[node] = "0")
usage: python -I sim_q5.py [--help]     (needs the venv with mpbn; writes results/sim_q5_*.tsv and prints a summary)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import itertools, csv, json, time, collections, os
import mpbn

HERE = os.path.dirname(os.path.abspath(__file__))
D_SWITCH = {"IL6neut": "D_IL6", "TNFneut": "D_TNF", "IL1Bneut": "D_IL1B", "JAKi": "D_JAK", "IKKi": "D_IKK", "NLRP3i": "D_NLRP3", "BRD4i": "D_BRD4", "EP300i": "D_EP300", "STAT3i": "D_STAT3"}
GENETIC = {"KD_IL6_tx": ["IL6_tx"], "KD_TNF_tx": ["TNF_tx"], "KD_IL1B_tx": ["IL1B_tx"], "KD_RELA": ["RELA"], "KD_STAT3": ["STAT3"]}
INTERVENTIONS = ["none"] + list(D_SWITCH) + ["IL6+TNF+IL1B neut"] + list(GENETIC)
SCENARIOS = ["damaging_mediator", "damaging_joint", "damaging_redundant", "compensatory", "consequence", "feedback_transient"]


def rules(sc, logic, receptor, negfb, qloop, proc):
    """Boolean rules. Edge provenance: Q = in edges_qualified.tsv, A = in edges_assumed.tsv."""
    r = {}
    inputs = ["WWOX_loss", "TRIG_PULSE", "ACT2"] + list(D_SWITCH.values())
    for i in inputs:
        r[i] = i  # self-hold: inputs keep their initial value
    r["W_route"] = "WWOX_loss"                                              # A/observation S077
    cyt = "(IL6_sig | TNF_sig | IL1B_sig)"
    if sc == "feedback_transient":
        r["TRIG"] = "TRIG_PULSE"                                            # A: unknown trigger, transient
    elif sc == "consequence":
        r["TRIG"] = "!MYELIN_OL"                                            # A: cytokines downstream of tissue damage
    else:
        r["TRIG"] = "WWOX_loss"                                             # A: unknown link WWOX loss -> cytokine program
    ikk_in = "TRIG"
    if receptor:
        ikk_in += " | TNF_sig | IL1B_sig"                                   # A: receptor steps
    r["IKBKB"] = f"({ikk_in}) & !D_IKK"
    ep = "!D_EP300"; br = "!D_BRD4"
    rela = "IKBKB" + (" & " + ep if logic == "COFACTOR" else "")           # IKK->RELA is A; EP300->RELA Q (logic is a premise)
    if qloop:
        rela = f"({rela}) | (RELA & {ep})"                                  # Q: RELA->RELA, RELA->EP300->RELA positive loops
    r["RELA"] = rela
    r["SOCS3"] = "RELA" if negfb else "0"                                   # Q: RELA->SOCS3 (+); its inhibitory role on JAK2 is A
    r["JAK2"] = ("IL6_sig & !D_JAK" + (" & !SOCS3" if negfb else "")) if receptor else "0"   # A
    r["STAT3"] = "(JAK2 | RELA) & !D_STAT3"                                 # Q: RELA->STAT3; JAK2->STAT3 Q complex in SIGNOR
    r["NLRP3_act"] = "RELA & ACT2 & !D_NLRP3"                               # Q: RELA->NLRP3; ACT2 A
    r["CASP1"] = "NLRP3_act"                                                # Q: NFKB1/RELA->CASP1, simplified
    il6 = "(RELA | STAT3)" + (f" & {ep}" if logic == "COFACTOR" else "")    # Q: RELA,STAT3,EP300->IL6
    tnf = "RELA" + (f" & {br} & {ep}" if logic == "COFACTOR" else "")       # Q: RELA,BRD4,EP300->TNF
    il1 = "(RELA | STAT3)"                                                  # Q: RELA,STAT3->IL1B
    r["IL6_tx"] = il6; r["TNF_tx"] = tnf; r["IL1B_tx"] = il1
    r["IL1B_act"] = "IL1B_tx & CASP1" if proc else "IL1B_tx"                # Q: CASP1->IL1B
    r["IL6_sig"] = "IL6_tx & !D_IL6"; r["TNF_sig"] = "TNF_tx & !D_TNF"; r["IL1B_sig"] = "IL1B_act & !D_IL1B"
    r["GFAP"] = "RELA | STAT3"                                              # Q: RELA,STAT3->GFAP (pathology level in data, transcript here: a proxy)
    if sc in ("damaging_mediator", "feedback_transient"): r["MYELIN_OL"] = f"!{cyt}"
    elif sc == "damaging_joint": r["MYELIN_OL"] = f"!(W_route & {cyt})"
    elif sc == "damaging_redundant": r["MYELIN_OL"] = f"!W_route & !{cyt}"
    elif sc == "compensatory": r["MYELIN_OL"] = f"{cyt} | !W_route"
    elif sc == "consequence": r["MYELIN_OL"] = "!W_route"
    return r


def build(r, clamp):
    f = mpbn.MPBooleanNetwork({k: v for k, v in r.items()})
    for g in clamp: f[g] = "0"                                              # NORDic-style permanent clamp
    return f


def attr_list(f, x0):
    return [dict(a) for a in f.attractors(reachable_from=x0)]


def settle(f, x0, free_star=1):
    A = attr_list(f, x0)
    return A


def run_cell(sc, prem, interv):
    r = rules(sc, *prem)
    names = list(r)
    gen = GENETIC.get(interv, [])
    # phase 1: disease state forms (genetic clamps already present = prevention)
    f1 = build(r, gen)
    x0 = f1.zero()
    x0["WWOX_loss"] = 1; x0["ACT2"] = 1
    if sc == "feedback_transient": x0["TRIG_PULSE"] = 1
    A1 = attr_list(f1, x0)
    outs = []
    for a in A1:
        x1 = f1.zero()
        for k, v in a.items(): x1[k] = 1 if v in (1, "*") else 0           # '*' (oscillating) starts at 1: stated simplification
        if sc == "feedback_transient": x1["TRIG_PULSE"] = 0                  # trigger withdrawn before phase 2
        # phase 2: pharmacology = drug switch(es) on; genetic stays
        f2 = build(r, gen)
        if interv in D_SWITCH: x1[D_SWITCH[interv]] = 1
        if interv == "IL6+TNF+IL1B neut":
            for d in ("D_IL6", "D_TNF", "D_IL1B"): x1[d] = 1
        for a2 in attr_list(f2, x1):
            outs.append(a2)
    return A1, outs


def summarise(a):
    g = lambda n: a[n]
    cyt = [g("IL6_sig"), g("TNF_sig"), g("IL1B_sig")]
    cytv = "*" if "*" in cyt else int(any(c == 1 for c in cyt))
    return dict(CYT=cytv, MYELIN_OL=g("MYELIN_OL"), GFAP=g("GFAP"), IL6_tx=g("IL6_tx"), TNF_tx=g("TNF_tx"), IL1B_tx=g("IL1B_tx"), STAT3=g("STAT3"), RELA=g("RELA"))


def healthy(sc, prem):
    r = rules(sc, *prem); f = build(r, [])
    x0 = f.zero(); x0["ACT2"] = 1
    return [summarise(a) for a in attr_list(f, x0)]


def key(sl):
    return json.dumps(sorted(json.dumps(s, sort_keys=True) for s in sl))


if __name__ == "__main__":
    t0 = time.time()
    grid = list(itertools.product(["OR", "COFACTOR"], [0, 1], [0, 1], [0, 1], [1, 0]))  # logic, receptor, negfb, qloop, proc
    cols = ["scenario", "logic", "receptor_edges", "neg_feedback", "qualified_loops", "il1b_processing", "intervention", "n_final_attractors", "final_states", "healthy_states", "readout_distance_to_healthy"]
    rows = []
    for prem in grid:
        for sc in SCENARIOS:
            if sc == "feedback_transient" and not (prem[1] or prem[3]):
                pass  # still run: shows that without a loop the transient trigger leaves nothing to treat
            H = healthy(sc, prem)
            for iv in INTERVENTIONS:
                A1, outs = run_cell(sc, prem, iv)
                S = [summarise(a) for a in outs]
                uniq = []
                for s in S:
                    if s not in uniq: uniq.append(s)
                hs = H[0]
                dist = sorted({sum(str(s[k]) != str(hs[k]) for k in ("CYT", "MYELIN_OL", "GFAP")) for s in uniq})
                rows.append([sc, prem[0], prem[1], prem[2], prem[3], prem[4], iv, len(uniq), json.dumps(uniq, sort_keys=True), json.dumps(H, sort_keys=True), json.dumps(dist)])
    with open(os.path.join(HERE, "results", "sim_q5_all.tsv"), "w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols); w.writerows(rows)
    print(f"{len(rows)} cells in {time.time()-t0:.1f}s -> results/sim_q5_all.tsv")
