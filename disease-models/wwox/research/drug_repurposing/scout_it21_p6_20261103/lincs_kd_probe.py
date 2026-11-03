#!/usr/bin/env python3
"""IT21 P6 light test for gap (b): what does knocking WWOX down shift, in neural cells, in LINCS L1000?

Question fixed before the run: (1) do LINCS shRNA knockdown (library LIB_6) signatures for WWOX exist, in which
cell contexts; (2) is the knockdown itself visible (WWOX value in its own signature; L1000 measures WWOX only if
it is a landmark or inferred gene, so absence is a possible answer); (3) do the six module genes of the IT7 P3
glycolysis/lactate module (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down in WWOX-loss build systems) appear in
the NPC signature, in the build direction; (4) is the NPC signature related to the other cell contexts (Spearman
over shared genes), i.e. is there a cell-type-independent WWOX-knockdown effect or only noise.

Stdlib only. Network: iLINCS (CC BY, key-less, free) GET SignatureMeta and POST ilincsR/downloadSignature, one
call per signature. Prints a summary and writes a small TSV (module genes only; no full signature is stored).
A knockdown signature is one shRNA consensus per cell line, not a patient allele and not WWOX-DEE evidence.

    python3 lincs_kd_probe.py --help
    python3 lincs_kd_probe.py [--gene WWOX] [--out lincs_kd_module.tsv]
"""
import argparse
import json
import math
import sys
import urllib.parse
import urllib.request

META = "https://www.ilincs.org/api/SignatureMeta"
DL = "https://www.ilincs.org/api/ilincsR/downloadSignature"
UA = {"User-Agent": "legend-scout/1.0 (research; no contact)"}
MODULE = {"SLC2A1": "up", "HK2": "up", "LDHA": "up", "LDHB": "up", "BNIP3": "up", "PDK1": "down"}


def get_meta(gene):
    flt = json.dumps({"where": {"compound": gene, "libraryid": "LIB_6"}, "limit": 200})
    req = urllib.request.Request(META + "?filter=" + urllib.parse.quote(flt), headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def download(sig):
    req = urllib.request.Request(DL, data=json.dumps({"sigID": sig, "display": True}).encode(),
                                 headers={"Content-Type": "application/json", **UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        rows = json.load(r)["data"]["signature"]
    return {x["Name_GeneSymbol"]: (x["Value_LogDiffExp"], x["Significance_pvalue"]) for x in rows}


def ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    rk = [0.0] * len(v)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
            j += 1
        for k in range(i, j + 1):
            rk[order[k]] = (i + j) / 2
        i = j + 1
    return rk


def spearman(a, b):
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return num / den if den else float("nan")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gene", default="WWOX")
    ap.add_argument("--out")
    a = ap.parse_args()
    meta = get_meta(a.gene)
    print(f"{a.gene}: {len(meta)} LIB_6 signatures")
    sigs = {}
    for m in sorted(meta, key=lambda m: m["signatureid"]):
        sigs[m["signatureid"]] = (m["cellline"], m["tissue"], m["time"], download(m["signatureid"]))
    npc = [s for s, v in sigs.items() if v[0] == "NPC"]
    for s, (cl, ti, tm, d) in sigs.items():
        own = d.get(a.gene)
        print(f"{s} {cl} ({ti}) {tm}: genes {len(d)}; {a.gene} own value {own}")
    rows = []
    for s in npc:
        d = sigs[s][3]
        for g, direc in MODULE.items():
            v = d.get(g)
            rows.append((s, g, direc, v[0] if v else "NA", v[1] if v else "NA"))
            print("MODULE NPC", s, g, "expected", direc, "value", v)
        for s2, (cl, ti, tm, d2) in sigs.items():
            if s2 == s:
                continue
            sh = sorted(set(d) & set(d2))
            print(f"SPEARMAN NPC vs {cl} {s2}: shared genes {len(sh)} rho {spearman([d[g][0] for g in sh], [d2[g][0] for g in sh]):.3f}")
    allpairs = []
    ids = list(sigs)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            d1, d2 = sigs[ids[i]][3], sigs[ids[j]][3]
            sh = sorted(set(d1) & set(d2))
            allpairs.append(spearman([d1[g][0] for g in sh], [d2[g][0] for g in sh]))
    allpairs.sort()
    if allpairs:
        print(f"ALL PAIRS n={len(allpairs)} median rho {allpairs[len(allpairs) // 2]:.3f} min {allpairs[0]:.3f} max {allpairs[-1]:.3f}")
    if a.out:
        with open(a.out, "w") as f:
            f.write("signature\tgene\texpected_in_build\tlogdiffexp\tp\n")
            for r in rows:
                f.write("\t".join(str(x) for x in r) + "\n")


if __name__ == "__main__":
    sys.exit(main())
