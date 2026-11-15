#!/usr/bin/env python3
"""Second read of IT29-P12 from the originals: what the held NCC supplements and the two papers' text say (stdlib only).

Inputs (all hashed in SHA256SUMS next to them): PMC5011342.xml (paper 1, differentiation screen), PMC5024459.xml (paper 2, cytokine
protection), p1_MOESM2.xlsx (paper 1 Additional file 2, sheet 'All Tox data'), p1_MOESM3.xlsx (paper 1 Additional file 3, sheet
'All OLga data'), p2_MOESM3.xlsx (paper 2 Additional file 3, the same sheet name).
Prints: (1) sheet names and headers, (2) whether paper 1's Additional file 3 and paper 2's Additional file 3 hold identical cell values,
(3) the number of compounds with at least 50 on the quetiapine scale at any dose against the 'actives' counts printed in each paper,
(4) the rows of the five 'contradiction' compounds and the control compounds in both sheets, (5) the compounds of paper 1's own Table 1
(confirmed differentiation hits, 'percent positive control') that belong to the 20 frozen compounds of IT29.
Run:  python3 -I recheck_ncc.py <dir with the five files>      (--help prints this text)
"""
import html
import re
import sys
import zipfile


def sheet(path):
    z = zipfile.ZipFile(path)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        x = z.read("xl/sharedStrings.xml").decode("utf-8")
        for si in re.findall(r"<si>(.*?)</si>", x, flags=re.S):
            ss.append(html.unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, flags=re.S))))
    name = re.findall(r'<sheet [^>]*name="([^"]+)"', z.read("xl/workbook.xml").decode())[0]
    x = z.read("xl/worksheets/sheet1.xml").decode("utf-8")
    rows = []
    for r in re.findall(r"<row[^>]*>(.*?)</row>", x, flags=re.S):
        d = {}
        for c in re.finditer(r'<c r="([A-Z]+)\d+"([^>]*?)(?:/>|>(.*?)</c>)', r, flags=re.S):
            v = re.search(r"<v>(.*?)</v>", c.group(3) or "", flags=re.S)
            val = v.group(1) if v else ""
            if 't="s"' in c.group(2) and val != "":
                val = ss[int(val)]
            d[c.group(1)] = val
        rows.append(d)
    return name, rows


def fl(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def text(path):
    t = open(path, encoding="utf-8").read()
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def main():
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 2:
        print(__doc__)
        return 0
    d = sys.argv[1].rstrip("/") + "/"
    n2, r2 = sheet(d + "p1_MOESM2.xlsx")
    n3, r3 = sheet(d + "p1_MOESM3.xlsx")
    np_, rp = sheet(d + "p2_MOESM3.xlsx")
    print("(1) sheets: p1 Additional file 2 = %r, p1 Additional file 3 = %r, p2 Additional file 3 = %r" % (n2, n3, np_))
    print("    headers p1 file 2:", [r2[0].get(c) for c in "BEFG"])
    print("    headers p1 file 3:", [r3[0].get(c) for c in "BEFGH"])
    print("(2) p1 Additional file 3 cells identical to p2 Additional file 3 cells:", r3 == rp, "(%d rows)" % (len(r3) - 1))
    cols = "EFGH"
    n50 = sum(1 for r in r3[1:] if any((fl(r.get(c)) or -999) >= 50 for c in cols))
    t1, t2 = text(d + "PMC5011342.xml"), text(d + "PMC5024459.xml")
    print("(3) compounds with >= 50 at any dose in the quetiapine sheet: %d; paper 1 text states %r; paper 2 text states %r" % (
        n50, re.findall(r"identified (\d+) actives", t1), re.findall(r"identified (\d+) actives", t2)))
    names = ("clobetasol", "ketoconazole", "miconazole", "tamoxifen", "triiodothyronine", "thyroxine", "quetiapine")
    print("(4) rows of the five compounds and controls (quetiapine sheet; tox sheet % DMSO at 10, 1, 0.1 uM):")
    tox = {(r.get("B") or "").lower(): r for r in r2[1:]}
    for r in r3[1:]:
        nm = (r.get("B") or "")
        if any(n in nm.lower() for n in names):
            tx = tox.get(nm.lower(), {})
            print("    %-24s quet(10,2,0.4,0.08)=%s  tox=%s" % (nm, [None if fl(r.get(c)) is None else round(fl(r.get(c)), 1) for c in cols],
                                                          [None if fl(tx.get(c)) is None else round(fl(tx.get(c)), 1) for c in "EFG"]))
    i = t1.find("Table 1 Confirmed acute OL differentiation hits")
    seg = t1[i:i + 1700]
    print("(5) paper 1 Table 1 footnote:", re.findall(r"a Values indicate [^.]*?control", seg), "| Table 1 entries for the frozen compounds:")
    for nm in ("Tamoxifen", "Quetiapine", "Benztropine", "Oxybutynin", "Ipatropium", "Ifenprodil", "Clemastine", "Bifonazole"):
        m = re.search(nm + r" (b )?(\d+|ND) ([\d.]+)", seg)
        print("    %-12s %s" % (nm, m.group(0) if m else "not in Table 1"))
    for nm in ("clobetasol", "ketoconazole", "miconazole", "liothyronine"):
        print("    %-12s in paper 1 Table 1: %s" % (nm, "yes" if nm in seg.lower() else "no"))
    print("    'quetiapine' occurrences in paper 1 text: %d (both inside tables, as a hit compound)" % len(re.findall("quetiapine", t1, flags=re.I)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
