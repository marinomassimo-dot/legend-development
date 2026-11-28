"""ADV-307: per-slice latency-on-distance fits and slope against early N1 amplitude.

Usage: python3 -I analyse.py "Conduction Velocity.xlsx" OUT_DIR   (standard library only)
"""
import itertools, re, sys, zipfile
from pathlib import Path

DIST = [0.5, 0.75, 1.0, 1.25]


def sheet1(path):
    z = zipfile.ZipFile(path)
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    shared = [strip(m) for m in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    cells = {}
    for ref, attrs, body in re.findall(r'<c r="([A-Z]+\d+)"([^>]*?)(?:/>|>(.*?)</c>)',
                                       z.read("xl/worksheets/sheet1.xml").decode(), re.S):
        v = re.search(r"<v>(.*?)</v>", body or "")
        if v:
            cells[ref] = shared[int(v.group(1))] if 't="s"' in attrs else float(v.group(1))
    return cells


def slices(c):
    out, animal, cur = [], None, None
    for row in range(2, 1 + max(int(re.sub(r"[A-Z]", "", k)) for k in c) + 1):
        animal = c.get(f"A{row}", animal)
        if f"C{row}" in c:
            cur = {"animal": animal, "genotype": c[f"C{row}"], "rows": []}
            out.append(cur)
        if f"D{row}" in c and cur:
            cur["rows"].append((row, c[f"D{row}"], c.get(f"E{row}"), c.get(f"F{row}"), c.get(f"G{row}"), c.get(f"I{row}")))
    return out


def ols(x, y):
    n = len(x); mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x); sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    slope = sxy / sxx; icpt = my - slope * mx
    res = sum((b - icpt - slope * a) ** 2 for a, b in zip(x, y)); tot = sum((b - my) ** 2 for b in y)
    return slope, icpt, 1 - res / tot


def ranks(v):
    s = sorted(v)
    return [s.index(a) + (s.count(a) + 1) / 2 for a in v]


def rho(a, b):
    x, y = ranks(a), ranks(b); n = len(x); mx, my = sum(x) / n, sum(y) / n
    num = sum((p - mx) * (q - my) for p, q in zip(x, y))
    den = (sum((p - mx) ** 2 for p in x) * sum((q - my) ** 2 for q in y)) ** 0.5
    return num / den


def perm_p(a, b):
    obs = abs(rho(a, b)); v = [abs(rho(a, list(p))) for p in itertools.permutations(b)]
    return sum(t >= obs - 1e-9 for t in v) / len(v)


def main():
    out = Path(sys.argv[2]); S = slices(sheet1(sys.argv[1])); usable = []; ratio_bad = []
    table = ["slice\tsheet1_rows\tanimal_label\tgenotype\tn_distances\tamp_at_0.5\tslope_ms_per_mm\tintercept_ms\tr2\tinverse_slope_m_per_s\tmean_of_printed_ratios\tN1_times\tN1_amps"]
    for i, s in enumerate(S, 1):
        rows = s["rows"]
        g = [d / t for _, d, t, _, _, _ in rows]
        for (row, d, t, _, printed, _), calc in zip(rows, g):
            if printed is None or abs(printed - calc) > 1e-4:
                ratio_bad.append(f"G{row}: printed {printed} recomputed {calc:.6f}")
        avg = [r[5] for r in rows if r[5] is not None]
        if avg and abs(avg[0] - sum(g) / len(g)) > 1e-4:
            ratio_bad.append(f"I{rows[0][0]}: printed {avg[0]:.6f} recomputed {sum(g)/len(g):.6f}")
        if [r[1] for r in rows] != DIST or rows[0][3] is None:
            continue
        slope, icpt, r2 = ols(DIST, [r[2] for r in rows])
        s.update(slope=slope, icpt=icpt, amp=rows[0][3], idx=i)
        usable.append(s)
        table.append("\t".join(str(x) for x in [
            i, f"{rows[0][0]}-{rows[-1][0]}", s["animal"], s["genotype"], len(rows), round(rows[0][3], 3), round(slope, 3),
            round(icpt, 3), round(r2, 4), round(1 / slope, 4), round(sum(g) / len(g), 4),
            ",".join(f"{r[2]:.3f}" for r in rows), ",".join(f"{r[3]:.3f}" for r in rows)]))
    (out / "per_slice.tsv").write_text("\n".join(table) + "\n", encoding="utf-8")
    print("slices", len(S), "usable", len(usable))
    print("printed ratios checked: mismatches", len(ratio_bad), ratio_bad[:6])
    amp, slp = [s["amp"] for s in usable], [s["slope"] for s in usable]
    print(f"pooled rho {rho(amp, slp):.3f} exact p {perm_p(amp, slp):.3f}")
    groups = sorted({s["genotype"] for s in usable})
    mean = {g: {k: sum(s[k] for s in usable if s["genotype"] == g) / sum(1 for s in usable if s["genotype"] == g)
                for k in ("amp", "slope", "icpt")} for g in groups}
    ca = [s["amp"] - mean[s["genotype"]]["amp"] for s in usable]
    cs = [s["slope"] - mean[s["genotype"]]["slope"] for s in usable]
    print(f"within-genotype (centred) rho {rho(ca, cs):.3f} exact p {perm_p(ca, cs):.3f}")
    for g in groups:
        sub = [s for s in usable if s["genotype"] == g]
        print(f"{g}: n {len(sub)} rho {rho([s['amp'] for s in sub], [s['slope'] for s in sub]):.2f} "
              f"mean slope {mean[g]['slope']:.3f} intercept {mean[g]['icpt']:.3f} amp {mean[g]['amp']:.3f} "
              f"slopes {[round(s['slope'], 3) for s in sub]} amps {[round(s['amp'], 3) for s in sub]}")
    loo = [rho(amp[:k] + amp[k + 1:], slp[:k] + slp[k + 1:]) for k in range(len(usable))]
    print("leave-one-slice-out pooled rho", [round(v, 2) for v in loo], "range", round(min(loo), 2), round(max(loo), 2))


if __name__ == "__main__":
    main()
