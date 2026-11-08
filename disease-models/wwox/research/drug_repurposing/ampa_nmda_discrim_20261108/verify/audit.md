# Blind audit, Package B (AMPA / NMDAR composition / general excitatory transmission / carbenoxolone)

Verifier label `vf-an`, task ORCH-IT39OS-20261108, 2026-11-08. Inputs read before the verdicts: the nine
`output/` tables named in `VERIFIER_BRIEF.md`, the receipts, `INDEX.tsv`. Not opened before this file was
written: `output/README.md`, `output/engine_consumption.md`, `output/consumer_delta.md`.
Labels DATO / INFERENZA / IPOTESI apply to my own statements. Everything here is a check of a package, not medical advice.

Reading route and depth (all plain `curl`, default user agent, PMC open-data bucket or PMC page, scratchpad
subdirectory `vfan_w`, nothing saved in the repository). Claims made for all eight PMIDs (`vf-an`).

| PMID | What I read | Depth I assign |
|---|---|---|
| 34634460 | full text (Methods, Results, Discussion, Table 1), all six figures viewed, supplementary docx text (Table S1, legends S1-S4) and all four supplementary images viewed (TIFF converted with ImageMagick) | `partial_fulltext_read` (reference list not read; everything that carries a number used here read or viewed) |
| 19535488 | full text from the PMC page (Methods, Results, Discussion; Figs 1-4 captions only, no images) | `partial_fulltext_read` |
| 20940167 | full text; Fig 1 viewed; Figs 2-4 not viewed | `partial_fulltext_read` |
| 23589583 | full text; Figs 2 and 6 viewed; Figs 1, 3, 4, 5, 7 captions only | `partial_fulltext_read` |
| 22553026 | full text incl. Table 1; figures not available in the bucket | `partial_fulltext_read` |
| 40994429 | full text main body, Tables 1 and 3; figures and supplement not available | `partial_fulltext_read` |
| 25229608 | full text, Table 1; Fig 1 viewed and measured; Figs 2-5 captions only | `partial_fulltext_read` |
| 15297615 | abstract only (PubMed metadata); full text is behind a bot-check page and was not tried | `abstract_only` |

---

## Headline

DATO. The producer's reading of the WWOX preparation is accurate: every headline number I could check is
correct (counts, d-APV, evoked response amplitudes, mEPSC, incubation ACSF, temperature, absence of other
blockers, recording Mg2+ not stated). All 37 full-text quotes in `evidence.tsv` are verbatim and within 25
words; the two abstract quotes are verbatim. Receipt fingerprints reproduce exactly for the seven
sources whose bytes I could re-fetch.

The substantive errors are few but real, and two of them change a statement used in a hypothesis:

1. The perampanel "text versus figure potency discrepancy" (FB10, EB34, probes, BH1) is most likely a misreading of the figure axis (see B5).
2. The d-APV residual "about 0.4 of baseline, not abolition" of the delayed evoked response is largely the measurement floor of the amplitude metric (WT also reads about 0.115 mV); it cannot carry the "incomplete block / threshold" argument (A5, AB04, BH2 step 1).
3. Madry 2010 at P20 tested carbenoxolone only in combination with La3+, not alone, and its null is underpowered against a 20 to 30 percent effect; BH3's use of it as counter-evidence is stronger than the source allows (B1b).
4. The matrix cell for H2/H3 under M07 ("bursts persist") is not entailed by the hypothesis, and M08's "matched charge" is metric-dependent (C).
5. There are further text/legend/table disagreements in 34634460 that the producer did not list (A4).

---

## A. The WWOX preparation (34634460)

### A1. Numbers: verdict per number

| Number used | Where I found it | Verdict |
|---|---|---|
| Bursts 36 of 42 KO slices (24 mice), 4 of 23 HT (14 mice), 0 of 11 WT (7 mice) | Results 2.1 | SUPPORTED (verbatim) |
| d-APV 50 uM; 51 bursts, 5 slices, 3 animals; bursts "eliminated", washout "returned to normal" | Results 2.2; Methods 5.4; Fig 3 legend; Fig 3C-D | SUPPORTED. Fig 3D has no d-APV bar; Fig 3C shows no burst in the displayed window. Washout frequency bar about 1.8 with error bar about 1 to 2.8 (my reading, raster): "returned to normal" is a loose statement |
| Evoked delayed response KO about 0.46 mV vs WT about 0.12 mV at 100 uA | Suppl Fig S3B (viewed, 1431 px TIFF) | SUPPORTED: KO 0.46 +/- about 0.2, WT about 0.115 |
| d-APV residual about 0.4 of baseline at 100 uA; washout about 1.3 | Suppl Fig S3C | SUPPORTED as a figure reading. PARTLY as an interpretation (see A5) |
| mEPSC larger at -70 mV in KO (KS p 4.99e-7 vs WT, 1.33e-6 vs HT); decay 5.18 vs 4.84 ms, p 0.2982 | Results 2.3; Fig 4 legend; Fig 4B viewed | SUPPORTED. KO curve shifts left between about -15 and -35 pA; averaged inset traces nearly overlap |
| Carbenoxolone 100 uM: frequency -87 percent (p 0.008), duration -18 percent (p 0.0274), not recovered on washout | Results 2.2; Fig 3D | SUPPORTED as printed. Direction and non-recovery stable across text, table and figure; magnitudes are not (A3) |
| Brilliant blue FCF 10 uM did not reduce frequency (median 0.84 to 0.78 per min); Fig 3D bar about 2.5 | Table S1; Fig 3D | SUPPORTED. See A4(g): the comparator is the pooled baseline column |
| Incubation ACSF 123 NaCl, 3.5 K, 1.3 Mg (as MgSO4), 1.5 Ca; slices 35 C 30 min then room temperature at least 60 min; experiment at 35 C | Methods 5.2 | SUPPORTED (the text prints "35o") |
| No GABA, glycine or glutamate-receptor blocker at baseline; pharmacology list = TTX 1 uM, d-APV 50, CBX 100, BB-FCF 10 | Methods 5.4 and 5.3 | SUPPORTED |
| Recording Mg2+ not stated | Methods 5.2-5.3 | SUPPORTED. The only Mg values in the paper are the 3 mM sucrose cutting solution, the 1.3 mM incubation ACSF, and 1 mM MgCl2 in the internal solutions |
| Table 1 (RMP -73.62 vs -79.25, +5.6 mV; Rin 143.03 vs 102.88 = +39 percent; sag; rebound; AP amplitude; cell counts 13/5, 15/6, 40/15) | Table 1 | SUPPORTED |
| sEPSC 23.3 vs 24.7 pA (about 6 percent); sIPSC 57.3 vs 27.5 pA; frequencies | Results 2.5 | SUPPORTED |
| Burst-onset reversal 6 +/- 11.6 mV; whole burst -31; HF -36; n = 30 bursts, 5 animals | Results 2.2; Fig 3A-B viewed | SUPPORTED; scatter is wide (Fig 3B), as the producer says |
| AMPA appears once in the text (mEPSC decay sentence); no NBQX, CNQX, GYKI, kainate, GluN2, bicuculline, gabazine, picrotoxin, mefloquine, ifenprodil | text search (I re-ran it on the PMC text and on the docx text) | SUPPORTED. Perimeter: these two text files, not the images |

