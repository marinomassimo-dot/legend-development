# Reader 3 (batch 1): HE verification against the original (ADV-293, 2026-11-26)

Reader: legend-delegate, sonnet, effort high, no search, nothing outside the packet. Report as delivered:
`R3_batch1_as_delivered.tsv` (rebuilt from the reply in the agent transcript; 78 units).

| units | OK | ADD | MUST CHANGE (reader) | MUST CHANGE (HE confirmed) | UNSETTLED | NOT A CLAIM |
|---:|---:|---:|---:|---:|---:|---:|
| 78 | 30 | 7 | 6 | 5 | 27 (reader 26, plus U1.14 regraded by HE) | 9 |

Strict rate: 5/42 assessable = 11.9 percent. Class T: 4/24 (OK 15, ADD 5, MUST CHANGE 4) = 16.7 percent; class S: 1 (U1.21).
Twenty-seven of 78 sentences are UNSETTLED: SCI and repository statements, search counts, negatives, full texts not in the packet.

## Confirmed
- U1.8 "adenosine receptors, acetylcholinesterase, CYP3A4 each in 2 to 3 rows": adenosine A1, A2a and A3, acetylcholinesterase
  and CYP3A4 have 2 rows each; the only targets with 3 or more rows are "Unchecked" (57) and "Mus musculus" (3). Count.
- U1.21 Heurteaux 1991 (PMID 1860065): the abstract says "less than 0.65 mM in the white matter of the cerebellum"; the
  sheet wrote 0.65 mM. A bound written as a value; changes the lower end of a range.
- U1.32 "holding potential ... not in these text cells": 17 memantine rows name a holding or membrane potential
  (-70, -75, -65, -60, -40 mV); Mg2+ and agonist concentrations are indeed absent.
- U1.45 "IC50 and Ki rows from 0.54 to 55 microM, about two orders": NMDA-assay rows with target "Unchecked" reach
  222 nM (26154473, GluN1-1a/GluN2C, human oocytes, CHEMBL5625199), 318, 367 nM and Ki 429 nM (12114410, pig cortex);
  222 nM to 55.4 microM is about 2.4 orders. Changes a range and an order of magnitude.
- U1.50 "same described configuration (oocytes, voltage clamp)" for 911 nM (activity 1912604, CHEMBL1146243): the ChEMBL
  text is "recombinant NR1/NR2A receptor expressed in Xenopus laevis oocytes", no clamp or potential.

## Regraded by HE
- U1.14 (reader MUST CHANGE, ethosuximide label "newest 2026-05-25" against 2026-07-24 in the packet) to UNSETTLED: the
  label set read on 2026-11-19 was not kept (the same route shows newer labels today); see batch 5.

## Not applied (reader additions)
U1.16, U1.24, U1.27 (four unmapped human GluN2C/GluN2D rows of 0.22 to 0.59 microM), U1.29 (the 1500/55000 nM pair recurs in
six documents, several flagged potential duplicate), U1.30, U1.38 (Victorino 2017 offspring exposure), U1.54 (two further
GluN2A rows inside the band: 8 of 10): kept in the TSV and the reply; none makes a written statement false.
