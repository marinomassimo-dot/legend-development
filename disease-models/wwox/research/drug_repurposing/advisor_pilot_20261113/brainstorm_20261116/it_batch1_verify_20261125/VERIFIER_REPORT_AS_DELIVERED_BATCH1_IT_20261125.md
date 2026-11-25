# Blind verifier report, batch 1, as delivered (2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high (stated in the dispatch), 25 statements as (statement, source, anchor), no candidate and no conclusion given. The delegate could not write its report file ("Subagents should return findings as text, not write report files"); the text below is its hand-back message, unchanged. Page images it opened were saved under `verify_batch1/out/` in the job tmp (not committed).

## Count per verdict (25 statements)
- SUPPORTED: 22 (A1-A11, A13, A14, B1-B4, C1-C5)
- UNDERSHOOT: 1 (A12)
- OVERSHOOT: 1 (C6)
- WRONG: 1 (A15, first clause only)
- UNVERIFIABLE: 0

## Non-SUPPORTED rows

**A12 - UNDERSHOOT.**
- Statement: IT doses of the Hudry studies start at 4.8E+12 vg per animal.
- Table S1 (mmc1.txt line 95; PDF page 10 opened) does print "Vehicle or AAV9 at 4.8x10^12-9.2x10^13 vg/animal" for the intrathecal route.
- But Table S2 (individual study designs) has no IT arm below 1.0E13. Study A is 1.2, 3.0 and 6.0 E13. Study B is 3.0E13 (Table S4 prints 6.0E13 for group 4). Study C is 1.00 and 3.00 E13. Study D is 2.73E13 capsids.
- The article text says "~1-6 x 10^13 vg/animal". 4.8E12 and 9.2E13 appear nowhere else in mmc1, mmc2 or the article XML.
- Correction: "Table S1 prints an IT range of 4.8E+12-9.2E+13 vg/animal. No IT arm in Table S2 (Studies A-D) is below 1.0E+13 vg/animal, and the text gives ~1-6E+13. The Table S1 bounds match no listed arm."

**A15 - WRONG (first clause).**
- Statement: the WWOX-JAK2/STAT3 interaction work uses cancer cells only, and its in vivo arms are overexpression experiments.
- The interaction experiments use 293T cells (Fig 3a, 4a, 4c, 4e: "293T cells were transfected with plasmids expressing Myc-tagged full-length Wwox or Flag-tagged full-length STAT3...").
- Endogenous co-IP uses "MCF-10A, MCF-7, and T47D cells" (Fig 3b) and "MCF-10A and T47D cells" (Fig 4b).
- NIH3T3 fibroblasts are used for the STAT3-dependence xenografts.
- The paper does not call 293T, NIH3T3 or MCF-10A cancer lines, and it groups MCF-10A with "luminal cells". That 293T is a kidney line and NIH3T3 a mouse fibroblast line is general knowledge, not stated in the file.
- The second clause holds. All in vivo arms are Wwox-overexpression versus control xenografts (MDA-MB-231 orthotopic, NIH3T3 with STAT3C or v-SRC, B16). I found no in vivo knockdown or knockout arm.
- Correction: "Interaction work uses 293T transfection and endogenous co-IP in MCF-10A, MCF-7 and T47D, not cancer cells only. In vivo arms are all Wwox-overexpression xenografts."

**C6 - OVERSHOOT.**
- Statement: as designed, the assay cannot tell apart exon skipping, intron retention, a cryptic splice site and alternative termination.
- The held text (PMID26857392 Europe PMC XML) gives no primer or probe design. It says only "captured by an exon 8/exon 9-spanning primer pair" versus "a primer pair spanning exons 4-6".
- A probe is never mentioned (zero hits for TaqMan or Probe; "probe" occurs only for EMSA). Primer sequences are in the Supplementary Methods, which are not held.
- The inability to distinguish the four mechanisms is an inference, not something the paper states or tests.
- Correction: "The paper measures exon 9 with an exon 8/exon 9-spanning primer pair against an exon 4-6 pair. It does not discriminate causes of reduced 8-9 signal. By inference, a lower 8-9/4-6 ratio would fit exon 9 loss, intron retention, a cryptic splice site or termination in intron 8 alike."

