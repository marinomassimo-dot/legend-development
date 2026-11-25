<!-- IT blind verifier (legend-delegate; asked sonnet, effort high), 2026-11-25, on PMID 27845895 only. Delivered text, unchanged except that the job scratch path is written as <job scratch>. Statements: statements_hsu2017.md. Hypothesis level; not medical advice. -->

The write to ./out/REPORT.md was refused by the harness ("Subagents should return findings as text"). I did not work around it, so the whole report follows here.

# Blind verification: Hsu et al. 2017, Oncotarget (PMID 27845895; PMC5386674; DOI 10.18632/oncotarget.13268)

Sources: only the files in `<job scratch>/v276c/src`. Image readings are by eye from the published raster (upscaled crops are in `.../v276c/out`), with no densitometry or particle counting. "L" means line numbers in `27845895.txt`.

## Verdict table

| ID | Verdict | One line |
|----|---------|----------|
| V1 | SUPPORTED, with qualifications | The claim and the missing death assay hold. Not all three proteins moved in each line, Smad3 did not move, and Hyal-2 has counter-observations. |
| V2 | SUPPORTED, with qualifications | "Average of two experiments" is stated for Fig 9B/C only. The supplement mentions floating dead cells in an HA FRET experiment. |
| V3 | SUPPORTED | There is also no sham or uninjured comparator, apoptosis method or animal methods section. |
| V4 | SUPPORTED as the authors' claim, with an image caveat | In Fig 2A, nuclear p-Smad2/3 and Smad2 look higher with HA than at dose 0. |
| V5 | SUPPORTED | All three wordings are verbatim, and the Abstract and S3/S4 legends add more. |
| V6 | SUPPORTED within the material checked | Panel images of main Figs 1, 3, 4, 5, 6 and 8 were not available. |
| V7 | **WRONG** | "No counts" is correct. "Boxed gold is cytoplasmic, not nuclear" is not. |
| V8 | SUPPORTED, small qualification | The only test is Fig 9C. WWOXsi alone is about at control level, not lower. |
| V9 | **UNDERSHOOT** | It omits the rat injury result (apoptotic nuclei, no HA) and the HA trigger. |

## V1
Quotes:
- L93: "High molecular weight HA increases the formation of endogenous Hyal-2/WWOX/Smad4 complex rapidly, followed by relocating to the nuclei in 20-40 min, in WWOX-expressing normal and cancer cells. No apparent cell death occurs."
- S1 title: "HA induces relocation of WWOX, Hyal-2 and Smad4 to the nuclei in prostate cancer DU145 cells" (human; S1B mean and SD, "n=3; 20 cells per count").
- L43: "By stimulating wild type Wwox+/+ MEF cells with HA, endogenous Hyal-2 rapidly translocated to the nucleus in 5 min (Figure 4C)." (mouse)

No viability, apoptosis or subG1 assay appears in the text or legends for any endogenous HA experiment. "No apparent cell death occurs" is asserted without data. Panels of Figs 1, 3, 4 and 8 were not viewable.

Qualifications:
- The proteins reported as moving differ by line. Hyal-2 nuclear movement is reported for DU145 (S1B), wild-type MEF (4C, S2), THP-1/U937 (pY216-Hyal-2, Fig 1F; U937 "data not shown") and U937 (WWOX/Hyal-2 co-IP, 4D).
- L36: "HA did not effectively cause relocation of cytosolic Smad3 to the nuclei".
- L73, HCT116 immunogold with HA: "little or no Hyal-2 was found".
- L45, THP-1 co-IP at 30 min: "the complex remained in the cytosol and no apparent translocation to the nucleus was shown".
- Low-weight image reading: the S1A fields at 80 and 120 min (HA 100 ng/ml) show few, rounded, compact cells. The authors do not comment, and this is not evidence of death.

## V2
Quotes:
- L70: "No cell death occurred. In contrast, Smad4/Hyal-2/WWOX-expressing cells underwent bubbling cell death [51, 52], post HA stimulation for 5-16 hr"
- L110: "DU145 cells were transiently overexpressed with each set of the following constructs"
- L83: "L929 cells were electroporated with Hyal-2 and/or Smad4 constructs, cultured 48 hr, and subjected to cell cycle analysis by FACS." and "All data are average from two experiments B, C."
- L94: "While native HA cannot induce cell death, HA may activate the overly expressed Smad4/Hyal-2/WWOX signaling complex and causes bubbling cell death."

