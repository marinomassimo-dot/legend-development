# ADV-292, increment 2: result, and the cumulative count for the batch (SCI, 2026-11-26)

Non-canonical working note; hypothesis level; reference genotype class only; not medical advice. Five held partial records (39923817, 37946251, 40858643, 26419537, 31781019), eleven repository sentences or sentence groups (S6a to S10). Frozen PREREG: `PREREG_ADV292_SCI_20261126.md` (sha256 `a002d131e0e19e404bfc75fac67c5deff294e228dce6b38e68e2b0efdbcfd780`). First reader: SCI. Blind sentence-level reader: `legend-delegate`, sonnet, effort high (asked in the prompt; read back in the census block below). Files looked at, with sha256: `FILES_VIEWED_ADV292_INC2_SCI_20261126.tsv`. Notes: `READER_NOTES_INC2_SCI_20261126.md`. Blind report, verbatim: `BLIND_REPORT_INC2_SCI_20261126.md`. Receipts: `RECEIPT_ADV292_INC2_*` (event ids `FTR-20261126-<pmid>-02`).

## 1 Matching rule (PREREG section 5), applied

| id | record | first reader | blind reader | class of the held file | outcome |
|---|---|---|---|---|---|
| S6a, S6b | 39923817 | STANDS | STANDS | article text (no image or supplement held); the only in-article table is Key Resources | stands |
| S7a, S7b, S7c | 37946251 | STANDS | STANDS | Table 1 image, Table S7 (Additional file 3), text | stands |
| S8a | 40858643 | ADD (PP3 treated as a wording point) | MUST CHANGE (one parenthetical: PP3 is on the SNV only, the exon-5 CNV is PVS1, PM2, PM3) | Supplementary Data 1 and 2 | **separate, reading-dependent**: on the natural reading (each allele carries the whole list) the sentence is unsupported for one allele and would be strict; on the union reading it is true. The first reader's frozen verdict was ADD, so it is not counted strict |
| S8b | 40858643 | ADD | ADD ("intron-5 acceptor" is not in the source; the CLAIM 033 text already says it is the repository's derivation, the PAPER 219 Transferability line does not) | Supplementary Data 1 (variant type "Exonic or near-exon variant") | loose |
| S8c | 40858643 | STANDS | STANDS | Supplementary Data 1 and 2, text | stands |
| S9 | 26419537 | ADD | ADD | Table S1 (supplementary), Fig 2, Fig S1 | loose |
| S10 | 31781019 | MUST CHANGE on the paper's own outlier exclusion | MUST CHANGE | Supplemental Table 1 (per-mouse counts, supplementary) and Fig 11 | **STRICT**, stated with its reading: with the one wild-type mouse the paper removes from the cortical analysis excluded, ethosuximide moves simple cortical spikes up in wild type (14.3 to 24.6 per hour, 4 of 5 mice) and down in APP/PS1 (48.7 to 35.4, 6 of 8); four other classes agree in sign. If that mouse is kept, cortical agrees and the sentence still needs an ADD (spike-wave discharges mixed, significance differs by genotype, no genotype-by-drug test) |

**Counts, increment 2. Strict: 1 of 5 records (31781019).** Loose: 3 of 5 (add 40858643 and 26419537). Separate: S8a. Sentences judged: 11 groups, strict 1.

## 2 Cumulative count for ADV-292 (ten records, two increments)

| | records | records strict | records loose (strict or ADD) | sentences strict |
|---|---|---|---|---|
| Increment 1 | 5 | 2 (39216838, 40485335) | 4 | 2 (S1a, S2b) |
| Increment 2 | 5 | 1 (31781019) | 3 | 1 (S10) |
| **Total** | **10** | **3** | **7** | **3** |

Against the PREREG: prediction 3 of 10 strict, range 1 to 5, rejecting observation at most 1 of 10. **Observed 3 of 10, equal to the prediction and inside the range; not rejected.** If S8a is counted strict on its natural reading the total is 4 of 10 (still inside the range). Held apart and not counted: S2a (reading-dependent, my bracket), S3b (first reader STANDS, blind ADD), S8a. Figure-class and supplement-class yields separately: supplement-class strict 2 (S1a screen on Supp Fig S3; S10 on Supplemental Table 1); figure-class strict 1 (S2b on Fig 6B) plus the current-and-iPSC half of S1a on main Figs 4B and 7. By record: the two supplement-class strict records are 39216838 and 31781019; the one figure-class strict record is 40485335 (assigned class supplementary, but the change rests on the main Fig 6B).

## 3 One line per checklist class (ADV-276 recipe)

* **Window / dose.** 26419537: the cca-1 test is on ethosuximide 1 mg/ml from conception; 31781019: ethosuximide 200 mg/kg intraperitoneal 30 min before a 3 h recording, within-animal and counterbalanced, washout at least 6 days.
* **Unit under n.** 31781019: animal (8 APP/PS1, 6 wild type; each mouse a 3 h session; the drug-effect degrees of freedom show 4 to 6 wild-type mice per class); 26419537: worms, 52 to 131 per arm; 39923817: rats (n = 5 to 12 per group), cells 17 to 22 from 4 rats.
* **Species / preparation / age.** 39923817: rat NAc by AAV and HEK293T, no human neural cell; 31781019: male mice 5 to 6 months; 26419537: C. elegans Tau V337M (cca-1 test) and dnj-14 (daf-16 test), different models.
* **Test behind the p.** 31781019: one-way repeated-measures ANOVA within genotype, no genotype-by-drug interaction (a two-way mixed model "could not be used"); 39923817: Fisher's LSD after one-way ANOVA for the cued-seeking contrast; 26419537: log-rank, and the text's 25 and 16 percent for the Tau lifespan gains do not match Table S1 (29.26 and 26.62 percent).
* **All / every / none / absent.** "Same-direction ... for the spike classes present in both" failed for one of five classes; "no RNA or protein" for the two WWOX cases is a dated negative on the held article text and tables (Additional file 1 of 37946251 not opened; for 40858643 the supplementary PDF was searched, the workbooks read only at the case rows); "no SLC2A1 or glucose readout" in 39923817 is a negative on the article text only (supplement not held).

## 4 Own errors in this increment

1. First-reader notes had said the two CLAIM 033 workbooks were read as workbooks; they were read through the held derived row extracts and searched by sharedStrings. Corrected in the notes and in the receipts' wording before recording.
2. My notes named the first author of 39923817 as Wiseman and the file of 31781019 as Kam; the article XML says Wood and Gureviciene (corrected).
3. The first draft of the S10 reading kept the wild-type outlier mouse and showed agreement; excluding it, as the paper itself does for the cortical class, reverses the sign. Both readings are reported.
4. 39923817 was assigned as tables only; its XML holds a single in-article table (Key Resources), and the Statistics Table is supplementary and not held. The class cannot be met on this file; the receipt records abstract, results, tables and discussion as read and figures, supplementary and limitations as not read.

## 5 What was not done

No repository sentence has been edited: consumers (investigations TSVs, discovery ledger, paper and claim registry) belong to IT and to the BATCH_COMMIT path; the corrected wordings are in the blind report and notes. Reserve records (36282524, 42807679) were not needed: all ten were readable. Supplements of 26419537 other than Table S1 and Fig S1 (Dataset S1, Figs S2 to S13) and of 31781019 beyond the per-mouse table were not opened; 41664646 has no supplement held.

## 6 Delegate census


Increment 2 delegate (`a00e30e5…`): asked sonnet, effort high stated in the prompt; read back sonnet x 32 of 32 turns, effort high x 32 of 32; 32 turns, 31,852 output tokens, birth context 24,850, peak 174,637, cache read 3,008,196. Increment 1 delegate (one resume included): sonnet x 55, effort high x 55; 50,732 output tokens, birth context 24,956, peak 245,834, cache read 7,644,090.
