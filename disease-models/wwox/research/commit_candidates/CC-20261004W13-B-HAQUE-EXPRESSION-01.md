# CC-20261004W13-B-HAQUE-EXPRESSION-01 - PMID 42136830 re-read: the no-expression bound of CLAIM 047 survives every surface; three measured details sharpen it (regimen "none" with four excluded immunosuppressed animals, 28 of 47 animals analysed, a construct-confounded time trend)

`context_policy: QUESTION_DRIVEN` (re-read of owed figure panels and supplements, intake wave 13, 2026-10-04, Scientist B). **Not medical advice. WWOX occurs zero times in the source.**
**Change class: MINOR.** CLAIM 047 is `in observation`, not a `consolidated baseline`; the append qualifies a bound with measured detail and reverses nothing. PAPER 227's "T5 for anything about expression, which is absent" is confirmed and needs no edit.
**Target records:** `disease-models/wwox/registries/claim_registry_current.md` `CLAIM 047` (one `replace-within`).
Receipt: `FTR-20261004-42136830-02` (prepared, not recorded) - manifest PASS (26 locators) - dossier part 2.

## 1 - The negative tested (FIND-X)
"No expression was measured anywhere in the paper." Surfaces searched: running text; Figures 1-5 (all axes vg/ug DNA, vg/DG, dose, necropsy day); graphical abstract; Tables 1-2; Supplementary Figure S1 (route schematic); a five-page raw-data PDF (vector-genome means only). Not available/searched: the publisher PDF article. **The negative survives.** The authors give a reason for TSHA-102: RNA expression was not evaluated because the construct is designed to be silenced by a microRNA-responsive element in wild-type brain.

## 2 - Measured details the first reading did not carry
- Methods: "No immunosuppression was used." Table 2 footnote b: four further TSHA-101 animals given immunosuppressants are excluded from the analysis and appear nowhere else (47 + 20 vehicle + 4 = 71, the paper's own opening count).
- Table 2 marks the qPCR animals only by bold type: 4 + 6 + 3 + 7 + 8 = 28 of 47 treated (graphical abstract: 28 macaques). 19 treated animals have no data in the paper.
- Figure 5: one straight line through three points of different constructs (day 30 single-stranded TSHA-101; days 90 and 180 can only be TSHA-102, an inference); SD at days 90 and 180 is over six tissue samples, n = 3 animals.
- Pre-screen: animals with detectable neutralising antibody (e.g. >= 1:10) preferentially went to diluent-only; no per-animal titres.

## 3 - Op (record-scoped)
`CLAIM 047`, `replace-within` (paragraph "Bound — what the primate numbers are not"):
- `old` (verbatim, measured unique in CLAIM 047 and in the file): `covering **five** NHP studies)`
- `new`: `covering **five** NHP studies; wave 13 re-read every figure panel, Table 2, Supplementary Figure S1 and a raw-data sheet and found no expression, RNA, protein or histology readout on any of them; the authors add that RNA expression of the TSHA-102 construct would be silenced by design in wild-type brain, that the analysed animals received no immunosuppression while four immunosuppressed TSHA-101 animals are excluded from the report, that only 28 of the 47 treated animals have vector-genome data, and that the day-30/90/180 trend in the brain plots one line through different constructs)`

## 4 - Defaults taken
- No wording of PAPER 227 is changed. The inference that the Figure 5 day-90/180 points are TSHA-102 is labelled INFERENZA in the manifest and the dossier.
- Transfer limit retained: wild-type macaques, four non-WWOX cassettes, vector genomes only.

### LOCATOR TRIPLES FOR BLIND AUDIT
- (Analysis restricted to biodistribution | Analysis was restricted to vector biodistribution, rather than gene or protein expression | Discussion, Strengths and limitations, `files/fulltext/PMID42136830_Haque2026_PMC.xml`)
- (RNA expression was not evaluated | Hence, RNA expression was not evaluated in this report. | Discussion, Strengths and limitations, `files/fulltext/PMID42136830_Haque2026_PMC.xml`)
- (No immunosuppression in the analysed animals | No immunosuppression was used. | Materials and methods, `files/fulltext/PMID42136830_Haque2026_PMC.xml`)
- (Four immunosuppressed TSHA-101 animals are excluded | Four additional animals, treated with TSHA-101 along with immunosuppressants, are not included in this analysis. | Table 2 footnote b, `files/fulltext/PMID42136830_Haque2026_PMC.xml`)
- (28 macaques were assessed by qPCR | `[panel attestation]` Tissue samples from 28 macaques were taken from the brain and spinal cord and assessed via qPCR | `files/supplement/PMID42136830/fmed-13-1819594-gr0001.jpg`)
- (Day 90 and 180 points are means over six brain slices | The Day 90 and 180 data points each correspond to the mean (SD) vg/DG value for six brain slices. | Figure 5 legend, `files/fulltext/PMID42136830_Haque2026_PMC.xml`)

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261004_007` · 2026-10-04 · ACTOR_ID `scientist` (Scientist Q, batch integrator)
**Working model:** WM_v7.19 -> WM_v7.20 (MINOR)
**Class re-judged (§7):** MINOR (`CLAIM 047`, consolidated baseline — evidence-boundary text only)
**Blind locator audit (BEFORE propagation, auditor had not seen this candidate):** 6 triples — 6 SUPPORTED (two with flagged truncations)
**What landed, and what the audit changed:** The no-expression bound SURVIVES every surface: no transgene or WWOX expression measurement of any kind exists, and the paper names WWOX nowhere. Three bounds added by the audit: the *«no immunosuppression»* sentence scopes to three of the four vector programmes; the denominators reconcile at 51 dosed, 47 treated, 28 analysed, 20 vehicle; and the time trend is confounded by construct AND by region set (six regions in four animals at the first timepoint against two regions in three animals later).
**Status / Type / Summary:** unchanged by this candidate.
**Not medical advice.** Class level only; no individual-level record, no geography and no parent-of-origin detail is carried.
