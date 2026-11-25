# RESULT ADV-287: error rate of fold, ratio, range, percent and "versus" statements in the cards (SCI, 2026-11-25; hypothesis level; reference genotype class only; not medical advice)

Frozen before any source was opened: `PREREG_A_ADV287_SCI_20261125.md` (hash 0d0f2fae45055823, 22:03:28Z) and `PREREG_B_ADV287_SCI_20261125.md` (hash e0275945644cda73, 22:04:43Z; counted universe, strata, seed 287, sample, screen rule). Files: `universe_adv287.py` and `.tsv`, `route_counts_adv287.tsv`, `sample_adv287.py` and `.tsv`, `sample_screened_out_adv287.tsv`; `producer/` (STEP1_TABLE_ADV287.tsv, src_01 to src_21.md, PRODUCER_NOTE.md; producer: legend-delegate, sonnet, effort high, 22 minutes, 136 plus 10 tool calls); `BLIND_REPORT_ADV287_SCI_20261125.md` (blind reader: legend-delegate, sonnet, effort high; it received the verbatim sentence and the extracted source material, not the producer's classes).

## 1. Answer

**The rejecting observation was NOT met: the cards are not in better shape than the sheets.** Of 20 sampled statements (12 card families), 3 were NOT ASSESSABLE and 17 were assessable. **Six of the 17 (35 percent; exact 95 percent interval 14 to 62) are INCOMPLETE or WRONG by both readers** (n=1, 2, 3, 14, 15, 20); the producer adds n=16 (7 of 17, 41 percent), the blind reader calls it CORRECT. Sensitivity: 5 of 17 (29 percent, 10 to 56) if n=20 is read as a statement about the label alone, 6 of 17 as above, 7 of 17 (41 percent, 18 to 67) with n=16. Every reading is above 10 percent; the lower interval bound is 10 to 18 percent. HE's 27 percent on the sheets and my 41 percent on null-note sentences sit inside the range.

## 2. Counts, predictions and verdicts

| | observed | PREREG A prediction | verdict |
|---|---|---|---|
| universe, union after de-duplication | 302 (route 1: 188; route 2 only: 114); 239 after excluding five IT-re-derived cards (62) and two Obeid-mention sentences | 250 to 500 | inside |
| route 1 share of the union | 62 percent | 40 to 70 | inside |
| not assessable of 20 | 3 (n=11 label and Reisman 2019 not held; n=18 a proposed design, no quantity; n=19 two abstracts not held) plus the Obeid-only draw (n=7), replaced by reserve 15 (n=21) | 3 to 8 | at the lower edge |
| INCOMPLETE-or-WRONG of the assessable | 6 of 17 (35 percent), 5 to 7 | central 25, range 10 to 45 | inside, above the central value |
| class mix | blind: INCOMPLETE 4 (n=1, 2, 14, 15), WRONG 2 (n=3, n=20, both borderline INCOMPLETE); producer: INCOMPLETE 7, WRONG 0 | INCOMPLETE at least as common as WRONG | held |
| rejecting observation (10 percent or below) | not met | | audit continues to step 2 |

Concentration limit: card family H02 supplied 7 of the 20 draws (it holds 40 of the 239 statements) and 3 or 4 of the errors; the estimate is for the pooled universe by the proportional rule, not for each family.

## 3. The seven statements that carry the error (verified by me on the held text where marked)

* **n=1 (H02, batch B1: "three independent centres put the rate ... between 22.1 and 44.7 percent"), INCOMPLETE by both.** The batch table and held full texts carry at least seven centres with an imaged-child rate (Beijing, Emory, Dammam, Toronto, Washington DC, UCLA 2024, Dutch registry; UCLA 2017 6 of 40 = 15.0 percent lies below the stated range); the Beijing 22.1 percent is 38 of 172 after dropping 193 imaged children with more than a year of exposure.
* **n=2 (A01, "8 to 78 times the class's HDAC enzyme IC50"), INCOMPLETE by both.** 8.3 to 78.1 is phenylbutyrate on HDAC1 and HDAC6 at 2 and 5 mM only; across all applied levels (0.5 to 10 mM) and all recombinant IC50s (64 to 260 micromolar) the span is about 2 to 156; butyrate in the same precedents gives 6.7 to 312.
* **n=3 (H02, "the one cohort reporting its exposed denominator gives about 26 percent"), WRONG by the blind reader (a count), INCOMPLETE by the producer.** Beijing (533), UCLA 2024 (108), Toronto (95, derived) and the Dutch registry (80) also give a treated denominator; Dammam's 34 of about 132 is derived from 57.6 percent. The per-exposed spread is about 7 to 26 percent.
* **n=14 (A02, "one not at all in the mouse (T191M), a stable but inactive allele (G307S) not at all"), INCOMPLETE by both.** The paper says bortezomib "seemed to stimulate a very small amount of enzyme activity" for T191M, and G307S was not tested there (an Introduction clause on earlier work, reference not held).
* **n=15 (B01, "largest genotype-classified cohort", 56.8 percent null/null), INCOMPLETE by both.** The 2025 cohort classifies 44 of 50 (25 of 44); Oliver 2023 classifies 75 (45 of 75 = 60.0 percent); the repository's own repair record M9 already states the 75 against 50.
* **n=20 (H02, "the age range of the N=205 study is not stated"), WRONG by the blind reader, INCOMPLETE by the producer.** The card's other assertion (DR-H02-029) holds the study abstract, "infants aged 24 months or less"; the sentence is true only as a statement about the label alone, and I checked that the card prints it in the developmental-stage field of the same assertion that holds the label locator.
* **n=16 (H02, "rodent and dog lesions at doses inside the human range, but vacuoles in neonatal and juvenile rats ... distinct"): contested.** Label 5.4 says the adult intramyelinic edema was seen at doses within the human range; label 8.4 says the neonatal and juvenile effects occurred at plasma levels substantially lower than those reached clinically in infants and children. The producer calls the sentence INCOMPLETE (the young-animal comparator is left out), the blind reader CORRECT. Counted only in the sensitivity range.

Verdicts of correctness the readers agree on: n=4, 5, 6, 8, 9, 10, 12, 13, 17, 21 (the whole-table checks of n=4, 12 and 17 and the figure-by-eye checks of n=9 and 13 are in `producer/src_*.md`).

## 4. Step 2: corrected sentences for IT, and the stated extension

Corrected sentences for n=1, 2, 3, 14, 15 and 20 (and 16 as an optional rewording) are in `producer/STEP1_TABLE_ADV287.tsv`, column `corrected_sentence`, and are the wording for IT; n=3 and n=1 must keep "derived" beside every denominator the sentence derives (Dammam 34 of about 132; Toronto 25 of 95).

**Extension (which strata next):** (1) a full pass of every statement of card family H02 (40 statements; 3 or 4 errors in 5 to 6 assessable draws) and of A01 (20); (2) a pass of the 22 statements of the universe that carry a superlative or count word ("the one", "the only", "largest", "three independent", "none", "at least"; H02 5, A01 3, E02 3, K01 3, F04 2, others 1 each; `universe_adv287.tsv`): four of the six agreed errors use such a word ("three independent", "the one cohort", "largest", "not at all"); (3) then a second random sample of 20 from the remaining families.

**Decision for the card-edit recipe:** a mechanical check enters it: before a card sentence uses "the one", "the only", "largest", "N independent", "not at all" or "not stated", print all rows of the source table and every other cohort or document in the same batch table, and count them; and a fold, ratio or range is written over all rows or says which rows it covers. This is a wording rule, not a new gate.

## 5. Limits

The blind reader was not fully blind: the extracted source files carried the producer's prose commentary (the reader was told to ignore it and re-derived from the tables and held primaries; one grep of the reader's own surfaced a single producer line identical to the material given). The producer's side finding that Table 1 of Yadav 2022 gives p = 0.085 does not reproduce (blind reader: 0.119 chi-square, 0.164 Fisher) and is not carried. Reading depth is abstract for n=5, 6 and 20, abstract bytes not held for n=8, an absent article for n=10, a manifest only for the 2025 article of n=15, and figure by eye (about 10 percent) for n=9 and 13. n=19 (anakinra, 73 percent of the 52 treated or of 75) and n=11 (omaveloxolone label) stay unresolved until the held bytes exist. One family supplied 7 of 20 draws. The Obeid 2026 article was not opened (n=7 was replaced by the next reserve before reading).
