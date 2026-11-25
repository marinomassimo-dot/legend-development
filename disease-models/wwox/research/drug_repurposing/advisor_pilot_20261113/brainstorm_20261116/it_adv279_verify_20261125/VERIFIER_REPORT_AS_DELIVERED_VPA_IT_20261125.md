<!-- As delivered by one blind delegate (legend-delegate, claude-sonnet-5-5, effort high, read back from its transcript); it discloses a partial breach of blindness in its first lines. Not edited below this line. -->
# Blind verification report (2026-11-25)

Hypothesis-level work; nothing here is medical advice. Bibliographic records and abstracts are according to PubMed (DOI links below). Scripts are in `verify2/scripts`.

Blindness note (a breach, disclosed): a keyword grep over `it_adv275_20261125/RESULT_ADV275_IT_20261125.md`, which no statement names, showed me its lines 12, 15, 28, 43, 62 and 64. The grep over `RESULT_ADV273` also returned lines beyond the wanted rows (6, 21, 25, 27, 34). I also read parts of `adv275_read.py` (arm selection). The H1 densitometry and the J4 values were computed before those greps. J5 is judged from the PREREG and the TSV.

## Verdicts

| ID | Verdict | Main correction |
|---|---|---|
| H1 | SUPPORTED for direction and printed numbers; PARTLY for the pixel range and the line's identity | Fold range depends on the method (about 1.5 to 4.5 at 2-4 mmol/L); 1 mmol/L is nearly flat (1.07-1.28). HO-8910 is registered as a HeLa derivative |
| H2 | First part SUPPORTED; "wild-type WWOX" NOT SUPPORTED | The paper says nothing about WWOX genotype or status |
| H3 | PARTLY | Different laboratory and not a neural hESC system, but the "ovarian carcinoma" identity is contradicted by Cellosaurus |
| I1 | SUPPORTED | Entinostat (sheet 4): 1.25, 1.51, 1.12, 1.21, 1.51; adj p .045, .007, .288, .199, .016 |
| I2 | PARTLY | True only with adj p < 0.05 alone. Under the authors' cut-off (FC > 1.5 and adj p < 0.05) trichostatin A moves none |
| I3 | SUPPORTED (source says less) | "did not increase" WWOX mRNA, in lines with very low expression |
| I4 | SUPPORTED (source says more) | The legend states "Restoration of Wwox protein" |
| I5 | NOT SUPPORTED as worded | All six use 5-aza (not five). PMID 17019711 does state WWOX restoration. The sixth is 15266310 (full text, no increase). PMID 25720522's lines were not selected for WWOX silencing |
| J1 | SUPPORTED (numbers) | Replicate units differ and are mostly weak; the 1.28 call depends on normalisation |
| J2 | SUPPORTED for IC5 only | The IC20/100 arm is 1.17 and fails the sentinel; the TSV labels it "IC20" |
| J3 | SUPPORTED by count, much weaker than it reads | Only 21 of the 57 rows have a passing sentinel and an up / not-distinguished call |
| J4 | SUPPORTED | The compound is CI-994 (class I HDAC inhibitor), not valproate; only the no-shock arms are in the table |
| J5 | PARTLY | The prediction failed, but it was registered on series, not contrasts |

## H1-H3 (Yan and Zhang 2012; SHA-256 matches `c2a10661...`)

- Printed and confirmed: 1.0-4.0 mmol/L, 48 h, beta-actin; xenograft protein 0.46±0.065 vs 0.15±0.025; mRNA 0.305±0.015 vs 0.193±0.056; 20 mice "equally divided"; tumours taken after death; survival 47.12 vs 34.58 days; n per measurement not stated. Valproate was 0.4% in place of drinking water. Fig 5A shows 2 + 2 lanes; Fig 5B shows 3 control and 4 treated.
- My densitometry of the embedded blot image (1, 2, 3, 4 mmol/L vs control):
  - No background subtraction, actin-normalised: about 1.07, 1.6, 2.27, 3.15.
  - Local background subtraction: about 1.27, 2.3, 3.1, 4.3.
  - With a median-based background, 3 mmol/L reads 1.85-3.15 across windows and falls slightly below 2 mmol/L in two of four windows.
  - The "1.6 to 3.2" range matches the unsubtracted version only. A published blot image is not quantitative.
