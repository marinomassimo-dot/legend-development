"""ADV-301: turn the held (untrusted) source files into plain text before the check.

Usage: python3 -I prepare_sources.py SRC_DIR OUT_DIR
Rules: XML drops <ref-list> and tags; HTML drops script/style/noscript/svg blocks and tags;
txt/soft and plain JSON are copied; BioC JSON drops its REF passages; entities are unescaped; the Lancet middle-dot decimal becomes ".".
Reason: reference lists, CSS and scripts carry thousands of numbers that would hide a missing one.
"""
import html, json, re, sys
from pathlib import Path

FILES = ["hupa_yu.html", "hupa_wong.xml", "hupa_dinday.xml", "hupa_nct.json",
         "bex_gse283905_family.soft", "bex_zhou.txt", "pmc13495681.xml", "bex_brown.txt",
         "bex_brown_supp.txt",
         "owen_oa/pmc9545781.xml", "eti_dorego.xml", "eti_schlichter.txt", "eti_thai.txt",
         "mtk_wang.json", "mtk_hennen.txt", "mtk_michael.txt", "mtk_xu.xml",
         "vera_ma.html", "vera_romermann.html", "elk.json", "vera_dravet.json", "pmc4657039.xml"]


def bioc_text(text):
    out = []
    for coll in json.loads(text):
        for doc in coll["documents"]:
            for p in doc["passages"]:
                if p.get("infons", {}).get("section_type") != "REF":
                    out.append(p.get("text", ""))
    return "\n".join(out)


def prepare(name, text):
    if name == "mtk_wang.json":
        text = bioc_text(text)
    if name.endswith(".xml"):
        text = re.sub(r"<ref-list\b.*?</ref-list>", " ", text, flags=re.S)
    if name.endswith(".html"):
        text = re.sub(r"<(script|style|noscript|svg)\b.*?</\1\s*>", " ", text, flags=re.S | re.I)
    if name.endswith((".xml", ".html")):
        text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"[ \t]+", " ", html.unescape(text).replace("·", "."))


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        raw = (src / name).read_text(encoding="utf-8", errors="replace")
        text = prepare(name, raw)
        (out / (Path(name).name + ".txt")).write_text(text, encoding="utf-8")
        print(f"{name}\t{len(raw)}\t{len(text)}")


if __name__ == "__main__":
    main()
