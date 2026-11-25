#!/usr/bin/env python3
"""Build the blind reader's file: the verbatim repository sentence per id, plus held-source paths. No first-reader class or fact is written here."""
import glob, json, sys
from pathlib import Path
R = "/home/desktop/legend-development/files/"
HELD = {
 "DR-A01-003": ["fulltext/PMID40485335_Shah2025_PMC12146831.xml", "figures/PMID40485335/ (figure images, incl. s001 to s004 tif)"],
 "DR-A01-004": ["fulltext/PMID42268630_Frick2026_PMC13251787.xml", "supplement/PMID42268630/PRP2-14-e70285-s001.xlsx", "figures/PMID42268630/"],
 "DR-A02-002": ["fulltext/PMID38378758_Clausen2024_PMC10879094.xml", "supplement/PMID38378758/ (3 pdf, 1 xlsx)", "fulltext/PMID38740822_Gronbaek2024_PMC11091098.xml", "supplement/PMID38740822/ (3 pdf, 1 xlsx)"],
 "DR-A02-009": ["fulltext/PMID38051092_Collard2023_PMC10761163_epmc_2026-10-29.xml"],
 "DR-E03-001": ["IN THE REPOSITORY (worktree path): disease-models/wwox/research/drug_repurposing/lucas_clarke_followup_20261026/chembl_named_activities.tsv, chembl_mechanisms.tsv, chembl_activities.tsv"],
 "DR-H01-003": ["fulltext/adv051_it_20261118/A/PMID40165594_europepmc_core.json (abstract only; no full text is held)"],
 "DR-M01-001": ["fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf and _fitz.txt (article)", "fulltext/PMID42397075_Steinberg2026_OUP-Supplement/ (File008 to File012 pdf and txt)"],
 "DR-D01-002": ["fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf and _fitz.txt (article)", "fulltext/PMID42397075_Steinberg2026_OUP-Supplement/ (File008 to File012 pdf and txt)"],
 "DA-LC-ATF4-002": ["fulltext/PMID42909904_PMC13684411.xml", "fulltext/PMID42909904_LucasClarke2026_BrainComms_fcag385.pdf", "fulltext/PMID42909904_supplement/ (Supplementary_material.docx, _derived.txt, Supplementary_tables.xlsx)"],
 "DR-AAV-GLU10-HD": ["fulltext/PMID42422765_Obeid2026_PMC_r2.xml", "figures/PMID42422765_r2/ (gr1 to gr7)", "fulltext/PMID42422765_Obeid2026_assets/ (mmc1.pdf, mmc2.pdf)"],
 "DR-AAV-GLU10-LD": ["fulltext/PMID42422765_Obeid2026_PMC_r2.xml", "figures/PMID42422765_r2/ (gr1 to gr7)", "fulltext/PMID42422765_Obeid2026_assets/ (mmc1.pdf, mmc2.pdf)"],
 "DR-P11-004": ["fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml"],
 "DR-H02-019": ["fulltext/PMID40670421_ADV272_PMC12267420_epmc_20261125.xml"],
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
    out.append(f"## {i}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n\nHeld source files (root path {R} unless a repository path is given):\n" + "\n".join(f"- {p}" for p in paths) + "\n")
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-281 (SCI, 2026-11-25)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