### A2. What is not stated (confirmed)

DATO. Recording Mg2+; recording K+ and Ca2+ if different from incubation; d-APV concentration for the Suppl Fig S3C
panel; washout duration; order of drug groups within a slice; any time-matched vehicle control; any AMPA, kainate
or GABA-A manipulation; any heterozygote pharmacology.

### A3. The producer's own disagreement list: real?

| Producer item | Verdict | Note |
|---|---|---|
| Baseline 2.29 vs 0.84 per min for the same 119 bursts | REAL. Further: 60 / 26.2 s = 2.29 exactly, so the text frequency is the reciprocal of the median inter-burst interval stated in the same sentence, while Table S1's 0.84 cannot be that reciprocal for the same sample | See A4(d) for what Fig 1D appears to favour |
| CBX n 36 bursts / 4 slices (legend) vs 13 bursts / 6 slices (Table S1) | REAL | Verified both places |
| BB-FCF n 73 bursts (legend) vs 25 (Table S1), slices 6 both | REAL | |
| CBX amplitude stated three ways | REAL | Text: "no change"; Table S1 median 0.36 to 0.53 (up about 47 percent); Fig 3D bar about 0.6 (down). Also duration: text -18 percent is 0.66 to 0.54 s (medians), bar about 0.57 |
| mEPSC frequency statement | REAL | Text: no change "as compared to S-HTs"; legend p: WT vs KO 2.4e-4, WT vs HT 0.0018, HT vs KO 0.5963. The section heading "not presynaptic" sits against a significant WT vs KO frequency difference |

### A4. Disagreements and limits the producer did not list (all DATO unless marked)

(a) Suppl Fig S3 sample size: the text says the 97 +/- 31 ms latency is "n = 6 animals"; the S3 caption says "n = 6 slices, 3 animals" (KO) and "n = 7 slices, 4 animals" (WT). Producer OB08 quotes both without flagging.
(b) Burst counts in Suppl Fig S1: panel G "126 bursts in 18 slices of 9 animals", panel D 102 bursts / 11 slices / 6 animals, panel F 41 bursts / 5 slices / 1 animal; Fig 1D and Table S1 give 119 bursts / 18 slices / 9 animals for the same 18 slices and 9 animals.
(c) Fig 4 legend: S-CTL (WT + HT) is "18 cells from 10 animals" for sEPSC while s-WT is 14 cells / 5 animals and s-HET 17 / 8; 14 + 17 = 31 cells and 5 + 8 animals cannot give 18 cells / 10 animals. The "about 6 percent" sEPSC mean difference compares KO with this S-CTL.
(d) INFERENZA (raster, +/- one bin). The Fig 1D inter-burst-interval histogram (bins about 15 s wide, 101 intervals, mode about 40 to 55 s with a tail to about 350 s) has well under half of the intervals below 30 s; by my tally the median lies near 70 to 90 s, which fits Table S1's 0.84 per min (71 s) and not the text's 26.2 s. If correct, the 2.29 per min figure is the less reliable one. Not usable as a number either way; the producer's decision to measure its own baseline (BE0) stands.
(e) Fig 3D normalisation: the baseline bar carries an error bar (about +/-0.15 in frequency, about +/-0.25 in amplitude), so values are normalised to a pooled baseline mean, not to each slice's own baseline; the legend names "unpaired t-test with Bonferroni's correction". Table S1 likewise has one pooled baseline column (119/18/9) against three drug columns. So every "x percent fall" is a between-group comparison on pooled bursts, not a within-slice paired effect. This weakens the 87 percent, the 0.78 and the non-recovery alike. It is a stronger reason than those listed to use only direction in BH3.
(f) Mean versus median: the BB-FCF Fig 3D mean frequency bar (about 2.5, error about 1.6-3.4) is far above baseline while the median in Table S1 is flat (0.84 to 0.78) with a maximum of 25.68 per min. A skewed distribution; "no reduction" is safe, "no effect" is not.
(g) HT amplitude: Fig 4 legend gives WT vs HT amplitude KS p = 1.98e-4; observation OB17 says HT amplitude is "intermediate or similar to wild type by KS tests". WT vs HT is significant by the same test (the curves overlap visually in Fig 4B).
(h) Highlights and Summary say the bursts are "NMDAR and gap junction dependent"; Discussion 3.4 itself says CBX may not be specific. The producer notes this (OB16).
(i) Docx image numbering: the supplementary Fig S3 is `image3.tiff` and S2 is `image2.tiff` in the docx relationship order; `figure_notes.tsv` FB07/FB08 say S3 = image2 and S2 = image1. Harmless to the content (the figure descriptions match the figures), wrong as a pointer. FB07 also says "468 px wide"; the embedded TIFF is 1431 px wide, so S3 is better resolved than stated.

### A5. The delayed evoked response and the "not to zero" claim

