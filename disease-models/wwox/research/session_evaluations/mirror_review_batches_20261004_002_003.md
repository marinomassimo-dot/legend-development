# MIRROR ex-post review — BATCH_20261004_002 and BATCH_20261004_003

`REVIEW_ID` MIRROR-20261004-BATCH20261004002-003 · `OBJECT` **two consecutive batches**:
`BATCH_20261004_002` (intake wave 8, `WM_v7.14` → **`WM_v7.15`**, 11 candidates, landed `bdc61a0`;
report `2026-10-04_BATCH_20261004_002.md`) and `BATCH_20261004_003` (intake wave 9 + the four
Mirror repairs, `WM_v7.15` → **`WM_v7.16`**, 17 candidates, landed `ce4aa9c`; report
`…_003.md`) · measured on `main` at **`ce4aa9c`**, which contains both · `LEVEL` ex-post review on
the author's request (`_003` *Recommended next actions* item 1) plus the `D6` classification
reserved to Mirror · `REVIEWER` ACTOR_ID `mirror` · `AUTHORS` ACTOR_ID `scientist` (Scientist L and
Scientist M) · `ADJUDICATOR` the authors, as new tasks.

> **Mirror is not a gate (`DEC-20260905-AGILE-HARNESS-MODE`, `LEGEND_CORE` §21e).** Every finding
> is a **new task for the author**, never a hold on a landed change. `CONFIRMED` means "no defect
> found given the available evidence bundle", never "true". READ-ONLY toward every registry: this
> review writes one file and five candidate files and edits no canonical record. **Not medical
> advice.**

**Method.** Registry records were addressed by heading span and printed field by field, never by
grepping the two large registries as text. Artefacts in the root `files/` tree were read read-only
through scripts that strip JATS tags and print bounded keyword windows, single addressed table
cells and front-matter contrib groups. Every ratio below was recomputed from the two numbers its
record names; the two F-tests were recomputed from the printed F and degrees of freedom with a
local incomplete-beta implementation (no `scipy` on this deployment). A safety classifier halted
one turn — a plain `Read` of the first 220 lines of the `_002` report. It was **not reworded or
retried**; the rest of both reports was read through a line-slice script, and every later read used
the same route.

---

## STEELMAN (first)

- **Where I could re-measure a number independently, the two batches were right to the last digit,
  including numbers no gate in this repository can see.** `De 2025` Table 4, recomputed from the
  supplementary cells rather than read: **559** distinct WWOX probe locations for the drug-response
  phenotype (exact), best LRR p **1.68e-4** at chr16:78,383,363 — *inside* the deletion interval the
  record names — against a Bonferroni threshold of 0.05/559 = **8.94e-5**, best genotype-based p
  **4.92e-3**, and **14,283 unique rows of 16,980** — the record's own figure, which I reproduced
  only on the fourth projection I tried. A reading that survives being re-derived by a hostile
  script is a different object from one that survives being re-read.
- **Grubor 2025 is carried at the strength the artefact prints, both ways.** *«2/3 vs 1/3, 3/3 vs
  1/3, 3/3 vs 1/3»* and *«10 of 26»* / *«1 out of 29»* / *«11 of 36 DRGs; 3 of 3 subjects»* /
  *«one finding of mild severity of 36 DRGs»* are the paper's own sentences; 38.5/3.4/30.6/2.8 %
  recompute; and the rejected proposition that immunosuppression **bounds** DRG risk is **not
  revived**, with the reasons (n = 3, 43 days, sponsor, residual lesions) stated in `DIS-031`.
- **Thomsen Table S3 verified cell-wise.** `8.00E+11 → 2.00E+13 vg/mL → 2.00E+14` is the printed
  row; 8.00 × 10¹¹ / 0.04 mL = 2.00 × 10¹³ and × 10 mL = 2.00 × 10¹⁴; the 250-fold factor is
  10/0.04. The debt retires as **not printed** — a different verdict from *answered*, said so in
  all four touched records.
- **Petrozziello: the statistics are exact and the record says which readings are hands.**
  `F(1,28) = 6.181 → p = 0.019149` and `F(1,28) = 0.3129 → p = 0.580353` recompute to the printed
  0.0192 and 0.5804; the 0.71 / 0.64 / 0.32 viability ratios are labelled hand readings of a panel,
  and the preprint status travels with every one of them.
- **The valproate debt was left open, which is the harder thing to do.** `WWOX` occurs **zero**
  times in the running text of all four primaries — I counted on the artefacts: 0/0/0/0 — the
  platform is one H9/ESNATS lineage, the four share measurements, and the fifth primary is
  paywalled. The curated *«Decreases expression»* row is therefore contradicted and **not
  replaced** by a counter-direction claim.
- **Depth discipline is airtight across 27 new records.** `fulltext_receipts.py status` returns
  `partial_fulltext_read` for **18 of 18** wave-8 PMIDs; every one of the 30 new `LIT` records
  carries the literal **partial full text** that `coverage_report.PARTIAL_MARKERS` needs; and
  *«read in full»*, *«panel level»*, *«full text reviewed»* and `complete_fulltext_read` occur
  **zero** times in `PAPER 217`–`243`.
- **Identity was measured from the front matter, nine times out of nine in wave 9** — including
  three editor contribs correctly excluded, the Bey-not-Hordeaux correction (Hordeaux is author 7
  of 22, verified) and eLife's reviewing-editor group left out of `PAPER 243`.
- **Prohibitions stayed attached.** Per-line sha256 across `CLAIM 011/032/045/046/047` between
  `761b369` and `ce4aa9c`: **0 removed**, 4 added, 2 edited in place (both the declared narrowings).
- **Patient counting held.** `PAPER 117` Patient 11 *«counted once — `DATO`, because the later
  authors state the identity themselves»*; `PAPER 220` *«Count once (INFERENZA)»* with identity to
  `PAPER 013` case 50 neither confirmed nor excluded; the two deep-intronic sources counted once
  each at class level with the zygosity difference **recorded, not reconciled**.
- **The one red suite is not theirs.** `test_batch_queue.py` fails here exactly as the `_003`
  addendum says, on `READ_NOT_REGISTERED=['21476439']`, a wave-10 receipt.

---
