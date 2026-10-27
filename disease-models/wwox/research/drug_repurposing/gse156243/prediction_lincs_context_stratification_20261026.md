# Is the LINCS reversal output of the WWOX-knockout organoid signature specific to that signature, or to the query protocol? — predictions fixed before the stratification was run

Declared 2026-10-26 by scientist-c (package P3B-2). Exploratory. Not medical advice; class level; no dose or suitability. Everything LINCS-derived is NOT WWOX EVIDENCE.
A knockout signature is NOT a rescue signature and NOT a Q230P or any variant-specific signature (`thresholds_and_query_declaration.md`).

## What is already on disk and what this adds
The four SigCom LINCS queries (S1, S2, S3, S0; one request each, 2026-10-22, scientist-b) returned the top 100 reversers and top 100 mimickers each; only the reversers
were annotated with cell line, dose and time (`derived/sigcom_reverser_summary.tsv`, verdict then: INCONCLUSIVE, with the universe unresolved). This analysis re-reads those stored
responses; it sends no new drug query. It needs one metadata call (key-less metadata API, the same one the first summary used) for the **mimicker** signature ids, which were never annotated.

## Disclosure that comes before the prediction
Before writing this I read the top 40 S1 reversers in `sigcom_reverser_summary.tsv` and saw that most are `MCLF*` cell lines, dose 4 uM, time 6 h, with TWS-119 (GSK3 beta inhibitor) at rank 3 and IWP-2 (Wnt-secretion inhibitor) at rank 36. I have NOT seen the S0, S2 or S3 rows, the mimicker lists, the tissue annotation or any overlap count.
So the predictions about context dominance are not blind for S1's top 40; the S0 comparison, the mimicker discordance and the S3 persistence are.

## The three gaps this addresses
1. **Gene universe.** The service ranks against its own signature universe; S0 was drawn from the 19,694 genes with total count >= 10 in the organoid counts file, a proxy. Gap measured here: the per-set fraction of requested symbols that map to a service entity (`derived/sigcom_entity_map.json`), the S0 composition against S1, and the sizes of the returned ranking (reversers 358,840 of 693,215 ranked signatures for S1).
2. **Mapping.** 43 requested symbols had no entity (listed in the map). Gap measured: unmapped fraction per set and whether any declared marker or module gene is among them.
3. **Signature interpretation.** Cell line, tissue, disease, dose, time, library and perturbation type are kept as separate strata; a reversal is read per stratum, never pooled.

## Predictions (each falsifiable by the script)
- **P1 (specificity, rule from the declaration).** S0's top-25 shares fewer than 10 compounds with S1's top-25 (prediction: at most 4). If 10 or more: S1 read as non-specific.
- **P2 (protocol dominance).** The share of `MCLF*` signatures at 4 uM / 6 h among the top-100 reversers is >= 50 percent in S1 AND within 15 percentage points of S0's share. If S0's share is lower by more than 15 points, the context is partly WWOX-specific.
- **P3 (discordance).** At least 30 percent of the distinct compounds in the S1 top-100 reversers also appear among the S1 top-100 mimickers (a compound that reverses in one line and mimics in another is context-discordant, not a reverser).
- **P4 (marker persistence).** S3 (declared composition/maturation markers removed) top-25 shares >= 12 compounds with S1 top-25. A lower value would mean the reversal is carried by the removed maturation/composition markers.
- **P5 (mapping).** The unmapped share of S0's symbols is within 2 percentage points of S1's.
- **P6 (stratum without the dominant context).** Restricting to signatures that are NOT `MCLF*`, the S1 top-ranked reverser compounds are mainly antiproliferative/cytotoxic classes (taxanes, kinase and farnesyltransferase inhibitors, cardiac glycoside analogues) — tested by listing, with the classification written in the output, not by a score.

