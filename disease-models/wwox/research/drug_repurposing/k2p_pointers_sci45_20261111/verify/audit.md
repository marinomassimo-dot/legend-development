# Audit V6 — K2P tool pointers (Q1): ONO-TR-772 potency and the TREK-1 pH slope

Blind verifier ks-y, 2026-11-11. `output/answers.md` and `output/phase_note.md` were not read. Depth is
`partial_fulltext_read` throughout (main text plus the SI items named; stated per item). Labels:
DATO (read in the source), INFERENZA (my arithmetic or reading), IPOTESI (not used).

## Verdicts

| Item | Verdict |
|---|---|
| 1 D02 potency | SUPPORTED |
| 2 D03 K2P panel | SUPPORTED |
| 2 D04 10 uM panel, Ki | SUPPORTED |
| 2 D05 no pH series | SUPPORTED |
| 3 D09 AVE1231 | SUPPORTED (compatibility flag strengthened) |
| 3 D10 ONO-2920632 | PARTLY |
| 3 D08 KU124 | SUPPORTED (two wording fixes) |
| 4 D11 slope absence | SUPPORTED (source list incomplete) |
| 4 D12 catalogue labels | SUPPORTED |
| 5 evidence rows | PARTLY (13 checked, 9 correct, 4 minor defects) |

No decisive proposition is overturned. No substantive error was found.

## 1. D02, potency of ONO-TR-772 (PMID 40365404)

Every potency value in the source (DATO, with locators):

| Value | Assay, species | Where |
|---|---|---|
| 15 nM | "TREK-1 IC50 = 15 nM", no assay or species | Abstract |
| 15 nM | human manual patch clamp (MPC) | Results, paragraph beginning "Up to this point" |
| 67 nM | mouse MPC | same paragraph |
| 0.26 uM | h TREK-1 Tl+ IC50 (CHO, human) | Table 3 (compound 14c) |
| Tl+ 263 nM, MPC 15 nM | structure panel graphic | Figure 4, left panel (the graphic repeats the 15 nM) |
| 0.15 uM | QPatch IC50, TREK-1 | SI Table S2, p. S4 |
| 0.17 uM | QPatch IC50, TREK-2 | SI Table S2 |
| 0.26 uM | Tl+ IC50 of "5" | follow-up PMID 41104520, Fig 1 and abstract |

The producer lists four of these places; Fig 4 (15 nM and 263 nM) is an extra repeat, not a new value.
The follow-up carries only the Tl+ value for the compound; it does not repeat 15 nM.

Arithmetic (INFERENZA): 10 uM/0.15 uM = 66.7; 10/0.26 = 38; 10/0.067 = 149; 10/0.015 = 667. The
paper's ">67-fold" over TASK-3, TRESK, TWIK-2 (">10 uM", 13-26 percent at 10 uM) therefore matches the
QPatch 0.15 uM value, taking 66.7 as 67 (strictly 66.7 is not "greater than 67"). It does not match
15 nM. The GtoPdb pIC50 7.82 equals 15.1 nM.

Consistency. Tl+ 0.26 and QPatch 0.15 uM differ by 1.7-fold (plausible, different assays). The MPC 15 nM
is 10-fold below QPatch and 17-fold below Tl+. In the follow-up, MPC/Tl+ ratios for the related compounds
10 and 11 are 3.2, 3.4, 1.45 and 0.58 (rat/mouse, Results), so a 17-fold gap is larger than any pair
reported there (INFERENZA, other compounds, not a test). Mouse MPC 67 nM is 4.5-fold weaker than human
MPC 15 nM but 2.2-fold stronger than human QPatch 150 nM. A decimal or unit slip between 15 nM and
0.15 uM (a factor of 10) is possible, as is a correct 15 nM with ">67" taken from the QPatch figure;
nothing in the paper separates them. A numeral coincidence is worth recording and not interpreting:
"0.067 uM" is also the human Tl+ and the mouse MPC IC50 of compound 10 in the follow-up.

