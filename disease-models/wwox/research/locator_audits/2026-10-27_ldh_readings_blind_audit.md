# Blind audit of the stiripentol / LDH readings (package W1.3), 2026-10-27

Class-level, public, de-identified, not WWOX evidence, not medical advice. Auditor is not the producer. Audited: `drug_repurposing/ldh_readings_w13_locators_20261027.md` (54 triples), `sada_ldh_precedent_p2a_20261026.md` sections 0, 2.2, 2.3, 7, 8, and `CC-20261027-SCIENTIST-D-LDHREADS-01.md`.
Limit on blindness: the triples came bundled with the producer's propositions and conclusions, so the five "correction" triples were judged by reading their source passages first, but the auditor had seen the producer's framing.

## Acquisition (own, public routes)
- Guyon 2022 (PMC9728051), Bouchez 2026 (PMC13080466), Bacq 2024 (PMC10960919): Europe PMC fullTextXML, fetched fresh today.
- Le Dudal 2019 (PMC6538379): public PMC article page, fetched fresh.
- Yadav 2026 (PMC13267918, not open access, Europe PMC returns HTTP 500 for full text): the persisted artefact `files/fulltext/PMID42035940_GBM2026_PMC_r2.xml` only. SHA-256 of all five persisted artefacts matches the hashes in the producer's table.
- Bouchez Supp Fig 2: `files/supplement/PMID41570991_r2/mmc1.pdf` page 2; Fig 5: `files/figures/PMID41570991_r2/gr5.jpg` (780 px wide, no larger render obtained).
- Mechanical check: my own whitespace-normalised exact match of all 54 quotes against the fresh text: 54 of 54 present (four, Y2, B2, Q5, Q7, only after removing tag-induced whitespace). Producer's "54 of 54" confirmed.

## Blind-audited triples (the five carrying corrections)
| # | Verdict | Basis |
|---|---|---|
| B2 | SUPPORTED (text quote and the text-versus-figure discrepancy) | Quote verbatim. Supp Fig 2 vector/raster check below: about 50 to 58 percent at 100 uM, not 70. |
| B5 | SUPPORTED | The sentence is the last of the Results section "Stiripentol is a complex I inhibitor", right after the intact-mitochondria data (Fig 5E-F), and conflicts with that heading and with the Discussion ("directly inhibits complex I"). Uncertainty, not error: the sentence may be a drafting remnant; "directly or specifically" is not the same as "inhibits". The same paragraph says succinate respiration rose, as with rotenone, which cuts against "unlike rotenone". |
| G4 | SUPPORTED | Methods sentence verbatim and it is the bevacizumab/phenformin schedule sentence; only 100 mg/kg appears in the Methods; 150 mg/kg occurs only in Results and Fig 6F legend (my regex over all "mg/kg" strings). Addition the producer did not make: that Methods sentence sits in a paragraph on the LDH-KO implantation cohorts with n = 8 per survival group, whereas the legend gives n = 15 to 16 for the stiripentol P3 experiment. The Methods therefore probably do not describe the Fig 6F cohort at all; discrepancy not established either way. |
| L4 | SUPPORTED as a quote, but OVERSHOOT in the note | Results "200 mg/kg/day ... 48 hours" versus Methods "200 mg/kg ... twice orally by gavage", urine taken 48 h after start. "Twice" over 48 h is exactly 200 mg/kg once a day for two days, so the two statements are most simply consistent. Note 2.3's "so possibly 400 mg/kg/day" is the less likely reading; wording should say "dosing schedule not fully specified". |
| Q7 | SUPPORTED as quote; the proposition and the CC UNDERSHOOT | The quoted Table 2 string has three LDH rows: LDHA/B 500 [69 Sada], oxalate synthesis 42 to 427 [74 Le Dudal], lactate production LDHA/B 500 [70 Guyon 2022 (checked in the reference list)]. The proposition names two; the CC and note section 8 say the range "is two sources". It is three; Guyon's 500 uM is the same concentration printed in cells, so the range 42 to 500 stands but its provenance is Sada (second-hand), Guyon (cellular lactate), Le Dudal (indirect oxalate). Error of omission, small. |

## Sample of the rest (22 triples, all five papers)
| # | Verdict | Note |
|---|---|---|
| Y1 | SUPPORTED but see Y-note | Cells are treated in the dish, then lysed and assayed. |
| Y3 | SUPPORTED | Quote verbatim; enzyme source after "lysates were then added" is ambiguous (UNVERIFIABLE which). |
| Y4 | SUPPORTED | Fig 1E not available to either of us: size of inhibition UNVERIFIABLE_SURFACE. |
| Y6 | SUPPORTED | Authors say "at least a partial role". |
| Y7 | SUPPORTED | Concentrations come from Y8 not from the quote. |
| Y8, Y9 | SUPPORTED | |
| G1 | SUPPORTED | |
| G5 | SUPPORTED | |
| G8 | SUPPORTED | INFERENZA on non-phenocopy stands; KO versus drug in different conditions. |
| G9 | SUPPORTED | |
| G10 | SUPPORTED | |
| B1 | SUPPORTED | |
| B7, B8 | SUPPORTED | 150 uM legend versus 50 uM Methods real. |
| B9 | SUPPORTED | |
| B11 | SUPPORTED | "200 mM" in Fig 5C/D legends. |
| B13 | SUPPORTED | Authors add "reversible inhibitor, for short-term incubation". |
| L1, L2, L5 | SUPPORTED | |
| L6, L7, L8 | SUPPORTED | "mice" for rats confirmed; n = 8 vs 40; patent footnote. |
| L10 | OVERSHOOT (minor) | The quoted "5 to 100 ug/ml" overlaps the 4 to 22 ug/mL serum range at its low end; only the upper part exceeds it. "Exceeds" in the CC and 2.2 should read "extends above". |
| Q1, Q3, Q4, Q5, Q6, Q8 | SUPPORTED | |
| Q9 | SUPPORTED (quote) / affiliation proposition not in the quote | Biocodex affiliation and funding are in the front matter and Funding statement (verified), not in the quoted sentence. |

