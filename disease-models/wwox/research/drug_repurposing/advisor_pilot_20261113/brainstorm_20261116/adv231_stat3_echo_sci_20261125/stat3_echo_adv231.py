"""ADV-231: STAT3-axis transcript echo in held Wwox-deficient brain tables. Print-only; implements PREREG_ADV231_SCI_20261125.md section 2.
Held files only, no network. numpy only. Same loader and rule as ADV-224.

Usage: python3 -I stat3_echo_adv231.py <animals|verdicts> <hippo.txt.gz> <cortex.txt.gz> <Ensembl92 cdna.fa.gz> <p47t_processed.csv.gz>
"""
import sys

if len(sys.argv) != 6 or sys.argv[1] not in ("animals", "verdicts"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, re
import numpy as np

mode, hippo, cortex, fasta, p47 = sys.argv[1:6]
GENES = ["Stat3", "Jak2", "Il6st", "Socs3", "Socs1", "Il6", "Osmr", "Bcl3", "Pim1", "Wwox"]
TARGETS = ["Socs3", "Socs1", "Il6", "Osmr", "Bcl3", "Pim1"]
tx2g, gsym = {}, {}
for l in gzip.open(fasta, "rt"):
    if l[0] != ">":
        continue
    tid = l[1:].split(" ", 1)[0]
    gid = re.search(r"gene:(\S+)", l).group(1)
    s = re.search(r"gene_symbol:(\S+)", l)
    if "_PATCH" in l.split(" ", 3)[2]:
        continue
    tx2g[tid] = gid
    gsym[gid] = s.group(1) if s else ""
sym2id = {}
for g, s in gsym.items():
    if s:
        sym2id.setdefault(s.upper(), []).append(g)

def load(path):
    f = gzip.open(path, "rt")
    head = f.readline().rstrip("\n").split("\t")
    animals = head[3:]
    gl, rows = {}, []
    for l in f:
        p = l.rstrip("\n").split("\t")
        if p[0] in tx2g:
            rows.append((tx2g[p[0]], np.array(p[3:], dtype=float)))
    ids = sorted(set(g for g, _ in rows))
    gi = {g: k for k, g in enumerate(ids)}
    G = np.zeros((len(ids), len(animals)))
    for g, v in rows:
        G[gi[g]] += v
    return animals, gi, G

def load_p47(path):
    f = gzip.open(path, "rt")
    head = f.readline().rstrip("\n").split("\t")
    animals = head[2:]
    rows, sym = [], {}
    for l in f:
        p = l.rstrip("\n").split("\t")
        rows.append((p[1].upper(), np.array([float(x) if x not in ("", "NA") else 0.0 for x in p[2:]])))
    gi, G = {}, []
    for s, v in rows:
        if s not in gi:
            gi[s] = len(G)
            G.append(v)
    return animals, gi, np.array(G)

DATA = {"hippo": load(hippo), "cortex": load(cortex)}
P47 = load_p47(p47)
CONTR = [
 ("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], True),
 ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], True),
 ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], True),
 ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
 ("CC_SW", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_NW", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_SN", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
]
p47a = P47[0]
for reg in ("PFC", "HPC", "CTX", "CB"):
    CONTR.append(("P47_" + reg, "p47", [a for a in p47a if a.startswith(reg + "_P47T")], [a for a in p47a if a.startswith(reg + "_WT")], True))

def evaluate(cname, reg, kon, ctn):
    animals, gi, G = P47[0:3] if reg == "p47" else DATA[reg]
    ko = [animals.index(n) for n in kon]
    ct = [animals.index(n) for n in ctn]
    mk, mc = G[:, ko].mean(1), G[:, ct].mean(1)
    thr = 10.0 if reg == "p47" else 1.0
    uni = (mk >= thr) & (mc >= thr)
    R = np.log2((mk + .5) / (mc + .5))
    Rc = R - np.median(R[uni])
    out = {}
    for g in GENES:
        if reg == "p47":
            key = [g.upper()] if g.upper() in gi else []
            idx = gi[key[0]] if key else None
        else:
            c = sym2id.get(g.upper(), [])
            idx = gi[c[0]] if len(c) == 1 and c[0] in gi else None
        if idx is None:
            out[g] = ("NOT MEASURABLE", None, None, None, None, None, False)
            continue
        kv, cv = G[idx, ko], G[idx, ct]
        sep = bool(kv.min() > cv.max() or kv.max() < cv.min())
        if not uni[idx]:
            call = "NOT MEASURABLE"
        elif Rc[idx] >= 0.3 and sep:
            call = "HIGHER"
        elif Rc[idx] <= -0.3 and sep:
            call = "LOWER"
        else:
            call = "NOT RESOLVED"
        out[g] = (call, mk[idx], mc[idx], Rc[idx], kv, cv, sep)
    return out

RES = {}
if mode == "animals":
    print("contrast\tgene\tcall\tmean_ko\tmean_ctl\tRc\tseparated\tko_animals\tctl_animals")
for cname, reg, kon, ctn, counted in CONTR:
    RES[cname] = evaluate(cname, reg, kon, ctn)
    if mode == "animals":
        for g in GENES:
            call, a, b, rc, kv, cv, sep = RES[cname][g]
            f = lambda x: "" if x is None else "%.3f" % x
            print("\t".join([cname, g, call, f(a), f(b), f(rc), str(sep), "" if kv is None else ";".join("%.2f" % x for x in kv),
                             "" if cv is None else ";".join("%.2f" % x for x in cv)]))
if mode == "verdicts":
    print("gene\tverdict\tcalls")
    ver = {}
    for g in GENES:
        calls = {c: RES[c][g][0] for c, *_ in CONTR}
        hip = [calls[c] for c in ("H_S", "H_N", "H_null")]
        v = "NOT RESOLVED"
        for d in ("HIGHER", "LOWER"):
            if hip.count(d) >= 2 or (calls["C_S"] == d and d in hip):
                v = d
        p47c = [calls["P47_" + r] for r in ("PFC", "HPC", "CTX", "CB")]
        p47v = "NOT RESOLVED"
        for d in ("HIGHER", "LOWER"):
            if p47c.count(d) >= 2:
                p47v = d
        noisy = any(calls[c] in ("HIGHER", "LOWER") for c in ("CC_SW", "CC_NW", "CC_SN"))
        if noisy and v in ("HIGHER", "LOWER"):
            v = "NOT RESOLVED (noise-prone)"
        if all(calls[c] == "NOT MEASURABLE" for c in ("H_S", "H_N", "H_null", "C_S")):
            v = "NOT MEASURABLE"
        ver[g] = (v, noisy)
        print("%s\tP17:%s|P47T:%s\t%s" % (g, v, p47v, ",".join("%s=%s" % (c, calls[c]) for c, *_ in CONTR)))
    hi = [g for g in TARGETS if ver[g][0] == "HIGHER"]
    lo = [g for g in TARGETS if ver[g][0] == "LOWER"]
    meas = [g for g in TARGETS if ver[g][0] != "NOT MEASURABLE"]
    anynoisy = any(ver[g][1] for g in GENES[:-1])
    if len(hi) >= 3 and not anynoisy:
        d = "1 echo"
    elif len(hi) <= 1 and len(lo) >= 1:
        d = "2 inverse"
    elif len(meas) >= 4 and not hi and not lo:
        d = "3 no echo"
    else:
        d = "4 not resolvable"
    print("#disposition\t%s\tHIGHER=%s\tLOWER=%s\tmeasurable_targets=%d\tanynoisy=%s" % (d, ",".join(hi), ",".join(lo), len(meas), anynoisy))