INFERENZA from Suppl Fig S3 (viewed). The amplitude metric is read at the benchmark latency of about 97 ms in every
genotype, so WT (no delayed deflection) reads about 0.115 mV, not 0. KO baseline at 100 uA is about 0.46 mV; d-APV
at about 0.4 of baseline is about 0.18 mV. Against the WT floor the delayed component would fall from about 0.35
to about 0.07 mV above floor, that is to about 20 percent of the component rather than 40 percent. The top-left KO
trace (d-APV in dark grey) is nearly flat. Consequences: (i) OB09's "residual about 40 percent could be non-NMDAR" is
overstated; (ii) AB04's "d-APV abolished bursts while the delayed evoked response fell only to about 40 percent"
loses much of its force as evidence for threshold behaviour; (iii) BH2 step 1 (labelled DATO "falls to about 0.4,
not to zero") should say that the metric has a floor. Verdict PARTLY.

---

## B. Compound mechanisms

### B1. Carbenoxolone

(a) Tovar 2009 (19535488). SUPPORTED. Verified in the full text: AMPA EPSC 63.3 +/- 4.5 percent (n = 28); NMDA EPSC 69.1 +/- 3.2 percent (n = 14) with higher PPR; IPSC 49.8 +/- 5.7 percent (n = 7) at 100 uM; 10 and 50 uM EPSC 80.0 and 79.2 percent; spike width +24.5 percent (100 uM), +11.4 percent (50 uM); 2.6 fewer spikes; Rin -20.6 percent; autaptic hippocampal micro-island culture, P0-P1 mouse, 6-15 DIV, all recordings at room temperature; EPSC recovery incomplete. The glutamate whole-cell test (95.7 +/- 1.2 percent, n = 5) was run with 100 uM d-AP5 or 5 uM d-CPP present, so direct NMDAR channel block was neither shown nor excluded (the producer's reading is right). Two corrections:
 * Recovery. The paper says EPSC reduction was irreversible/incomplete but the **IPSC reduction was "rapidly and fully reversible"**. BH3 step 3 reads "...and reduced IPSCs, recovering incompletely"; that attaches the incomplete recovery to the IPSCs. Fix: EPSCs recovered incompletely, IPSCs fully.
 * Genetic standard. The Tovar authors name "genetic ablation or dominant negative approaches" as the standard, not specifically connexin-36 deletion. BH3 context says "genetic connexin-36 deletion is the standard named by the Tovar authors". M13 words it correctly; the hypothesis row should match.
 Also not used but relevant: Tovar notes the EPSC reduction started within the 7.5 s interstimulus interval and that reduced inhibition "could lead ... to net increases in network activity", which bears on the GABA-A gap in C.

(b) Madry 2010 (20940167). PARTLY. Verified: rat hippocampal slices (225-300 um), CA1 pyramidal cells, 33 +/- 1 C, chemical ischaemia; CBX 100 uM in bath **and** pipette after at least 30 min pre-exposure; peak anoxic-depolarisation current about 2.1 (n = 6) vs about 2.7 nA (n = 14), P = 0.46 (Fig 1G viewed); glutamate and GABA-A receptor blockers abolished it (P = 0.0006), La3+ and mefloquine also without effect; mefloquine lengthened latency (544 vs 382 s, attributed to K+ channel block); CBX reduced propidium uptake and the authors attribute that to non-specific actions "for example on voltage-gated calcium channels" citing Vessey and Chepkova (a carried statement). Errors and limits:
 * **P20 tested carbenoxolone only together with La3+** ("applied in combination", P = 0.43); the producer's probes.tsv, EB35 and BH3 say CBX alone at P12 and P20.
 * The CBX mean is 22 percent below control (2.1 vs 2.7 nA) with n = 6 vs 14 and SE about 0.3 to 0.4 nA; the test cannot exclude a 20 to 30 percent reduction, the size Tovar found for NMDA EPSCs. "Did not affect" is not "no reduction".
 * The anoxic-depolarisation current is driven by massive glutamate release by reversed uptake in ischaemia, not by evoked vesicular release; a presynaptic release effect (Tovar) would not appear in it, and a modest NMDAR block would be hard to see against ischaemic glutamate concentrations. So Madry neither contradicts Tovar's culture result (M09's wording "which does not predict the culture result" is too strong) nor excludes an NMDAR effect. BH3's "points against a strong direct NMDAR block at 100 uM in that setting" is correct only with those qualifiers.
 Depth: Fig 1 viewed, Figs 2-4 not; my own depth `partial_fulltext_read`.

(c) Chepkova 2008 (18555495) was never read by the producer or by me (no PMC). Every statement that CBX blocks NMDAR rests on that title and on the WWOX paper's own sentence.

### B2. Brilliant blue FCF / Panx1 (23589583). SUPPORTED with two wording points

Verified: mouse Panx1 in Xenopus oocytes (two-electrode clamp, -60 mV holding, +60 mV pulses, OR2 solution; "rapid and fully reversible within minutes"), IC50 0.27 uM, "plateau at 75% inhibition" in the text, Fig 2B read by me at about 0, 22, 66, 80 and 85 percent at 0.01, 0.1, 1, 10, 100 uM (n = 4-6, SD bars); no block of BzATP-induced human P2X7 current at 100 uM; 100 uM did not change Cx46 or Cx32E143 hemichannel currents (n = 4); Fig 6 (viewed): wild-type inhibition probenecid about 81, BB FCF about 86, Fast Green about 92, carbenoxolone about 88 percent, carbenoxolone concentration not given in legend or text. Points:
 * "Plateau 75 to 85 percent" mixes the text (75) and the figure (80-85); say so.
 * probes.tsv says BB FCF block "is lost in four of five" alanine mutants; the text says "attenuated"; in S240A it is still about 27 percent and in I247A about 51 percent. Say "attenuated in four of five".
 * Nothing in the source tests BB FCF in slices, neurons, Na+ channels or NMDAR/AMPAR; the 10 uM used in the WWOX paper is about 37 times the oocyte IC50 and the producer rightly asks for an engagement readout.
 * The Wang paper explicitly tested hemichannels, not two-cell gap junctions; EB22 note says so.

### B3. TCN-201 (22553026). SUPPORTED; three items to add

Verified: oocytes (23 C, -40 mV) and HEK293 (23 C, -60 mV); IC50 320 nM at 3 uM glycine, 100 nM at 1 uM, 1.6 uM at 30 uM (16-fold), no detectable inhibition by 10 uM at 300 uM glycine; >1000-fold GluN2A selectivity at 3 uM glycine; 10 uM did not affect GluA1 or GluK2 (**"data not shown"**); Kb 45 nM, alpha 0.0025; solubility limit "estimated to be 18 uM". Corrections:
 * The 18 uM solubility estimate is in the Results paragraph on Fig 9, not in Methods (EB25 note says Methods).
 * Table 1 gives **maximum inhibition 81 +/- 1 percent at 3 uM glycine and 73 +/- 2 percent at 30 uM glycine**, while the text says TCN-201 "completely inhibited" GluN1/GluN2A at 3 uM glycine. The source is internally inconsistent; incomplete maximal inhibition is a limit for M06 (a plateau below abolition by TCN-201 would not by itself signal "another receptor").
 * No slice, native receptor or triheteromer datum in the source (producer says so).

### B4. Radiprodil (40994429). SUPPORTED, with two additions

Verified (main text and Tables 1 and 3): oocytes at room temperature, 100 uM glutamate and 30 uM glycine; human GluN1-1a/GluN2B IC50 0.029 uM (91 percent max), rat 0.026, GluN1-1b 0.13; triheteromer GluN2A/GluN2B IC50 0.091 uM, **45 +/- 10 percent** max; 2B/2C 64, 2B/2D 65 percent; 4.7 +/- 1.2 percent recovery after 3 minutes ("up to an hour to recover fully", authors); kinetic KD 0.175 uM; slices: horizontal 280-300 um, P17-P22, +40 mV, 30-32 C, 10 uM NBQX and 10 uM gabazine, 3 uM radiprodil reduced the evoked NMDAR EPSC from 33 to 16 pA (WT, n = 6) and 48 to 25 pA (S810R, n = 9); in vivo 3 mg/kg i.p., GTCS latency 207 +/- 23 vs 458 +/- 90 s, 16 of 26 treated mice seizing (latency computed only in those that seized); memantine 10 uM in the text and 30 uM in the Fig 5 legend. Additions:
 * **Mg2+ inside the source disagrees with itself.** The slice Methods list aCSF with 1.5 mM MgSO4; the Fig 4B and Fig 5 legends say the NMDAR EPSCs were recorded in "reduced extracellular Mg2+ (0.2 mM)". Relevant because the package's own premise is that Mg2+ is the unstated variable; the producer's description gives +40 mV only.
 * "No effect on GluN2A, GluN2C or GluN2D diheteromers" is a sentence that cites **Supplementary Fig 1B, which neither the producer nor I could read**; it is carried text. Say so in probes.tsv and EB26.
 * The slice recording is hippocampal CA1 (not cortex), the adult in vivo model is a GluN2B gain-of-function mouse, and the 3 uM bath concentration is about 100 times the oocyte IC50 (producer says this). About 50 percent EPSC reduction at 100 times IC50 is the empirical ceiling the source gives in a slice.

### B5. Perampanel (25229608). PARTLY; one substantive correction

Verified: abstract wording ("selective negative allosteric AMPA receptor antagonist of high-affinity and slow blocking kinetics"); cultured rat hippocampal neurons (E18), 7-25 DIV, -60 mV, temperature not stated; AMPA and kainate recordings in 500 nM MK-801; NMDA recordings in 10 uM NBQX, 3 uM glycine, 0.2 mM Ca2+; 30 uM did not change 10 or 100 uM NMDA currents (n = 6); Table 1 IC50 0.4/0.8/0.9 (peak) and 0.4/0.9/1.2 (late) uM, kainate 0.58/0.51/0.58 uM; k_on 1.51 +/- 0.10 e5 per M per s, k_off 0.58 per s (mean tau_off-derived 0.68 per s), KD 3.9 uM; onset tau about 1.2 s at 3 uM, recovery tau 3.3 +/- 1.5 s; funding "in part" by Eisai, authors not employees (the producer says "Eisai-funded", acceptable but strictly "in part").
 * **The potency "text versus figure" discrepancy is probably an artefact of reading the raster axis.** In Fig 1D (viewed and zoomed) the long tick marks of the log axis are 164 px apart, the data points sit at half-decade spacing (82 px) on those ticks, and the printed numerals 0.01, 0.1, 1, 10, 100 are spaced only 132 px apart, i.e. they are not under the ticks. Reading the ticks as decades (the data then span 0.03 to 10 uM, consistent with sample traces at 0.3, 1, 3, 10 uM in Fig 1A and with the text statement that 1 uM "produced near half-maximal inhibition") puts the 50 percent crossing at about 0.45 uM for 10 uM AMPA and about 1 uM for 100 uM AMPA, which matches Table 1 (0.4 and 0.9). Reading by the printed numerals gives the producer's 1 and 3 to 5 uM. INFERENZA, because it depends on which of tick or numeral is right; the tick geometry is self-consistent with the text and the numerals are not. So FB10, EB34 ("unresolved"), the probes row and BH1 ("curve-read about 1 to 5 uM, unresolved") should say: "figure axis labels are offset from the tick marks in the raster; tick-based reading agrees with Table 1; the kinetic KD (3.9 uM) is a separate, higher number the paper does not reconcile with its IC50s".
 * The AMPA/kainate protocol contains MK-801 and the NMDA protocol contains NBQX, so "no NMDA effect" and "no AMPA effect on NMDA" were each tested under an agonist-specific cocktail; fine, but it means the result is for 30 uM perampanel on 10 and 100 uM NMDA in 0.2 mM Ca2+, not on a synaptic NMDAR EPSC.
 * Kainate-evoked current in these neurons is mostly AMPAR (the paper says so); a kainate-receptor contribution is not separated, as the producer says.

### B6. Mefloquine (15297615), d-APV, NBQX, GYKI, memantine, probenecid

 * Mefloquine. SUPPORTED at abstract depth; the abstract quotes EB38/EB39 are verbatim; it also states that evoked EPSPs/IPSPs were unchanged at 25 uM and intrinsic properties "mostly unaffected", which the producer's row reports in part. The coupling readout was in interneurons.
 * d-APV, NBQX, GYKI: correctly labelled as use-only or carried; no mechanism source was read for any of them (and I did not read one either).
 * Probenecid: Fig 6 only, concentration not stated; as the producer says.

### Which claims go beyond the source (summary)

1. Perampanel text-vs-figure potency conflict (B5).
2. Madry as counter-evidence to NMDAR block, and the P20 wording (B1b).
3. BH3 "IPSCs recovering incompletely" (B1a) and "genetic connexin-36 deletion is the standard" (B1a).
4. "d-APV leaves 40 percent of the delayed response" as evidence of incomplete block (A5).
5. BB FCF "lost in four of five mutants" (B2).
6. "Radiprodil ... no effect on GluN2A/2C/2D" presented without the note that it rests on an unread supplement (B4).
7. "TCN-201 inhibits completely" is the source's text; Table 1 says 73-81 percent (B3).

---

## C. Logic of the matrix and BH1-BH3

### C1. Arm by arm

| Arm | Verdict | Reasoning |
|---|---|---|
| M01 | SUPPORTED | Prerequisite; correct that the bath Mg2+, K+ and slice thickness (400-500 um) are unreported for recording. Add temperature and perfusion rate as to be measured |
| M02 | SUPPORTED | Time-matched vehicle is the right missing control; Fig 3D normalisation and the unpaired t-test (A4e) make it more important than the producer says |
| M03 | SUPPORTED | Correct that all seven predict abolition and that the arm cannot separate hypotheses (d-APV abolition cannot separate AMPA-led drive, GluN2B or GluN2A drive, general loss, or depolarisation plus Mg2+ relief). The "delayed response reduced, partly" cell should carry the floor caveat (A5) |
| M04 | PARTLY | Sound as the reference curve. "NMDAR EPSC at stated holding potential and Mg2+" is the right x-axis but it is measured on an isolated EPSC (AMPA and GABA-A blocked); GABA-A block in a slice that bursts may itself change the network, so it should be done in separate slices or cells, not by pre-treating the burst slices |
| M05 | PARTLY | Reasoned correctly that a triheteromer-rich cortex gives a plateau resembling H3. But a plateau below d-APV abolition cannot separate a GluN2A-diheteromer share from a GluN2A/2B triheteromer share (45 percent ceiling), which the cell states for H3 but the "separates H2 from H3" sentence slightly overstates. Radiprodil's slice behaviour is a CA1 P17-P22 result at 0.2 or 1.5 mM Mg2+ (B4) |
| M06 | PARTLY | Internal control (low vs surmounting glycine) is well reasoned. Add: Table 1 maximum inhibition 73-81 percent; the 18 uM solubility ceiling means the "surmounting" level must be reachable with a measured co-agonist; glycine alone as control is correct |
| M07 | PARTLY | The H2/H3 cell says "bursts persist, possibly changed in shape; abolished when d-APV is added". That is not entailed. NMDAR-regenerative bursts in a slice with 1.3 mM Mg2+ and RMP about -74 mV usually need AMPAR-mediated depolarisation to relieve the block (the producer's own AB05/H7 logic), so AMPA block abolishing bursts is expected under H2 as well. Only persistence under verified block is informative, as the BH1 weakening result already says. The matrix cell should read "persist or abolished; abolition does not separate H1 from H2" |
| M08 | PARTLY | See C2 |
| M09 | PARTLY | Reasoned correctly that H5 and H6 predict the same fall and only EPSC, spike width, Rin and coupling readouts separate them. Madry is mis-weighted (B1b). The prediction "EPSCs reduced about 63/69 percent" is a culture transfer, labelled as such |
| M10 | SUPPORTED | Right control for H5; suffers from the same metric problem as M08 (equal percent EPSC reduction of which EPSC) |
| M11 | SUPPORTED | Engagement readout requirement is correct; BB FCF 10 uM engagement in a 400-500 um slice is unmeasured in every source |
| M12 | SUPPORTED | Correctly held (abstract_only) |
| M13 | SUPPORTED | Correct that a genetic route is the standard; costly; conditional |
| M14 | SUPPORTED | The WT-in-low-Mg2+ positive control is the right way to bound H7. Add K+ at 2.5 mM because 3.5 mM is above the usual value |
| M15 | SUPPORTED | Genotype and gene-dose comparator; HT amplitude differs from WT by KS (A4g), so HT is not a clean "intermediate" control |

### C2. M08, the matched-effect arm

M08 separates "general loss of drive" from "receptor specificity" only under one metric. INFERENZA. Percent of total evoked charge removed (fast plus delayed) is dominated by the slow NMDAR component, whereas recruitment of a network burst depends on peak depolarisation and recurrent gain, not on charge; an AMPAR-antagonist curve and a d-APV curve can coincide or be ordered depending on whether the common axis is charge, peak current, fEPSP slope or recruited cells. A coincident result under one metric does not prove generality, and a left- or right-shifted result under one metric does not prove receptor specificity. What M08 fails to separate: Mg2+/voltage coupling (an AMPA block removes the depolarisation that relieves NMDAR block), recurrent-gain nonlinearity, and presynaptic from postsynaptic loss. What the arm needs to be decisive: a second receptor-agnostic manipulation that lowers both EPSCs proportionally (for example reduced release probability by Ca2+/Mg2+ ratio or an adenosine A1 agonist) read on the same axis, and at least two metrics. As written, "provided the common readout is defined before the experiment" is a necessary condition, not a sufficient one.

### C3. Arms or hypotheses a pharmacologist would expect and the package lacks

1. **GABA-A / disinhibition.** The knockout sIPSC amplitude is halved (57.3 to 27.5 pA) and AB06 is listed as an alternative, but there is no H-column, no arm and no experiment (BE0-BE4) for it. A bicuculline/gabazine or positive-allosteric-modulator arm in the burst slices and an evoked IPSC measurement are the natural controls. Tovar also reports that CBX reduces IPSCs, which could raise network activity.
2. **Kainate receptors.** Perampanel, NBQX and GYKI all act on AMPA and kainate receptors; no hypothesis or arm separates a GluK contribution (an isolated kainate arm would need a selective tool).
3. **Group I mGluR and other slow modulators** (Wwox S-KO slices were not tested with any); lower priority, but absent without a stated reason.
4. **Intrinsic excitability** (RMP +5.6 mV, Rin +39 percent, sag, rebound, AP amplitude) is the strongest cell-level knockout phenotype and enters only as H7/AB05; the HCN question sits in another package (`hcn_20261107`), which should be referenced.
5. **TTX/AP dependence of the burst** and heterozygote pharmacology (HT burst slices 4 of 23, no drug tested).

### C4. Increased current as harmful; drug response as proof of target defect

DATO. I found no step that treats the larger mEPSC amplitude or the larger evoked delayed response as harmful in itself, and BH1 states in words that a drug response is not proof of a defect in its target. BH2's step 5 ("a pharmacological question can then be posed at the receptor-composition level") is a design statement, not a benefit claim. No violation.

### C5. Is the drug question sharper than "another antagonist list"?

INFERENZA. Yes in design: the package replaces "which antagonist" by "does the burst fall along the same curve at equal percent removed, with the condition (bath Mg2+, K+) measured and the order of application fixed", with explicit kill conditions (bursts surviving a verified AMPA block; NAM curve coincident with d-APV). The sharpness is limited in three ways: it is a measurement plan, not yet a compound question; M08's axis is metric-dependent (C2); GABA-A and kainate are missing (C3). It does not hold anything back for a literature substitute, which is correct.

### C6. The three hypotheses

| Hyp | Verdict | Reason |
|---|---|---|
| BH1 (AMPAR dependence) | PARTLY | Right form: IPOTESI, with survival under verified block as the weakening result. Fix the perampanel potency sentence (B5), the H2 prediction cell (M07), and note that kainate receptors are not separated. Step 3 ("kinetic signature of an AMPA-type quantum") remains INFERENZA, correctly labelled |
| BH2 (NMDAR composition / total gain) | PARTLY | Correct that no WWOX subunit or glycine or Mg2+ datum exists. Step 1's "not to zero" is weakened by the floor (A5). The radiprodil mechanism is verified, but its slice precedent is hippocampal CA1 at P17-P22 with Mg2+ stated two ways (B4). M05 cannot isolate GluN2B-diheteromer share from triheteromer share |
| BH3 (carbenoxolone attribution) | PARTLY, near SUPPORTED as a withdrawal of the gap-junction attribution | Direction-only use of the CBX numbers is correct and is reinforced by A4(e). Fix IPSC recovery, P20/La3+, the strength of the Madry counter, and the "connexin-36" standard wording |

No hypothesis rests on a disputed number except through the CBX magnitude in BH3, which the producer already excludes; BH2 rests on a figure reading (0.46 vs 0.12, 0.4, 1.3) that is accurate as a reading but over-interpreted (A5).

---

## D. New measurements

SUPPORTED that every datum the hypotheses need and no source supplies is flagged as new (recording Mg2+/K+, isolated NMDAR EPSC, NAM-sensitive fraction, slice co-agonist level, verified fast-EPSC block, EPSC/spike/Rin/coupling under CBX, Panx1 engagement, own baseline frequency). Missed or understated, all of them new measurements and not transfers:

1. A noise-floor control for the delayed-response amplitude (WT reads about 0.115 mV at the same latency).
2. Within-slice paired normalisation (baseline per slice) instead of pooled-baseline comparisons.
3. AMPAR/NMDAR ratio and AMPA EPSC kinetics in the KO cells (the mEPSC amplitude shift is an AMPA inference only); evoked IPSC and E/I ratio.
4. Slice equilibration time for each drug in 400-500 um slices at 35 C (Tovar: "tens of minutes" for CBX; perampanel and radiprodil kinetics are culture/oocyte at room temperature).
5. Temperature: sources used room temperature (Tovar, Banke oocytes, Hansen), 30-32 C (Banke slices), 33 C (Madry), unstated (Chen); the WWOX preparation is 35 C.
6. d-APV concentration for the S3 panel and a titration (M04 covers the titration).
7. Heterozygote drug sensitivity (4 of 23 bursting slices).

---

## E. Evidence rows and absence claims

### E1. Quotes

Checked 39 rows. Verbatim at the cited source and 25 words or fewer: 37 full-text rows (EB01-EB37, by script against the PMC text, the docx text and the PMC page text) and the two abstract rows (EB38, EB39, against the PubMed abstract). Defective: **2**.
 * EB15: the "quote" is the table row label "Frequency (bursts/min)"; it carries none of the proposition (the numbers are in the note). Replace with a statement that carries a number, for instance a Table S1 cell with its column.
 * EB25: the note puts the 18 uM solubility in "Methods"; it is in Results, the paragraph on Fig 9.
 Borderline: EB08 is exactly 25 words; EB26's proposition rests on a sentence that cites an unread supplement (B4); EB34's note repeats the B5 figure misreading.

### E2. Absence claims and perimeter

 * "No AMPA-antagonist experiment in 34634460 and its supplement": SUPPORTED within the perimeter the producer states (two text files, the strings listed; images viewed). I re-ran the text search and got the same: one whole-word AMPA hit (the mEPSC decay sentence), none for the antagonist and receptor-subunit strings; recording Mg2+ not stated. Residual risk: a drug name inside an image, which I did not see in any of the ten images.
 * "No WWOX-connexin/pannexin literature": **perimeter not recorded**. `queries.tsv` has no query for it (QB17 is the local text search; QB03-QB06 are carbenoxolone queries). I re-ran PubMed on 2026-11-08: `(WWOX OR Wwox) AND (connexin OR pannexin OR "gap junction" OR carbenoxolone)` returned 1 hit, the WWOX paper itself; `(WWOX OR Wwox) AND (AMPA OR NBQX OR perampanel OR GYKI OR "AMPA receptor")` returned 0; `(WWOX OR Wwox) AND (NMDA OR GluN2B OR ifenprodil OR "NMDA receptor")` returned 1, again 34634460. So the claims hold in PubMed; the producer should add these three strings, the database and the date to `queries.tsv`. Preprint servers and Europe PMC full-text were not searched by anyone.
 * "No primary papers read for NBQX/GYKI/felbamate/ifenprodil/Ro 25-6981": true as a statement about what was read. QB12's three zero-hit queries are long natural-language strings that PubMed ANDs together; a short query `NBQX[Title] AND (AMPA OR kainate)` returns 110 records, so literature exists and the real gap is "not read / not open access" (QB18 reports no PMCID for four candidate AMPA-antagonist mechanism papers). The phrase "open routes absent" in BH1 is acceptable; the zero-hit result should not be quoted as evidence of absence. No felbamate, ifenprodil or Ro 25-6981 query is recorded at all.

---

## F. Receipts

Spot-checked all eight at metadata level and five in detail (34634460, 19535488, 25229608, plus fingerprint checks on 40994429, 23589583, 22553026, 20940167).

 * Source fingerprints: the SHA-256 of the bucket text I downloaded equals the receipt fingerprint for 34634460 (135eab...), 25229608 (ab9bee...), 40994429 (856e30...), 23589583 (e673c5...), 22553026 (1c1457...), 20940167 (95a415...), and my PMC-page-to-text conversion of 19535488 reproduced cd7bfe... exactly. PASS. 15297615 has no fingerprint (abstract only), correct.
 * Section lists: PASS for 34634460 (figures and supplementary "read", references "not_read"), 25229608 (figures "captions_only" although the evidence_basis says Fig 1 and Fig 5 were viewed; the coverage field is the conservative one), 19535488 (figures `captions_only`).
 * Quoted locators: 19535488 and 25229608 verbatim. 34634460's last locator ("tetrodotoxin (TTX), d-APV, carbenoxolone (CBX) and brilliant blue FCF (BB-FCF)") is **not verbatim**: the source reads "tetrodotoxin (TTX), 2-amino-5-phosphonopentanoic acid (d-APV), carbenoxolone (CBX) and brilliant blue FCF (BB-FCF)"; an elision was made without an ellipsis.
 * Narrative defect: the 19535488 receipt says "the five figure legends"; the article has four figures.
 * `prior_receipt` for 34634460 (FTR-20261019-34634460-01) and reread_reason `new_question_outside_prior_coverage` are consistent with the ledger lookup the producer reports; I did not re-query the ledger.

---

## Verdicts, probe by probe

| Probe | Mechanism claim | Stated limit | Verdict |
|---|---|---|---|
| Carbenoxolone | SUPPORTED (non-selective; EPSC irreversibly reduced, IPSC reversible; AP broadening, Rin; Panx1 block in oocytes) | Partly: NMDAR block via Chepkova unread; the Madry counterweight overstated | PARTLY (wording corrections B1) |
| Brilliant blue FCF | SUPPORTED | engagement and slice penetration unknown, stated | SUPPORTED with B2 wording |
| TCN-201 | SUPPORTED | glycine dependence and solubility stated; max inhibition 73-81 percent and "data not shown" for GluA1/GluK2 to be added | SUPPORTED with B3 additions |
| Radiprodil | SUPPORTED | 45 percent triheteromer ceiling, 4.7 percent recovery, memantine 10/30 uM stated; Mg2+ 0.2 vs 1.5 mM and unread Suppl Fig 1B to be added | SUPPORTED with B4 additions |
| Perampanel | SUPPORTED (noncompetitive-negative-allosteric, no NMDA effect at 30 uM, kinetics) | potency discrepancy claim not substantiated (B5) | PARTLY |
| Mefloquine | abstract level only | stated | SUPPORTED at abstract depth |
| d-APV, NBQX, GYKI, memantine, probenecid | use-only or carried | stated | SUPPORTED as labelled; UNVERIFIABLE as mechanisms (no primary read) |

## Corrections the producer must make

| File | Row / location | Correction |
|---|---|---|
| `output/probes.tsv` | Perampanel, `measured_in` and `specific_limit` | Replace "curves ... about 1 to 5 uM, higher than the text" by the tick/label-offset finding and the tick-based reading (about 0.45 and 1 uM), INFERENZA |
| `output/figure_notes.tsv` | FB10 | Same; drop "not reconciled by the paper" for IC50; keep KD 3.9 uM as the separate, higher number |
| `output/evidence.tsv` | EB34 note | Same |
| `output/hypotheses.tsv` | BH1 `compound_or_probe` | Same sentence ("text IC50 0.4 to 1.2 uM against curve-read about 1 to 5 uM, unresolved") |
| `output/probes.tsv`, `output/evidence.tsv` EB35, `output/hypotheses.tsv` BH3 | Carbenoxolone rows | P20 tested CBX plus La3+, not CBX alone; add "mean 22 percent lower, n 6 vs 14, ischaemic reversed-uptake glutamate, not evoked release" |
| `output/hypotheses.tsv` | BH3 chain step 3 | "reduced IPSCs, recovering incompletely" to "reduced IPSCs (fully reversible) and EPSCs (recovering incompletely)" |
| `output/hypotheses.tsv` | BH3 `compound_or_probe` | "genetic connexin-36 deletion is the standard named by the Tovar authors" to "genetic ablation or dominant-negative approaches" |
| `output/hypotheses.tsv` | BH2 chain step 1; `output/alternatives.tsv` AB04 "fits"; `output/observations.tsv` OB09 caveat; `output/prediction_matrix.tsv` M03 | Add: the amplitude metric reads about 0.115 mV in WT, so a normalised 0.4 is near the floor (INFERENZA); do not use 0.4 as evidence of an incomplete block |
| `output/prediction_matrix.tsv` | M07, H2 and H3 cells | "Bursts persist" is not entailed; AMPA block can abolish an NMDAR-regenerative burst through loss of Mg2+ relief; abolition does not separate H1 from H2 |
| `output/prediction_matrix.tsv` | M08 and M10 | State the metric dependence; require a second receptor-agnostic release-reducing manipulation and two metrics |
| `output/prediction_matrix.tsv`, `output/hypotheses.tsv`, `output/experiments.tsv` | whole package | Add a GABA-A arm (and the kainate and E/I measurement) or state why it is out of scope; reference `hcn_20261107` for intrinsic excitability |
| `output/observations.tsv` | OB08, OB02/OB05/OB06, OB17 | Add the disagreements A4(a)-(c), (e), (g): S3 n animals 6 vs 3; S1 burst counts 119/126/102+41; S-CTL 18 vs 31 cells; unpaired pooled-baseline normalisation; HT vs WT amplitude KS p 1.98e-4 |
| `output/observations.tsv` | OB02 | Add that 2.29 per min equals 60/26.2 s and that Fig 1D appears to favour the larger interval (A4d, INFERENZA) |
| `output/probes.tsv` | TCN-201 | Add max inhibition 81 and 73 percent (Table 1) vs "completely inhibited" in the text; GluA1/GluK2 "data not shown"; 18 uM in Results not Methods |
| `output/evidence.tsv` | EB25 | Locator "Results, Fig 9 paragraph" |
| `output/probes.tsv`, `output/evidence.tsv` EB26 | Radiprodil | Selectivity sentence cites Supplementary Fig 1B, unread; slice legends say 0.2 mM Mg2+, Methods say 1.5 mM |
| `output/probes.tsv` | BB FCF | "attenuated in four of five mutants", plateau "75 (text) to 85 (figure)" |
| `output/evidence.tsv` | EB15 | Replace the row-label quote by a quote that carries a proposition |
| `output/queries.tsv` | new rows | Add the three WWOX searches and date; mark QB12 zero hits as over-specific, not as absence; no felbamate, ifenprodil or Ro 25-6981 query was recorded |
| `output/figure_notes.tsv` | FB07, FB08 | Docx image order: S2 = image2, S3 = image3; S3 TIFF is 1431 px wide |
| `output/receipts/FTR-20261108-34634460-61.json` | evidence_basis, last locator | Restore the "2-amino-5-phosphonopentanoic acid" elision or add an ellipsis |
| `output/receipts/FTR-20261108-19535488-61.json` | evidence_basis | "five figure legends" to "four" |

## What changes in a hypothesis or the matrix

 * BH1: the perampanel potency caveat disappears; H2's M07 prediction changes from "bursts persist" to "persist or abolished"; kainate receptors enter as an unseparated alternative.
 * BH2: the 0.4 residual stops being evidence of an incomplete NMDAR dependence of the delayed response; M05 cannot split diheteromer from triheteromer share; Mg2+ for the radiprodil slice precedent is ambiguous in the source.
 * BH3: Madry and Tovar are both kept, with lower weight on Madry; IPSC recovery fixed; the A4(e) between-group normalisation strengthens the direction-only rule.
 * Matrix: M08 and M10 need a second metric and a release-reducing control; a GABA-A column and arm should be added or explicitly excluded.

## Addendum, written after the verdicts above (README, engine_consumption and consumer_delta read afterwards)

No verdict above was changed by reading these three files. They propagate four items I flagged, which should be corrected before any consumer edit:

 * `consumer_delta.md` row 2 (delayed response "reduced to about 0.4 of baseline") needs the measurement-floor caveat (A5); row 3's disagreement list should add A4(a)-(c), (e) (S3 n animals, S1 burst counts, pooled-baseline normalisation); row 4 repeats "rat CA1 slices (P12, P20) 100 uM did not change the glutamate-driven ischaemic inward current" (P20 was CBX plus La3+; B1b) and "incomplete recovery" without separating EPSC (incomplete) from IPSC (full); row 7 repeats the perampanel "text 0.4 to 1.2 uM against curve-read about 1 to 5 uM" (B5).
 * `README.md` line 2 (0.4, "not abolition"), line 5 (P12/P20) and "What changed" bullet 2 ("a text-versus-figure potency disagreement") carry the same items.
 * `engine_consumption.md` format limits are accurate as far as I could check them against the producer's own tables; I did not open the generator, validators or `needs.json` and make no claim about them. Its list of text/legend/table disagreements is the producer's five; add mine if the `limits` text is extended.

## What I could not reach

 * Full text of 15297615 (bot-check page, not retried); the Chepkova 2008 NMDAR paper (18555495, no PMC); no primary mechanism paper for NBQX, GYKI 52466, felbamate, ifenprodil or Ro 25-6981 (none read by anyone).
 * Figures of 19535488, 22553026 and 40994429 (not in the bucket), and Supplementary Fig 1B of 40994429.
 * Madry Figs 2-4; Wang Figs 1, 3, 4, 5, 7; Chen Figs 2-5 (not viewed).
 * Quantitative reading of Fig 1D beyond the raster resolution (A4d), and of the figure axis in perampanel Fig 1D beyond the tick-versus-numeral test (B5).
 * The ledger itself (I did not re-run `fulltext_receipts.py status`), the registries, and the three files I was told not to read before the verdicts.

---

## Recheck

Second look after the producer's corrections (verifier `vf-an`, same constraints; I re-read the revised `hypotheses.tsv`, `prediction_matrix.tsv`, `probes.tsv`, `observations.tsv`, `alternatives.tsv`, `figure_notes.tsv`, `experiments.tsv`, `evidence.tsv`, the two `-62` receipts, `README.md`, `engine_consumption.md` and `consumer_delta.md`; I re-fetched nothing new from the sources except the Chen Fig 1D crop below and a re-run of the verbatim test on all 40 evidence rows). All TSVs have equal column counts per row.

### (1) Were my ten corrections applied as meant, and was anything overstated?

| Item | Verdict |
|---|---|
| Perampanel axis reading | APPLIED, kept as INFERENZA. I re-viewed Chen Fig 1D at a new crop and measured the tick pattern directly. The long tick marks of the log axis are about 153 px apart in a 2.8x crop and the printed numerals 0.01, 0.1, 1, 10, 100 only about 125 px apart; the offset grows from left to right (numeral "0.01" is nearly under its tick, numeral "100" sits well left of the last long tick). The last data point lies on the fourth long tick, immediately beside the numeral "100" when read by numerals, which would put it at roughly 80 to 100 uM; Methods give 0.01 to 30 uM, and the sample traces and the text statement that 1 uM is near half-maximal fit the tick reading. Tick reading therefore gives 50 percent crossings of about 0.45 and 1 uM, matching Table 1. Still not proof (a raster, two competing scales), so INFERENZA is right. The producer's added argument (numeral-read last point above the Methods maximum) is mine and is sound |
| Madry (P20 La3+, 22 percent, reversed-uptake current) | APPLIED in probes, EB35, EB41, BH3, M09, README and delta row 4; no new overstatement ("neither contradicts nor excludes") |
| IPSC fully reversible vs EPSC incomplete | APPLIED (BH3 step 3, probes, EB40, README, delta row 4) |
| Genetic standard wording | APPLIED ("genetic ablation or dominant-negative approaches") |
| d-APV residual and floor | APPLIED; see (2) |
| M07 | APPLIED as meant: H2/H3 cell now reads persist or abolished, abolition expected under H2 through loss of Mg2+ relief, only persistence under a verified block informative; the note adds that AMPA/kainate tools do not separate a kainate contribution (M17). No overstatement |
| M08 / M10 | APPLIED: two metrics plus a receptor-agnostic release-reducing control, "necessary but not sufficient", metric dependence, Mg2+ relief and pre/post-synaptic non-separation stated; BE1 outcomes match. **One inconsistency left:** the `order_application_washout` cell of M08 still says "the common x-axis is percent of evoked charge removed (fast plus delayed)", i.e. a single metric. Change to "one x-axis per metric (evoked charge; peak current or fEPSP slope; recruited-cell fraction)" |
| M16 | NEW, mostly sound (tools use-only, no mechanism paper, AB06 not a matrix column, same-as-H4 note). **Overstatement to fix:** the cell placed under the H7 column (and the BE5 outcome text) says GABA-A positive modulation abolishing bursts "would show that restored inhibition is sufficient and that d-APV dependence is a permissive necessity". Abolition by a GABA-A potentiator is also predicted by H4 (any large cut in drive; the same row's note admits this), and it says nothing about whether the d-APV dependence is permissive. Reword to: "abolition is compatible with AB06 and with H4 and is separated only by the evoked-IPSC and E/I measurements; it does not by itself show that NMDAR dependence is permissive". Also the cell sits in the H7 (network state or recording artefact) column although it tests AB06; say so in the column header cell or move it to the note column |
| M17, M18 | SUPPORTED. M17 states honestly that no kainate-selective tool or mechanism paper exists in the package; M18 is a pointer only and claims no separation |
| New alternatives AB14, AB15; experiment BE5 | SUPPORTED, with the BE5 outcome-wording fix above |
| Other applied items (extra disagreements OB11, OB17, OB18; TCN-201 maximum inhibition, GluA1/GluK2 "data not shown", 18 uM locator; radiprodil Suppl Fig 1B and the Mg2+ 1.5 vs 0.2 mM; BB FCF "attenuated"; EB15 replaced by a cell that carries numbers; EB25/EB26/EB34/EB35 notes; EB40-EB42 added; FB07 now "image3" and 1431 px; three WWOX perimeter strings and the NBQX title query logged) | APPLIED. All 40 evidence quotes are verbatim in the sources and 25 words or fewer; the two abstract rows were checked before |

Minor residue, not an error: the boilerplate "NEW MEASUREMENTS ... a floor control for the delayed-response metric" is repeated verbatim in BH3's `what_would_change_the_decision` although BH3 does not use that metric; harmless but should be dropped from BH3. BH1's weakening result introduces "a verified fast-EPSC block of about 90 percent or more" as the criterion; that figure is a design choice with no source. Label it "pre-specified before the experiment, no source value" or give the measured block as a variable.

### (2) The "about 20 percent" restatement

DATO for the inputs, INFERENZA for the floor assumption. 0.4 x 0.46 mV = 0.184 mV; (0.184 - 0.115) / (0.46 - 0.115) = 0.069 / 0.345 = 0.20. That is what I meant. It is applied consistently in OB09 (caveat), AB04, BH2 step 1, M03 (both cells), FB07, the d-APV probe row, README line 2, delta row 2 and BE0. Two cautions to add once in OB09: (a) it is a point estimate from a raster; with the d-APV error bar of about +/-0.1 on the normalised value the range is roughly 7 to 33 percent, still well below 40 and still not "incomplete block"; (b) the floor is assumed equal in KO and WT. Neither changes the conclusion.

### (3) Replacement receipts

PASS. `FTR-20261108-34634460-62` and `-19535488-62`: source fingerprints equal the SHA-256 I computed from the bucket text (135eab3d...) and from my PMC-page conversion (cd7bfecaf...); `prior_receipt` points to the `-61` receipt, `reread_reason` is `receipt_correction`, `analysis_at` precedes `event_at`; the WWOX locator now reads "tetrodotoxin (TTX), 2-amino-5-phosphonopentanoic acid (d-APV), carbenoxolone (CBX) and brilliant blue FCF (BB-FCF)", which is a verbatim substring of Methods 5.4; the Tovar receipt now says four figure legends (the article has Figs 1 to 4). Coverage fields unchanged and correct. Note for the integrator: both `-61` and `-62` carry the same study, and `-62` names the staged `-61` as prior, so they must be recorded in that order (or `-62` alone), not in parallel. I did not run the staged-receipt checker (out of scope here).

### (4) README, engine_consumption, consumer_delta

No number or claim in these three files contradicts the corrected tables. Specific checks passed: README lines 2, 3, 5, 6, 7 and the delta rows 2, 4, 5, 7 reproduce the corrected wording (floor 20 percent, P12 alone / P20 with La3+, IPSC reversible, perampanel withdrawn as probable misread, Mg2+ 1.5 vs 0.2 mM, 73-81 percent, 110 PubMed records); the format limits in `engine_consumption.md` are unchanged and I make no claim about the generator or validators. The NEW MEASUREMENTS list (README line 10; engine_consumption items 1 to 10) is complete for the arms and is not replaced by transfer: every culture, oocyte or CA1 number appears with its preparation and is labelled transfer. Items from my section D that are not in the list and should be added or declared out of scope: (i) AMPAR/NMDAR ratio and AMPA EPSC kinetics in the knockout cells (the mEPSC amplitude shift is an AMPA inference only); (ii) slice equilibration time per drug at 400-500 um and 35 C, and the temperature mismatch with the source preparations (room temperature, 30-32 C, 33 C); (iii) TTX/action-potential dependence of the bursts and heterozygote drug sensitivity (M15 covers heterozygote comparators but not as a stated new measurement).

### (5) Are BH1 to BH3 stated at the strength the evidence allows?

Yes, with three small adjustments. All three are labelled IPOTESI, exploratory, premise not established, with "PARTLY" and what each rests on. BH1: drop or qualify the "90 percent" criterion (see above). BH2: appropriate; step 4 is IPOTESI and step 1 no longer uses the residual. BH3: the status text ("close to a withdrawal of the gap-junction attribution; no datum supports the gap-junction half") is accurate as a statement about the sources read; "no datum supports" should read "no datum in the sources read separates it from the off-target explanations", because the WWOX carbenoxolone fall is not inconsistent with a coupling contribution, it is merely unattributable. The explicit M16-not-required statement in BH3's experiment column is acceptable but should add that Tovar's IPSC reduction by carbenoxolone could oppose a burst fall, which is why M16 is kept in BE5.

### Further corrections requested after the recheck

1. `output/prediction_matrix.tsv` M08, column `order_application_washout`: replace "the common x-axis is percent of evoked charge removed (fast plus delayed)" by one x-axis per metric.
2. `output/prediction_matrix.tsv` M16 (H7 cell) and `output/experiments.tsv` BE5 (`what_each_outcome_would_mean`): remove "restored inhibition is sufficient" and "d-APV dependence is permissive"; state compatibility with AB06 and H4 and the separation by evoked IPSC and E/I.
3. `output/observations.tsv` OB09: add the 7 to 33 percent range and the equal-floor assumption.
4. `output/hypotheses.tsv` BH1: label the 90 percent block as a pre-specified design value; BH3: drop the floor-control sentence and soften "no datum supports" as above.
5. `output/README.md` line 10 and `engine_consumption.md` new-measurements list: add (i) to (iii) above or mark them out of scope.

Nothing else changed in my verdicts. Hypothesis verdicts remain PARTLY for BH1, BH2 and BH3.