## Reading rules (fixed now)
- Strata are cell line / tissue / disease / dose / time / library / perturbation type, never merged. A compound is called "stratum-replicated" only if it is a top-100 reverser in at least 3 distinct cell lines of at least 2 different tissues at the same dose and time; otherwise it is "single-context".
- `MCLF*` identifiers are LINCS cell lines whose tissue and disease annotation are read from the metadata and reported as returned; they are not assumed to be neuronal.
- Antiproliferative/cytotoxic or oncology-line signatures do not show neuronal recovery.
- Outcome vocabulary: **USEFUL** (a stratum-replicated, non-cytotoxic, S0-distinct reverser set appears, which is still only a lead and never a drug claim) · **INCONCLUSIVE** (protocol or cytotoxic context dominates; the limit is named) · **DISCARD**.
- No compound is chosen for fame or approval status; a compound absent from the result is "not returned in this query", never "ineffective".

---

# ADDENDUM A (declared 2026-10-26, after the stored-data stratification was read, BEFORE the one new request)

## What the stored-data readout showed (so the addendum is not blind to it)
P1, P4, P5 held; P2 and P3 did not (result section below). S1's top-100 reversers are 74 percent `MCLF*` signatures (61 percent at 4 uM / 6 h), S0's are 1 percent; the 4 uM / 6 h `MCLF*` signatures also fill 59 of the top-100 **mimickers**. A set whose reversers and mimickers come from the same signature family is not showing a direction-specific reversal: it may be matching the gene content that family measures.

## The one new request: a direction-permuted control, S1P
Same 834 genes as S1 (so the gene universe, the mapping and the gene content are identical); the labels "up" and "down" are shuffled at random (517 as "up", 317 as "down", seed 20261026), so the direction pattern is destroyed and the content is kept. One request, to the same service, same database, same limit, no re-run.
- **P7.** In S1P the `MCLF*` 4 uM / 6 h share of the top-100 reversers plus top-100 mimickers is >= 40 percent (the family is selected by gene content, not by direction).
- **P8.** The strongest |z-sum| in S1P reversers is >= 50 percent of S1's (S1 strongest: 16.65); i.e. the score is largely a property of the gene set, not of the up/down pattern.
- **P9.** S1P's top-25 reverser compounds overlap S1's top-25 by fewer than 5 (the specific compounds are not preserved when direction is shuffled).
- **Reading.** P7 and P8 true: the S1 output is a gene-content (coverage) match to one signature family, not a reversal, and the reversal list cannot be read as drug candidates; named limit = the service has no null that matches gene content, and a content-matched direction null is the minimum control any later reversal query must carry. P7 or P8 false: the direction pattern contributes and S1's output stays an exploratory lead, to be stratified further.
- Outcome vocabulary as above. Labels: exploratory; NOT WWOX EVIDENCE.

---

# RESULT (appended 2026-10-26; the predictions above are unchanged)

Scripts: `lincs_context_stratification.py` (stored responses plus one key-less metadata call for the mimicker signatures; outputs `derived/lincs_context_stratification.json` and `.tsv`), `sigcom_permuted_direction_query.py` (addendum A, two requests: seeds 20261026 and 20261027 — the second is a **declared deviation**: the first returned an empty ranking, a repeat of the identical request was empty too, and a second shuffle was run to tell a seed accident from something systematic, not to improve an outcome). Responses are stored with UUID hyphens removed as elsewhere here (`uuid_transform_manifest.tsv`, LOSSLESS).