Qualifications:
- No HA appears in the Fig 9 text, legend or panel labels. Cells are mouse L929, with no error bars.
- The two-experiment statement attaches to 9B and 9C. Fig 9A has no replicate number of its own beyond the generic "repeated 2-5 times" (L112).
- The generic electroporation method (L106) says cells were "then treated with hyaluronan and/or bovine hyaluronidase PH-20". Fig 9 reports no such arm.
- Bubbling death is in human DU145 with ECFP-Smad4, EGFP-Hyal-2(-sp) (cytosolic, no GPI anchor) and DsRed-WWOX. It rests on one still (Fig 7H) and video, with no death count, death assay or HA-free death control reported.
- **Supplementary Video 2 legend** (the Smad4/WWOX/p53 set, for which the text says no death): "False positive signals were due to floating dead cells. (This may be seen in other videos)". Dead cells were present; cause and fraction are not stated.
- L13 says without qualification: "The Smad/Hyal-2/WWOX complex relocated to the nucleus to induce cell death."

## V3
Quotes:
- L86: "rats were pierced with needles into their brains [40, 53]. We determined that post injury for 3 and 24 hr, there were increased numbers of apoptotic neurons in the brain cortex."
- Fig 10 legend: "with the presence of the Hyal-2/WWOX complex in the apoptotic nuclei of neurons."

No HA is mentioned for the rats. Neither the main text nor the supplement gives an animal number, count, quantification or counting method. The supplement has no rat content.

Qualifications:
- "Endogenous" is not the paper's word here; it follows from no construct being reported.
- Also absent: sham or uninjured control (so "increased" has no shown comparator), any method for calling a neuron apoptotic, rat strain, and any animal or injury methods. The immunoEM method (L103) describes HCT116 only.
- The generic "repeated 2-5 times" is the only replicate wording that could apply.
- Smad4 was not examined (WWOX 10 nm, Hyal-2 20 nm).
- L13 claims "a critical role of nuclear Hyal-2 and WWOX in causing apoptosis", but the experiment is observational.

## V4
Quotes:
- L24: "Treatment of MDA-MB-231 with HA did not effectively induce accumulation of p53 and Smad2/3 in the nucleus (Figure 2A; less than 10% for each indicated protein compared to the levels at time zero). Similarly, MDA-MB-435S cells were not responsive to HA-mediated nuclear translocation of WWOX2, p53, Smad4, and p-Smad2/3 (Figure 2B)."
- Fig 2 legend: "(<10% increase in nuclear localization compared to controls)".

Proteins measured (human breast cancer lines; replicate unit and number not given):
- **MDA-MB-231:** Hyal-2, p53, Smad2, Smad3, p-Smad2/3, WWOX, alpha-tubulin. Smad4 was not measured.
- **MDA-MB-435S:** p53, Smad4, p-Smad2/3, WWOX2, and alpha-tubulin (cytosol only). Hyal-2 and Smad3 were not measured.
- **Numbers:** "<10%". Fig 2B also prints "% increase in nuclear localization 0.0 0.1" under the nuclear -/+ lanes below the WWOX2 row, without saying which protein it covers.

Qualifications:
- Image reading of 2A: nuclear p-Smad2/3 is barely detectable at 0, shows a band at 25, weaker at 50, and is present at 100. Nuclear Smad2 is absent at 0 and faint at 25-100. This does not look like "<10%". The bands are weak, the JPG is low resolution, and no nuclear loading control is shown.
- The text says "levels at time zero", but 2A is a dose series (0, 25, 50, 100 µg/ml), while the legend says 25 µg/ml for 1 hr.
- MDA-MB-435S is not WWOX-null: "express little or no wild type WWOX, but MDA-MB-435S has WWOX2 expression".
- There is no WWOX-positive comparator on the same blot and no WWOX re-expression.

