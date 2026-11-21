"""ADV-162 addendum 1: coarse stage/subclass correlation of the public WWOX-KO organoid bulk set (GSE156243) onto the NeuRoDev
compact pseudobulk tables. NOT a NeuRoDev mapping (see the addendum). Usage: python3 -I coarse_correlation.py <tables dir> <count table .gz>"""
import sys
import os
import gzip
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min

SHEETS = ["corticogenesis", "neurogenesis", "gliogenesis"]


def read_query(path):
    q = {}
    with gzip.open(path, "rt") as f:
        head = f.readline().rstrip("\n").split("\t")
        samples = head[1:]
        cols = [[] for _ in samples]
        genes = []
        for line in f:
            p = line.rstrip("\n").split("\t")
            genes.append(p[0])
            for i, v in enumerate(p[1:]):
                cols[i].append(float(v))
    tot = [sum(c) for c in cols]
    for gi, g in enumerate(genes):
        q[g] = [math.log2(cols[i][gi] / tot[i] * 1e6 + 1) for i in range(len(samples))]
    return samples, q


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    sa = math.sqrt(sum((x - ma) ** 2 for x in a))
    sb = math.sqrt(sum((x - mb) ** 2 for x in b))
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb)


def main(d, cpath):
    samples, q = read_query(cpath)
    print("samples", samples, "genes in query", len(q))
    for kind in ["stage", "subclass"]:
        for i, sh in enumerate(SHEETS, start=1):
            rows = xlsx_min.read_rows(os.path.join(d, kind + "_pseudobulk_expression.xlsx"), sheet="xl/worksheets/sheet%d.xml" % i)
            head = rows[0][1:]
            ref = {}
            for r in rows[1:]:
                if r and r[0] in q and all(isinstance(x, float) for x in r[1:1 + len(head)]):
                    ref[r[0]] = r[1:1 + len(head)]
            genes = [g for g in ref if sum(q[g]) / len(samples) >= 2.0]
            rm = {g: sum(ref[g]) / len(head) for g in genes}
            print("\n## %s / %s: reference columns %d, genes used %d (of %d shared)" % (kind, sh, len(head), len(genes), len(ref)))
            res = {}
            for si, s in enumerate(samples):
                qv = [q[g][si] - rm[g] for g in genes]
                cs = [pearson(qv, [ref[g][j] - rm[g] for g in genes]) for j in range(len(head))]
                res[s] = cs
            groups = {"WT mean": ["cwt1", "cwt2"], "KO mean": ["cko1", "cko2", "cko3", "cko4"]}
            for s in samples:
                cs = res[s]
                o = sorted(range(len(head)), key=lambda j: -cs[j])
                print("  %-5s top3 %s | spread best-10th %.3f" % (s, ", ".join("%s %.3f" % (head[j], cs[j]) for j in o[:3]), cs[o[0]] - cs[o[min(9, len(o) - 1)]]))
            for gname, mem in groups.items():
                cs = [sum(res[m][j] for m in mem) / len(mem) for j in range(len(head))]
                o = sorted(range(len(head)), key=lambda j: -cs[j])
                print("  %-7s top3 %s" % (gname, ", ".join("%s %.3f" % (head[j], cs[j]) for j in o[:3])))
            if sh == "corticogenesis":
                kocs = [sum(res[m][j] for m in groups["KO mean"]) / 4 - sum(res[m][j] for m in groups["WT mean"]) / 2 for j in range(len(head))]
                print("  KO-minus-WT correlation difference (descriptive):", ", ".join("%s %+.3f" % (head[j], kocs[j]) for j in sorted(range(len(head)), key=lambda j: -abs(kocs[j]))[:6]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
