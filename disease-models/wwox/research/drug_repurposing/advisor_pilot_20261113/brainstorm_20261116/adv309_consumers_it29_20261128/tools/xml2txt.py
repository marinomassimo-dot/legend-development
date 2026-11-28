import sys, re
import xml.etree.ElementTree as ET
src, dst = sys.argv[1], sys.argv[2]
tree = ET.parse(src)
root = tree.getroot()
out = []
BLOCK = {"p","title","sec","abstract","caption","label","table-wrap","fig","tr","article-title","kwd-group","ref","list-item","td","th","trans-abstract","table-wrap-foot","fn","disp-quote","supplementary-material","tbody","thead","table"}
def tag(e):
    return e.tag.split('}')[-1] if isinstance(e.tag,str) else ''
def walk(e):
    t = tag(e)
    if t in ("xref",):
        out.append((e.text or ""))
        for c in e: walk(c)
        out.append(e.tail or "")
        return
    if t in ("td","th"):
        out.append(" | ")
    if t in BLOCK and t not in ("td","th"):
        out.append("\n")
    if t in ("sup",): out.append("^")
    if t in ("sub",): out.append("_")
    out.append(e.text or "")
    for c in e:
        walk(c)
        out.append(c.tail or "") if False else None
    if t in BLOCK and t not in ("td","th"):
        out.append("\n")
def walk2(e):
    t = tag(e)
    if t in ("td","th"): out.append(" | ")
    if t in BLOCK and t not in ("td","th"): out.append("\n")
    if t=="sup": out.append("^")
    if t=="sub": out.append("_")
    out.append(e.text or "")
    for c in e:
        walk2(c)
        out.append(c.tail or "")
    if t in BLOCK and t not in ("td","th"): out.append("\n")
walk2(root)
s = "".join(out)
s = re.sub(r"[ \t]+"," ",s)
s = re.sub(r" *\n *","\n",s)
s = re.sub(r"\n{3,}","\n\n",s)
open(dst,"w",encoding="utf-8").write(s.strip()+"\n")
print(dst, len(s))