| Prediction | Result | Verdict |
|---|---|---|
| P1 S0 vs S1 top-25 compound overlap <= 4 | **0** of 25 (top-100 signatures shared: 0; top-100 compounds shared: 3) | held: S1 is not read as non-specific by the declared rule |
| P2 MCLF share >= 50 percent in S1 and within 15 points of S0 | S1 **74 percent** (61 percent at 4 uM / 6 h); S0 **1 percent** (1 percent) | **not held (the second half)**: the output depends strongly on the gene set; S0 is not a matched null |
| P3 >= 30 percent of S1 reverser compounds also mimickers | **4 of 76** (5 percent: SB-225002, TWS-119, nutlin-3, rolipram) | **not held** at compound level — but see post hoc below |
| P4 S3 top-25 shares >= 12 with S1 | **20** of 25 (S2: 15) | held: removing the declared composition/maturation markers barely moves the list |
| P5 unmapped share of S0 within 2 points of S1 | S1 2.16 percent, S0 1.08 percent, S2 1.91, S3 2.20 | held; 43 symbols unmapped overall, 18 in S1 |
| P6 non-MCLF reversers mainly antiproliferative | of 26 non-MCLF S1 reversers, 8 have an antiproliferative or targeted-oncology profile (cabazitaxel, GDC-0068, vandetanib, gefitinib, MK-1775, nutlin-3, indirubin, istaroxime), 7 are unidentified BRD codes, and 3 are in NPC lines annotated central nervous system (varenicline, ketamine, haloperidol, 24 h) | **not held** ("mainly" fails: 31 percent); the reader's classification is the one written here |
| P7-P9 direction-permuted control S1P | **not evaluable**: both shuffles (503/313 and 509/307 mapped genes, no shared entity between arms) returned `reversers 0, mimickers 0, results []`, deterministic on repeat, while S0 (random expressed genes, 8 genes in both arms) returned a ranking of weak scores (strongest reverser z-sum -6.2 against S1's -16.7) | no reason is given by the service; a shuffled set of the same genes should behave like S0, so the empty answer is **unexplained**, not evidence for direction-specificity |

## Post hoc (not pre-registered; labelled)
- The 4 uM / 6 h MCLF signatures fill **both tails** of S1: 61 reversers and 59 mimickers among the top 100 each (S2 54/60; S3 60/59). A direction-specific reversal would not fill the mimicker tail equally; this pattern is what a **gene-content/coverage match to one signature family** produces.
- Six compounds are top-100 reversers in >= 3 distinct MCLF lines at one dose and time and never a mimicker: BRD-K09398529 (5 lines), BRD-K52904470, BRD-K55591206, nimodipine, quiflapon, sildenafil (3 lines each). That is replication **inside one signature family** (donor lines of one project, tissue and disease fields not provided), never across tissues: the pre-registered cross-tissue replication rule finds **none**.
- 74 of the 100 S1 reverser signatures carry no tissue annotation at all.

## Reading, at the strength it has
**INCONCLUSIVE, with the limit named.** (1) The S1 ranking is concentrated in one signature family (FIBR-batch MCLF lines, 4 uM, 6 h, a 2021 library) whose tails are balanced, so it cannot be read as a reversal list; (2) the S0 null is not matched on gene content, and the matched null that was meant to settle it (direction shuffle) returned nothing for an unexplained reason; (3) tissue and disease annotation is absent for most returned signatures, so "neural" is unknown, not assumed; (4) the non-MCLF stratum is small, oncology-line-weighted, and has no cross-tissue replicated compound. What it does establish: a knockout contrast produces a ranking that is not S0's, survives marker removal, and is not an artefact of unmapped genes. What a later reversal query must carry: a null matched on gene content (direction-shuffled, with the service's empty answer understood first) and stratified output by library, cell line, dose and time. **A knockout signature is not a rescue signature and not a Q230P signature; no compound here is a drug claim.** Reopening condition: the service documents why a shuffled set returns nothing, or an independent library (below) is queried with the same sets and agrees.
Disclosure kept: the top-40 of S1 had been read before the predictions were written (see the declaration).

---

# POINTER (appended 2026-10-27 by scientist-d; the text above is unchanged)

The addendum-A control (S1P, S1P2) returned an empty ranking because of a client-side encoding defect (hyphen-stripped entity ids were sent); with the ids restored it returns full rankings, and P7 and P8 are then **not held**. See `lincs_iteration2_interpretation_20261027.md` sections 1.2 and 1.3, which also supersede the "content-match" reading under POST HOC and the "unexplained" wording of this file's last two paragraphs. The OUTCOME for this file's iteration-1 question stays INCONCLUSIVE.
