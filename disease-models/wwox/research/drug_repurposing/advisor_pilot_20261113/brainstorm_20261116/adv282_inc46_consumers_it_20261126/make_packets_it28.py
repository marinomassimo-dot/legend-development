"""IT 2026-11-26 (IT28): builds the two blind packets from edits_it28.py and the card packets, so the checked text is the text that is applied.
The reader gets the new text, the assertion's own context fields and the held source files, and nothing else. Run from the repository root.
usage: python3 make_packets_it28.py OUTDIR. Hypothesis level; nothing here is medical advice."""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("edits_it28", HERE / "edits_it28.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
DR = Path("disease-models/wwox/research/drug_repurposing")
R = "/home/desktop/legend-development/files"
AB = R + "/fulltext/adv282_abstracts_sci_20261126"
HEPG = "disease-models/wwox/research/drug_repurposing/missense_recovery_it5_p8_20261029"
SRC = {
 "N02": [R+"/fulltext/PMID30290271_Hussain2019_PMC_r2.xml", R+"/fulltext/PMID34634460_Breton2021_PMC.xml"],
 "DR-A01-007": [R+"/fulltext/PMID30266908_Guiberson2018_PMC6162227.xml", R+"/supplement/PMID30266908/41467_2018_6507_MOESM1_ESM.pdf (Supplementary Fig 12, page 19)",
                HEPG+"/hdac_enzyme_potency_chembl_20261029.tsv (repository ChEMBL table)", HEPG+"/munc18_cytosolic_precedent_panel_readings_20261029.tsv (earlier bar readings)"],
 "DR-B01-002": [R+"/fulltext/PMID40544182_Hristodor2025_PMC_2026-10-20.xml"],
 "DR-W2-004": [R+"/fulltext/PMID42652189_Alekseeva2026_PMC.xml (figures: look under "+R+"/figures and "+R+"/fulltext for this PMID)"],
 "DA-L01-005": [R+"/fulltext/PMID37897534_Cheng2023_PMC.xml", R+"/fulltext/PMID37897534_assets/18_2023_4950_MOESM1_ESM.pdf (Supp Fig 8, page 15)", R+"/figures/PMID37897534/18_2023_4950_Fig6_HTML.jpg"],
 "DR-L01-003": [R+"/fulltext/adv282_l01_003_sci_20261126/PMC13701765.xml"],
 "DR-A02-010": [R+"/fulltext/PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml"],
 "DR-A02-006": [R+"/fulltext/PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml", R+"/fulltext/PMID39041895_Mijatovic2024_PMC11264351_epmc_2026-10-29.xml"],
 "DR-A02-007": [R+"/fulltext/PMID37319242_Gupta2023_PMC10270616_epmc_2026-10-29.xml"],
 "DR-H02-008": [R+"/fulltext/PMID24321005_ADV272_PMC4102583_pmcpage_20261125.html"],
 "DA-K01-007": [R+"/geo/GSE158681/ and "+R+"/geo/GSE158682/ (TPM tables)", R+"/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz (transcript to symbol)",
                "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv282_null_note_control_audit_sci_20261125/recompute_k01_007_adv282.py (a recompute script: read it before use, you may write your own)"],
 "DR-H02-036": [AB+"/PMID35980256_efetch.xml", AB+"/PMID31349008_efetch.xml"],
 "DR-H02-023": [AB+"/PMID1940119_efetch.xml", AB+"/PMID2767014_efetch.xml"],
 "DR-H02-024": [AB+"/PMID2757909_efetch.xml"],
 "DR-H02-030": [R+"/fulltext/adv056_it_20261118/B/PMID19054414_x2009_europepmc_core.json"],
 "DR-I01-014": [AB+"/PMID16765624_efetch.xml"],
 "DR-I01-006": [AB+"/PMID16651305_efetch.xml"],
 "DR-I01-001": [AB+"/PMID29913407_efetch.xml"], "DR-I01-002": [AB+"/PMID29913407_efetch.xml"], "DR-I01-004": [AB+"/PMID29913407_efetch.xml"],
 "DR-P9-009": [R+"/fulltext/ketamine_kds_it_20261117/p4_harms/PMID41288262_Wang2026_europepmc-fulltextxml.xml"],
 "DR-P9-010": [R+"/fulltext/ketamine_kds_it_20261117/p6_metabolic_ocular/LABEL_memantine_openfda.json"],
 "DR-E01-002": [AB+"/PMID42771346_efetch.xml"], "DR-E01-003": [AB+"/PMID42179084_efetch.xml"],
}
A_IDS = ["N02", "DR-A01-007", "DR-B01-002", "DR-W2-004", "DA-L01-005", "DR-L01-003", "DR-A02-010", "DR-A02-006", "DR-A02-007", "DR-H02-008", "DA-K01-007"]
B_IDS = ["DR-H02-036", "DR-H02-023", "DR-H02-024", "DR-H02-030", "DR-I01-014", "DR-I01-006", "DR-I01-001", "DR-I01-002", "DR-I01-004", "DR-P9-009", "DR-P9-010", "DR-E01-002", "DR-E01-003"]
assert sorted(A_IDS + B_IDS) == sorted({x["id"] for x in E.NEW})

HEAD = """BLIND VERIFICATION PACKET {name} (hypothesis level; public, class level; nothing here is medical advice)

Each block holds one sentence set that a repository record is about to carry, the record's own context fields, and the held source files.
Check the sentence set against the sources only. Do not open the repository's cards, result files, reports or other notes: read only the files listed in the block
(and, for a figure, an image file of the same article under the same files/ tree). No network.
For each block give one verdict:
  MUST CHANGE: a word, number, attribution, comparator, unit, species, cell, group size, direction or generalisation is wrong, unsupported or says more than the source;
  ADD: supported, but an omission would mislead a reader who sees only this sentence set;
  STANDS: supported as written.
Grade every clause, not only the main fact. Absolute words (only, no, none, every, all) need the whole table or text read; if you cannot, say UNSETTLED for that word.
For a negative, say what you searched. For a number read from a figure, say figure, panel and bar, and view the image. A clause about another assertion id (for example DR-A02-004
or DR-A02-008) or about the repository's own plan is outside your check: say OUTSIDE. For MUST CHANGE and ADD give the minimal replacement wording; a card may not carry
a dose written with a mass-per-body-weight or concentration symbol, so describe doses in words (millimolar and micromolar written out are allowed).
Report: a summary table (id, verdict), then per block the findings with locators. Say which files and figures you opened and which you could not.
"""

def lookup(i, card):
    p = json.loads((DR / f"cards/{card}.packet.json").read_text(encoding="utf-8"))
    if i == "N02": return None
    for k in ("drug_assertions", "disease_assertions"):
        for a in p.get(k, []):
            if a["id"] == i: return a
    raise SystemExit("missing " + i)

def block(i):
    es = [x for x in E.NEW if x["id"] == i]; card = es[0]["card"]; a = lookup(i, card)
    L = [f"\n=== BLOCK {i}"]
    if a is None:
        L.append("record: card on the NMDA-receptor intervention class, field 'functional evidence available' (WWOX systems)")
    else:
        for k in ("source", "target_id", "endpoint", "direction", "reading_depth"):
            new = [x["new"] for x in es if x["field"] == k]
            L.append(f"{k}: {new[0] if new else a.get(k)}" + ("   <- NEW wording, check it too" if new else ""))
        L.append("context: " + json.dumps(a.get("context"), ensure_ascii=False))
    for x in es:
        if x["field"] in ("note", "measured_result_note") or i == "N02": L.append("SENTENCE SET: " + x["new"])
    L.append("held sources: " + " ; ".join(SRC[i]))
    return "\n".join(L)

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for name, ids in (("A", A_IDS), ("B", B_IDS)):
    t = HEAD.format(name=name) + "\n".join(block(i) for i in ids) + "\n"
    (out / f"BLIND_PACKET_{name}_IT28.txt").write_text(t, encoding="utf-8")
    print(name, len(ids), len(t))
