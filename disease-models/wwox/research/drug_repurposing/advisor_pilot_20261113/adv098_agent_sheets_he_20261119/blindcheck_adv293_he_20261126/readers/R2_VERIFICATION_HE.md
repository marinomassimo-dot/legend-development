# Reader 2 (batches 4 and 5): HE verification against the original (ADV-293, 2026-11-26)

Reader: legend-delegate, sonnet, effort high, no search, nothing outside the packet. Report as delivered: the two TSVs here.

| Batch | units | OK | ADD | MUST CHANGE (reader) | MUST CHANGE (HE confirmed) | UNSETTLED | NOT A CLAIM |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4 | 34 | 16 | 6 (reader 5, plus U4.1 regraded by HE) | 6 | 5 (4 distinct errors) | 4 | 3 |
| 5 | 35 | 18 | 7 | 4 | 2 | 7 (reader 5, plus U5.20 and U5.31 regraded by HE) | 1 |

Strict rate (confirmed MUST CHANGE / (OK + ADD + MUST CHANGE)): batch 4 5/27 = 18.5 percent (class T: 5/22 = 22.7);
batch 5 2/27 = 7.4 percent (class T: 0/19; both confirmed errors are class S, titles of abstracts). Pair: 7/54 = 13.0 percent.

## Confirmed (from the held rows or abstracts)
- U4.6 and U4.33: "flips with the potential" holds for GluN2A only. CHEMBL6083260: GluN2B ketamine 510 against memantine
  780 nM at -60 mV and 15,220 against 25,630 nM at -40 mV (ketamine stronger at both); GluN2A 500 against 840 and 53,320
  against 28,070 (flips). CHEMBL3232957 (2014 oocytes, GluN2A, -40 mV): ketamine 3,310, memantine 4,360 nM.
  Changes an order. One error in two units.
- U4.17: 22 Ki rows of 180 nM in CHEMBL4680282; the table holds 25 numeric Ki rows in all, 22 at 180 nM and three
  other values (420, 684, 1,900 nM): "not 25 measurements" is not supported either way.
- U4.22: Ki 3,830 nM (activity 1522869) is "L-[3H]glutamate ... rat brain synaptic membranes"; the 880 nM row (421988) is
  "[3H]CPP ... rat cortical membrane". Tissue and ligand named wrongly for one value.
- U4.26: 0.86 microM (activity 213208) is "[3H]TPC ... whole rat brain homogenate"; the MK-801 rows are 610 (385662,
  417213) and 700 nM (19252436).
- U5.16: abstract title of PMID 30631446 ends "associated with potential use-limiting visual field defects".
- U5.27: PMID 25463517 title ends "on newborn DGC structure and spontaneous EEG seizures following hypoxia-induced
  neonatal seizures"; the abstract says Wistar rats at P10; PMID 28192112 title ends "in the mammalian brain".

## Regraded by HE
- U4.1 (reader MUST CHANGE) to ADD: "no ketamine-memantine potency order is readable" is a judgement about stability
  across subunits, potentials and documents, which the rows support (GluN2A flips; another document gives the opposite
  order at -40 mV); the GluN2B order inside one document is readable and is added. The reader flagged it as a judgement call.
- U5.20 and U5.31 (reader MUST CHANGE) to UNSETTLED: the label sets of the sheet (2026-11-19, three labels, newest
  2024-11-18 and 2025-01-08) were not kept; the same route on 2026-11-26 returns labels of 2026-06-15 (vigabatrin) and
  2026-01-27 (bumetanide). A dated route result, not a proof that the sheet was wrong. Separately, every vigabatrin label
  returned today lists infantile spasms in its indications text, so "infantile spasms in other labels: not read here" is a
  statement about reading, not a false statement.

## Not applied (reader additions; true as reported, not verified by HE)
U4.5, U4.14, U4.19 (a third ratio-like row, activity 1500111, 280 = 460/1640), U4.27, U4.32, U5.5, U5.6, U5.13, U5.23, U5.28,
U5.29, U5.35: see the TSVs and the reader's reply (kept in the session transcript); they would add rows, flags and
scopes, none changes a written statement to false.
