# GSE156243 reversal query: thresholds and query format, declared before any drug resource was queried

Declared 2026-10-22 by scientist-b in task REPURP-10H-GSE156243-B-20261022. This file is committed BEFORE
the first request to SigCom LINCS, iLINCS, Enrichr or any drug-to-gene resource. Nothing below may be
changed after a result has been seen; a deviation is recorded as a deviation, not edited in.
Everything produced is EXPLORATORY. Nothing here is medical advice; class level, no dose, no suitability.
All LINCS-derived output is NOT WWOX EVIDENCE.

## Input and what it is not
- Input: WWOX-knockout versus wild-type human embryonic-stem-cell-derived cerebral organoids, week 15,
  WiBR3 line, four KO and two WT libraries (GEO GSE156243). A knockout contrast. NOT a signature of
  Q230P, of a child, or of rescue (no rescue-versus-KO RNA contrast is in the three files).
- The lists are the authors' DESeq2 lists pre-filtered on pvalue < 0.01 and fold change > 1.2; padj reaches 0.0684.
  Only padj-filtered sets are described as FDR-filtered; the p-value-only list is never called FDR-controlled.
- Counts were not re-tested and not passed to any model expecting normalised expression.

## Gene sets (fixed)
| Set | Rule | Role |
|---|---|---|
| S1 PRIMARY | padj <= 0.01 and abs(log2FoldChange) >= 0.26 (paper FC > 1.2 is log2 0.263; the file stores two decimals) | the query whose result is reported first |
| S2 SENSITIVITY | padj <= 0.05, same effect filter | breadth check |
| S3 SENSITIVITY | S1 with every gene of marker_sets_declared.tsv removed | composition/maturation sensitivity, NOT deconvolution, NOT a demonstrated correction |
| S0 CONTROL | random gene set, same up/down sizes as S1, drawn from the counts-file proxy universe (total count >= 10) with seed 20261022 | null expectation of the same service |
Symbols: HGNC approved symbol for the ENSG (previous symbols converted through ENSG, conversion kept in
derived/symbol_validation.tsv); genes with no HGNC approved symbol are dropped from the query and counted.
If the service refuses a set for size, S1/S2 are cut to the 500 most significant per direction by padj
(ties by abs log2FC) and this is recorded as a deviation.

## Query format
1. Primary service: SigCom LINCS (maayanlab.cloud/sigcom-lincs), key-less, two-sided rank: up_entities and
   down_entities as lists of approved symbols, against the L1000 chemical-perturbation signatures,
   result sorted by the service's own reverser score (signatures that move the up genes down and the down genes up).
   Order of runs: S1, then S2, S3, S0. One request each; no re-runs to improve an outcome.
2. Fallback only if (1) is unreachable or demands a key/account: Enrichr (same host, key-less) with the up and
   down sets submitted separately against the LINCS L1000 chemical-perturbation up/down libraries; a
   reverser is a perturbation appearing in the library "down" for the up set and "up" for the down set.
3. iLINCS: qualified for reachability and input format only; if its concordance endpoint needs a full
   signature table with values, it is run on S1 with log2FoldChange only if key-less. SigCom LINCS, Enrichr
   LINCS and iLINCS share the LINCS L1000 data: concordance among them is ONE vote, not independent votes.
4. If no service accepts the input without a key or an account: say so and stop at the qualification.

## Reading rules (fixed in advance)
- Report the top 25 reverser signatures per run as returned; retain perturbation, cell line, time, dose when the
  service provides them. Compound-level summary: a compound is called "recurrent" only if it appears among
  the top 100 in at least 3 distinct cell lines. No drug is chosen for fame, approval status or fit to the paper.
- A tumour or non-neural cell line is context-flagged. An antiproliferative or cytotoxic profile (e.g. cell-cycle
  genes in the shared lists) is flagged as such and does not show neuronal recovery.
- S0 control: if the S0 top-25 looks like S1's (same compounds in at least 10 of 25), the S1 result is read as
  non-specific.
- A compound absent from the result is "not indexed/not returned in this query", never "ineffective".
- Target-to-drug comparison: the kg_thin_slice.py Monarch/DGIdb slice for WWOX and for the top
  S1 module genes of the paper (named in the paper, not chosen from the drug result), with its
  pagination and incompleteness states reported.
- Decision rule: KEEP if the reversal output adds an interpretable item absent from the plain lookup and S0 differs
  from S1; INCONCLUSIVE if context (tumour lines, bulk composition, n=4 vs 2) dominates; DISCARD otherwise.
