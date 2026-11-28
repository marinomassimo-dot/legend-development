"""ADV-328 census (IT35, 2026-11-28): held full texts that mention WWOX/WOX1 and name a cell-restricted deletion
(near a Wwox word) and/or interneuron/glial markers. Search recall only; every hit is read by a human/delegate.
Usage: python3 -I census_adv328.py <fulltext_dir> <out.tsv>"""
import os, re, subprocess, sys, html
src, out = sys.argv[1], sys.argv[2]
W = re.compile(r"\b(WWOX|Wwox|WOX1|Wox1)\b")
COND = re.compile(r"(flox|floxed|loxP|\bcKO\b|conditional(?:ly)?[\s-]+(?:knock|delet|allele|ablat|null)|\b[A-Za-z0-9]+-?Cre\b|\bCre[\s-]?(?:driver|line|recombinase|mice)|neuron[\s-]specific|(?:cell|neuronal|glial|astrocyte|interneuron)[\s-]specific(?:ally)?\s+(?:knock|delet|ablat)|tamoxifen)", re.I)
MARK = re.compile(r"(parvalbumin|\bPvalb\b|\bPV[\s+-]|neuropeptide Y|\bNPY\b|somatostatin|\bSST\b|GAD6[57]|\bGFAP\b|\bIba-?1\b)", re.I)
def text(p):
    e = p.rsplit(".", 1)[-1].lower()
    try:
        if e == "pdf":
            return subprocess.run(["pdftotext", "-q", p, "-"], capture_output=True, text=True, timeout=60).stdout
        raw = open(p, "rb").read().decode("utf-8", "ignore")
        if e in ("xml", "html", "htm"):
            raw = re.sub(r"<[^>]+>", " ", raw)
        return html.unescape(raw) if e != "txt" else raw
    except Exception as ex:
        return ""
rows = []
for f in sorted(os.listdir(src)):
    p = os.path.join(src, f)
    if not os.path.isfile(p) or f.rsplit(".", 1)[-1].lower() not in ("xml", "pdf", "txt", "html", "htm"):
        continue
    t = re.sub(r"\s+", " ", text(p))
    nw = len(W.findall(t))
    if nw < 3:
        continue
    near = 0
    for m in COND.finditer(t):
        s = t[max(0, m.start() - 150): m.end() + 150]
        if W.search(s):
            near += 1
    nm = len(MARK.findall(t))
    rows.append((f, len(t), nw, near, nm))
with open(out, "w") as o:
    o.write("file\tchars\twwox_mentions\tcond_term_near_wwox\tmarker_terms\n")
    for r in rows:
        o.write("\t".join(map(str, r)) + "\n")
print(len(rows), "files with >=3 WWOX/WOX1 mentions;", sum(1 for r in rows if r[3] > 0), "with a restricted-deletion term within 150 chars of a Wwox word;", sum(1 for r in rows if r[3] > 0 and r[4] > 0), "of those with marker terms")