Not decidable from the SI (DATO, searched the whole SI text and viewed S4): QPatch and MPC protocol,
bath and pipette pH, temperature, whether any stimulus was present, the species of the QPatch cells
(Table S2 does not state it), number of cells, curves, and which value the TREK-1 "IC50" of the
abstract is. The SI Tl+ method (S5) is written for % activation against BL-1249 and does not give the
inhibition equation for TREK-1.

What a reader may carry (label): "ONO-TR-772 inhibits human TREK-1 with a Tl+ flux IC50 of 0.26 uM
(CHO, room temperature, HBSS + 20 mM HEPES, pH not stated; DATO) and 0.15 uM in QPatch (SI Table S2,
method absent; DATO); the paper also declares human manual patch clamp 15 nM and mouse 67 nM without
a method, and these figures are not consistent with its own '>67-fold' arithmetic (DATO plus
INFERENZA); the correct patch-clamp value is unresolved." Use 0.15-0.26 uM for any quantitative
statement and 0.015 uM only as a declared, unreconciled figure.

## 2. D03-D05

D03. SI Table S2 (rendered, viewed): QPatch IC50 TREK-1 0.15, TREK-2 0.17, TASK-3 >10 (19 percent at
10 uM), TRESK >10 (26 percent), TWIK-2 >10 (13 percent); row "MPC %inhibition at 10 uM": TRAAK -41
(labelled activation), TASK-1 17, TASK-2 7. Confirmed. The table does not state species. The main text
puts TASK-1, TASK-2 and TRAAK in the ">67-fold" list although they were tested at one point only and
TRAAK was activated.

D04. SI Table S3 (viewed): Cav1.2 -0.9, HCN4 0.6, Kir2.1 -1.1, Kir2.2 51.6 (transient), Kv1.5 2.4,
Kv4.3/KChIP 2.1, KCNQ1/E1 47.3, Nav1.5 1.1, hERG 38.4. Confirmed. Main text: "Kir2.2 (52%)" and
Ki 0.48 (A3), 2.6 (L-type benzothiazepine), 0.54 (dihydropyridine), 0.65 uM (sodium site 2); the SI
Table S1 shows only percentages (84, 56, 76, 84) and its caption names ONO-2920632 and 30 uM (copy
artefact; its header says 10 uM). Main text says 68 targets, SI caption 72. Ratio 3.2-17.3 against
0.15 uM is correct and would be 32-173 against 15 nM, so it depends on D02.

D05. Searched main text and SI text for patch, clamp, bath, pipette, intracellular, extracellular, pH,
acid, temperature, stimulus: nothing for QPatch or MPC. SI pH 7.4 appears only in plasma binding (DPBS)
and microsome (phosphate) methods; Tl+ flux is HBSS + 20 mM HEPES, room temperature, compound 10 min,
then Tl+ stimulus buffer. Follow-up SI "Patch clamp technique" (S3): whole-cell, CHO-K1 stably
expressing hTREK-1 or transiently expressing mouse TREK-1, hold -80 mV, 0 mV 500 ms then ramp, bath
pH 7.4, pipette pH 7.35, effect at 0 mV, no temperature, no activator. Confirmed, and correctly labelled
INFERENZA for transfer to ONO-TR-772.

## 3. D09, D10, D08

D09 (PMID 31001961; article PDF and supplement viewed). Supplementary Table 1: wild-type IC50 0.2 +/- 0.1
uM, Hill 1.1 +/- 0.1, "+40 mV with five different concentrations (n = 3-6 cells per concentration)";
Methods: 20-22 C, pH 7.4 (5 mM HEPES), human TASK-1, oocytes, holding -80 mV. Main text: 245 nM (20 min)
leaves 74.1 +/- 4.3 percent, 10 uM (20 min) leaves 19.3 +/- 7.7 percent, n = 3; measured at +20 mV;
Fig 1d legend says "240 nM" while the panel and text say 245 nM.
Compatibility (INFERENZA): with IC50 0.2 uM and Hill 1.1, 245 nM should block about 56 percent
(producer: about 50) and 10 uM about 98 percent; observed 26 and 81 percent. A two-point logistic through
the main-text values gives IC50 about 1.2 uM. Possible reasons stated nowhere in the paper: +20 versus
+40 mV, cumulative application, incomplete equilibration (Fig 1d: the 10 uM trace is still falling at
40 min). The producer's flag is right; the 10 uM discrepancy was not mentioned. Kv1.5 origin: Introduction,
"Initially these compounds were developed as KV1.5 inhibitors" (declared, citing earlier work).
The GtoPdb/ChEMBL assay note calls the assay "patch-clamp"; it is two-electrode voltage clamp.

