# CC-20261004W12-B-WINDOW-BAILEY-01 - PMID 41712282's supplement: the delivery numbers behind DIS-033 recomputed exactly, one confound the record does not name, a dose-range detail for RL-GT-004, and a tolerability scope

`context_policy: QUESTION_DRIVEN` (re-read of PMID 41712282 against DIS-033, RL-GT-002, RL-GT-004 and PAPER 168, intake wave 12, 2026-10-04, Scientist B)
**Date:** 2026-10-04 · **Change class: MINOR.** DIS-033 (a dismissal: the window cannot be bounded) is strengthened and not narrowed; the ops add measured qualifications. No `consolidated baseline` claim is touched and no WWOX statement is made.
**Target records:** `disease-models/wwox/research/dismissal_ledger_current.md` (`DIS-033`, one `replace-within`), `disease-models/wwox/registries/paper_registry_current.md` (`PAPER 168`, one `replace-within`), `disease-models/wwox/research/research_lines_current.md` (`RL-GT-004`, one `replace-within` and one `append`).
Receipt: `FTR-20261004-41712282-02` (prepared, not recorded) · Manifest PASS · Dossier `PMID41712282.md`, part 2.
**Nothing here is medical advice. WWOX occurs zero times in the paper or its supplement; earned null for the gene.**

## 1 - Answer to the assigned question

Does an age-stratified panel re-open the window question? **No.** The only age-stratified panels are Figure 8A (P10 cohort) and 8B (3-month cohort), which are separate cohorts compared in prose only; the legend states one unpaired t test per panel and none between ages. Efficacy panels are separate cohorts tested at about 4 and about 9 months, on a challenge whose wild-type baseline moves with age (Racine about 1.4 and about 3). There is no age-by-treatment test. DIS-033's conclusion stands.

## 2 - What was measured (Supporting Data Values workbook, per animal; numbers recomputed here)

- **Delivery numbers reproduced exactly.** P10 high-dose cerebellum, n = 14: mean 15,694, SEM 3,070. Adult IT, n = 4: mean 1,162, SEM 742. Adult ICM, n = 5: mean 7,455, SEM 5,883. Ratio P10 high dose to adult IT 13.5 (ICM over IT 6.4). 3 of the 14 P10 animals (1,057, 1,271, 2,501) lie below the largest adult IT value (3,362).
- **The confound the record does not name.** "The same dose" is the same absolute total (8 x 10^11 vg). The paper's own day-0 body weights (Supplemental Figure 2, P10 high dose, n = 22, mean 5.8 g; Supplemental Figure 5, adult IT, n = 7, mean 21.1 g) make that about 1.4 x 10^14 vg/kg at P10 and about 3.8 x 10^13 vg/kg at 3 months, a factor of about 3.6. The authors state no per-kilogram figure: this is arithmetic done here from their weights. Follow-up also differs (about 4 months against up to 6 months), and the adult IT group is 3 female and 1 male.
- **RL-GT-004 numbers reproduced.** Plasma citrate, % of wild type, n = 10 per knockout group: high dose 64.9 SEM 8.0 (text 65 +/- 8.0), low dose 87.1 SEM 7.6 (text 87 +/- 7.7), knockout vehicle 121.5. High-dose individuals range about 28 to 111 %, two near 30 %.
- **Tolerability scope.** The Results say blood biochemistry stayed in range "across all groups" (Supplemental Figure 3); the figure's legend shows vehicle wild type, vehicle knockout and the **low dose only** (n = 6 to 7); Supplemental Table 1 lists no urine or chemistry cohort for the high dose or for any adult arm.
- **Data-handling notes, not carried into records:** starred and "value excluded" cells in the Figure 8A sheet with no stated rule; the adult ICM liver mean in the text is reproduced only without one animal; the unit label differs between sentence and axis; only two of three lot certificates appear in Supplemental Figure 8; adult wild-type vehicle deaths are "2 of 8" in the text against 7 analysed in Supplemental Table 1.

## 3 - Ops (record-scoped; `old` measured unique in each record)

### Op 1 - `DIS-033`, the delivery sentence

- `old` (unique in `DIS-033`): `against *«1.2 × 10^3 ± 7.4 × 10^2»* vg per genome — an order of magnitude of delivery.`
- `new`: `against *«1.2 × 10^3 ± 7.4 × 10^2»* vg per genome — an order of magnitude of delivery. (2026-10-04, intake wave 12, from the paper's per-animal supporting data: 15,694 ± 3,070 with n = 14 against 1,162 ± 742 with n = 4, a ratio of 13.5, with 3 of the 14 younger animals below the largest older value. "The same dose" is the same absolute total: from the paper's own day-0 body weights it is about 1.4 × 10^14 against 3.8 × 10^13 vg/kg, about 3.6-fold higher per kilogram at P10, an arithmetic the authors do not state. The contrast is between separate cohorts, untested by the paper, followed for about 4 and up to 6 months. It strengthens the confounding finding of this record and does not bound a window.)`

### Op 2 - `PAPER 168`, `Role`

- `old` (unique in `PAPER 168`): `(cerebellar vector 15.7 x 10^3 at P10 against 1.2 x 10^3 at 3 months, vg per genome), partly recovered by switching the adult route - which is why its apparent window result resolves to delivery.`
- `new`: `(cerebellar vector 15.7 x 10^3 at P10 against 1.2 x 10^3 at 3 months, vg per genome as printed on the axes; the sentence introducing the P10 panel says vg per microgram host DNA), partly recovered by switching the adult route - which is why its apparent window result resolves to delivery. ⚠️ Recomputed from the per-animal data (2026-10-04): ratio 13.5, n = 14 against 4, separate untested cohorts, and the same absolute dose is about 3.6-fold higher per kilogram at P10 (arithmetic from the paper's own weights).`

