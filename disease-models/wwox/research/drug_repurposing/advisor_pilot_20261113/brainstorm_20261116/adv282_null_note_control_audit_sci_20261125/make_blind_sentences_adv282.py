#!/usr/bin/env python3
"""Build the blind reader's file for the six deposit rows of ADV-282 increment 1: the verbatim repository sentence per id,
plus held-source paths. No first-reader class or fact is written here. Run from the repository root; argument: output path."""
import glob, json, sys
from pathlib import Path

F = "/home/desktop/legend-development/files/"
IDS = ["DA-GSE-PDK-003", "DA-L01-003", "DA-W2-012", "DA-J01-007", "DA-K01-002", "DA-I01-001"]
HELD = [F + "geo/GSE156243/ (Salmon gene count table, two deposited differential-gene lists, family SOFT file)",
        F + "fulltext/PMID34268881_Steinberg2021_PMC_r2.xml (article of the deposit)",
        F + "figures/PMID34268881_r2/ (article figures, incl. expanded view)",
        F + "geo/GSE150123/ (series matrix and raw tar of an unperturbed time course; only where a sentence leans on culture time)"]
rows = {}
for f in sorted(glob.glob("disease-models/wwox/research/drug_repurposing/cards/*.card.json")):
    inp = json.load(open(f))["input"]
    for k in ("drug_assertions", "disease_assertions"):
        for a in inp.get(k) or []:
            rows.setdefault(a["id"], a)
out = []
for i in IDS:
    a = rows[i]
    sent = " ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x)
    ctx = "; ".join(f"{k}: {a.get(k)}" for k in ("target_id", "endpoint", "direction"))
    out.append(f"## {i}\n\nRow fields: {ctx}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n")
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 1 (SCI, 2026-11-25)\n\nEach block is a card note as it stands in the repository.\n\nHeld source files for every block:\n"
                             + "\n".join(f"- {p}" for p in HELD) + "\n\n" + "\n".join(out))
print(len(out), "blocks")
