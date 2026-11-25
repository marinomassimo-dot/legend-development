#!/usr/bin/env python3
"""Blind reader's file for ADV-284: the verbatim repository sentence of DR-D01-001 plus held-source paths (whole source, not the quoted row).
Run from the repository root; argument: output path (python3 -I -P -E)."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
SUP = FT + "PMID42397075_Steinberg2026_OUP-Supplement/"
rows = {}
for f in sorted(glob.glob("disease-models/wwox/research/drug_repurposing/cards/*.card.json")):
    inp = json.load(open(f))["input"]
    for k in ("drug_assertions", "disease_assertions"):
        for a in inp.get(k) or []:
            rows.setdefault(a["id"], a)
a = rows["DR-D01-001"]
sent = " ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x)
ctx = "; ".join(f"{k}: {a.get(k)}" for k in ("target_id", "endpoint", "direction"))
txt = ("# Sentence for the blind reader, ADV-284 (SCI, 2026-11-25)\n\nThe block is a card note as it stands in the repository.\n\n"
 f"## DR-D01-001\n\nRow fields: {ctx}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n\n"
 "Held source files (the whole source, every panel of the figure and the whole legend, not only the quoted values):\n"
 f"- {SUP}brain-2025-03809-File010.pdf : Supplementary Figures; Supplementary Figure 7 is on pdf page 12 (all panels A-G) with its legend on page 13\n"
 f"- {SUP}brain-2025-03809-File009.pdf and .txt : Supplementary Methods (organoids, MYC inhibition, immunostaining, quantification, statistics)\n"
 f"- {SUP}brain-2025-03809-File008.pdf/.txt, File011, File012 (other supplementary files; the supplementary tables and reagents)\n"
 f"- {FT}PMID42397075_Steinberg2026_OUP-AM.pdf and PMID42397075_Steinberg2026_OUP-AM_fitz.txt : accepted manuscript (the MYC inhibition paragraph is in the Results)\n")
Path(sys.argv[1]).write_text(txt)
print(len(txt), "chars")
