#!/usr/bin/env python3
"""Blind reader's file for ADV-282 increment 3: verbatim repository sentence per id plus the WHOLE held source (not the quoted row); nothing from the first reading. Run from the repository root; argument: output path (python3 -I -P -E)."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
HELD = {
 "DA-I01-002": [F + "geo/GSE126075/ (the deposit: GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz, gse126075_soft_full.txt, GSM3590948.txt to GSM3590951.txt)", FT + "PMID31543760_Kosla2019_PMC.xml and PMID31543760_Kosla2019_EPMC.xml (article)", FT + "PMID31543760_assets/ (Data_Sheet_1 to 4 pdf and pdftotext)", F + "figures/PMID31543760/ (figures g001 to g011)"],
 "DA-K01-005": [FT + "PMID35328751_Baryla2022_PMC.xml (article)", F + "figures/PMID35328751/ (figures g001 to g012)", FT + "PMID35328751_assets/ (supplement zip and s001 folder)"],
 "DA-K01-006": [FT + "PMID35328751_Baryla2022_PMC.xml (article)", F + "figures/PMID35328751/ (figures g001 to g012)", FT + "PMID35328751_assets/ (supplement zip and s001 folder)"],
 "DA-I01-004": [FT + "PMID35328751_Baryla2022_PMC.xml (article)", F + "figures/PMID35328751/ (figures g001 to g012)", FT + "PMID35328751_assets/ (supplement zip and s001 folder)"],
 "DR-W2-002": [FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606.xml (article)", FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606_supp_S1_functional.docx (functional data)", FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606_supp_S2_clinical.xlsx (clinical table, whole sheet)"],
 "DR-W2-003": [FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606.xml (article)", FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606_supp_S1_functional.docx", FT + "PMID41489401_Karnstedt2026_Epilepsia_PMC13075606_supp_S2_clinical.xlsx (clinical table, whole sheet)"],
 "DR-W2-007": [FT + "PMID39507621_Teplyshova2024_PMC_r2.xml (article)", FT + "PMID39507621_Teplyshova2024_assets/ (figures, tables)"],
 "DR-K01-006": [FT + "PMID34021541_ADV272_PMC8202868_epmc_20261125.xml (the only one of the four named PMIDs held in full; PMIDs 24889205, 36655171 and 42276303 are not held in files/fulltext)"],
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
    out.append(f"## {i}\n\nRow fields: {ctx}\n\nVerbatim repository sentence (the note, whole):\n\n> {sent}\n\nSource label the repository gives: {a.get('source')}\n\nHeld source files (the whole source, every figure and table, not only the quoted values):\n" + "\n".join(f"- {p}" for p in paths) + "\n")
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 3 (SCI, 2026-11-25)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
