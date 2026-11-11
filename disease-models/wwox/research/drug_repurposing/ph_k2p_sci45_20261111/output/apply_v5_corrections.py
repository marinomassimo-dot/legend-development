#!/usr/bin/env python3
"""Apply the V5 corrections (verify/audit.md section 9) to the producer tables as annotations; never delete producer text.
Appends ' [V5: ...]' to a named column of a named row, and adds rows. Idempotent (skips rows already annotated)."""
import csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ANN = [  # file, key column, key, column to annotate, text
 ("decisive.tsv","prop_id","D10","statement","V5: the sentence 'RMP and Rin not found' is wrong. Labbaf Results give Rin of S1 layers 2-4 pyramidal neurons: persistent firing WT 121.4 +/- 10.1 MOhm (n 16) vs knock-out 257.2 +/- 21.2 (n 33); accommodating WT 109.3 +/- 8.6 (n 19) vs 271.1 (n 1); RMP bars in Fig 10H. Adult, layers 2-4, constitutive knock-out, no pH step."),
 ("native_evidence.tsv","row_id","NE04","transfer_gap_to_cortical_L2_3","V5: Rin and RMP are in the text (see D10 correction)."),
 ("evidence.tsv","ev_id","E18","note","V5: Rin is reported in the Results; 'not found' is wrong."),
 ("native_evidence.tsv","row_id","NE11","effect (value, unit)","V5: NOT SUPPORTED as worded: a juvenile neocortical native pH response exists in layer V (row NE12, Yao 2017). The absence stands for layer II/III within the verifier's perimeter (V05, V06, V09, V12)."),
 ("decisive.tsv","prop_id","D09","statement","V5: the hippocampal, thalamic and cerebellar items are abstract level; the juvenile cortical datum is Yao 2017 (NE12), checked by the verifier and rechecked by the Orchestrator in the text (51.7 +/- 4.7 vs 31.1 +/- 4.3 pA at -60 mV, n 5, 9-15 day old mice, room temperature, layer V)."),
 ("tissue_ph.tsv","row_id","TP12","note","V5: NOT SUPPORTED as worded. Walz and Harold 1990 (2155690, abstract): rat hippocampal slices with pHo measured in CA1; lactic acid 20 mM gave pH 6.8 in the slice; sodium lactate up to 30 mM was applied but its pHo effect is not in the abstract. Roberts 1998 (9479044): 20 mM sodium lactate with pHi and pHo measured. These are acid additions or high loads; the absence survives only for a physiological lactate rise, at abstract level."),
 ("decisive.tsv","prop_id","D17","statement","V5: the last sentence (no abstract reports pHo after a lactate step) is not supported as worded (see TP12). 'GDP suppression proportional to the fall' belongs to Ruusuvuori; Mukhtarov 2011 concludes the opposite."),
 ("decisive.tsv","prop_id","D15","statement","V5: omits the basal slice depth gradient: Walz 1989 (abstract-level): centre of a 500 um CA1 slice 0.24 pH unit more acid than the surface, activity 0.03 alkaline then 0.05 acid; Krnjevic and Walz 1990: gradient more than twice as steep at 37 C than at 22 C. The producer's 'moves little' holds for activity, not for depth."),
 ("decisive.tsv","prop_id","D18","statement","V5: H328 was shown in recombinant and cell-free patches; the slice result (astrocytes) is MCT-dependent; the abstract says nothing on pHo."),
 ("tools.tsv","tool_id","T04","neuronal_evidence","V5: Labbaf 2025 also reports spadin in mouse reticular thalamic neurons: 1 uM no effect on firing; 10 uM shifted RMP from -65.4 to -53.4 mV (n 9)."),
 ("tools.tsv","tool_id","T01","identifier","V5: identifiers in tools.tsv are PubChem name matches (CID, formula, IUPAC name) without InChIKey and not compared with a structure drawn in a source; only ML365 is text-consistent with Table 2 of Flaherty 2014."),
 ("decisive.tsv","prop_id","D02","statement","V5: remaining fractions recomputed. Bagriantsev uses a modified Hill with free Imin and free H, so pH50 is the midpoint between Imin and Imax. Honest TASK-1 remaining fraction relative to the alkaline reference: 0.50-0.87 at pH 7.4, 0.39-0.81 at 7.2, 0.28-0.73 at 7.0 (three sources); relative to the pH 7.4 current a step to 7.0 leaves 0.55-0.84. Slope: about 1.1 (TASK-1, TASK-3) and about 0.7 (TREK-1, poor fit) in Bagriantsev; about 1.2 (TASK-1) and 1.9 (TASK-3) in Rinne. The 0.7 unit gap in TASK-1 pK (6.6 vs 7.3-7.4) is not resolved: K+, species and normalisation differ."),
 ("decisive.tsv","prop_id","D03","statement","V5: TASK-3 0.97 at 7.4 does not follow from pH50 6.29 with slope 1 (0.93); it follows from the measured points and the paper's fit. No full-read source puts the TASK-3 midpoint inside 6.8-7.4; Berg (abstract) says about 6.8 and Kang (abstract) percentages imply about 6.9-7.0 (verifier inference, mammalian and native cells)."),
 ("decisive.tsv","prop_id","D04","statement","V5: 'native' means cultured human trabecular meshwork cell line and primary cells. Counter-statement to carry: Weller 2016 (26920692, abstract only) reports acid enhancing a TREK-like K+ current in mouse hippocampal astrocytes after Kir4.1 block; Piechotta reports a block at low pHi. Independent confirmation of extracellular-acid inhibition: Cohen 2008 (abstract)."),
 ("ph_sensitivity.tsv","row_id","PH01","hill","V5: modified Hill, Imin and H free (Methods); murine."),
 ("ph_sensitivity.tsv","row_id","PH14","species","V5: rat."),
 ("ph_sensitivity.tsv","row_id","PH04","fraction_at_7.4","V5: 0.56."),
]
NEW = {
 "native_evidence.tsv": [["NE12","pH-sensitive background K+ current (TASK-1/TASK-3 double knock-out comparison)","layer V pyramidal neurons","mouse neocortex, coronal slices (male C57BL6/J and TASK-/-)","9-15 days","room temperature","pipette 120 K-methanesulfonate, 10 HEPES, 10 EGTA, 3 MgATP, 0.3 GTP-Tris, pH 7.2; ACSF 24 mM NaHCO3 pH 7.35","bath step pH 7.3 to 5.9 (Fig 4C; no intermediate pH); isoflurane 0.5 mM as a second probe","pH-sensitive current at -60 mV 51.7 +/- 4.7 pA (WT) vs 31.1 +/- 4.3 pA (TASK-/-; 40 percent less); holding current 58.4 +/- 5.4 vs 43.3 +/- 7.2 pA at pH 7.3 (26 percent less); RMP -75.1 +/- 0.3 vs -71.1 +/- 1.6 mV","n 5 each","PMID 28276488","Results (TASK-like currents, Fig 4C,D; RMP paragraph); Methods","full_text_read by verifier V5; text numbers rechecked by the Orchestrator (Orchestrator recheck 2026-11-11)","measured","Juvenile and cortical and pyramidal, with the pipette pH buffered at 7.2 (HEPES 10 mM). Gaps to the Wwox preparation: layer V not II/III; room temperature; 1.4 unit step, so no pH-response curve; double knock-out (compensation; 60 percent of the pH-sensitive current persists in the knock-out); the 26 percent holding-current share is a share of current at -60 mV, not of conductance (INFERENZA)"]],
 "tissue_ph.tsv": [["TP13","slice (rat hippocampus, 500 um)","rat","adult slices","not stated","bicarbonate-buffered","pH depth gradient and activity transients","centre 0.24 pH unit more acid than the surface; activity 0.03 alkaline then 0.05 acid; gradient more than twice as steep at 37 C than 22 C (Krnjevic and Walz 1990)","none","PMID 2155690 / Walz 1989 / Krnjevic and Walz 1990","abstract level (verifier V5)","abstract_only","measured","V5 addition: a basal depth gradient larger than the activity transients; relevant to any pH comparison between slices of different thickness, depth or temperature"]],
}
def edit(fn, keycol, key, col, text):
    p = HERE / fn
    rows = list(csv.reader(open(p, newline=""), delimiter="\t")); h = rows[0]
    ki, ci = h.index(keycol), h.index(col)
    for r in rows[1:]:
        if r[ki] == key:
            if "[V5:" in r[ci] or text.startswith("V5:") and ("[" + text + "]") in r[ci]: return
            r[ci] = (r[ci] + " [" + text + "]").strip()
            break
    else: raise SystemExit(f"{fn}:{key} not found")
    csv.writer(open(p, "w", newline=""), delimiter="\t", lineterminator="\n").writerows(rows)
for a in ANN: edit(*a)
for fn, rs in NEW.items():
    p = HERE / fn; rows = list(csv.reader(open(p, newline=""), delimiter="\t"))
    have = {r[0] for r in rows[1:]}
    for r in rs:
        assert len(r) == len(rows[0]), (fn, len(r), len(rows[0]))
        if r[0] not in have: rows.append(r)
    csv.writer(open(p, "w", newline=""), delimiter="\t", lineterminator="\n").writerows(rows)
print("applied")