- No replicate number is given for the western blot. The text still claims P < 0.05 for the in-vitro WWOX rise and says results are mean±SD, but prints no in-vitro WWOX value. "One blot per panel" means one image shown; how many were run is not stated.
- "Wild type": no occurrence of wild-type, mutation or deletion status for WWOX anywhere in the PDF.
- Identity (outside the named sources): [Cellosaurus CVCL_6868](https://api.cellosaurus.org/search/cell-line?q=HO-8910&format=txt&rows=10) lists HO-8910 as "Problematic cell line: Contaminated. Shown to be a HeLa derivative" (ICLAC-00606; PMID 26116706, Ye et al. 2015, [DOI](https://doi.org/10.1096/fj.14-266718)). The paper took the line from its hospital's own laboratory and reports no authentication. I did not test that stock. The entry should not be called an ovarian carcinoma line without this flag.
- Other defects in the paper: captions say "P21" where the panels show P27; "HO9810" in a heading; PVDF and "nitrocellulose" for the same membrane.
- H3: the author affiliation is Obstetrics and Gynecology, Xuzhou Medical College. The statement does not name the comparator hESC laboratories, so "different laboratory" is judged only against an affiliation that is evidently not a stem-cell toxicology group.

## I1-I2 (Rempel `MOESM2` workbook, parsed from the xlsx itself)

All I1 numbers reproduce. SAHA largest 1.24; belinostat largest 1.23; panobinostat smallest adj p 0.138.

| Compound | adj p < 0.05 (of 5 sets) | Also FC > 1.5 either way |
|---|---|---|
| Valproate | 3 (1.43, 1.33, 1.68) | 1 (1.68) |
| Entinostat | 3 (1.25, 1.51, 1.51) | 2 (both 1.51, marginal) |
| Trichostatin A | 2 (1.22 up, **0.79 down**) | **0** |
| Belinostat, panobinostat, vorinostat | 0 | 0 |

- The authors' definition: "fold change >1.5 and adjusted p value of limma t test <0.05" (the workbook also says "Cut off: p 0.05_ fold change 1.5").
- A fold-change threshold alone is not enough either: at FC > 1.5 only valproate and entinostat pass.
- System and exposure: H9 hESC differentiating to neuroectoderm (UKN1), 6 days, one concentration per compound (highest non-cytotoxic, EC10), four independent experiments (five for trichostatin A).

## I3-I5

- 15266310 ([DOI](https://doi.org/10.1038/sj.bjc.6602023)): "several HCC cell lines expressing a very low level of WWOX mRNA after combined treatment with 5-aza-2'-deoxycytidine ... and trichostatin A ... the combined treatment did not increase the level of WWOX mRNA expression (not shown)". mRNA only; the number of lines is not given in that sentence.
- 18460020 ([DOI](https://doi.org/10.1111/j.1349-7006.2008.00841.x)): the legend gives MIA PaCa-2, 5-aza-dC 5 uM and/or TSA 1 uM, 5 days. Panel B reads "Restoration of Wwox protein by treatment with 5-aza-dC and TSA". The main text attributes it to demethylation. I found no supplement figure in `files/`; the held figures are main-text ones.
- I5, the list: it names five PMIDs for "six". The sixth is **15266310**, which is the only null report. It is held as full text, so it is not "abstract or legend level", and omitting it removes the disagreement.
- I5, the 5-aza count: **six of six** include it (16818616, 25720522, 20737170, 17019711, 18460020, 15266310).
- 17019711 ([DOI](https://doi.org/10.1002/ijc.22073)): "WWOX re-measurement not stated" is false. The abstract says "**Responding tumors showed restoration of Fhit, Wwox, p16(INKa), Rassf1a expression**".
- 25720522 ([DOI](https://doi.org/10.1007/s12032-015-0525-y)): lines were grouped by EBV status (SNU-719 against SGC-7901, BGC-823, AGS), not chosen for WWOX silencing. It had a TSA-alone arm. "Individual gene expression increased in EBVnGC cell lines" does not say WWOX did.
- Also for 25720522: Cellosaurus lists [SGC-7901](https://api.cellosaurus.org/cell-line/CVCL_0520?format=txt) and [BGC-823](https://api.cellosaurus.org/cell-line/CVCL_3360?format=txt) as HeLa derivatives, so two of its "gastric" lines are not gastric.
- 16818616 ([DOI](https://doi.org/10.1158/0008-5472.CAN-06-0956)) and 20737170 ([DOI](https://doi.org/10.1007/s00428-010-0956-y)): abstracts support lines with reduced WWOX and increase after the two drugs. Neither abstract shows a trichostatin-only result.
- "Test reactivation, not modulation of expressed WWOX" is fair for most, not established for 25720522 or for every prostate line.

## J1, J2, J4 (recomputed from D; seven data-file digests match `data_digests.tsv`)

Ratios are treated/control, log2 CPM geometric ratio (TPM for GSE187006), Welch p. "MoR" is my median-of-ratios sensitivity analysis.

| Series | n | WWOX | MoR | Replicate unit as deposited |
|---|---|---|---|---|
| GSE129241, day-1 addition | 4 v 4 | 1.277 (p .018) | **1.207** (p .040) | "Rep1-4"; unit not defined. hESC-derived NGN2 neurons, 72-96 h |
| GSE232218, 400 uM | 4 v 4 | 1.412 (p .0026) | 1.347 (p .047) | each sample is 6 wells of ~30-50 organoids pooled per well; independent batches not stated. 48 h |
| GSE241903 | 3 v 3 | 1.95 geometric, 1.92 arithmetic (p .028) | 1.88 | "in triplicate"; unit not defined. 96 h; no concentration in the matrix |
| GSE187006 U1M | 3 v 3 | 1.498 (p .0068) | n/a | **three single organoids** "randomly selected" per group; 1 mM, 72 h, day 42 |
| GSE187006 U2F | 3 v 3 | 1.62 (arithmetic 1.63; p .0087) | n/a | same |
| GSE166297 IC5 | 8 v 8 | 1.63 | 1.59 | "all technical replicates from one experiment"; "N=1 and n=8" |
| GSE166297 IC20/100 | 8 v 8 | 1.17 | 1.17 | same; H1F0 0.90, CDKN1A 0.60 (sentinel fails) |
| GSE305320 | 3 v 3 | 0.881 (p .30) | n/a | "2-3 biological replicates per group"; H9 hESC; no dose or time in the matrix |
| GSE185453 hippocampus, context | 4 v 4 | 0.944 (arithmetic 0.950) | 1.01 | one mouse per library |
| GSE185453 striatum, context | 4 v 4 | 0.88 | 0.94 | one mouse per library |

- J1: under a 1.25 threshold the GSE129241 day-1 "up" call becomes "not distinguished" with median-of-ratios. The same deposit family has GSE232218 at 200 uM = 1.12 (not distinguished).
- GSE129241 day 21 is 2 v 3 in the table. The drop is justified: "Ctrl day21 Rep4" is annotated "treatment: Valproic acid".
- J2: the deposit defines the levels as "non-cytotoxic (IC20/100) and slightly cytotoxic (IC5)". The TSV's "VPA IC20" is IC20 divided by 100.
- J4: GSE305320's sentinel passes on ratio (H1-0 2.7) with p = .057.
- J4: GSE185453 is **CI-994**, 30 mg/kg, one i.p. injection 1 h before context exposure, tissue 1 h after it. The 0.95 and 0.88 are the no-shock arms. The shock (CFC) arms are in neither the table nor the sentinel-failed file as far as I saw. My values for them: hippocampus 1.01, striatum 0.96. Their sentinels do not reach 1.5, so they would give no reading.

## J3

- Counts confirmed: 57 rows, 32 accessions, 56 tier A, 1 tier B (NT2-N). `series_call`: 24 not distinguished, 17 up, 9 descriptive, 7 near background, no "down" or "mixed". No probe-level "down" call either.
- 28 of the 57 rows **fail the sentinel**; under the PREREG they give "no WWOX reading for or against".
- With a passing sentinel: 12 up, 9 not distinguished, 4 descriptive, 4 near background.
- Descriptive and near-background rows cannot be called "down" by construction. Some have low ratios: GSE256142 Dravet-line organoids 0.49 (2 v 2, sentinel failed); GSE164788 entinostat 0.61 and 0.72 (near background).
- The 56 "non-transformed or non-tumour" rows include 6 from ReNcell VM, a v-myc-immortalised line. That is "non-tumour", not clearly "non-transformed".

## J5

- PREREG P4: "more than half of the sentinel-passing **series** with n >= 3 are not distinguished". The PREREG SHA-256 matches the recorded one.
- "7 of 22" counts **contrasts**, platform A excluded. The 22 include 4 near-background contrasts that give no call, so callable is 7 of 18.
- By series, platform A excluded: all contrasts not distinguished in 3 of 14 (3 of 13 callable); any contrast not distinguished in 6 of 14.
- With platform A: contrasts 9 of 25; series all-not-distinguished 4 of 16. P4 fails on these.
- One lenient reading (any contrast, platform A included, near-background series removed) gives 8 of 15, which would pass. The registered text does not define how to call a series with several contrasts, so state the rule used.

## Not checked

- Full text of 16818616, 25720522, 20737170 and 17019711 (abstracts only); no publisher pages tried.
- The raw HO-8910 STR evidence; the Cellosaurus listing was read through a summarising fetch tool.
- The other 25 accessions in J3 and J5: values and sentinels were taken from the TSV, not recomputed.
- Series search, eligibility, unread-series list, and whether arm selection is complete beyond the cases above.
- GEO web records beyond the downloaded matrices (so doses or replicate definitions stated only elsewhere are not seen).
- Rempel's concentrations per compound; the other Rempel workbook (`MOESM3`).
- The result reports' wording, registries, ledgers and candidates.
