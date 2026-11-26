#!/usr/bin/env python3
"""Blind reader's file for ADV-282 increment 6: verbatim repository note per id plus the WHOLE held source; nothing from the first reading. Run from the repository root; argument: output path (python3 -I -P -E)."""
import glob, json, sys
from pathlib import Path
F = "/home/desktop/legend-development/files/"
FT = F + "fulltext/"
R = "disease-models/wwox/research/drug_repurposing/"
GUPTA = [FT + "PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml (article, with every figure legend; figure images are not held)"]
AB = FT + "adv282_abstracts_sci_20261126/PMID%s_efetch.xml (PubMed record with abstract; no full text held)"
HELD = {
 "DR-I01-006": [AB % "16651305"],
 "DR-I01-001": [AB % "29913407"],
 "DR-I01-002": [AB % "29913407"],
 "DR-I01-004": [AB % "29913407"],
 "DR-I01-014": [AB % "16765624"],
 "DA-K01-007": [F + "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz and " + F + "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz (transcript-level TPM tables; sample names are the only group labels held)", F + "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz (Ensembl 92 transcript-to-gene symbols; the headers carry gene_symbol)"],
 "DR-P9-010": [FT + "ketamine_kds_it_20261117/p6_metabolic_ocular/LABEL_memantine_openfda.json (openFDA label JSON, whole)"],
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
Path(sys.argv[1]).write_text("# Sentences for the blind reader, ADV-282 increment 6 (SCI, 2026-11-26)\n\nEach block is a card note as it stands in the repository.\n\n" + "\n".join(out))
print(len(out), "blocks")
