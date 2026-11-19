"""SCI 2026-11-19 (ADV-082): render the held Breton 2021 JATS XML to one paragraph per line (table rows as `label | cell | cell`, table footnote included).
Reads the XML under files/fulltext (absolute path below) and writes breton_plain.txt into the job scratch folder named below; edits nothing else.
Run:  python3 -I render_breton_plain_sci_20261119.py   (the scratch path is the one used on 2026-11-19; change it to reproduce elsewhere)"""
import hashlib, re, sys
from pathlib import Path
from xml.etree import ElementTree as ET
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
src = Path("/home/desktop/legend-development/files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml")
b = src.read_bytes()
print("sha256", hashlib.sha256(b).hexdigest(), len(b))
root = ET.fromstring(b)
lines = []


def text(e):
    return " ".join("".join(e.itertext()).split())


def walk(e, path):
    tag = e.tag.split("}")[-1]
    if tag in ("p", "title", "label", "caption", "article-title", "kwd"):
        if tag == "caption":
            lines.append(f"[{path}] CAPTION: {text(e)}")
        elif tag == "p":
            lines.append(f"[{path}] {text(e)}")
        elif tag in ("title", "article-title"):
            lines.append(f"## {text(e)}")
        return
    if tag == "table-wrap":
        lab = e.find("label")
        lines.append(f"[TABLE] {text(lab) if lab is not None else ''}")
        for tr in e.iter():
            if tr.tag.split("}")[-1] == "tr":
                lines.append("   ROW: " + " | ".join(text(td) for td in tr))
        for foot in e.iter():
            if foot.tag.split("}")[-1] == "table-wrap-foot":
                lines.append("   TABLE FOOTNOTE: " + text(foot))
        return
    for c in e:
        t = c.tag.split("}")[-1]
        walk(c, path + ">" + (text(c.find("title")) if t == "sec" and c.find("title") is not None else t))


walk(root, "")
out = Path("/home/desktop/.claude/jobs/22f2465c/tmp/breton_plain.txt")
out.write_text("\n".join(lines), encoding="utf-8")
print(len(lines), "lines;", sum(len(l.split()) for l in lines), "words")
