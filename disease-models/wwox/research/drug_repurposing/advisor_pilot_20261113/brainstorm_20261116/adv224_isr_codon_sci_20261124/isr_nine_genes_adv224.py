"""ADV-224 NQ-B: nine ISR readout genes in the held P17 Wwox TPM tables (GSE158681 hippocampus, GSE158682 cortex).
Print-only; implements PREREG_ADV224_SCI_20261124.md section 2. Held files only, no network. numpy only.

Usage: python3 -I isr_nine_genes_adv224.py <hippo.txt.gz> <cortex.txt.gz> <Ensembl92 cdna.fa.gz> <it6_key_genes.tsv>
"""
import sys

if len(sys.argv) != 5:
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, re
import numpy as np

hippo, cortex, fasta, it6 = sys.argv[1:5]
GENES = ["Atf4", "Ddit3", "Chac1", "Eif2ak1", "Ppp1r15a", "Fgf21", "Herpud1", "Dele1", "Eif2s2"]
CARRIED = set(GENES[:5])
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

DATA = {"hippo": load(hippo), "cortex": load(cortex)}
CONTR = [
 ("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], True),
 ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], True),
 ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], True),
 ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
 ("CC_SW", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_NW", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_SN", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
]
ref = {}
for r in csv.DictReader(open(it6), delimiter="\t"):
    ref[(r["contrast"], r["gene"])] = r
res = {}
print("contrast\tgene\tmeasurable\tmeanTPM_KO\tmeanTPM_ctl\tR_centred\tseparated\tcall\tKO_animals\tctl_animals\tIT6_Rc\tIT6_match")
for cname, reg, kon, ctn, counted in CONTR:
    animals, gi, G = DATA[reg]
    ko = [animals.index(n) for n in kon]
    ct = [animals.index(n) for n in ctn]
    mk, mc = G[:, ko].mean(1), G[:, ct].mean(1)
    uni = (mk >= 1.0) & (mc >= 1.0)
    R = np.log2((mk + .5) / (mc + .5))
    Rc = R - np.median(R[uni])
    for g in GENES:
        c = sym2id.get(g.upper(), [])
        if len(c) != 1 or c[0] not in gi:
            print("\t".join([cname, g, "unresolved"] + [""] * 9))
            res[(cname, g)] = "NOT MEASURABLE"
            continue
        i = gi[c[0]]
        kv, cv = G[i, ko], G[i, ct]
        sep = bool(kv.min() > cv.max() or kv.max() < cv.min())
        m = bool(uni[i])
        if not m:
            call = "NOT MEASURABLE"
        elif Rc[i] <= -0.3 and sep:
            call = "LOWER"
        elif Rc[i] >= 0.3 and sep:
            call = "HIGHER"
        else:
            call = "NOT RESOLVED"
        res[(cname, g)] = call
        rr = ref.get((cname, g))
        irc = rr["R_centred"] if rr else ""
        match = ""
        if rr and irc not in ("",):
            try:
                match = "yes" if abs(float(irc) - Rc[i]) <= 0.01 else "NO"
            except ValueError:
                match = ""
        print("\t".join([cname, g, str(m), "%.3f" % mk[i], "%.3f" % mc[i], "%.3f" % Rc[i], str(sep), call,
                         ";".join("%.2f" % x for x in kv), ";".join("%.2f" % x for x in cv), irc, match]))
print()
print("#gene verdicts (>=2 of H_S,H_N,H_null same call, or C_S plus one hippocampal; noise-prone if a call in any control contrast)")
for g in GENES:
    calls = {c: res[(c, g)] for c, *_ in CONTR}
    hip = [calls[c] for c in ("H_S", "H_N", "H_null")]
    verdict = "NOT RESOLVED"
    for d in ("LOWER", "HIGHER"):
        if hip.count(d) >= 2 or (calls["C_S"] == d and d in hip):
            verdict = d
    noisy = any(calls[c] in ("LOWER", "HIGHER") for c in ("CC_SW", "CC_NW", "CC_SN"))
    if noisy and verdict in ("LOWER", "HIGHER"):
        verdict = "NOT RESOLVED (noise-prone: control-contrast call)"
    if all(v == "NOT MEASURABLE" for v in calls.values()):
        verdict = "NOT MEASURABLE"
    print("%s\t%s\t%s\t%s" % (g, "carried" if g in CARRIED else "new", verdict, ",".join("%s=%s" % (c, calls[c]) for c, *_ in CONTR)))
