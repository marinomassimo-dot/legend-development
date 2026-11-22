"""ADV-171: per-animal checks of the synapse sheets (Fig3A transcripts, Fig3B synaptosome proteins), the lipid droplet sheets (Fig6D, S13) of Ma et al. 2025 S1 Data.
Stdlib only. Usage: python3 -I cyfip2_unread_checks.py <S1 Data workbook xlsx>. Writes nothing; prints the tables.
Layouts (read from the sheet labels): Fig3A has R87C animals only, values normalised to the WT mean (WT animals are not in the sheet); Fig3B has WT and R87C columns per age;
Fig6D / S13 have WT and R87C columns of per-animal values. Region: cortex block (gene in column A) and hippocampus block (gene in column H for 3A, L for 3B).
"""
import math
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def betacf(a, b, x):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1.0 + aa / c
        c = c if abs(c) > 1e-30 else 1e-30
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1.0 + aa / c
        c = c if abs(c) > 1e-30 else 1e-30
        de = d * c
        h *= de
        if abs(de - 1.0) < 3e-14:
            break
    return h


def betai(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lbt) * betacf(a, b, x) / a
    return 1 - math.exp(lbt) * betacf(b, a, 1 - x) / b


def p_two(t, df):
    return betai(df / 2.0, 0.5, df / (df + t * t))


def mean(v):
    return sum(v) / len(v)


def sd(v):
    m = mean(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))


def one_sample(v, mu=1.0):
    t = (mean(v) - mu) / (sd(v) / math.sqrt(len(v)))
    return t, p_two(t, len(v) - 1)


def welch(a, b):
    va, vb = sd(a) ** 2 / len(a), sd(b) ** 2 / len(b)
    t = (mean(b) - mean(a)) / math.sqrt(va + vb)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    return t, p_two(t, df)


def col(c):
    n = 0
    for ch in c:
        n = n * 26 + ord(ch) - 64
    return n