### Op 3 - `RL-GT-004`, the citrate numbers

- `old` (unique in `RL-GT-004`): `**65 ± 8.0 %** at the high dose`
- `new`: `**65 ± 8.0 %** at the high dose (recomputed from per-animal data, n = 10 per knockout group: 64.9 ± 8.0 and 87.1 ± 7.6 at the low dose; high-dose individuals about 28 to 111 % of wild type, two near 30 %)`

### Op 4 - `RL-GT-004`, append one bullet

`op: APPEND` bullet:

`- 🟢 **Append-only, 2026-10-04 (intake wave 12, \`CC-20261004W12-B-WINDOW-BAILEY-01\`): in the source that carries the two-sided dose, the tolerability chemistry exists for the low dose only.** The Results report blood biochemistry in range «across all groups»; the figure's legend plots vehicle wild type, vehicle knockout and the low dose (n = 6 to 7), and the supplement lists no urine or chemistry cohort for the high dose or for either adult route. For the high dose (65 % citrate, individuals near 30 %), tolerability rests on weight, survival and activity. The abstract's «safe and well tolerated» for pups and adults therefore carries no high-dose chemistry and no adult chemistry. Transfer limit: knockout mouse, synthetic promoter, one cassette; not WWOX.`

## 4 - Defaults taken

- The per-kilogram factor is stated as this reader's arithmetic from the supplement's body weights (all animals of those weight groups, not only the biodistribution subsets); the authors' statements are quoted separately.
- DIS-033's status and revival trigger are left alone: the reread adds a confound and exact numbers, not a matched-expression contrast.

### LOCATOR TRIPLES FOR BLIND AUDIT

- (Both cohorts' IT contrast is made in prose across two panels | In agreement with our prior work in WT mice | Results, Biodistribution, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (Figure 8 group sizes are 15, 14, 5 and 4 and the test is per panel | n = 15 KO+LD, 14 KO+HD, 5 KO+ICM, 4 KO+IT | Figure 8 legend, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (Biodistribution was analysed by an unpaired two-tailed t test | Biodistribution was analyzed using a Student’s unpaired 2-tailed t test | Methods, statistics, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (Animals were followed to about four months in the P10 study | mice were followed up to approximately 4 months (mo) postinjection | Results, P10 efficacy study, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (Adult animals were followed up to six months | Animals were then followed up to 6 months postinjection | Methods, virus delivery, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (The Results state chemistry stayed in range across all groups | blood biochemistry markers remained within normal ranges across all groups | Results, tolerability, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (The legend of the cited supplementary figure names vehicle and low dose only | WT and KO Slc13a5 littermates were treated with vehicle or 2e11 vg (LD) | Supplemental Figure 3 legend, `files/fulltext/PMID41712282_Bailey2026_supplement/s303.txt`)
- (The abstract says pups and adults were safe and well tolerated | AAV9/SLC13A5 administration in both pups and adult mice was safe and well tolerated | Abstract, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)
- (P10 high-dose and adult IT cerebellum values reproduce the text means | `[table attestation]` Supporting data values, sheets Fig 8A rows KO+HD (14 animals, cerebellum column) and Fig 8B rows KO+IT (4 animals, cerebellum column) | `files/fulltext/PMID41712282_Bailey2026_supplement/s304_cellwise.txt`)
- (High-dose citrate values include two near 30 percent | `[table attestation]` Supporting data values, sheet Fig 2B-C, rows KO+HD (10 animals) | `files/fulltext/PMID41712282_Bailey2026_supplement/s304_cellwise.txt`)

## BATCH DISPOSITION — `BATCH_20261004_006` (2026-10-04, ACTOR_ID `scientist`, Scientist P), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED

Class re-judged **MINOR** (a dismissal strengthened, not narrowed; two registry/research records qualified). **Blind locator audit over the per-animal workbook: 9 triples and 6 independent checks — 8 SUPPORTED, 1 NOT_SUPPORTED_AS_LABELLED.** Every number the candidate recomputed reproduced exactly (15,694 ± 3,070 at n = 14; 1,162 ± 742 at n = 4; ratio 13.5; 3 of 14 below the largest older value; citrate 64.9 ± 8.0 and 87.1 ± 7.6; day-0 weights 5.82 g and 21.13 g; per-kilogram factor 3.63). The adverse verdict was repaired at source: the legend names **one** test for both panels and it is applied **per tissue**, so *«one test per panel»* is a structure the source never states. Three audit findings were folded in because they bound the record further: the intracisternal arm's apparent advantage **rests on one animal of five** (its SEM is 79 % of its own mean); the tolerability chemistry covers **three of the study's seven groups**, and the only three values in that panel **outside** the normal range are flagged as excluded outliers in the workbook's own key; and the published liver mean of one adult arm reproduces exactly at **n = 4** while its legend declares n = 5, with no cell flagged — restoring the fifth animal roughly doubles that arm's liver load, so the paper's *«comparable»* liver statement does not survive its own declared n. Landed as 1 op on `DIS-033`, 1 on `PAPER 168`, 1 `replace-within` and 1 appended bullet on `RL-GT-004`.
