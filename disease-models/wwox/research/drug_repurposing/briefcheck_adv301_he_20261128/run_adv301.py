#!/usr/bin/env python3
"""ADV-301: run framework/scripts/fragment_source_check.py over every sentence of five briefs.

Usage: python3 run_adv301.py PREP_DIR [--side]
This is a caller, not a second checker: numbers, absolute words and negative phrases come from the
tool's own normalise(), source_numbers() and check(). --side prints counts only for the two briefs
outside the set (no sources, so no number verdict).
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
REPORTS = ROOT / "disease-models/wwox/research/drug_repurposing/view/research_reports"
FIELDS = ["summary", "graph", "evidence", "inference", "hypothesis", "experiment", "limits"]
SOURCES = {
    "huperzine-a": ["hupa_yu.html", "hupa_wong.xml", "hupa_dinday.xml", "hupa_nct.json"],
    "bexarotene": ["bex_gse283905_family.soft", "bex_zhou.txt", "pmc13495681.xml", "bex_brown.txt",
                   "bex_brown_supp.txt"],
    "etifoxine": ["pmc9545781.xml", "eti_dorego.xml", "eti_schlichter.txt", "eti_thai.txt"],
    "montelukast": ["mtk_wang.json", "mtk_hennen.txt", "mtk_michael.txt", "mtk_xu.xml"],
    "verapamil": ["vera_ma.html", "vera_romermann.html", "elk.json", "vera_dravet.json",
                  "pmc4657039.xml"],
}
SIDE = ["dimethylglycine", "dalfampridine"]


def sentences(brief):
    for field in FIELDS:
        value = brief[field]
        items = value.items() if isinstance(value, dict) else enumerate(
            value if isinstance(value, list) else [value])
        for key, text in items:
            parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text.strip())
            for i, s in enumerate(parts):
                yield f"{field}.{key}.{i}", s


def load_tool():
    spec = importlib.util.spec_from_file_location("fsc", ROOT / "framework/scripts/fragment_source_check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    tool = load_tool()
    side = "--side" in sys.argv
    print("brief\tsentence\tclass\titem\ttext")
    for name in (SIDE if side else SOURCES):
        brief = json.loads((REPORTS / f"{name}.json").read_text(encoding="utf-8"))
        numbers = set()
        if not side:
            texts = [tool.normalise((Path(sys.argv[1]) / f"{f}.txt").read_text(encoding="utf-8"))
                     for f in SOURCES[name]]
            numbers = tool.source_numbers(texts)
        n = 0
        for sid, s in sentences(brief):
            n += 1
            unsupported, absolutes, negatives = tool.check(s, numbers)
            for cls, items in (("number", [] if side else unsupported), ("absolute", absolutes),
                               ("negative", negatives)):
                for item in items:
                    print(f"{name}\t{sid}\t{cls}\t{item}\t{s}")
        print(f"{name}\t-\tscanned\t{n}\t-")


if __name__ == "__main__":
    main()
