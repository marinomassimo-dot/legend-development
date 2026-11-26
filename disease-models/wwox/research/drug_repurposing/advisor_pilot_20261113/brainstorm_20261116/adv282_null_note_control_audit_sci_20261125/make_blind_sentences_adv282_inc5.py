#!/usr/bin/env python3
"""Blind reader's file for ADV-282 increment 5: verbatim repository note per id plus the WHOLE held source; nothing from the first reading. Run from the repository root; argument: output path (python3 -I -P -E)."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
R = "disease-models/wwox/research/drug_repurposing/"
GUPTA = [FT + "PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml (article, with every figure legend; figure images are not held)"]
AB = FT + "adv282_abstracts_sci_20261126/PMID%s_efetch.xml (PubMed record with abstract; no full text held)"
HELD = {
 "DR-E01-003": [AB % "42179084"],
 "DR-W2-004": [FT + "PMID42652189_Alekseeva2026_PMC.xml (article)", F + "figures/PMID42652189/ and " + F + "figure_renders/ (PMID42652189_mA.png, PMID42652189_mB.png, p42652189/): figure images"],
 "DR-H02-008": [FT + "PMID24321005_ADV272_PMC4102583_pmcpage_20261125.html (the PMC page of the article, full text, saved 2026-11-25)"],
 "DR-H02-023": [AB % "1940119", AB % "2767014"],
 "DR-H02-024": [AB % "2757909"],
 "DR-H02-036": [AB % "31349008", AB % "35980256"],
 "DR-H02-030": [FT + "adv056_it_20261118/B/PMID19054414_x2009_europepmc_core.json (Europe PMC record with the abstract; no full text held)"],
}
rows = {}
for f in sorted(glob.glob(R + "cards/*.card.json")):
    inp = json.load(open(f))["input"]
    for k in ("drug_assertions", "disease_assertions"):
        for a in inp.get(k) or []:
            rows.setdefault(a["id"], a)
out = []
for i, paths in HELD.items():
    a = rows[i]
    sent = " ".join(x for x in (a.get("measured_result_note"), a.get("note")) if x)
    ctx = "; ".join(f"{k}: {a.get(k)}" for k in ("target_id", "endpoint", "direction", "reading_depth"))
    out.append(f"## {i}\n\nRow fields: {ctx}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n\nHeld source files (the whole source, every figure and table):\n" + "\n".join(f"- {p}" for p in paths) + "\n")
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 5 (SCI, 2026-11-26)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