## V5
Quotes:
- Results L29: "when knockout Wwox−/− MEF cells were stimulated with HA, endogenous Smad4 did not appear to relocate into nucleus"
- Fig 2 legend: "When knockout Wwox−/− MEF cells were stimulated with HA, Smad4 appeared to relocate into nucleus in 4 hr"
- Discussion L93: "In WWOX-deficient cells, HA cannot effectively induce nuclear translocation of Smads, whereas Smad4 may spontaneously migrate to the nucleus."

Qualifications:
- The Discussion says "spontaneously", so strictly it is not a description of behaviour "after HA".
- Abstract: "In WWOX-deficient cells, HA failed to induce Smad2/3/4 relocation to the nucleus."
- S3 legend: "Endogenous Smad4 did not appear to relocate into nucleus".
- S4 legend: "it took about 4 hr for Smad4 to relocate into nucleus in knockout Wwox-/- MEF cells."

Fig 2D, approximate image reading (mouse MEF; "n=4; 20 cells per count"; error bars undefined; x axis not to time scale), in %:

| | cont | 0 | 5 min | 10 | 20 | 40 | 60 | 2 h | 4 h | 6 h | 8 h | 24 h |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| +/+ | 11 | 15 | 54 | 82 | 100 | 84 | 73 | 45 | 33 | 22 | 27 | 18 |
| −/− | 0 | 0 | 0 | 20 | 9 | 2 | 0 | 15 | 27 | 9 | 0 | 4 |

Knockout is far below wild type from 5 min to about 2 h. It has two small rises (about 20% at 10 min and 27% at 4 h, the latter close to wild type). Knockout baseline is about 0%, below wild type, so this panel shows no spontaneous nuclear Smad4 in untreated knockout cells.

## V6
Searched with Python `re`, case-insensitive (the CI pattern case-sensitive), over article lines 1-118, the supplement text and a fresh `pdftotext -layout`. The reference list was counted separately. Script: `<job scratch>/v276c/scripts/search.py`.

| Pattern | Hits |
|---|---|
| `\bp\s*(<\|=\|>\|≤\|≥\|⩽)\s*0?\.\d` | 0 |
| `\bp[- ]values?\b` | 0 |
| `\*+\s*p\b` | 0 |
| `signific` | 3, none a test result ("significant amounts", "significantly shortening of life span", "Functional significance") |
| `statisti` | 0 |
| `anova\|analysis of variance` | 0 |
| `\bt[- ]?tests?\b\|student` | 0 |
| `confidence\|\bCIs?\b\|\b95\s*%` | 0 |
| `mann\|whitney\|wilcoxon\|chi[- ]?squ\|fisher\|tukey\|bonferroni\|dunnett\|kruskal\|newman\|duncan\|scheff\|post[- ]?hoc` | only "manner" (plus 2 in references) |
| `probabilit` | 0 |
| `standard\s+(deviation\|error\|±)\|\bS\.?E\.?M\.?\b\|\bS\.D\.\|\bSD\b\|±` | "mean standard ± deviation" (S1) and "(±)-Blebbistatin" |
| `\bn\s*=\s*\d+` | Fig 2 legend (n=4), S1 legend (n=3) |

- Visual check of Figs 2, 7, 9, 10 and the supplement pages found no P value, test or significance mark. The asterisks in 2C, 7H and S4 mark cells. Error bars (2D, 7, S1B) are descriptive.
- A mark inside the unavailable panels (Figs 1, 3, 4, 5, 6, 8) cannot be excluded.
- "No inferential statistics" is accurate; "no statistics" would not be, since means, SD and n appear.

## V7 (WRONG on location)
"Immunogold micrographs without counts" is correct.

What I see in Fig 10:
- **3 h, panel a:** box b is cytoplasmic. Box c straddles the nuclear edge, with its upper part in nucleoplasm.
- **3 h, enlarged c:** the nucleus and its envelope fill the upper left. **The upper arrowheaded gold cluster is inside the nucleus**; the lower one is in cytoplasm.
- **24 h, panel a:** box c straddles the left nuclear border, much of it over nucleoplasm carrying gold. Enlarged c has arrowheaded particles on both the pale cleft side and the uniform nucleus-like side. Boxes b and d sit in the folded peripheral zone and look mostly cytoplasmic or borderline.
- **24 h:** many gold particles are scattered over the central nucleus labelled N, outside the boxes.