def load(path, sheet_no):
    z = zipfile.ZipFile(path)
    ss = [re.sub(r"<[^>]+>", "", m) for m in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    g = {}
    x = z.read("xl/worksheets/sheet%d.xml" % sheet_no).decode()
    for r in re.findall(r"<row [^>]*>(.*?)</row>", x, re.S):
        for attrs, body in re.findall(r"<c ([^>]*?)(?:/>|>(.*?)</c>)", r, re.S):
            v = re.search(r"<v>(.*?)</v>", body or "")
            if not v:
                continue
            ref = re.search(r'r="([A-Z]+)(\d+)"', attrs)
            val = v.group(1)
            if 't="s"' in attrs:
                val = ss[int(val)].strip()
            else:
                val = float(val)
            g[(int(ref.group(2)), col(ref.group(1)))] = val
    return g


def blocks(g, gene_col, animal_col, value_cols, maxrow):
    """returns {gene: [ [values per animal] per value column ]}"""
    out, cur = {}, None
    for r in range(4, maxrow + 1):
        name = g.get((r, gene_col))
        if isinstance(name, str) and not name.startswith("Animal"):
            cur = name
            out[cur] = [[] for _ in value_cols]
        a = g.get((r, animal_col))
        if cur is None or not (isinstance(a, str) and a.startswith("Animal")):
            continue
        for i, c in enumerate(value_cols):
            v = g.get((r, c))
            if isinstance(v, float):
                out[cur][i].append(v)
    return out


def fig3a(g):
    maxrow = max(r for r, _ in g)
    res = {}
    for region, gcol, acol, vcols in (("cortex", 1, 2, [3, 4, 5, 6]), ("hippocampus", 8, 9, [10, 11, 12, 13])):
        res[region] = blocks(g, gcol, acol, vcols, maxrow)
    return res


def report3a(g):
    ages = ["PWK 1", "PWK 7", "PWK 14", "PWK 28"]
    res = fig3a(g)
    print("== Fig3A (qRT-PCR, R87C animals only, values relative to WT mean) ==")
    for region, genes in res.items():
        print("  %s: %d genes; animals per gene-age: %s" % (region, len(genes), sorted(set(len(v) for vs in genes.values() for v in vs))))
        for ai, age in enumerate(ages):
            sig, up, down, allbeyond, rows = 0, 0, 0, 0, []
            for gene, vs in genes.items():
                v = vs[ai]
                if len(v) < 3:
                    continue
                t, p = one_sample(v)
                m = mean(v)
                if p < 0.05:
                    sig += 1
                    up += m > 1
                    down += m < 1
                if all(x > 1 for x in v) or all(x < 1 for x in v):
                    allbeyond += 1
                rows.append((p, gene, m, len(v), all(x > 1 for x in v) or all(x < 1 for x in v)))
            n = len(rows)
            print("   %-6s genes tested %2d; P<0.05 against 1: %2d (up %d, down %d; chance about %.1f); every animal on one side of 1: %d" % (age, n, sig, up, down, 0.05 * n, allbeyond))
            if age == "PWK 7":
                for p, gene, m, k, ab in sorted(rows)[:6]:
                    print("          PWK 7 %-9s mean %.3f (n %d) P %.3f every animal one side %s" % (gene, m, k, p, ab))


def report3b(g):
    ages = ["PWK 1", "PWK 7", "PWK 14", "PWK 28"]
    maxrow = max(r for r, _ in g)
    print("== Fig3B (synaptosome western blots, WT and R87C per animal) ==")
    for region, gcol, acol, base in (("cortex", 1, 2, 3), ("hippocampus", 12, 13, 14)):
        vcols = [base + i for i in range(8)]
        genes = blocks(g, gcol, acol, vcols, maxrow)
        print("  %s: %d proteins" % (region, len(genes)))
        for ai, age in enumerate(ages):
            sig, rows = 0, []
            for gene, vs in genes.items():
                wt, mu = vs[2 * ai], vs[2 * ai + 1]
                if len(wt) < 3 or len(mu) < 3:
                    continue
                t, p = welch(wt, mu)
                sep = max(mu) < min(wt) or min(mu) > max(wt)
                sig += p < 0.05
                rows.append((p, gene, mean(mu) / mean(wt), len(wt), len(mu), sep))
            print("   %-6s proteins tested %2d; Welch P<0.05: %2d (chance about %.1f); complete animal separation: %d" % (age, len(rows), sig, 0.05 * len(rows), sum(r[5] for r in rows)))
            if age == "PWK 7":
                for p, gene, ratio, a, b, sep in sorted(rows)[:6]:
                    print("          PWK 7 %-9s R87C/WT %.3f (n %d, %d) P %.3f separation %s" % (gene, ratio, a, b, p, sep))


def report_two_col(g, name):
    wt = [g[(r, 2)] for r in range(4, 40) if isinstance(g.get((r, 2)), float)]
    mu = [g[(r, 3)] for r in range(4, 40) if isinstance(g.get((r, 3)), float)]
    t, p = welch(wt, mu)
    print("== %s: WT n %d mean %.3f; R87C n %d mean %.3f; Welch P %.3f; complete separation %s ==" % (name, len(wt), mean(wt), len(mu), mean(mu), p, max(mu) < min(wt) or min(mu) > max(wt)))


def main(path):
    report3a(load(path, 5))
    report3b(load(path, 6))
    report_two_col(load(path, 34), "S13 lipid droplet spot number (PWK 14, per article text)")
    g = load(path, 17)
    report_two_col(g, "Fig6D LD spot number (PWK 28, per legend)")


if __name__ == "__main__":
    main(sys.argv[1])


def extra(path):
    """POST-HOC (labelled in the result): the complex proteins across ages and the raw S13 / Fig6D values."""
    g = load(path, 6)
    maxrow = max(r for r, _ in g)
    for region, gcol, acol, base in (("cortex", 1, 2, 3), ("hippocampus", 12, 13, 14)):
        genes = blocks(g, gcol, acol, [base + i for i in range(8)], maxrow)
        for name in ("CYFIP2", "WAVE1"):
            row = []
            for ai, age in enumerate(["PWK 1", "PWK 7", "PWK 14", "PWK 28"]):
                wt, mu = genes[name][2 * ai], genes[name][2 * ai + 1]
                row.append("%s %.2f (n %d,%d)" % (age, mean(mu) / mean(wt), len(wt), len(mu)))
            print("  POST-HOC %s %s R87C/WT: %s" % (region, name, "; ".join(row)))
    for no, name in ((34, "S13 PWK 14"), (17, "Fig6D PWK 28")):
        g = load(path, no)
        print("  POST-HOC %s WT values %s" % (name, [round(g[(r, 2)], 2) for r in range(4, 40) if isinstance(g.get((r, 2)), float)]))
        print("  POST-HOC %s R87C values %s" % (name, [round(g[(r, 3)], 2) for r in range(4, 40) if isinstance(g.get((r, 3)), float)]))


if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == "extra":
    extra(sys.argv[1])
