# CC-20261004W13-B-WISEMAN-ANTIBODY-01 - PMID 39358605 re-read: "no antibody assay anywhere" is false as worded (an unnamed-antigen antibody-titre table exists for the wild-type primate study); "tested only in wild-type animals" survives every surface

`context_policy: QUESTION_DRIVEN` (re-read of owed figures and supplements, intake wave 13, 2026-10-04, Scientist B). **Not medical advice. WWOX occurs zero times in the source.**
**Change class: MINOR.** PAPER 167 is a corpus record and RL-GT-002 a research-layer line; neither is a `consolidated baseline` claim. The edit corrects one quantifier and keeps the line's thesis (the protein-naive host is untested) intact. (If the integrator reads RL-GT-002's sentence as load-bearing for a baseline claim, the change is MAJOR and the triples below are the blind-audit set; nothing here edits a baseline.)
**Target records:** `disease-models/wwox/registries/paper_registry_current.md` `PAPER 167` (one `replace-within`); `disease-models/wwox/research/research_lines_current.md` `RL-GT-002` (one `replace-within`).
Receipt: `FTR-20261004-39358605-02` (prepared, not recorded) - manifest PASS (26 locators, 26 artefacts) - dossier part 2.

## 1 - The negatives tested (FIND-X)
Quantifiers: "no antibody assay **anywhere**"; "**only** wild-type". Surfaces searched (antibod*, ADA, NAb, neutraliz*, ELISA, IgG, IgM, ELISpot, titre/titer, immun*, cytokine, interferon): running text; Figures 1-9; Figures EV1-EV5 (from the Expanded View PDF; the PMC images for EV1-EV3 are byte-identical copies of Figures 3, 7 and 9); Appendix text (pages 23-35 read, pages 24 and 33 rendered); peer-review file; the member names of the nine source-data archives (no deposit exists for any Expanded View figure). Not read: workbooks inside the archives.
- **"No antibody assay anywhere" FAILS.** Appendix pages 33-34: "Humoral immune response - Antibody titer", per animal, pre-dose, day 7, day 29, day 113; 13 cynomolgus animals (4 vehicle, 3 low, 6 high); every treated animal at least 3,540 by day 7 (ceiling printed >6250); nine of 13 with a numeric pre-dose titre, four negative; vehicle titres flat and non-zero. The antigen is **not named**; the main text calls the NHP findings "minor and well-established immune responses to AAV9". No antibody to the transgene product is reported anywhere.
- A cellular immune assessment is scheduled ("Cellular and Humoral") and no cellular result is listed.
- **"Only wild-type" SURVIVES.** Knockout cohorts (Figures 3-7, EV2-EV4) carry no immune panel; every immune readout is in wild-type animals.
- Mouse ELISpot: n = 4 in Methods, n = 3 per group in the EV5 legend; the EV5 title says "no B cell response" for a T-cell interferon-gamma assay.

## 2 - Ops (record-scoped)
### Op 1 - `PAPER 167`, `replace-within` (Role)
- `old` (verbatim, measured unique in the file): `with an interferon-gamma ELISpot and no antibody assay anywhere`
- `new`: `with an interferon-gamma ELISpot (n = 4 in the Methods, n = 3 per group in the Figure EV5 legend, whose title says «no B cell response» for a T-cell assay) and no assay for an antibody to the transgene product anywhere (a per-animal antibody-titre table exists in the Appendix for the wild-type cynomolgus study: 13 animals, antigen not named, the text calling it a response to AAV9; the cellular immune assessment its schedule lists has no result table)`

### Op 2 - `RL-GT-002`, `replace-within`
- `old` (verbatim, measured unique in the file): `with an interferon-γ ELISpot and **no antibody assay anywhere**`
- `new`: `with an interferon-γ ELISpot and **no assay for an antibody to the transgene product anywhere** (a per-animal antibody-titre table exists in the Appendix for the wild-type cynomolgus study, antigen not named; the main text calls it a response to AAV9)`

## 3 - Defaults taken
- The thesis of RL-GT-002 (the protein-naive host is the unmeasured parameter) is unchanged: the antibody table is from a wild-type primate and names no transgene-specific antigen.
- DRG findings in the Appendix incidence table are in the dossier for DIS-031 awareness; no DIS record is edited.

### LOCATOR TRIPLES FOR BLIND AUDIT
- (The ELISpot is run in wild-type mice | Mice were sacrificed at 3 months and splenocytes were extracted, dissociated and ran through an ELISpot immunoassay against the hAP4B1 transgene peptides (n = 4). | Methods, ELISpot safety study, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)
- (The EV5 title says no B cell response | AAV9/hAP4B1 treatment generated no B cell response to the hAP4B1 peptides | Figure EV5 title, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)
- (The NHP conclusion cites immune responses to AAV9 | minor and well-established immune responses to AAV9 | Results, NHP safety, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)
- (A humoral antibody-titre table exists for the NHP study | Humoral immune response Antibody titer | Appendix pages 33-34, `files/supplement/PMID39358605/44321_2024_148_MOESM1_ESM.txt`)
- (The low-dose row | F 220013005 180 >6250 5131 >6250 | Appendix antibody-titre table, `files/supplement/PMID39358605/44321_2024_148_MOESM1_ESM.txt`)
- (A vehicle animal has flat non-zero titres | F 220013003 141 86 98 86 | Appendix antibody-titre table, `files/supplement/PMID39358605/44321_2024_148_MOESM1_ESM.txt`)
- (A cellular and humoral immune response is scheduled | Immune response X X X X X Cellular and Humoral) | Appendix schedule of events, `files/supplement/PMID39358605/44321_2024_148_MOESM1_ESM.txt`)

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** **MAJOR contingency, judged MAJOR as a candidate and landed as evidence-boundary text only** (`PAPER 167`, `RL-GT-002`)
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 7 triples — 7 SUPPORTED, over 29 enumerated surfaces
**What landed, and what the audit changed:** The contingency is CONFIRMED: *«no antibody assay anywhere»* is FALSE as worded — an appendix table of per-animal antibody titres covering 13 wild-type primates at four timepoints exists, naming no antigen, no platform and no units, and never cited in the main text. *«Tested only in wild-type animals»* is TRUE and the source names both animal sets as wild-type. Added: the schedule of events promises a CELLULAR primate read-out at five timepoints that is reported nowhere. No `Status`, `Type` or `Summary` moved.
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
