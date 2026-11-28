# ADV-316 step 1 (SCI, window c82f0240, 2026-11-28): partial records ranked by consumer units

Hypothesis level; not medical advice; no delegate; held files and two ID lookups only. PREREG `PREREG_STEP1_ADV316_SCI_20261128.md` (sha256 b4a825295e3d2b46a51c1ff9fe04420f2a0e29a838c10fd1b57ab850d66b5c63), frozen before the first count. Script `rank316.py.txt`; full ranking `RANK_STEP1_ADV316.tsv`.

## Verdict: step 2 gate MET (at least 3 qualify). Step 2 NOT STARTED
305 partial records; 153 carry at least one consumer; 96 of these also have a section not read in the union of their receipts (the other 57 are declared partial with every counted section read, and were set aside).

The ranking counts a card and its packet once ("distinct units", as ADV-302 did). Without that merge, 39570186 and 39641935 would have ranked second and third.

| Rank | PMID (record) | Units (claim and model) | Unread in union | Qualifies | Why |
|---|---|---|---|---|---|
| 1 | 36537114 (PAPER 017) | 8 (4) | figures captions only; supplement unavailable | **no: no lawful full text** | no PMCID (ID converter, 2026-11-28); receipt FTR-20261020-36537114-01 records OA status closed. Operator supply list: Chong 2023 |
| 2 | 41744777 (PAPER 228) | 3 (3) | all five figures (captions only) | **yes** | CLAIM 047's liver de-targeting and "no toxicity endpoint of any kind" sentences rest on panels never viewed. Held JATS; PMC12938943 |
| 3 | 28045433 (CORPUS-STUB-061) | 3 (2) | figures | no | the two opened consumers use its reference list and retraction status only |
| 4 | 42395553 (PAPER 532, bioRxiv preprint) | 3 (2) | Figs 1, 2 and Supplementary Fig. 1 by legend only | **yes** (weakest of the three) | Fig. 2 is an rWWOX dose-response (1 to 500 ng/mL, SH-SY5Y); the record says the dose reasoning has "a floor and no ceiling". Held PDF |
| 5 | 27339895 (PAPER 362) | 3 (1) | supplement | **yes** | consumers state that the Ser14 work rests on laboratory-made phospho-site antibodies; a supplement could hold their validation. Held HTML; PMC5016130 supplement route not yet tried |
| 6, 7 | 39570186, 39641935 | 3 (1) | figures; supplement | reserve | VABAM co-factor sentences in CLAIM 001 and card H02; 39570186's XML shows no supplement, 39641935 has Table S1 (docx) |

**Step 2 set (frozen rule): 41744777, 42395553, 27339895.**

## Limits
"Matters" was judged from captions and consumer lines, before any unread part was opened. One or two consumer hits were opened per record; one working-model hit for 41744777 is a bookkeeping note. Section states are what receipts declare.
