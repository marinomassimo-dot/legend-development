# ADV-164 transfer check: eligible source sets frozen BEFORE any query (IT, 2026-11-21)

Hypothesis level; reference genotype class only; no dose; not medical advice. Written read-only from the receipt ledger (`registries/fulltext_read_receipts.jsonl`, PMID taken from the receipt event id) and the paper registry short titles. **No query was run and no scout, harvest or flag output was looked at.** "Held" means a receipt exists (depth varies; stated). I did not open the scout's own search output for either row, so I cannot say which records came from a row's own search: where I suspect it, it is labelled below. Public routes only; nothing contacted.

## Which rows (answer to "change it if you know better")
* **Row A = recovery_it10_p23_20261031 R1** (Q230P protein fate): accepted. The item says "Q230P protein fate" and omits the gene (the gene is only in the row's `queries_and_sources` monitor strings); Q230P is a WWOX-specific token, so a query on the variant alone may already work and the routing failure is only partly real.
* **Row B: NOT NP3A1.** NP3A1's item text says "parvalbumin composition in the **Wwox**-deletion mouse": it names the gene, so `--gene-anchor` adds nothing there and the case is not the routing failure. **Better row: functional_it13_p3a_20261031 NP3A3** ("Resting potential and the M-current (Kv7) component in neuron-deleted versus control slices at P13 to P17, ..."): no gene and no drug word in the item, the relevant held records are WWOX-named, and the Kv7 side is non-WWOX class pharmacology, so it can show the anchor both helping and hurting.

## Row A (R1, Q230P protein fate): 10 WWOX-bearing held records
Relevance boundary: a held record that reports a WWOX missense, nonsense or splice variant together with a WWOX protein, expression, stability or translation observation (or the lack of one); class-level variant-proteostasis papers without WWOX are NOT eligible (they are a second, labelled list below).
| PMID | Record | Held depth | Note |
|---|---|---|---|
| 29808465 | Johannsen 2018 (Q230P: complete loss of WWOX protein) | full text read | the direct Q230P protein record |
| 36537114 | Chong 2023 (WOREE spectrum, Q230P) | partial full text | |
| 30853297 | Weisz-Hubshman 2019 (exon 6, Q230P) | receipt, depth in ledger | |
| 36828035 | Hussain 2023 (P47T partial loss of function) | complete full text | protein abundance observations; PAPER 007 and 112 are one PMID |
| 24369382 | Mallaret 2014 (SCAR12, P47T and G372R) | complete full text | |
| 35792847 | Al Baradie 2022 (nine patients, P47T among variants) | complete full text | |
| 40875931 | Gao 2025 (WWOX-DEE genotype-phenotype) | full text reviewed | variant classes, protein not measured |
| 39416860 | Feng 2024 (case report, variant of unclear significance) | complete full text | |
| 36926521 | Colin 2023 (multi-omics; one WWOX genotype, blood RNA) | partial full text | expression, not protein |
| 30746283 | Ehaideb 2018 (splice-donor and nonsense families) | receipt, depth in ledger | variant carried, protein not measured |
Possibly surfaced only because they were this row's own monitor hits (WWOX AND Q230P): 29808465, 36537114, 30853297. Labelled diagnostic, not a clean recall target. Second, non-WWOX class list (eligible only if the scout is meant to find class methods; not part of the gene-anchor test): 30266908 (Guiberson 2018), 29785012 (Matreyek 2018), 32023956, 33914734, 39216838, 41178115, 38509072, 22938201.

## Row B (NP3A3, M-current and resting potential in neuron-deleted slices): 11 held records, 8 direct + 3 indirect
Relevance boundary: a held record reporting excitability, network or interneuron electrophysiology (resting potential, burst, seizure, E/I or PV readout) in a Wwox-deficient neuron-targeted, null or organoid preparation; WWOX-named. The Kv7 class literature (Brown 2016, West 2018, Liddiard 2024 and others) is held but does NOT name WWOX: listed separately, it is the case where an anchor should hurt.
| PMID | Record | Class |
|---|---|---|
| 34634460 | Breton 2021 (neocortical excitability, Wwox neuron-deleted) | direct (the row's own source family) |
| 32000863 | Cheng 2020 (GSK3 beta seizure axis, null pups) | direct |
| 30290271 | Hussain 2019 (GABA and glia, PV count) | direct |
| 34268881 | Steinberg 2021 (brain-organoid WOREE model) | direct |
| 34831305 | Steinberg 2021 (atlas of WWOX models) | direct |
| 42397075 | Steinberg 2026 (WWOX-MYC organoids, neurogenesis, rescue) | direct |
| 36828035 | Hussain 2023 (P47T mouse: epilepsy, progressive neurodegeneration) | direct |
| 42422765 | Obeid 2026 (neuron-specific gene therapy) | direct |
| 42558002 | Lange 2026 (astrocytes in genetic epilepsies; WWOX rows) | indirect |
| 41477840 | Stamouli 2026 (glia-to-interneuron reprogramming; WWOX transcript) | indirect |
| 41712282 | Bailey 2026 (metabolic and seizure endpoints do not share a dose) | indirect |
Non-WWOX Kv7 records held (for the "should hurt" arm; PMIDs I can state from receipts or sheets): 26865186 (Brown 2016, juvenile rat exposure), 30328622 (West 2018, slice), 38176909 (Liddiard 2024), 32652600 (Kanyo 2020, abstract level).
Labelled diagnostic: I do not know which of these the NP3A3 row's own search produced; the row's source family is Breton 2021 and Cheng 2020, so treat 34634460 and 32000863 as diagnostic.

## Notes
* The sets are frozen by this file; a later look at any query output must not edit them.
* Fewer than 10 for Row A if the three diagnostic records are removed (7); Row B direct set is 8.
* The registry short title was used for relevance; two records (30853297, 30746283) were not read by me for this task; their depth is in the ledger.
