"""SCI46 package P: apply the V8 verifier's substantive corrections to the producer tables as annotations (the producer's text is kept; a bracketed
[V8: ...] note is appended, or a named clause replaced), add the two sources the verifier found (Winkel 2015 abstract, Zhu 2025 full text scanned) and fix two receipt
coverage fields. Rechecked by the Orchestrator against the texts: Zhu 2025 (PMC11870791) and Costa 2024 (PMC11362529) by Europe PMC XML; Winkel 2015 abstract by the PubMed tool.
  python3 apply_v8_corrections.py"""
import csv, json
from pathlib import Path
HERE = Path(__file__).resolve().parent

def load(name):
    with open(HERE / name, encoding="utf-8", newline="") as fh:
        r = csv.reader(fh, delimiter="\t"); rows = list(r)
    return rows[0], rows[1:]

def save(name, head, rows):
    with open(HERE / name, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(head); w.writerows(rows)

def edit(name, key, col, fn):
    head, rows = load(name); i = head.index(col); n = 0
    for r in rows:
        if r[0] == key:
            new = fn(r[i])
            if new == r[i]: print("already applied:", name, key, col)  # the script can be re-run
            r[i] = new; n += 1
    assert n == 1, (name, key); save(name, head, rows)

app = lambda s: (lambda old: old if s[:12] in old else old + " " + s)

# evidence.tsv
edit("evidence.tsv", "E13", "note", lambda o: o.replace("figure shows near-baseline values under annonacin", "[V8: NQO1 mRNA about 0.2 to 0.5 of the no-annonacin control in every arm (Fig 6d); HO-1 about 0.5 to 0.9 except HPP-D and licochalcone A]"))
edit("evidence.tsv", "E36", "pmid_or_doi", lambda o: o.replace("CHEMBL3822038", "CHEMBL3822044"))
edit("evidence.tsv", "E08", "note", app("[V8: the Results say 'successfully downregulated' Nrf2, NQO1 and nuclear NRF2; 'apparent insufficient' is the authors' Discussion wording; 'inadequate' is the producer's reading]"))
# assay_rows.tsv and knockdown_arms.tsv
edit("assay_rows.tsv", "A14", "locator", lambda o: o.replace("all fields checked: standard_value, value, activity_comment, data_validity_comment, activity_properties are empty", "[V8: this is the one numeric row of the siRNA design: FC, relation '=', standard_value 6.0, units null; activity_comment, data_validity_comment and activity_properties are empty]"))
edit("knockdown_arms.tsv", "K01", "verification", lambda o: o.replace("every numeric field empty", "one numeric row (FC 6.0, non-targeting arm); all NRF2-siRNA rows categorical [V8]"))
edit("knockdown_arms.tsv", "K02", "locator", lambda o: o.replace("activities 16621149-16621159", "activities 16621149, 16621150, 16621154, 16621155, 16621158, 16621159 [V8]"))
# decisive.tsv
edit("decisive.tsv", "D08", "statement", app("[V8: Supp Fig S4f (control-siRNA cells, N 2) shows NQO1 mRNA about 0.97 with annonacin plus vehicle and about 1.45 with annonacin plus Ki 696-2 (not marked significant), while Fig 6d shows about 0.2 and 0.3: the two panels do not share a baseline and mRNA sampling times are not stated, so 'not elevated under annonacin' is not one measurement]"))
edit("decisive.tsv", "D09", "statement", lambda o: o.replace("NRF2 siRNA in LUHMES was inadequate", "NRF2 siRNA in LUHMES left a visible residual [V8: the Results say 'successfully downregulated'; 'apparent insufficient Nrf2-knockdown' is the authors' Discussion wording; 'inadequate' is the producer's reading]").replace("the authors state independence could not be excluded", "the authors state they could not definitely exclude an alternative mechanism independent of Nrf2 activation"))
edit("decisive.tsv", "D10", "statement", app("[V8: the declared 'over 95%' is the authors' text; the Fig 5B mRNA reads are about 0.10 (0.08-0.14) for shRNA and about 0.05 (0.03-0.08) for CRISPR knockout, that is about 86-92% by mRNA, and faint Nrf2 bands remain; radiation read at 24 h in Methods and 72 h in Fig 5F]"))
edit("decisive.tsv", "D11", "statement", app("[V8: also 50 Gy to the cervical spine in vivo; TUNEL under loss (25-28%) is not at a floor, CCK-8 (0.20) cannot exclude one; in vivo rats got 50 mg/kg i.p. daily for 5 months, BBB score at month 5 about 12 of 21 with C7 versus 0 without, and no NRF2-loss arm in vivo]"))
# D15 reworded in place after the first run (see the annotation in decisive.tsv)
edit("decisive.tsv", "D17", "statement", lambda o: o.replace("no alternative binder meets C1 to C4.", "none of these three meets C1 to C4 [V8: the universal clause is withdrawn: Winkel 2015 (D20) reaches C1 and C2 at abstract depth]."))
edit("decisive.tsv", "D18", "statement", app("[V8: add Zhu 2025 (D21): hiPSC-derived cortical interneurons, binder at 1 uM on a KEAP1-overexpression background, no NRF2-loss arm]"))
head, rows = load("decisive.tsv")
rows = [r for r in rows if r[0] not in ("D20", "D21")] + [
 ["D20", "Winkel 2015 (RA839, a non-covalent Kelch-domain binder, Kd about 6 uM by ITC and X-ray): at 10 uM RA839 regulated 105 probe sets in bone-marrow-derived macrophages, pathways of Nrf2 signalling were activated and also after Keap1 silencing, RA839 regulated only two genes in Nrf2 knock-out macrophages, and RA839 and CDDO-Me (covalent) both prevented the LPS induction of iNOS and nitric oxide; a binder with a genome-wide loss-of-NRF2 arm and a covalent comparator in the same cell type, at abstract depth only; knock-out verification and whether CDDO-Me was run in the knock-out arm are not known; myeloid, not neural.", "26459563 / 10.1074/jbc.M115.678136", "Abstract (PubMed tool; Orchestrator and verifier)", "abstract read; full text unreachable (PubMed tool empty, Europe PMC XML HTTP 500 on two attempts; PMC4653701 exists; not retried by another route)", "abstract_only", "compound/class read", "species=Mus musculus; system=bone-marrow-derived macrophages, Nrf2 knock-out and wild type; cell=macrophage; time=not stated; compound conc=10 uM (arrays); readout=genome-wide transcript arrays, iNOS and nitric oxide; knockdown=Nrf2 knock-out (verification not stated in the abstract)"],
 ["D21", "Zhu 2025: the binder KI696 at 1 uM for 48 h on hiPSC-derived cortical interneurons from schizophrenia donors that overexpress KEAP1 (pcDNA KEAP1) was followed by higher intracellular Fe2+ and MDA, lower GSH and GPX4, more lipid oxidation and higher inflammatory mediators than the same cells without KI696 (authors: disruption of KEAP1-NRF2 signalling exacerbates inflammation); no siRNA, shRNA, knock-out or NRF2 inhibitor in the text (keyword scan of the full text), and the SCZ group already shows higher NRF2 and HO-1: a human neuronal use of the binder with a direction opposite to protection, uninterpretable for dependence and relevant to the stated risk arm H6 and to H2.", "40021790 / 10.1002/brb3.70311", "Results (KEAP1/NRF2 section), Methods 2.12, Discussion; Orchestrator recheck in Europe PMC XML of PMC11870791", "supported by the verifier's scan and by the Orchestrator's recheck of the sentences", "partial_fulltext_read", "compound/class read", "species=Homo sapiens; system=hiPSC-derived cortical interneurons, schizophrenia donors, pcDNA KEAP1 transfection; cell=interneuron; time=48 h; compound conc=1 uM; readout=Fe2+, MDA, GSH, GPX4, C11-BODIPY, cytokines; knockdown=none"],
]
save("decisive.tsv", head, rows)
head, rows = load("evidence.tsv")
rows = [r for r in rows if r[0] not in ("E38", "E39")] + [
 ["E38", "Winkel 2015", "26459563", "abstract_only", "support", "D20", "RA839 regulated only two genes in Nrf2 knock-out macrophages.", "Abstract", "[V8-added; Orchestrator read the abstract through the PubMed tool] mouse bone-marrow-derived macrophages; full text not reached"],
 ["E39", "Zhu 2025", "40021790", "partial_fulltext_read", "context", "D21;D18", "KI696 was added to the culture media of pcDNA KEAP1 at a concentration of 1 µM", "Methods 2.12", "[V8-added; Orchestrator recheck in Europe PMC XML] hiPSC-derived cortical interneurons; Results state exacerbated inflammation after KI696"],
]
save("evidence.tsv", head, rows)
# receipts: figures that carry the numbers were viewed (figure_notes F01-F04)
for pm in ("39209951", "39497026"):
    p = HERE / "receipts" / f"FTR-20261111-{pm}-79.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["coverage"]["figures"] = "read"; p.write_text(json.dumps(d, indent=1, sort_keys=True) + "\n", encoding="utf-8")
print("V8 corrections applied")
