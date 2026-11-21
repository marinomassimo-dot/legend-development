"""ADV-166: checks on Source Data Fig. 4 of Javed et al. 2026 (sheets 4c, 4d, 4e, 4g). Stdlib only.
Usage: python3 -I javed_fig4_checks.py <Source Data Fig 4 workbook.xlsx>. Prints every number used in the result file."""
import math, os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min

def betacf(a, b, x):
    tiny = 1e-300; qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap; d = tiny if abs(d) < tiny else d; d = 1.0 / d; h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2)); d = 1.0 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c; c = tiny if abs(c) < tiny else c; d = 1.0 / d; h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2)); d = 1.0 + aa * d; d = tiny if abs(d) < tiny else d
        c = 1.0 + aa / c; c = tiny if abs(c) < tiny else c; d = 1.0 / d; de = d * c; h *= de
        if abs(de - 1.0) < 1e-14: break
    return h

def betai(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    lb = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    f = math.exp(lb + a * math.log(x) + b * math.log(1 - x))
    return f * betacf(a, b, x) / a if x < (a + 1) / (a + b + 2) else 1 - f * betacf(b, a, 1 - x) / b

def t_two_p(t, df):
    return betai(df / 2.0, 0.5, df / (df + t * t))

mean = lambda v: sum(v) / len(v)
def var(v):
    m = mean(v); return sum((x - m) ** 2 for x in v) / (len(v) - 1)

def welch(a, b):
    se2 = var(a) / len(a) + var(b) / len(b)
    t = (mean(b) - mean(a)) / math.sqrt(se2)
    df = se2 ** 2 / ((var(a) / len(a)) ** 2 / (len(a) - 1) + (var(b) / len(b)) ** 2 / (len(b) - 1))
    return t, df, t_two_p(t, df)

def student(a, b):
    sp2 = ((len(a) - 1) * var(a) + (len(b) - 1) * var(b)) / (len(a) + len(b) - 2)
    t = (mean(b) - mean(a)) / math.sqrt(sp2 * (1 / len(a) + 1 / len(b)))
    return t, len(a) + len(b) - 2, t_two_p(t, len(a) + len(b) - 2)

def mwu_exact(a, b):
    allv = a + b; n = len(a); obs = sum(1 for x in a for y in b if y > x) + 0.5 * sum(1 for x in a for y in b if y == x)
    cnt = tot = 0
    for idx in itertools.combinations(range(len(allv)), n):
        ga = [allv[i] for i in idx]; gb = [allv[i] for i in range(len(allv)) if i not in idx]
        u = sum(1 for x in ga for y in gb if y > x) + 0.5 * sum(1 for x in ga for y in gb if y == x)
        tot += 1
        if abs(u - len(a) * len(b) / 2) >= abs(obs - len(a) * len(b) / 2) - 1e-12: cnt += 1
    return cnt / tot

def sheet(path, i):
    return [r for r in xlsx_min.read_rows(path, f"xl/worksheets/sheet{i}.xml")]

def run(path):
    print("=== Fig 4c human OrgH CRISPRi (unit check) ===")
    rows = [r for r in sheet(path, 1)[1:] if r and isinstance(r[1], str)]
    data = {}
    for r in rows:
        cond = "KD" if "KO" in r[1] else "Ctl"
        org = r[2].strip()
        data.setdefault((cond, org), []).append(dict(gfp=r[4], sox=r[5], nd2=r[6], ratio=r[9]))
    for cond in ("Ctl", "KD"):
        orgs = sorted(k[1] for k in data if k[0] == cond)
        print(f"{cond}: organoids {orgs}; images per organoid {[len(data[(cond, o)]) for o in orgs]}")
    per_org = {}
    for (cond, org), ims in sorted(data.items()):
        mr = mean([x["ratio"] for x in ims])
        pooled = sum(x["nd2"] for x in ims) / max(1, sum(x["sox"] for x in ims))
        fs = mean([x["sox"] / x["gfp"] for x in ims]); fn = mean([x["nd2"] / x["gfp"] for x in ims])
        zero = sum(1 for x in ims if x["nd2"] == 0)
        per_org[(cond, org)] = (mr, pooled, fs, fn)
        print(f"  {cond} {org}: images {len(ims)}, mean image ratio {mr:.3f}, pooled NEUROD2/SOX2 {pooled:.3f}, mean SOX2/GFP {fs:.3f}, mean NEUROD2/GFP {fn:.3f}, images with 0 NEUROD2+ {zero}, mean GFP+ {mean([x['gfp'] for x in ims]):.1f}, mean SOX2+ count {mean([x['sox'] for x in ims]):.1f}")
    for k, name in ((0, "mean image ratio"), (1, "pooled ratio"), (2, "SOX2 fraction of GFP+"), (3, "NEUROD2 fraction of GFP+")):
        a = [v[k] for (c, o), v in per_org.items() if c == "Ctl"]; b = [v[k] for (c, o), v in per_org.items() if c == "KD"]
        t, df, p = welch(a, b)
        print(f"per-organoid {name}: Ctl mean {mean(a):.3f} (n={len(a)}), KD mean {mean(b):.3f} (n={len(b)}), Welch t {t:.2f} df {df:.1f} P {p:.4f}")
    imc = [x["ratio"] for (c, o), ims in data.items() if c == "Ctl" for x in ims]; imk = [x["ratio"] for (c, o), ims in data.items() if c == "KD" for x in ims]
    print(f"image level: Ctl n={len(imc)} mean {mean(imc):.3f}, {sum(1 for x in imc if x == 0)} zeros; KD n={len(imk)} mean {mean(imk):.3f}, {sum(1 for x in imk if x == 0)} zeros")
    abs_c = [x["sox"] for (c, o), ims in data.items() if c == "Ctl" for x in ims]; abs_k = [x["sox"] for (c, o), ims in data.items() if c == "KD" for x in ims]
    nd_c = [x["nd2"] for (c, o), ims in data.items() if c == "Ctl" for x in ims]; nd_k = [x["nd2"] for (c, o), ims in data.items() if c == "KD" for x in ims]
    g_c = [x["gfp"] for (c, o), ims in data.items() if c == "Ctl" for x in ims]; g_k = [x["gfp"] for (c, o), ims in data.items() if c == "KD" for x in ims]
    print(f"absolute per image: SOX2+ Ctl {mean(abs_c):.1f} KD {mean(abs_k):.1f}; NEUROD2+ Ctl {mean(nd_c):.1f} KD {mean(nd_k):.1f}; GFP+ Ctl {mean(g_c):.1f} KD {mean(g_k):.1f}")
    for drop in sorted(set(o for (c, o) in data if c == "KD")):
        a = [v[0] for (c, o), v in per_org.items() if c == "Ctl"]; b = [v[0] for (c, o), v in per_org.items() if c == "KD" and o != drop]
        t, df, p = welch(a, b); print(f"leave KD {drop} out: KD mean {mean(b):.3f}, Welch P {p:.4f}")
    for drop in sorted(set(o for (c, o) in data if c == "Ctl")):
        a = [v[0] for (c, o), v in per_org.items() if c == "Ctl" and o != drop]; b = [v[0] for (c, o), v in per_org.items() if c == "KD"]
        t, df, p = welch(a, b); print(f"leave Ctl {drop} out: Ctl mean {mean(a):.3f}, Welch P {p:.4f} (n Ctl={len(a)})")

    print("\n=== Fig 4d mouse overexpression, EdU E16 read E17 ===")
    rows = [r for r in sheet(path, 2)[1:] if r and isinstance(r[2], str)]
    g = {"Ctl": [], "JUNB": []}
    for r in rows:
        g[r[2]].append(dict(rg=r[3], ip=r[4], n=r[5], tot=r[6], ratio=r[7]))
    for k, v in g.items():
        print(k, "images (one per replicate):", len(v))
    for name, f in (("ratio (IP+N)/RG", lambda x: x["ratio"]), ("RG count", lambda x: x["rg"]), ("IP count", lambda x: x["ip"]), ("N count", lambda x: x["n"]), ("All EdU+ epor cells", lambda x: x["tot"]),
                    ("RG fraction", lambda x: x["rg"] / x["tot"]), ("IP fraction", lambda x: x["ip"] / x["tot"]), ("N fraction", lambda x: x["n"] / x["tot"]), ("IP+N count", lambda x: x["ip"] + x["n"])):
        a = [f(x) for x in g["Ctl"]]; b = [f(x) for x in g["JUNB"]]
        t, df, p = student(a, b)
        print(f"{name:22} Ctl {mean(a):7.3f} [{', '.join(f'{x:.2f}' for x in a)}]  JUNB {mean(b):7.3f} [{', '.join(f'{x:.2f}' for x in b)}]  Student t {t:.2f} df {df} P {p:.4f}; Welch P {welch(a, b)[2]:.4f}")

    print("\n=== Fig 4e BrdU+NEUROD2+ / epor cells in cortical plate (P1) ===")
    rows = [r for r in sheet(path, 3)[1:] if r and isinstance(r[1], str)]
    a = [r[2] for r in rows if r[1] == "Ctl"]; b = [r[2] for r in rows if r[1] == "JUNB"]
    t, df, p = student(a, b)
    print(f"Ctl {mean(a):.4f} n={len(a)}; JUNB {mean(b):.4f} n={len(b)}; Student t {t:.2f} P {p:.5f}; every JUNB above every Ctl: {min(b) > max(a)}; no count columns, fraction only")

    print("\n=== Fig 4g pFUCCI G1/S fraction (E16, 24 h) ===")
    rows = [r for r in sheet(path, 4)[1:] if r and isinstance(r[1], str)]
    a = [r[9] for r in rows if r[1] == "Ctl"]; b = [r[9] for r in rows if r[1] == "JUNB"]
    ca = [r[5] for r in rows if r[1] == "Ctl"]; cb = [r[5] for r in rows if r[1] == "JUNB"]
    t, df, p = student(a, b)
    print(f"G1/S Ctl {mean(a):.4f} n={len(a)}; JUNB {mean(b):.4f} n={len(b)}; Student P {t_two_p(t, df):.4f} (legend says Student, Methods say Mann-Whitney); exact MWU P {mwu_exact(a, b):.4f}; total epor cells per image Ctl {mean(ca):.1f} JUNB {mean(cb):.1f}")

if __name__ == "__main__":
    run(sys.argv[1])
