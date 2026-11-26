# ADV-292, increment 1: result (SCI, 2026-11-26)

Non-canonical working note; hypothesis level; reference genotype class only; not medical advice. Five held partial records, ten repository sentences (S1a to S5). Frozen PREREG: `PREREG_ADV292_SCI_20261126.md` (sha256 `a002d131e0e19e404bfc75fac67c5deff294e228dce6b38e68e2b0efdbcfd780`). First reader: SCI. Blind sentence-level reader: `legend-delegate`, sonnet, effort high (asked in the prompt; read back **high x 55 of 55 turns** by `session_model_census.py`, 55 turns, 50,732 output tokens, birth context 24,956). Files looked at, with sha256: `FILES_VIEWED_ADV292_INC1_SCI_20261126.tsv`. Notes: `READER_NOTES_INC1_SCI_20261126.md`. Blind reports, verbatim: `BLIND_REPORT_INC1_SCI_20261126.md`.

## 1 Matching rule (PREREG section 5), applied

Strict = (a) first reader verified on a held file that the sentence as written is false or unsupported AND (b) blind reader MUST CHANGE. Only one of the two = listed separately with both readings. Loose = strict, or a window, dose, species, unit or evidence level must be added.

| id | record | first reader | blind reader | class of the held file | outcome |
|---|---|---|---|---|---|
| S1a | 39216838 | MUST CHANGE | MUST CHANGE | supplementary (Supp Fig S3 screen, 4 of 10 ligands raised total alpha1, ZK93423 lowered D219N) and main Fig 4B/7 (current HEK293T only; iPSC surface fluorescence and PLA only) | **STRICT** |
| S1b | 39216838 | ADD | ADD | text (binding taken from literature, not measured; 6 of 10 screened ligands did not rescue) | loose |
| S1c | 39216838 | ADD | ADD ("binds", "best-instrumented" untestable) | ledger line, not a consumer unit | loose, not counted |
| S2a | 40485335 | STANDS | MUST CHANGE under "class includes glycerol"; ADD under "class = 4-PBA" | main Fig 3B, 4D-E | **separate, reading-dependent**: the first MUST CHANGE came from my bracket, not the repository wording; the card's candidate is "4-phenylbutyrate class and bile-acid chemical chaperones" and bile acids are not in this paper |
| S2b | 40485335 | MUST CHANGE | MUST CHANGE | main Fig 6B ("not markedly altered" for wild-type hGAT-1 in fly glia); HEK293 wild-type blots unquantified | **STRICT** |
| S2c | 40485335 | STANDS | STANDS | main Fig 3B, 6C, 6E, 6G, 6H, Supp Fig 4C | stands |
| S3a | 41178115 | ADD | ADD | supplementary (Supp Fig S4 P260L has no current; mRNA control D219N only) and main Fig 5C (IXA105 surface bar unmarked) | loose |
| S3b | 41178115 | STANDS | ADD (25 micromolar toxicity noted, no viability data; wild-type alpha1 and CHOP only) | text and Supp Fig S1E, S2 | **separate**: first reader STANDS, blind ADD |
| S4 | 42268630 | ADD | ADD | supplementary workbook (dose labels, tetracaine mean cell) and main text (12-bp deletion) | loose |
| S5 | 41664646 | STANDS | STANDS (graph readings 0.358/0.269 m/s and 3.15/1.22 responses, within about 0.005 and 0.03) | main Figs 4, 5 | stands |

**Counts. Strict: 2 of 5 records (39216838, 40485335); 2 of 10 sentences judged (S1c is a ledger line and S2a is held apart).** Loose: 4 of 5 records (add 41178115 and 42268630). Figure-class strict: S2b (Fig 6B) and the current-and-iPSC half of S1a; supplement-class strict: the screen half of S1a (Supp Fig S3). For the PREREG prediction (3 of 10 strict, range 1 to 5, rejecting at 1 or fewer in ten), increment 1 gives 2 of its 5: the stop rule (0 of 5) is not triggered, so increment 2 proceeds.

## 2 One line per checklist class (ADV-276 recipe)

* **Window / dose.** 4-PBA doses differ by system in 40485335 (10 mM HEK293, 24 h; 1 mM fly food, 48 h); 42268630 states the dose three ways in one paper (text 25 and 50 micromolar; Fig 1D legend 10 and 25; workbook "mM"); 41178115 IXA554 and IXA105 only to 10 micromolar (toxic at 25).
* **Unit under n.** 42268630: nine larvae recorded in baseline and 45 to 60 min windows then compared as unpaired (df 16); 41664646: networks (n = 15, N = 5 chips) with two co-culture networks excluded and the legend n not reconciled; 41178115: blots 3 to 5 experiments, current 8 cells, iPSC 19 to 36 neurons from at least three differentiations.
* **Species / preparation / age.** 39216838 current is HEK293T only; iPSC heterozygous G251D line has surface fluorescence and PLA only; 40485335 fly arm (3 to 5 day old males) does not reproduce the HEK293 wild-type rise.
* **Test behind the p.** 42268630 stxbp1a vs tetracaine P = 0.9983 (assay floor not separated); stxbp1b ictal-like events unpaired t test P = 0.8593 with a 95 percent CI of -7.18 to 8.51; Fig 5C IXA105 in 41178115 has no asterisk although the text gives 2.3-fold.
* **All / every / none / absent.** S2b "every target" was the one absolute word that failed (Fig 6B); S1a "modulators" covered 4 of 10 ligands (screen printed in full, Supp Fig S3).

## 3 Own errors in this increment

1. The S5 block was empty in the first sentence file (my extraction slice returned nothing); the blind reader said so, and I resent it. Cost: one resume.
2. I added an interpretive bracket to S2a ("class = 4-PBA and the paper's other chemical chaperone"). It was mine, not the repository's, and it produced the MUST CHANGE reading; the result is therefore kept apart from the strict count.
3. First-reader note on 41178115 listed the three G251D surface folds without saying the IXA105 bar is unmarked; the blind reader caught it (addendum in the notes).
4. First reader called S2a STANDS and did not see the glycerol reading of "class"; the blind reader's two-reading answer is the better record.

## 4 What was not done

Supplementary information for 41664646 is not held (Supp Figs S2, S3, Videos S1, S2): its supplementary class stays not_read. Main figures of 39216838 and 42268630 and, apart from Fig 5, of 41178115 were not re-read in this event (receipts say so). No repository sentence has been edited: the consumers (cards, packets, investigations) are IT's; the proposed corrected wordings are in the blind report and notes and go to IT with the owed items.

## 5 Next

Increment 2 (39923817 tables only; 37946251; 40858643; 26419537; 31781019; reserve 36282524, then 42807679).
