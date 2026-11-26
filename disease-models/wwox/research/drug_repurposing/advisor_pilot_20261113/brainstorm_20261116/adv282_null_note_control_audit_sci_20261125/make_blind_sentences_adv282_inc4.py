#!/usr/bin/env python3
"""Blind reader's file for ADV-282 increment 4: verbatim repository note per id plus the WHOLE held source; nothing from the first reading. Run from the repository root; argument: output path (python3 -I -P -E)."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
R = "disease-models/wwox/research/drug_repurposing/"
GUPTA = [FT + "PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml (article, with every figure legend; figure images are not held)"]
HELD = {
 "DA-L01-005": [FT + "PMID37897534_Cheng2023_PMC.xml (article)", F + "figures/PMID37897534/ (Figures 1 to 7, images)", FT + "PMID37897534_assets/18_2023_4950_MOESM1_ESM.pdf (all supplementary figures; text in ..._pdftotext.txt)"],
 "DR-A02-010": GUPTA,
 "DR-A01-007": [FT + "PMID30266908_Guiberson2018_PMC6162227.xml (article)", F + "supplement/PMID30266908/41467_2018_6507_MOESM1_ESM.pdf (all supplementary figures)",
                R + "pharmacology_it5_20261029/proteostasis_pba_a01.tsv (repository ChEMBL table)", R + "missense_recovery_it5_p8_20261029/hdac_enzyme_potency_chembl_20261029.tsv (repository ChEMBL table)"],
 "DR-A02-006": GUPTA + [FT + "PMID39041895_Mijatovic2024_PMC11264351_epmc_2026-10-29.xml (the human kidney-line paper)"],
 "DR-A02-007": GUPTA,
 "DR-B01-002": [FT + "PMID40544182_Hristodor2025_PMC_2026-10-20.xml (article, with figure legends)"],
 "DR-P9-009": [FT + "ketamine_kds_it_20261117/p4_harms/PMID41288262_Wang2026_europepmc-fulltextxml.xml (article)", FT + "ketamine_kds_it_20261117/p4_harms/txt/PMID41288262_Wang2026_abstract.txt"],
 "DR-E01-002": [FT + "adv282_abstracts_sci_20261126/PMID42771346_efetch.xml (PubMed record with abstract; no full text held)"],
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
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 4 (SCI, 2026-11-26)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