D10 (PMID 39981749). Table 2 image (viewed): 19b human Tl+ TREK-1 2.8 uM (95 percent Emax), TREK-2 0.30
uM (184 percent Emax), fold 9.3; text: mouse MPC TREK-1 2.7 (109 percent), TREK-2 0.57 uM (105 percent).
Confirmed. Correction: "acting on unstimulated basal flux" is not a statement of the paper. SI shows
compound or DMSO for 10 min, then Tl+ stimulus buffer, normalised to 10 uM BL-1249; no activator and no pH
beyond "HBSS + 20 mM HEPES". It is a reasonable reading but should be labelled INFERENZA (decisive.tsv D10
kind "measured"; pointers.tsv T5 assay cell). No acid pHo experiment exists (the only acid is acetic acid in
the in vivo writhing test). Also pointers.tsv T5 selectivity cell gives "more than 150-fold" (Results); the
abstract says ">91-fold" for the same panel.

D08 (PMID 40635742). Fig 7 viewed: points at 0.1, 1, 10, 100 uM about 23, 55, 63, 79 percent, curve
reaching about 85 percent, error bars wide (INFERENZA from the raster); text "KU124's extrapolated IC50
value is 1.38 +/- 0.652 uM", "Each point ... average of four or more independent 96-well plate trials",
doxapram 10 uM control. No selectivity data, no pH, no assay species ("inducible TASK-1-GFP CHO", gift of
a named laboratory); the docking uses PDB 6rv2 chains C and D (the text gives no species for it). Fixes
for pointers.tsv T3: (a) "compound added then Tl+ for 20 min" is the producer's reading; the Methods say
15 uL of wash solution "containing five times the desired final concentration of thallium" then
incubation 20 min, without naming the compound step; (b) "room temperature" is stated for dye loading
(1-1.5 h) only; (c) the paper cites the dose-response as Figure 6 in the Discussion.
Not verified by me: the Discussion's statement that TASK-3 and hERG remain to be tested.

## 4. D11 and D12