## Notes on SUPPORTED rows that a user could misread
- **A4:** Table S3 footnote b says "Equivalent dose not assessed in murine model". The scaled mouse equivalent is 3.05E14/10 mL x 0.04 mL = 1.22E12 vg. The supplement also lists an mdx arm at 1.6E+12 vg, which is above that value but not equal to it. The statement stays literally true.
- **A5 recomputed:** Macaque (200+8)/90 = 2.31, printed 6.8. Mouse (3+0.5)/0.3 = 11.67, printed 11.7 (match). Rat (20+1)/2.2 = 9.55, printed 9.5 (match). Human 1882/1400 = 1.34, printed 1.3 (match). The rat row and the macaque CSF volume of 15 cm3 are as stated.
- **A6/A7:** the tables label the column "Day 1". "Pre-dose" is inferred from Table S1 ("pre-dose Day 1") and Table S2. 10^5.44 = 275,423, so "about 275,000" is right.
- **A8:** the Table S5 footnote group labels disagree with the table headings (the footnote calls Group 2 IT 1.00E13 and Group 4 ICM vehicle; the headings call Group 2 the ICM vehicle). I used the headings; P0003 reads 20480 at day -15.
- **A9:** Table S2 covers only AAV9 and AAVDJ, the two Study 1 capsids. Animal 40 is also "+" for AAVDJ (31.3). The positivity threshold is <=50% signal ratio.
- **A10:** the Methods print 40 mg/body to day 24 only for study 2. For study 1, days 3-24 are printed as "20 mg/kg (40 mg/mL, 1 mL/body)". That equals 40 mg only for a 2 kg animal. Study animals are 2-3 kg (Table 1), so 20 mg/kg would be 40-60 mg, a mismatch of at most 1.5-fold.
- **A14:** the Fig 4B legend and figure give no n. Fig 4A alone says "n=4 biological replicates". F(1,28) in a 2x2 design implies 32 observations; that is my inference, not stated in the source.
- **B1/B2:** Panels L and M values were read from the 300 dpi image of File010 page 2. Panel L prints no value under WSM S2 or WSM S5. The File012 page 7 original for panel M has seven lanes.
- **C2:** r = 0.68 is the baseline value. The paper gives r = 0.80 after gemcitabine. The 67% is relative to a cloned full-length cDNA reference.
- **C3/C5:** these hold for the main text only. The Supplementary Methods for PMID26857392 are not held, so a primer or assay for intron-8-terminating transcripts or an exon-9-loss control could sit there.
- **C4:** rs11644322 is an intron 8 SNP, tested against the 8-9 amplicon in Fig 4D. The paper presents it as altering Sp1 binding, and "splice" and "skipp" never occur in the text. No splice-altering variant is assayed, but the statement should keep the word "splice-altering".

## Not opened or only partly read
- **Engelhard 2026 (A5):** only the PMC XML is held, no PDF.
- **Chang 2018 (A15):** supplementary files are not held. Supplementary Figs 3 and 4 were read through the main text only.
- **Petrozziello PDF:** opened at pages 30 and 38 only.
- **Hudry:** mmc1.pdf pages 10, 13, 14 and 15 opened; the Table S2 page and the mmc2 and article XML were searched as text only.
- **Okai:** mmc1.pdf page 10 opened; mmc2-mmc6 and the article PDF not opened.
- **Thomsen:** mmc1.pdf page 19 opened; the main article XML was searched by keyword only.
- **Steinberg:** File010 page 2 and File012 pages 6-7 opened; other pages of File010 and File012, plus File008 and File011, not opened.
- **PMID26857392:** only the Europe PMC XML is held; the Supplementary Methods and supplementary tables are not, which limits C3, C5 and C6.