What I cannot see: the exact envelope position at 24 h; 10 nm versus 20 nm identity for most particles outside the 3 h insets; any nucleus-to-cytoplasm density ratio; labelling specificity (no antibody control shown); whether the cell is apoptotic.

## V8
Quotes:
- L84: "Ectopic WWOXsi blocked Smad4-mediated growth inhibition and apoptosis (Figure 9C). In controls, scramble siRNA had no effect"
- Heading: "suppression of WWOX by siRNA abrogates Smad4-mediated apoptosis"

The one experiment is Fig 9C: mouse L929, electroporated Smad4 with a WWOX siRNA plasmid, 48 h, FACS, average of two experiments, no HA. Image-read subG1 (%):

| Control | Scramble | Smad4 | Smad4+scramble | WWOXsi | Smad4+WWOXsi |
|---|---|---|---|---|---|
| ~10 | ~15 | ~47 | ~45 | ~12 | ~12 |

No experiment shows that WWOX loss or knockdown causes death. The knockout MEF, MDA-MB and dn-WWOX experiments (4G, 7B, 7F, S6) have no death readout.

Qualifications:
- WWOXsi alone is about equal to control (G1 ~63 vs 60). "Lower" applies to Smad4+WWOXsi against Smad4+scramble.
- Knockdown efficiency is not shown in this paper.
- The death tested is induced by overexpressed Smad4, so this is not a test of basal WWOX loss.
- Scramble alone moves G1 (~45 vs 60) despite "had no effect".
- Shortened life span with WWOX null mutations is cited literature, not an experiment here.

## V9 (UNDERSHOOT)
Both halves have textual support (L93; title "causes bubbling cell death when the signaling complex is overexpressed"). What the sentence omits or compresses:
- **Rat injury:** Hyal-2/WWOX (Smad4 not tested) in apoptotic neuronal nuclei, with no HA and no constructs. The authors present it as in vivo support for a death role. The sentence implies no endogenous protein was linked to death, although the link is only an uncontrolled association.
- **HA,** the trigger of the nuclear accumulation, is not named.
- **"Cell death was shown with overexpressed constructs"** merges HA-triggered, non-apoptotic bubbling death in DU145 with HA-free subG1 apoptosis in L929.
- **Overexpression was not always sufficient:** Smad4/WWOX/p53 gave blebbing "without cell death".
- **WWOX dependence** of nuclear movement, a main claim, is absent.
- **"Endogenous complex" in the nucleus:** "reported" is right, but the evidence is mostly separate proteins moving. SK-N-SH and Jurkat/L929R co-IPs show the cytosolic complex falling, with relocation inferred (L45-46). The U937 nuclear co-IP is WWOX/Hyal-2 only. HCT116 immunoEM found little or no Hyal-2 with HA alone; the large nuclear three-protein signal needed HA then TGF-beta1.

Possible wording: "The authors report HA-induced nuclear accumulation of endogenous WWOX, Smad and (in some cells) Hyal-2 without apparent cell death (not assayed); in cultured cells, death was shown only with introduced constructs (HA-triggered bubbling death in DU145; HA-free apoptosis in L929); an uncontrolled, unquantified rat brain-injury experiment places Hyal-2/WWOX in apoptotic neuronal nuclei."

## Other internal inconsistencies seen (outside the statements)
- Knockout MEF nuclear Hyal-2 is "~60%" (L42-43) but "Around 30% of the cells" in the S3 legend.
- HCT116 immunoEM HA exposure is "60 min" (L73) but "20 min" in the Fig 8 legend.
- The DU145 100 ng/ml timing is "20 min" (L16) but "40 min" in the Fig 1 legend.
- Fig 9B text says apoptosis rose "from 30% to 60%"; the bar reads about 52%. WWOX+Smad4 (~38%) is little above either alone (~31%).
- Smad4-alone subG1 is 61.8% in 9A, ~31% in 9B and ~47% in 9C.

## Not checked
- Panel images of main Figs 1, 3, 4, 5, 6 and 8 (not in `./src`); anything about them rests on text and legends.
- Supplementary Videos 1-10 (only legends and still frames).
- Cited references, including the bubbling-death definition and siRNA validation.
- Correction, expression-of-concern or retraction status (no web access).
- Image integrity (duplication or splicing).
- No densitometry or gold-particle counting.

No one was contacted and there was no spend.