D11. Strings and counts are in `queries_verifier.tsv` (PubMed tool: 0, 0, 11, 3, 0, 22; Europe PMC REST:
141, 245, 13, 396; one 503). Opened full text: PMC3181481, PMC3411076 (table image), PMC7608817 (text and
supplement), PMC6532698, PMC11711774 (text searched for Hill, slope, pK, temperature), PMC5376757.
- Bagriantsev 2011 (PMID 21765396, not in the producer's list): Methods fit pHo responses with
  I = Imin + (Imax - Imin)/(1 + ([H+]o/K1/2)^H), "H is the Hill coefficient", solutions exchanged pH 9.0 to
  5.9 at 22.5 C, 2 mM K+, Tris/HEPES/MES, oocytes, murine K2P2.1. Supplementary Table S1 lists pK1/2 and
  Imin/IpH9.0 only: TREK-1 7.51 +/- 0.06 and 0.25 +/- 0.03 (n = 30); TREK-2 7.69; TASK-3 6.29; TASK-1
  7.30; TASK-2 8.41. H is not reported. DATO.
- Bagriantsev 2012 (PMID 22728824): Table 1 image viewed, "pHo IC50 +/- s.e." 7.51 +/- 0.05, footnote
  "Data from fits to the Hill equation"; the Hill coefficient is not tabulated. Same laboratory, same clones,
  same pH value: not an independent datum.
- Sci Adv 2020 (PMC7608817): Methods describe a Hill fit (22.5 C); no wild-type TREK-1 pH value in text or
  supplement. PMC6532698: patch clamp at 22-23 C, no Hill. Nothing at 30-37 C found.
Verdict: the absence of a stated Hill slope stands for every reached full text; the producer's list should
read "two papers from one laboratory (2011 supplement, 2012 Table 1), same pK 7.51, slope unstated".
Slope could only be fitted from Fig 2B-type raster data (INFERENZA). Sandoz 2009 and Cohen 2008 were not
requested again (producer's unreachable list). No pH-dependence study of ONO-TR-772, ONO-2920632, ML365-class
or AVE1231 was found (VQ06, VQ07, VQ13; titles and, for ML365, abstracts only).

D12. Catalogue rows (`ph_k2p_sci45_20261111/search/search_rows.tsv`): ONO-TR-772 Rat pIC50 7.82 (15.1 nM);
Cpd8l Rat 6.10; ONO-2920632 Human pEC50 5.55 (2.8 uM); AVE1231 Human 6.70 (0.2 uM); KU124 Human 5.85
(1.4 uM). Paper checks: ONO-TR-772 text says human MPC (the "Rat" is unsupported; the abstract's "rat Kp"
is a possible origin, INFERENZA); KU124 has no assay species; Cpd8l abstract has none (full text not
reached; PubMed MeSH lists Humans and Mice, indexer terms). Conversions match the papers.

## 5. Evidence rows and receipts

Rows E01-E13 checked against the source at the stated locator.
Correct (9): E01, E04, E05, E06, E07, E09, E10, E11, E13 (quotes verbatim; E09 restores "50" and the compound
name that PubMed strips, acceptable).
Defective, minor (4): E02 and E03 state "human recombinant" but SI Tables S2 and S3 give no species;
E08 "Supplementary Table 1: IC50 WT 0.2 +/- 0.1 uM, Hill coefficient 1.1 +/- 0.1" combines two table cells
and is not a verbatim quote (values correct); E12 "fitted to the Hill equation" is not verbatim (Table 1
footnote "Data from fits to the Hill equation"; Methods "fitted with a modified Hill's equation").
Class extension: species assertions and verbatim form checked on all 13 rows; only these four.
Other corrections: pointers.tsv T1 identifier cell and decisive.tsv D01 locator give "SI p. S28" for the
name; the chemical name of 14c is on SI p. S24, S28 is the 13c NMR page, S29 is the 14c NMR drawing (viewed,
4-F-phenyl as drawn). Fig 4 graphic gives "Mouse Kp = 0.46"; the text says 0.44 (not in the producer's tables).

Receipts. All five fingerprints reproduce exactly: 40365404 `0fd00694...`, 39981749 `822941d9...`, 40635742
`20709499...`, 41104520 `376b6c00...` (sha256 of bucket text) and 31001961 `56d8d698...` (publisher PDF).
Section lists are consistent with the figure notes except that figures are "captions_only" in four receipts
(39981749, 40635742, 41104520, 31001961) although figure_notes record images viewed (under-claim). My
receipts (event ids ending -85, `prior_receipt` set to the producer's -86 or -88 ids, `reread_reason`
adversarial_reanalysis; 21765396 first read) are in `receipts/`; validation result in `receipts/INDEX.tsv`.
Not recorded in the ledger.

## Not reached or not done

Cpd8l full text (not requested; producer's route returned 403). Sandoz 2009 and Cohen 2008 full text (not
requested). SI synthesis and PK of 40365404 (not read). Figures of 40635742 other than Fig 7, of 39981749 and
31001961 other than Fig 1 and Table 2/Fig 2 (not viewed). PMC11711774 and PMC6532698 were searched by text
only. Europe PMC REST returned a 503 on one query (not retried by another route). No bot check, 403 or 429
occurred in my routes. Route deviations: none; the publisher route for 31001961 is the producer's own.
