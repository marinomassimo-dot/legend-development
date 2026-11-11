# Audit V7 — package N1 (proton sensitivity of NMDA receptors and ASIC1a), blind verifier ks-z, 2026-11-11

Non-canonical research material. Not medical advice; no dose, no compound recommendation, no claim on WWOX. Labels DATO / INFERENZA / IPOTESI. Verdicts were written to `verdicts.tsv` before `output/answers.md` and `output/phase_note.md` were opened; section 7 (priors) was written after.

## 1. Result in six lines

1. D01-D03 (Kostakis 2011) are correct and reproduce exactly: 0.65 / 0.49 / 0.33 (exon 5 absent) and 0.94 / 0.82 / 0.56 (present) at pH 7.4 / 7.2 / 7.0 for a zero floor and pH 9 reference. The paper states no floor, no reference formula and no residual current at saturating acid, so those numbers are one model, not a measurement (INFERENZA, as the producer labelled it).
2. The producer's "surprise" (GluN2B at least as proton-sensitive as GluN2A) is **right, and now has primary support**: Tian 2021 (Nat Commun, same lab, same conditions) gives pH IC50 7.00 (GluN2A, Hill 1.91) versus 7.60 (GluN2B, Hill 1.37); Regan 2019 gives 7.50 for wild-type GluN1-4a/GluN2B. "GluN2B is less proton-sensitive than GluN2A" is **contradicted** for recombinant diheteromers. Neither primary was opened by the producer (Regan 2019 was in its own query Q21 and was set aside).
3. One substantive error in the ASIC rows: the +0.15 offset of the desensitisation function is a deliberate equilibrium correction by the authors, not a misfit of the function to the data. Availability at 7.2 is about 0.84 after 60 s (data) and about 0.21 at equilibrium (the authors' function).
4. One substantive error in PS13: the claim that the native NMDA points "are not one Hill-1 curve" rests on an unnormalised comparison; normalised to pH 7.6 the Hill-1 value at 7.1 is 0.71 against 0.78 +/- 0.07 (SD).
5. Both absence claims (native NMDAR proton measurement at 30-37 C or layer II/III; K2P + NMDAR + ASIC on one cell in a 0.1-0.3 unit step) hold within the stated perimeters after 26 independent strings; one qualification is needed for the first (section 6).
6. Rows: 73 checked, 63 correct, 10 defective (two substantive: PS13, PS17/D11; eight minor). Seven of the producer's receipts have the right fingerprint; two overstate figure coverage.

## 2. D01-D03, Kostakis 2011 (PMID 21883211), partial_fulltext_read

Opened from the PMC XML (Table 1, Methods, Results, Fig 5 and 8 legends, Discussion lines); the open-data bucket has json/txt/xml only, so no figure image could be viewed (captions only).

Verbatim (Table 1): "NR1-1a/NR2A (− exon-5) 7.21 ± 0.02 1.45 ± 0.06" (n = 13 oocytes); NR1-1b/NR2A (+ exon-5) 6.96 ± 0.02, 2.70 ± 0.27 (n = 8); both differences marked p < 0.0001. The Table 1 title says "NR1-1b/NR2B" while the rows are NR2A (typo in the paper; not the producer's). Fig 8b legend: wild-type NR1-1a/NR2A pKa 7.2 ± 0.1 (n = 12).

Conditions confirmed: Xenopus oocytes, two-electrode clamp, 22-24 C, Mg2+-free Ba2+-Ringer (96 NaCl, 2 KCl, 1.8 BaCl2, 5 HEPES, 0.5 percent DMSO, pH 7.5), Vh -70 mV, 200 uM NMDA + 10 uM glycine, peak current, normalised to the same oocyte at pH 9, "IC50s and Hill coefficients for proton inhibition were derived ... by the logistic equation" over pH 9 to 6 (the form is not written out).

Recomputation (own code, formula f = floor + (1 - floor) / (1 + 10^(nH (pK - pH))); no script is saved in the repository; see `recompute_proton.tsv`):

| model | f(7.4) | f(7.2) | f(7.0) | 7.2 / 7.4 | 7.0 / 7.4 |
|---|---|---|---|---|---|
| GluN1-1a/2A, floor 0, ref pH 9 (producer's model) | 0.653 | 0.492 | 0.332 | 0.752 | 0.507 |
| same, floor 0.1 | 0.688 | 0.542 | 0.398 | 0.788 | 0.579 |
| same, floor 0.2 | 0.723 | 0.593 | 0.465 | 0.821 | 0.644 |
| same, pK and nH at -1 SEM / +1 SEM | 0.662 / 0.644 | 0.508 / 0.474 | 0.352 / 0.310 | 0.767 / 0.736 | 0.532 / 0.482 |
| exon 5 present, floor 0 | 0.939 | 0.816 | 0.562 | 0.869 | 0.598 |
| exon 5 present, floor 0.2 | 0.951 | 0.853 | 0.649 | 0.897 | 0.683 |

Producer values match to three decimals; the stated 25 and 13 percent losses between 7.4 and 7.2 are 24.8 and 13.1 percent. Sensitivity: a residual of 0.1-0.2 lowers the 7.4-to-7.2 loss of the exon-5-free receptor to 21-18 percent. **No residual current at saturating acid is reported** (the paper never states one; the Fig 8b mutant text says "over 75% tonic proton inhibition" at pH 6.0 only for a mutant). Verdicts: D01 SUPPORTED, D02 SUPPORTED, D03 SUPPORTED (model-dependent, labelled).

## 3. The GluN2B direction (producer's surprise), item 2

**Hansen 2021 (PMID 34753794), Table 5, opened in full from the XML.** Values confirmed: H+ IC50 GluN1/2A 0.080-0.22 uM (pH 6.74-7.20); GluN1/2B 0.040-0.060 uM (pH 7.3-7.5); Yi 2018 rows GluN1-1ac/1ac/2A 0.20 uM (pH 6.80), 2B 0.036 uM (pH 7.54); activity coefficient 0.8; "Data are for rat recombinant receptors expressed in oocytes or HEK cells" (per-entry temperature, Mg2+, agonists not carried). The review text says GluN2A-, GluN2B- and GluN2D-containing receptors all lie in pH 7.0-7.4.

**Correction to the sources of each value.** The table footnote maps superscript 1 = Traynelis 1998, 2 = Traynelis 1995, 3 = Yi 2018, but superscript 1 sits on the Zn2+ column. The H+ column of GluN1/2A cites only Traynelis 1995 (ref 2); GluN1/2B cites Traynelis 1995 and Yi 2018 (refs 2, 3). The producer wrote "refs Traynelis 1995 and 1998" in both PS03 and PS07 (error class: column-to-reference mapping; extended to both rows, no third row carries it).

**Primary values reached legally (new, not in the producer's tables):**

| source | construct | pH IC50 | Hill | conditions |
|---|---|---|---|---|
| Tian 2021 Nat Commun (PMC8342458), Fig 3d legend | rat GluN1-1a K178AzF / rat GluN2A, before UV | 7.00 +/- 0.02 (n = 9) | 1.91 +/- 0.11 | oocytes, RT, Vh -60 mV, 0.3 mM Ba2+, no Mg2+, 100 uM Glu + Gly, HEPES-enriched bath |
| same | same GluN1 / mouse GluN2B, before UV | 7.60 +/- 0.01 (n = 7-9) | 1.37 +/- 0.05 | same oocytes and bath |
| Regan 2019 Nat Commun (PMC6338780), Table 4 | rat GluN1-4a / GluN2B, wild type | 7.50 +/- 0.02 (n = 6); IC50 40 +/- 1.7 nM | not reported | oocytes, about 23 C, Vh -40 mV, 0.5 mM Ba2+, 100 uM Glu + 30 uM Gly |

Caveats: the Tian values are for the GluN1 K178 photo-crosslinkable mutant before UV; the legend plots wild-type curves as overlapping (Fig 3d viewed) but gives no wild-type pH number in the text, so the wild-type claim rests on the figure (INFERENZA). Traynelis 1995 (Science), Traynelis 1998, Banke 2005 and Yi 2018 text were not reachable (the producer's own unreachable list; Traynelis 1995 has an abstract only: "Protons inhibit NMDA receptor function by 50 percent at pH 7.3 through interactions with the NR1 subunit").

**Verdict.** "GluN2B is less proton-sensitive than GluN2A" is **CONTRADICTED** for recombinant GluN1/GluN2 diheteromers: three independent lines (compilation of Traynelis 1995 and Yi 2018; Tian 2021; Regan 2019) put GluN2B at pH 7.3-7.6 and GluN2A at 6.74-7.21. The across-laboratory spread for GluN2A (6.74-7.21) is as large as 0.5 unit, so the within-study pairs (Tian 7.00 / 7.60; Yi 6.80 / 7.54) are the discriminating evidence. Companion fact: GluN2A curves are steeper (Hill 1.9 versus 1.4 in Tian), yet the fractional loss for a 0.2 unit fall from 7.4 is still larger for GluN2B (21-36 percent) than for GluN2A (9-26 percent), and at pH 7.4 the GluN2B receptor is already 44-65 percent inhibited (f = 0.35-0.56) against 15-39 percent for GluN2A (f = 0.61-0.85).

**Honest range of the fraction of current (relative to the fully relieved receptor)**, built from the table above and the compiled ends with Hill 1 assumed (illustrative where the Hill slope is not reported):

| | pH 7.4 | pH 7.2 | pH 7.0 | loss 7.4 to 7.2 |
|---|---|---|---|---|
| GluN2A | 0.61-0.85 | 0.47-0.74 | 0.31-0.65 | 9-26 percent (17 percent Tian, 25 Kostakis; 18 percent with floor 0.2) |
| GluN2B | 0.35-0.56 | 0.22-0.44 | 0.13-0.33 | 21-36 percent (36 Tian; 25 Regan with Hill 1 assumed) |
| GluN2A exon 5 present (Kostakis) | 0.94-0.95 | 0.82-0.85 | 0.56-0.65 | 10-13 percent |

Triheteromers: no proton midpoint, slope or residual in any source I read (Table 5 H+ column "-"; Hansen 2014; Cheriyan 2016; Tian; Regan): D05 SUPPORTED as a bounded absence.

## 4. D07-D09, native NMDA (Evlanenkov 2023, PMID 37629153), partial_fulltext_read

The brief names Cheriyan 2016 for this item; the P13-P19 prefrontal neuron data are Evlanenkov 2023 (Cheriyan 2016 is the HEK triheteromer spermine paper). Opened from the XML (Introduction, Results, Discussion, Methods) with Figs 3, 4 and 5 viewed (the producer viewed Figs 3 and 4 only).

Confirmed: Wistar rats 13-19 days; slices of hippocampus, cortex, striatum; neurons freed by vibrodissociation without enzyme (acutely isolated somata); room temperature 22-24 C; extracellular solution NaCl 143, KCl 5, CaCl2 2.5, glucose 18, MES 10, HEPES 10, pH 7.6, **no Mg2+ in the pH series** (an omission from the solution list; "Mg-free" is not written) with a separate 1 mM Mg2+ test at pH 7.6 and an I/V at pH 6.5 (Fig 6); Vh -80 mV; 300 uM NMDA + 10 uM glycine; data pooled across cells (at least five per pH) and normalised to the pH 7.6 response; mean +/- SD. "The steady-state responses to NMDA demonstrated a pH50 of 6.97 (IC50 = 0.11 ± 0.04 µM)". No peak pH50 for NMDA alone is given (6.97 is also the glutamate peak value, IC50 0.11 +/- 0.02). Text at pH 7.1: protons first, peak 22 +/- 7 and steady state 26 +/- 3 percent (n = 5); simultaneous application, peak 0 +/- 5 percent and steady state 28 +/- 5 percent (Fig 5: "Inhibitory effect of weak acidification (pH 7.1) develops slowly"). **Layer: not stated** (Fig 1C: "pyramidal neuron of the prefrontal cortex"). **Subunit: no statement, no GluN2B-selective tool** in the paper.

Figure 4B (viewed): NMDA peak, response 5, normalised to pH 7.6: about 0.88 (7.4), 0.78 (7.1), 0.43 (6.8), 0.25 (6.5), 0.12 (6.2), 0.05 (5.9); Fig 4C steady state about 0.35 (7.6), 0.38 (7.4), 0.23 (7.1), 0.13 (6.8), 0.065 (6.5). All the producer's raster readings are reproduced within 0.03. The 7.1/7.4 ratio 0.78 / 0.88 = 0.89 gives the 11 percent (INFERENZA) of D08.

Defect (PS13 note): the producer calls the 7.1 point (0.78) inconsistent with a Hill-1 curve because that curve gives 0.57. 0.57 is the unnormalised value; with the data normalised to pH 7.6 as in the paper, Hill-1 at pH50 6.97 gives 0.709 at pH 7.1, so 0.78 +/- 0.07 (SD) is within about one SD. The claim is **not supported** (the figure's curve at 7.6 is also above 1). PS13 also fills the midpoint column with the steady-state pH50 while the fractions are peak values: say so.

Verdicts: D07 SUPPORTED, D08 SUPPORTED, D09 SUPPORTED (bounded absence).

## 5. D10-D12, ASIC1a (Alijevic 2020, PMID 32180707) and the slow proton block (Evlanenkov 2023)

Opened from the XML plus rendered Table 1 (page 8) and Figs 2 and 4 (Fig 2 panel A and C compared). Recombinant human ASIC1a clone carrying G212D, stable CHO cells, whole cell, Vh -60 mV, 20-25 C, Tyrode with 1 mM MgCl2, HEPES + MES, conditioning pH 7.4.

* Activation (Table 1): a-infinity = 1 / (1 + 23.67^1.48 * 10^(1.48 * 2.797 (pH - 7))) gives pH50 6.509, slope 4.14 in log units; model activation 0.0002 (7.4), 0.0014 (7.2), 0.0092 (7.0). Data (Fig 2A): 0.02-0.03 at 7.0, 0.05 at 6.8, 0.42 at 6.6, 0.69 at 6.4. The paper's own sentence: "To induce ion current or charge transport, an acidification to ≤pH 6.7 was necessary in the model." It adds that the model's charge transport at pH 7.0-7.15 "was not observed in experiments" (omitted by the producer in D10; add).
* Steady-state desensitisation, 60 s conditioning, I2/I1 (Fig 2A right, 2C): about 1.1 (7.6), 1.0 (7.4), 1.02 (7.3), 0.84 (7.2, error bar about 0.78-0.90), 0.46 (7.1, bar about 0.33-0.59), 0.06 (7.0), 0 (6.9). The producer's readings are confirmed.
* **The 0.15 offset.** Results: the first model, run through the same 60 s protocol, drifted from the SSD data because "the duration of the conditioning pH step was 1 min, which ... is too short to obtain complete desensitization"; "to compensate for this, the function s∞ was shifted toward higher pH values by 0.15 pH units (green curve in the right panel of Figure 2C)". So the green function in Fig 2C sits 0.15 alkaline of the data **by construction**, and in Fig 2A the unshifted green function tracks the data. The producer's wording "data and fitted function disagree by about 0.15 pH units" (PS17 note) and the listing of the fitted function next to the data as if a discrepancy (D11) misreads this. Correct statement: s-infinity (Table 1, pH50 7.261, slope 9.45) is the authors' equilibrium function; availability = 0.954 (7.4), 0.210 (7.2), 0.003 (7.0) at equilibrium; = 0.998, 0.874, 0.082 for the unshifted function that reproduces the 60 s data; the measured values are 1.0, 0.84, 0.06. Rates near pH 7.2 are about 1e-5 per ms (Fig 2B), so a slow step to 7.2 desensitises far more than 16 percent over minutes. Additional omitted fact: this clone has G212D, which shifts SSD 0.08 unit to the alkaline side relative to G212 (Discussion). **Judgement: the data are a 60 s non-equilibrium reading and the producer's "16 percent desensitised" is right for 60 s only; at equilibrium the authors' function says about 79 percent.**
* Native (Evlanenkov): "no significant ASIC-mediated currents (response 4) are seen" at pH 7.1; pH50 6.19 (EC50 0.64 +/- 0.13 uM), maximal response 1.6 +/- 0.11 times the NMDA control; Alijevic Fig 6F legend: pH50 6.29 +/- 0.23 (WT, n = 10), 6.67 +/- 0.03 (ASIC2-/-, n = 4), E14-15 mouse cortical culture. Both verified.
* Slow NMDA proton block (Evlanenkov Fig 5, viewed): protons at 7.1 together with NMDA leave the peak unchanged (0 +/- 5 percent) and lower the steady state by 28 +/- 5 percent; protons first give 22 +/- 7 and 26 +/- 3 percent; conditions as in section 4.

Verdicts: D10 SUPPORTED (add the model-versus-experiment caveat), D11 PARTLY (numbers right, interpretation of the 0.15 offset wrong), D12 SUPPORTED.

## 6. D13-D15, absence (my own strings; `queries_verifier.tsv` V01-V26)

* (a) native NMDAR proton measurement at 30-37 C or in layer II/III. Strings: PubMed tool (V08, V09, V11: 0, 20 off-topic, 0 hits), Europe PMC abstract-field and full-text strings with temperature, layer, region and "proton block" terms (V12-V19: 0, 0, 0, 23 control, 0, 0, 0, 1, 13, 8 hits). Opened or screened: titles of all 20 PubMed hits (none about proton effects), Evlanenkov (already read), the Chesler-laboratory CA1 slice papers (Makani 2007 and 2012; 20631217) at abstract level, one restricted stub (PMC3514870, Makani 2012, not on the producer's list, recorded unreachable, not retried). **Result: no reachable text states a native NMDAR proton measurement at 30-37 C or in layer II/III. Qualification: mouse hippocampal CA1 slice papers that measure the NMDAR contribution of pH transients exist (abstracts: EPSC decay -32 percent, charge -39 percent with added carbonic anhydrase), and their recording temperature could not be read; "none exists" is not shown.** The producer's D15 wording "all proton-sensitivity values found ... are from 20-25 C" is too strong: every value with a stated temperature is 20-25 C, but the compiled Hansen rows and Cheriyan 2016 state none. D15 PARTLY.
* (b) K2P + NMDAR + ASIC on one cell in a 0.1-0.3 unit step. Strings V10, V20-V23 (0; 242, 2156, 51, 42 hits; first 25 titles of each screened). Abstracts opened through the PubMed tool: 42897310 (ASIC1a/NMDAR/TRPM review), 38965228 (pH-sensitive luminopsin), 39444753 (intracellular pH in cultured neurons), 42153246 (TREK-1 review); none measures the three targets on one cell. The 2131 unscreened hits of V21 are the perimeter's open edge. **D13 SUPPORTED within perimeter.**

## 7. Rows, receipts, error classes (items 6 and 7)

**Evidence rows.** All 19 verbatim quotes from full-text sources (EV01-EV19) were found at their locators by a normalised string search of the XML (dash, micro and whitespace variants); each is at most 25 words (EV01-EV19 checked; EV03 is 19 words). The five abstract-only quotes (EV20-EV24) match the PubMed abstracts exactly (Tang 1990, Makani 2007, Hatch 2023, Ziemann 2008, Traynelis 1995). Row counts: proton_sensitivity 19 rows, native_evidence 15, decisive 15, evidence 24 = **73 rows checked; 63 correct; 10 defective**:

| row | file | defect | class |
|---|---|---|---|
| PS03 | proton_sensitivity.tsv | locator refs "Traynelis 1995 and 1998": H+ ref is Traynelis 1995 only | A column-to-reference mapping |
| PS07 | proton_sensitivity.tsv | same; correct refs Traynelis 1995 and Yi 2018 | A |
| PS04 | proton_sensitivity.tsv | "0.5 pH units below the Kostakis value": 7.21 - 6.80 = 0.41 | B arithmetic |
| PS12 | proton_sensitivity.tsv | agonists "100 uM NMDA + 10 uM Gly": the pH 6.4 spermine experiments used 100 uM glutamate + 10 uM glycine | C agonist transcription |
| EV08 | evidence.tsv | species_system "100 uM NMDA + 10 uM Gly" (same) | C |
| PS13 | proton_sensitivity.tsv | Hill-1 comparison unnormalised; midpoint/fraction mixing steady-state and peak | substantive |
| PS17 | proton_sensitivity.tsv | "data and fitted function disagree by about 0.15" | substantive, equilibrium |
| D11 | decisive.tsv | same framing; no equilibrium availability; G212D shift omitted | substantive (same error) |
| D15 | decisive.tsv | "all proton-sensitivity values ... 20-25 C" | overclaim |
| NE06 | native_evidence.tsv | "5 to 10 cells per pH (declared)": the paper says at least five | n imprecise |

Error-class extension. Class A (Table 5 column mapping): checked every row that cites Table 5 (PS03-PS10, PS15): only PS03 and PS07 carry the Traynelis 1998 mistake; PS04-PS06 and PS08-PS10 cite Yi 2018 correctly. Class B (differences between computed values): checked all stated differences (PS02 0.25, PS08 0.74, PS10 0.71, D03 25/13 percent, PS17 0.15 shift = 7.26 - 7.11): only PS04 wrong. Class C (agonist for Cheriyan): PS12, EV08 only (D06 itself is correct). The 0.15 misreading: PS17, D11 and the `answers.md` N3 line and prior table ("desensitisation begins near 7.2 (84 percent available)") inherit it; they should say "after 60 s".

**Receipts, spot-check of two plus fingerprints.** FTR-20261111-21883211-84 (Kostakis): coverage matches what I could verify (figures captions_only because the bucket has no images; supplement not read); verbatim locator found. FTR-20261111-37629153-84 (Evlanenkov): `figures: read` overstates; Figs 1, 2, 5, 6 are captions only by the producer's own notes (FIG notes F07-F09) and I viewed Fig 5, which the producer had not; the vocabulary has no "partial" so `captions_only` with the viewed figures named is the honest choice. FTR-20261111-32180707-84 has the same `figures: read` with Figs 1, 5, 7-11 captions only. The `source_fingerprint` of all seven producer receipts equals the SHA-256 of the PMC XML I fetched. Producer receipts record `first_read` and no prior except 24607230 (prior -99), consistent with the ledger.

**My receipts** (8, staged, validated OK with `staged_receipt_check.py --check-doi`, not recorded): 21883211, 34753794, 37629153, 32180707, 26917100 with `prior_receipt` the producer's -84 id and `reread_reason adversarial_reanalysis`; 24607230 with `prior_receipt` FTR-20261111-24607230-99 (the ledger-recorded one; the producer's staged -84 sits on top of it) and `adversarial_reanalysis`; 34354080 (Tian 2021) and 30659174 (Regan 2019) `first_read`. Hansen 2018 (30037851) was only quote-checked (one sentence) and has no receipt.

## 8. Priors re-scored from my own reading (PREREGISTRATION.md, not edited)

| prior | verdict | basis |
|---|---|---|
| N1 | PARTLY (one clause held, two contradicted) | GluN1/2A midpoint 7.21 (Kostakis) but 7.00 (Tian) and 6.74-6.80 (compiled): not "7.2-7.4" in general; "2B less sensitive (6.9-7.2)" is contradicted (7.50, 7.60, 7.3-7.5); GluN2A is not the most sensitive diheteromer; exon 5 lowers sensitivity: held (0.25 unit, Kostakis; Yi 6.80 to 6.58) |
| N2 | PARTLY | 7.4 to 7.2 removes 17-25 percent of GluN1/2A (inside 15-35); GluN2B loses 21-36 percent, not less; native juvenile PFC neurons: about 8 percent for 7.4 to 7.2 by interpolation, 11 percent for 7.4 to 7.1 (below the range; room temperature, Mg-free, pH 7.6 reference) |
| N3 | HELD, with a time-dependence qualifier | no current 7.4-7.2; threshold near 7.0 (2-3 percent); half-activation 6.51 (recombinant) and 6.19-6.29 (native); SSD starts at 7.2: 16 percent in 60 s, about 79 percent at equilibrium (authors' function) |
| N4 | HELD within perimeter | V10, V20-V23 and the producer's own strings |
| N5 | HELD, detail differs | juvenile native evidence at room temperature exists (acutely isolated PFC neurons, not cultured or sliced); not at 35 C and not layer II/III in reachable text; CA1 slice papers of unread temperature exist |

## 9. What I could not reach, and route deviations

* Not reached: Traynelis 1995 (abstract only), Traynelis 1998, Banke 2005, Yi 2018, Dravid 2007, Makani 2007 and 2012 full text, Hatch 2023 text (all restricted stubs or no PMC text; none re-requested except Makani 2012, which was not on the producer's list); Kostakis figures (no image in the bucket). Not viewed by me: Evlanenkov Figs 1, 2, 6; Alijevic Figs 1, 3, 5-11; Supplementary files of Kostakis, Alijevic, Tian, Regan.
* Deviations: no `paper_packet claim` was run (it writes outside the allowed folder); no script saved in the repository (recomputation is by an inline formula, written in this file and in `recompute_proton.tsv`); PubMed MCP query times were not logged per call (approximate times in `queries_verifier.tsv`); no browser header, no e-mail or registration service, no captcha or 403 encountered; the producer's unreachable list was not requested again.
* Brief item 3 names Cheriyan 2016 for the native P13-P19 data; the correct source is Evlanenkov 2023. Flag for whoever reuses the brief.
