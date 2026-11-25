"""ADV-239: the ranked table of carried small-n transcript inferences. The rows are hand-built from consumers that
were opened and read (PREREG two-hit rule); values quoted in first_read come from out/influence_adv239.tsv,
out/gsea_loo_adv239.tsv and the files named in leave_out_history. This script only orders and writes them.

Usage: python3 -I build_ranked_table_adv239.py <out.tsv>
"""
import sys

if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

ORG = "GSE156243 human cerebral organoid, week 15, bulk"
ORGU = "KO cko1 cko2 cko3 cko4; WT cwt1 cwt2"
ORGN = "4 v 2"
P47 = "GSE215425 P47T mouse brain, adult, bulk"
FB = "forebrain (HPC CTX PFC): WT M3 M2 M1 F5 F4; P47T M7 M6 F9 F8 F10"
CBU = "cerebellum: WT M3 M2 F5 F4; P47T M6 F8 F10"
P17H = "GSE158681 mouse hippocampus P17, bulk"
P17C = "GSE158682 mouse cortex P17, neuronal deletion, bulk"
HU = "S_Ctrl_1-2 v S_KO_1-3; N_Ctrl_1-2 v N_KO_1-2; WT_1-3 v KO_1-2"
CU = "CRTX_S_Ctrl_1-4 v CRTX_S_KO_1-3"
NT = "not testable"
NO = "none found"
ORGW = "arm of 2 (2 WT libraries); four KO on one side of both WT is descriptive only"

