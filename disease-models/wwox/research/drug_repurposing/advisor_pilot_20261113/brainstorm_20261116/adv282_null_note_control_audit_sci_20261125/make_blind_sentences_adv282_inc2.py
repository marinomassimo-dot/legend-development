#!/usr/bin/env python3
"""Blind reader's file for ADV-282 increment 2: verbatim repository sentence per id plus held-source paths; nothing from the first reading. Run from the repository root; argument: output path."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
HELD = {
 "DA-J01-006": [FT + "PMID31340538_Tochigi2019_PMC_r2.xml", F + "figures/PMID31340538_r2/ (figures)", FT + "PMID33914858_Repudi2021_Brain_operator_supplied.txt and .pdf (article)", FT + "PMID33914858_Repudi2021_Brain_operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.pdf and .txt (supplement, figures at pdf page 7)"],
 "DA-K01-008": [FT + "PMID42909904_PMC13684411.xml", FT + "PMID42909904_supplement/ (Supplementary_material.docx, Supplementary_material_derived.txt, Supplementary_tables_derived.txt)"],
 "DA-M01-002": [FT + "PMID42397075_Steinberg2026_OUP-AM.pdf and PMID42397075_Steinberg2026_OUP-AM_fitz.txt (accepted manuscript; Figure 3 is on pdf page 34)", FT + "PMID42397075_Steinberg2026_OUP-Supplement/ (File008 to File012 pdf and txt)"],
 "DA-W2-002": [FT + "PMID34634460_Wwox_osc2021_PMC_r2.xml", F + "supplement/PMID34634460_r2/ (mmc1.docx, mmc1_text.txt)", F + "figures/PMID34634460_r2/"],
 "DA-J01-008": [FT + "PMID36828035_Hussain2023_PMC.xml", FT + "PMID36828035_Hussain2023.pdf", F + "supplement/PMID36828035/ (supplementary figures pdf, tables docx, derived txt)", F + "figures/PMID36828035/"],
 "DA-J01-002": [FT + "PMID30290271_Hussain2019_PMC_r2.xml", F + "figures/PMID30290271_r2/ and F + supplement/PMID30290271_r2/ (both folders may be empty)"],
 "DA-M01-007": [FT + "PMID33914858_Repudi2021_Brain_operator_supplied.txt and .pdf (article)", FT + "PMID33914858_Repudi2021_OUP_browserprint_pdftotext.txt (second copy)", FT + "PMID33914858_Repudi2021_Brain_operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.pdf and .txt (supplement, figures at pdf page 7)"],
 "DA-L01-001": [FT + "PMID30290271_Hussain2019_PMC_r2.xml", F + "figures/PMID30290271_r2/ and F + supplement/PMID30290271_r2/ (both folders may be empty)"],
}
rows = {}
for f in sorted(glob.glob("disease-models/wwox/research/drug_repurposing/cards/*.card.json")):
    inp = json.load(open(f))["input"]
    for k in ("drug_assertions", "disease_assertions"):
        for a in inp.get(k) or []:
            rows.setdefault(a["id"], a)
out = []
for i, paths in HELD.items():
    a = rows[i]
    sent = " ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x)
    ctx = "; ".join(f"{k}: {a.get(k)}" for k in ("target_id", "endpoint", "direction"))
    out.append(f"## {i}\n\nRow fields: {ctx}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n\nHeld source files (root path {F} unless a repository path is given):\n" + "\n".join(f"- {p}" for p in paths) + "\n")
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 2 (SCI, 2026-11-25)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
