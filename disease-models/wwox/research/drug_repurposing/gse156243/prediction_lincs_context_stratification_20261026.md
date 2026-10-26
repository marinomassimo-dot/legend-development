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
