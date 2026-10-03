# COMMIT CANDIDATE — CC-20261003W6-B-MOVEMENT-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 6 2026-10-03, branch `task/sci-B-20261003w6`.
**context_policy:** `SOURCE_FIRST` — first pass written from the source before any registry record was opened; comparison afterwards (see `research/intake_wave_20261003w6_B.md`).
**Not medical advice.** Class-level statements about published patients only.

## Target
- `research/discovery_ledger_current.md`, record `DL-MECH-030`: one `replace-within` after "distonia in 8/13" recording that (a) the four WWOX rows of PMID 42068099 Table 2 all cite this cohort (PMID 36779245) and are re-descriptions, and (b) the pooled 15/18 dystonia row of PMID 40217411 cannot be de-duplicated against it.

## Findings carried
1. **PMID 42068099** — WWOX in four Table 2 rows (IESS; excessive startle/hyperekplexia; corpus callosum abnormalities; white matter changes); each cites ref 66 = PMID 36779245. One cohort, four labels. The selection record named three rows; there are four.
2. **PMID 40217411** — Table 2 WWOX (n = 18, unnamed primaries): dystonia 15/18, hypokinesia 5/18, ataxia 2/18, myoclonus 1/18, tremor 1/18, chorea 0, stereotypies 0. Table 1 (OMIM) lists WWOX under dystonia, myoclonus, ataxia, tremor and hypokinesia — **not chorea** (the selection record's "chorea" comes from flattened text, where the dystonia gene list runs into the next row label). The 2021 "hypokinetic from the neonatal period only with WWOX" sentence (PMID 33919646, held at abstract level in `analysis/ft116_cohort_triage_20260921.md` §7.4) is **not repeated**: hypokinesia is now a six-gene OMIM association in text, ten genes in Table 1.

## Change class
**MINOR** — annotation; no claim status, block or consolidated baseline changed. It narrows nothing: it prevents a count from being inflated.

## Registry need
PMIDs 40217411 and 42068099 need identity records — `CC-20261003W6-B-REGISTRY-01` (provisional `PAPER 161`/`162`, `LIT-0454`/`0455`).

## Ordering
Apply after `CC-20261003W6-B-CBDRESPONSE-01` or before — the two ops touch different sentences of `DL-MECH-030` (both dry-run exit 0 independently). Receipts `FTR-20261003-40217411-01`, `FTR-20261003-42068099-01` appended first.

## Op list — `discovery_ledger_current.md` (dry run 2026-10-03: exit 0, 1 op, key `DL-MECH-030`)
```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-030",
  "old": "distonia in 8/13",
  "new": "distonia in 8/13 (wave-6 note, `CC-20261003W6-B-MOVEMENT-01`: the four WWOX rows of PMID 42068099 Table 2 — IESS, excessive startle/hyperekplexia, corpus callosum abnormalities, white matter changes — all cite this cohort and are re-descriptions, not corroboration; the 15/18 dystonia row of PMID 40217411 Table 2 pools unnamed primaries and cannot be de-duplicated against this cohort, so it is not additive)"
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT
(WWOX is listed for excessive startle/hyperekplexia citing ref 66 | Excessive startle/hyperekplexia ARHGEF9, 75 GRIA2, 71 GRIA3, 76 KCNQ2, 77 PURA, 78 STXBP1, 79 SCN1A, 41 SCN2A, 80 SCN8A, 81 WWOX, 66 YWHAG | PMID 42068099, Table 2; files/fulltext/PMID42068099_Mohammad2026_PMC.xml)
(WWOX is listed for corpus callosum abnormalities citing ref 66 | Corpus callosum abnormalities ARX, 107 FOXG1, 108 NAA10, 109 RHOBTB2, 54 TMEM63B, 59 UBA5, 110 WWOX 66 | PMID 42068099, Table 2; files/fulltext/PMID42068099_Mohammad2026_PMC.xml)
(WWOX is listed for white matter changes citing ref 66 | White matter changes CACNA1B, 118 GABRB2, 119 GABRB3, 120 GRIA2, 83 NAA10, 109 WWOX 66 | PMID 42068099, Table 2; files/fulltext/PMID42068099_Mohammad2026_PMC.xml)
(the review is not systematic | Although this was not a systematic review | PMID 42068099, Methods para 1; files/fulltext/PMID42068099_Mohammad2026_PMC.xml)
(WWOX pooled row: dystonia 15/18, hypokinesia 5/18, chorea 0 | WWOX 0 15/18 0 2/18 1/18 1/18 5/18 | PMID 40217411, Table 2 row WWOX; files/fulltext/PMID40217411_Yuan2025_PMC.xml)
(hypokinesia genes come from OMIM, six named in text | A review of the OMIM database revealed that mutations in several genes are associated with hypokinesia, include ATP1A3, PIGP, SCN2A, SCN8A, TBC1D24, and WWOX | PMID 40217411, Hypokinesia section; files/fulltext/PMID40217411_Yuan2025_PMC.xml)
(Table 2 includes only articles giving types with proportions | Only articles that provided specific descriptions of movement disorder types and their corresponding proportions were included in the statistical table (Table 2). | PMID 40217411, Characteristics of movement disorders; files/fulltext/PMID40217411_Yuan2025_PMC.xml)