Not sampled: Y2, Y5, Y10 to Y12, G2, G3, G6, G7, B3, B4, B6, B10, B12, L3, L9, Q2 (mechanically present only).

## Y-note (a finding about the use of Yadav in the inference)
Yadav Methods: U87 cells are treated with stiripentol in culture (duration not stated), then lysed, and the lysate is assayed. Stiripentol is a reversible inhibitor per Bouchez, so the assay is not a clean cell-free dose-response of the enzyme with the drug present at the nominal concentration; it reports LDH activity after cell exposure. Note 2.2 calls LDH assays "cell-free" and uses Yadav as the cell-free LDH comparator. That is a mislabel; Yadav is a treated-cell lysate readout.

## Independent figure readings (Bouchez 2026)
Method: Fig 5 is a 780 px JPEG (no vector content). Bar tops measured by pixel scan against the NADH = 100 bar and baseline; values below are bar means. Supp Fig 2 page 2 is an embedded 5434 x 2691 raster with only axis ticks as vector, so I read bar heights from the full-resolution crop against the 0 to 80 axis (vector tick geometry gave no data). Unresolvable at this resolution: individual points.

Fig 5A (permeabilised mouse heart, NADH-driven, percent of NADH condition): 25 uM about 48; 50 about 24; 75 about 9; 100 about 5; 125 about 3; 150 about 1.
Fig 5B (liver): 25 about 67; 50 about 53; 75 about 41; 100 about 36; 125 about 30; 150 about 23 (pixel tops are 2 to 3 px low).
Producer F1/F2 values (47, 25, 10, 5, 3, 1; 67, 55, 44, 38, 32, 24): agree within a few points. SUPPORTED.
Requested figures: percent respiration remaining at 25 / 100 / 150 uM, heart about 48 / 5 / 1; liver about 67 / 36 / 23. Half effect heart at or just below 25 uM (not bracketed: lowest point is already below half), liver about 60 to 75 uM.
Supp Fig 2 (uncoupled respiration): 2405 control about 64; 50 uM about 46; 100 about 30; 200 about 12; 500 about 5.7; antimycin about 4.7. 1578 control about 52; 43.5; 25.5; 11; 7.5; antimycin about 6.3. Inhibition at 100 uM: 53 percent (2405) and 51 percent (1578) raw; 57 and 58 percent net of antimycin. At 200 uM: 81 and 79 raw, 88 and 89 net. Producer F6 SUPPORTED (text's "70 percent at 100 uM" overstated versus figure by 12 to 19 points; "90 percent at 200 uM" fits the net value).
Note: Fig 5 normalises to the NADH condition per experiment (so the NADH bar has no variance) and the y axis is "percent endogenous-AA".

## Judgement on "complex I looks more potent than LDH in cell-free systems"
Verdict: NEEDS WORDING CHANGE (directionally supported, "more potent" overshoots).
- What is supported: in the readings, stiripentol effects on NADH-driven respiration of isolated mouse mitochondria appear at 25 to 100 uM, whereas LDH inhibition appears only at 250 to 500 uM (Yadav) or about 10 to 38 percent at 500 uM (Rico-Molina as quoted by the producer, not re-read here). The ordering of effective concentrations is real.
- What overshoots: no LDH IC50 exists (the note itself says so), so "more potent" and "several-fold" compare a measured half effect with a bound. Different species and preparations (freeze-thawed mouse organelles versus human recombinant enzyme versus treated U87 lysate, see Y-note); Yadav is not cell-free; mitochondrial protein amount and drug binding affect nominal concentrations; no head-to-head assay; and Bouchez itself contains the contradictory sentence B5, plus an INT/duroquinone dose discrepancy (150 versus 50 uM).
- Suggested wording: "In the sources read, effects of stiripentol on NADH oxidation by isolated mouse mitochondria occur at lower nominal concentrations (25 to 100 uM) than the LDH inhibition reported in a treated-cell lysate and on recombinant enzyme (250 to 500 uM). No assay compares them directly; potencies are not comparable." Label INFERENZA, two-sided caveat kept.

## Errors versus uncertainty
Errors: (1) Q7 and CC item 5 "two sources" should be three; (2) note 2.2 "cell-free" for the Yadav assay; (3) note 2.3 "possibly 400 mg/kg/day" is the less natural reading (L4); (4) L10/CC "exceeds" should be "extends above"; (5) potency wording above. None touches a quote or a figure reading.
Uncertainty (not error): Yadav Fig 1E size; B5 intent; G4 whether the Methods cohort is the Fig 6F cohort; second-hand 2015 report; pixel readings of a 780 px figure (about +/- 3 points).
