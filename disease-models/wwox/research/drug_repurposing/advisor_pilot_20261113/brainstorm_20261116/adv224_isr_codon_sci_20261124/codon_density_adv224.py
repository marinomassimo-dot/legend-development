"""ADV-224 NQ-C: arginine-codon ribosome density in the public processed tables of GSE113751. Print-only; implements
PREREG_ADV224_SCI_20261124.md section 3. Reads only the extracted GSM*.codon.ribo.density.tsv.gz files passed by directory; no network.

Usage: python3 -I codon_density_adv224.py <dir_with_extracted_GSE113751_files>
"""
import sys

if len(sys.argv) != 2:
    print(__doc__)
    raise SystemExit(0)
import glob, gzip, os

ARG = ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"]
SETS = {"HEK293T_rpC_3h": "293t_rpC_%s_3h", "HCT116_3h": "hct116_%s_3h", "HeLa_3h": "hela_%s_mono_3h", "HEK293T_rpC_6h_argonly": None}

def S(path):
    f = gzip.open(path, "rt")
    head = f.readline().rstrip("\n").split("\t")
    cols = [i for i, h in enumerate(head) if i > 0 and -10 <= int(h) <= 10]
    out = {}
    for l in f:
        p = l.rstrip("\n").split("\t")
        out[p[0]] = max(float(p[i]) for i in cols)
    return out

def find(d, tag):
    m = glob.glob(os.path.join(d, "*_%s.codon.ribo.density.tsv.gz" % tag))
    return m[0] if len(m) == 1 else None

d = sys.argv[1]
print("cell_line\tcodon\tS_arg\tS_leu\tS_rich\tratio_arg_over_rich\tratio_leu_over_rich\tSLOWED")
summary = {}
for name, pat in SETS.items():
    if pat is None:
        continue
    fa, fl, fr = (find(d, pat % k) for k in ("arg", "leu", "rich"))
    if not (fa and fl and fr):
        print(name, "missing file", fa, fl, fr)
        continue
    a, l, r = S(fa), S(fl), S(fr)
    n = 0
    for c in ARG:
        ra, rl = a[c] / r[c], l[c] / r[c]
        slow = ra >= 1.5 and ra >= 1.5 * rl
        n += slow
        print("%s\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%s" % (name, c, a[c], l[c], r[c], ra, rl, slow))
    summary[name] = n
# 6 h time check, HEK293T rpC arg 6h vs rich 3h (no 6h rich in this set) is not comparable: report arg 6h ratio to rich 3h only as a note
f6, fr = find(d, "293t_rpC_arg_6h"), find(d, "293t_rpC_rich_3h")
if f6 and fr:
    a6, r3 = S(f6), S(fr)
    print("#time note (arg 6h over rich 3h; not like-for-like)\t" + ",".join("%s=%.3f" % (c, a6[c] / r3[c]) for c in ARG))
print("#SLOWED arginine codons per cell line\t" + ",".join("%s=%d" % kv for kv in summary.items()))