# id, deposit, units, n per arm, statement, consumers, (unused column), leave_out_history, first_read, disposition, wording
R = [
 ("O1", ORG, ORGU, ORGN, "Wnt transcriptional output higher in knockout",
  "card D01_a51; card D02_wnt_tankyrase; card M01; portfolio RP-008; CLAIM 002", 3,
  "one: gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md (leave-one-library-out, WT drops leave 1)",
  "AXIN2 LEF1 NKD1 APCDD1 mean +1.19 log2(CPM+1); all 4 KO above both WT; every single drop >= 0.86 of the effect", NT,
  "4 knockout against 2 wild-type libraries of one parental line; direction identical in every knockout library; not testable for single-library influence on the control side"),
 ("O3", ORG, ORGU, ORGN, "Glycolytic and hypoxia-response transcripts higher (LDHA, HK2, SLC2A1, EPAS1; paper GSEA glycolysis up)",
  "card K01; card E02; card I01; investigation INV-16; CLAIM 002", 3, NO,
  "LDHA +0.74, HK2 +2.17, SLC2A1 +1.38, EPAS1 +1.34: all 4 KO above both WT", NT,
  "add '4 v 2 libraries, one parental line' wherever the number is quoted alone"),
 ("C1", "GSE126075 human neural progenitors and neurons, shRNA, CAGE", "hNSC, Neurons, hNSC_WWOX_del, Neurons_WWOX_del", "1 v 1 per stage",
  "ISR higher; PDK1 lower in sign; HIF-type set higher; ERBB4 higher; adhesion genes; CAGE DE/GSEA of PAPER leg",
  "investigation INV-02; card I01; portfolio RP-038; portfolio RP-033; CLAIM 014", 3, NO,
  "one library per arm: no leave-out exists", NT,
  "already worded 'one library per arm' in CLAIM 014 and I01; carry the same words in INV-02, RP-033 and RP-038 quotes"),
 ("S1", "GSE158684 mouse hippocampus P17, single nucleus (one pool per genotype)", "one pooled library per genotype", "1 v 1",
  "PV/Erbb4/receptor/microglial readings from nuclei", "investigation INV-15; portfolio RP-019; portfolio RP-038; portfolio RP-017", 2,
  NO, "pooled: no animal can be left out", NT,
  "keep 'one pool per arm'; a nucleus count is not an animal count"),
 ("H2", "Hussain 2019 (PMID 30290271) null hippocampus, qRT-PCR", "4 KO v 4 WT, no identifiers", "4 v 4",
  "Il6 transcript higher (Tnf-a higher but not significant)", "CLAIM 005; card L01; card J01; investigation INV-14", 1,
  NO, "no per-animal values printed (mean and SEM only)", NT, "no change: CLAIM 005 already states n and the mark"),
 ("O4", ORG, ORGU, ORGN, "PDK1 lower in sign only", "investigation INV-07; card E03; card I01", 3, NO,
  "-0.34; all 4 KO below both WT; the carried text already says inside the single-gene null", NT, "no change"),
 ("O8", ORG, ORGU, ORGN, "No reactive-astrocyte or cytokine transcript programme", "card J01; CLAIM 005; card L01", 1, NO,
  "astro set +0.34, KO and WT overlap; IL1B, IL6, TNF below 0.4 CPM in all six", NT,
  "a non-finding in 4 v 2 libraries without microglia; already worded so"),
 ("O11", ORG, ORGU, ORGN, "Receptor and transporter transcripts present; oligodendrocyte-lineage transcripts barely detectable",
  "card F01; card F02; card F03; card F04", 4, NO,
  "presence holds library by library (GRIN1/2B/2D, SLC12A2/5 > 4 CPM in all six). SOX10, MOG, OLIG1 below 1 CPM, but PLP1 is 48 to 198 CPM",
  "presence: not a contrast",
  "F02: write 'oligodendrocyte-lineage markers (SOX10, MOG, OLIG1) below 1 CPM; PLP1 is 48 to 198 CPM (isoforms not resolved)'"),
 ("H1", "Hussain 2019 (PMID 30290271): RNA-seq on neurospheres, qRT-PCR on hippocampus", "neurospheres 2 KO v 3 WT; hippocampi 4 v 4; no identifiers", "2 v 3 and 4 v 4",
  "Grin2c, Grm3 and Kcna2 transcripts down", "trigger T19; trigger T20", 2, NO,
  "no per-animal values in the article, no accession in its text; the DEG supplement read in August (receipt FTR-20260806-30290271-01) is absent from this checkout and was not reopened; arm of 2 either way", NT,
  "T19: 'Grin2c and Grm3 transcripts down (qRT-PCR, 4 v 4 whole hippocampus; discovery RNA-seq on neurospheres 2 v 3)'; it is not 'NMDA receptor, glutamate receptor and Kv channel genes' as families. Kcna2 belongs to T20"),
 ("O2", ORG, ORGU, ORGN, "ATF4/ISR target set lower", "investigation INV-02; card E01", 2, NO,
  "-0.30; all 4 KO below both WT", NT, "keep 'exploratory, 4 v 2'"),
 ("O5", ORG, ORGU, ORGN, "NFE2L2 lower (AhR target higher)", "investigation INV-08; card L01", 2, NO, "NFE2L2 -0.39; all 4 KO below both WT", NT, "no change"),
 ("O6", ORG, ORGU, ORGN, "HIF1A transcript flat or +0.46, not robust", "investigation INV-19; card K01", 1, NO, "-0.25 in this scale; overlap", NT,
  "no change; note the sign depends on normalisation (INV-19 already says not robust)"),
 ("O9", ORG, ORGU, ORGN, "NPY lower, GAD1/GAD2 higher", "CLAIM 005; CLAIM 002", 0, NO,
  "NPY -2.50 (all below); GAD1 +3.03 (all above); GAD2 +1.41 but overlaps; GAD2 smallest ratio 0.40", NT, "GAD2: 'higher on average; libraries overlap'"),
 ("M5", P17C, CU, "4 v 3 (cortex); hippocampus 2 v 3", "astrocyte-activation transcripts raised after neuron-restricted deletion",
  "card J01; CLAIM 005", 1, NO,
  "cortex set (Gfap Vim Serpina3n Lcn2 Cd44) +1.01; every drop >= 0.73; Serpina3n above all controls", "robust (cortex); hippocampus not testable",
  "may add: 'in cortex no single animal carries it (4 v 3)'"),
 ("T1", P47, FB, "5 v 5", "HYPOXIA, GLYCOLYSIS, APOPTOSIS hallmark enrichment in all three forebrain regions", "card K01", 1,
  "one: p47t_it12 leave_one_animal_out (own sets, not hallmarks); two: ADV-233 (M6, F8)", 'set mean without M6: HPC 0.63 to 0.82 of the effect left (hold); CTX HYPOXIA 0.21, GLYCOLYSIS 0.38, APOPTOSIS 0.22 left; PFC 0.62 to 0.85 left. NES stays positive on every single removal; cortex APOPTOSIS is below q 0.05 with no removal at all (q 0.27)',
  'robust in hippocampus and PFC; cortex one-animal-driven (M6) on the set mean', "'hippocampus and prefrontal cortex hold without any one animal; the cortical set-mean rise rests more than half on animal M6; in the repository re-run cortical APOPTOSIS does not reach q 0.05. The six-gene glycolytic-enzyme shift in cortex still holds without M6'"),
 ("T12", P47, FB, "5 v 5", "TNF/NF-kB/IL1B/RELA and IL6/JAK/STAT3 (regulator-level inflammatory inference of the authors)",
  "card J01", 0, "two: ADV-233 (M6, F8): carried by two animals", 'set mean without M6: TNFA 0.49, 0.12, 0.45 left (HPC CTX PFC); IL6 0.55 to 0.73 left; INFLAMMATORY 0.68, 0.21, 0.67. NES: cortex TNFA +1.47 becomes -0.71 without M6; IL6 stays positive (1.09 or more) on every single removal and 1.21 to 1.38 without M6 and F8',
  'TNFA one-animal-driven (M6); IL6 robust to one animal and keeps sign without M6 and F8; INFLAMMATORY cortex one-animal-driven', "'TNFA/NF-kB: rests more than half on animal M6 (cortex reverses without it). IL6/JAK/STAT3: loses the q threshold without M6 and F8 but keeps its sign and about three quarters of its enrichment score'"),
 ("T2", P47, FB + "; " + CBU, "5 v 5; 4 v 3", "organoid-like selective HIF pattern NOT reproduced", "card K01", 1,
  "one: p47t_it12 leave_one_animal_out", "HIF_SEL_UP6 +0.22 HPC (drop M6 leaves 0.05), +0.11 CTX, -0.07 PFC: no drop reaches the +0.30 rule", "robust (the non-reproduction)", "no change"),
 ("T3", P47, FB + "; " + CBU, "5 v 5; 4 v 3", "NRF2 targets Hmox1 and Srxn1 modestly higher in all four regions", "card L01", 1,
  "one: p47t_it12 (NRF2_5 set); two: ADV-233 (NRF2_5)",
  "Srxn1 robust in all four; Hmox1 robust HPC, PFC, CB; cortex Hmox1 (0.44 left) and the five-gene NRF2 set (0.47 left) lose more than half without M6",
  "robust except Hmox1 cortex (one-animal-driven)",
  "'Srxn1 higher in all four regions; Hmox1 higher too, with the cortical rise resting more than half on animal M6'"),
 ("T4", P47, CBU, "4 v 3", "REACTIVE_OXYGEN_SPECIES hallmark among the top cerebellar sets", "card L01", 1, NO,
  'CB set mean +0.17, 0.76 or more left on every removal; NES 1.88 or more, q met on all 7',
  'robust', 'no change (4 v 3; robust means no single animal carries it, not a significance or cell claim)'),
 ("T5", P47, CBU + "; " + FB, "4 v 3; 5 v 5", "cerebellar cholesterol, fatty-acid, mTORC1 enrichment; forebrain not", "portfolio RP-036", 0,
  "two: ADV-233 (forebrain only; cerebellum per animal)", 'CB cholesterol, fatty acid, mTORC1: q met on all 7 removals, set mean 0.79 or more left. Forebrain cholesterol not enriched: holds on every removal in CTX and PFC; in HPC it reaches q < 0.05 when F5 or F9 (one wild type, one mutant) is removed. mTORC1 meets q in all three forebrain regions with all animals',
  'robust (cerebellum); forebrain absence one-animal-dependent in hippocampus', "RP-036: 'cholesterol set not enriched in cortex and prefrontal cortex; hippocampus depends on single animals. Only the cholesterol set is cerebellum-restricted: mTORC1 meets the threshold in all four regions and fatty acid in hippocampus and cerebellum'"),
 ("T6", P47, FB, "5 v 5", "HDAC5 mRNA nominally lower, SLC2A1 nominally higher", "investigation INV-16", 1, NO,
  "Hdac5 negative on every drop in HPC CTX PFC (CTX -0.38, robust); Slc2a1 positive on every drop in forebrain (CTX falls to 0.47 of the effect); CB Slc2a1 negative",
  "robust in direction; Slc2a1 cortex magnitude one-animal-driven", "'forebrain only; cerebellum goes the other way for Slc2a1'"),
 ("T7", P47, FB + "; " + CBU, "5 v 5; 4 v 3", "no Erbb4 transcript deficit", "portfolio RP-038", 0, NO,
  "HPC +0.09, CTX -0.21, PFC -0.19, CB +0.13; single drops range -0.28 to +0.24", "not testable for absence",
  "'no clear Erbb4 change (|log2| up to 0.21, single-animal drops -0.28 to +0.24)'"),
 ("T8", P47, FB, "5 v 5", "Wwox transcript not different", "CLAIM 007", 0, NO,
  "-0.17, -0.02, -0.15, -0.12 (CB); no drop exceeds 0.25", "not testable for absence (consistent with the claim)", "no change"),
 ("T9", P47, FB + "; " + CBU, "5 v 5; 4 v 3", "thresholded tables do not list Gfap, Aif1, Il1b, Tnf, Il6, Lcn2", "card J01", 0, NO,
  "a list absence, not a measurement", "not testable (list absence)", "no change: already worded so"),
 ("T10", P47, FB, "5 v 5", "myelin-challenge microglial signature does not transfer to whole hippocampus", "portfolio RP-017", 0,
  "one: ganaxolone_p47t_20261123 (leave-one-out inside its adjusted fit)", "the dossier states the leave-one-out range is wide and the sign of the residual uncertain",
  "not testable beyond the dossier's own statement", "keep the dossier's words"),
 ("M1", P17H + " (carried) and cortex", HU + "; " + CU, "2 v 3 (carried contrast)", "lower Pvalb transcript in the neuron-targeted deletion",
  "investigation INV-15", 1, "none by leave-out; per animal in ADV-068",
  "hippocampus S -1.70, all 3 KO below both controls; cortex -0.59, every drop >= 0.76, libraries overlap",
  "not testable (carried, hippocampus); robust but overlapping (cortex)",
  "'2 control against 3 knockout animals in hippocampus; cortex 4 v 3 shows a smaller fall with overlapping animals'"),
 ("M2", P17C + " and " + P17H, CU + "; " + HU, "4 v 3; three hippocampal contrasts with an arm of 2", "no elevation of HIF-axis/glycolysis transcripts",
  "card K01", 1, NO, "cortex set -0.44, every drop >= 0.78, all KO below all controls", "robust (cortex); hippocampus not testable", "no change"),
 ("M3", P17C, CU, "4 v 3", "GSK-3/Wnt transcript premise not distinguishable from random sets", "card D02", 1, NO,
  "set-versus-random comparison not re-run here", "not recomputed", "no change"),
 ("M4", P17H + " and cortex", HU + "; " + CU, "arms of 2; cortex 4 v 3", "NKCC1:KCC2 transcript ratio not raised (hippocampal contrasts)",
  "card F03", 1, NO, "hippocampus ratios negative; cortex +0.24, falling to 0.085 when CRTX_S_Ctrl_1 is removed",
  "not testable (hippocampus); cortex one-library-driven", "F03 may add: 'cortex is not informative: a +0.24 rise rests on one control library'"),
 ("M6", P17C + " and " + P17H, CU + "; " + HU, "4 v 3; arms of 2", "mouse bulk tables disagree in sign for CTGF", "investigation INV-06", 1, NO,
  "cortex +0.19, single removals from -0.37 (without CRTX_S_KO_3) to +0.46 (sign flips)", "one-animal-driven (cortex sign)", "'the cortical sign itself changes with one library removed'"),
 ("M7", P17C + " and " + P17H, "dossier memantine_20261123 (3 v 2 hippocampus; 3 v 4 cortex)", "3 v 4; 3 v 2",
  "prolonged-NMDA-stress signature fails its prespecified test in untreated Wwox brain", "portfolio RP-024", 1,
  "one: memantine_20261123 (leave-one-library-out)", "cortex +0.044 to +0.111 on every drop; hippocampus -0.242 to +0.114",
  "robust (cortex); hippocampus not testable", "no change"),
 ("O7", ORG, ORGU, ORGN, "CTGF higher", "investigation INV-06", 1, NO, "+1.09; all 4 KO above both WT", NT, "no change"),
 ("O10", ORG, ORGU, ORGN, "SLC12A2:SLC12A5 ratio not higher", "card F03", 1, NO, "-0.61; all 4 KO below both WT", NT, "no change"),
 ("O12", ORG, ORGU, ORGN, "libraries correlate with progenitor-like early prenatal stages", "portfolio RP-043", 0, NO, "not recomputed", NT, "no change"),
 ("O13", ORG, ORGU, ORGN, "MYC higher", "card K01", 0, NO, "+0.54; all 4 KO above both WT", NT, "no change"),
]

def n_decision(cons):
    """consumers that are compound or experiment decisions: cards, matching triggers, investigations (mechanical)"""
    return sum(c.split(" ")[0] in ("card", "trigger", "investigation") for c in cons.split("; "))


R.sort(key=lambda r: (-len(r[5].split("; ")), -n_decision(r[5]), r[0]))
with open(sys.argv[1], "w") as o:
    o.write("rank\tid\tdeposit\tunits\tn_mutant_v_control\tstatement\tconsumers\tn_consumers\tn_decision_consumers\t"
            "leave_out_history\tfirst_read\tdisposition\twording_for_IT\n")
    for k, r in enumerate(R, 1):
        i, dep, units, n, st, cons, nd, hist, first, disp, word = r
        o.write("\t".join([str(k), i, dep, units, n, st, cons, str(len(cons.split("; "))), str(n_decision(cons)), hist, first, disp, word]) + "\n")
print("rows", len(R))
