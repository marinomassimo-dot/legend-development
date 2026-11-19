"""SCI 2026-11-19 (ADV-083): render a held JATS XML to one paragraph per line (captions, table rows as `label | cell | cell`, table footnotes, figure legends).
Reads the XML given as argument 1 and writes the plain text to the path given as argument 2; prints the source sha256 and the line and word counts; edits nothing else.
Run:  python3 -I render_jats_plain_sci_20261119.py <xml> <out.txt>"""
import hashlib
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

if len(sys.argv) != 3 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
src, dst = Path(sys.argv[1]), Path(sys.argv[2])
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
dst.write_text("\n".join(lines), encoding="utf-8")
print(len(lines), "lines;", sum(len(x.split()) for x in lines), "words")
