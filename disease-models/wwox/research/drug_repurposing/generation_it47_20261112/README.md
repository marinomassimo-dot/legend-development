# IT47: from the available hypotheses to effective pharmacological generation

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Every hypothesis is IPOTESI unless a line says DATO or INFERENZA; no rank, tier, direction or need was changed by this work. Drug repurposing for WWOX loss of function; gene therapy is outside the pharmacological proposals. Foundation research page: https://www.wwox.org/current-research

## What the generator does now that it did not
| Step | Before | After | Where |
|---|---|---|---|
| Hypotheses reachable through the manifest role `hypotheses_only` (HE46) | 19 reachable, **0 read** by the generator | **16 read** from three packages of different structure (INV-18 pH/K2P, INV-08 NRF2/KEAP1, INV-09 GSK3/eIF2B), 8 more reported as reachable and unmapped | `generation_it40_20261109/conditional_proposals.py` (`PKG_MAP`, `package_rows`), `conditional_proposals_packages_it47.tsv`, `p1_hypotheses_it47.md` |
| Meaning of the cells | not defined | explicit per package: observation, recorded support, relation, context, action, unresolved premise, prerequisites, discriminating outcomes, expected result; a missing cell says "not stated by the package"; **no direction is invented**; other rows of a package are listed without being called rivals | same |
| Dashboard | 6 conditional hypotheses (INV-05, INV-18) | + KP1 (INV-18), NRF2-H1 and H2 (INV-08), GSK3-H1 (INV-09), five languages | `reader_view.tsv`, `build_reader_rows.py` |
| Cell context in the proposals | none | the channels or genes of each package joined to the held cell-class tables (e.g. TREK-1 and TASK-1 shared between classes, KEAP1 and NFE2L2 not neuron-attributable, GSK3B shared) | `cell_context` column |

## The new case (P4): the GSK3 / eIF2B package, INV-09 (fixed before the rows were read)
`p4_gsk3/prereg_it47.md` → `p4_gsk3/result_it47.md`; blind reader `p4_gsk3/verify/VERDICTS.md`.
* **Simple target search:** 6 catalogue molecules on GSK3A/GSK3B, **none for the eIF2B node**; **previous path:** the card's compound arm; **new path:** 5 conditional rows and 7 premises or prerequisites the card lacked (baseline of eIF2B epsilon Ser535 phosphorylation with total GSK3 and replicates; isoform; epistasis with the DYRK2 and dead-form controls; an engagement control for the probe; the null stated first). The next experiment changed **in order**.
* **Independent check of the decisive propositions** (originals): 7 of 8 supported, 1 partly (a missing control, now a question); **a wrong link of mine** (the measure slot read from a prerequisite cell) and **a wrong prediction of mine** (the context join was said to add nothing; GSK3B is in the held tables) are disclosed in the result and corrected after the case.
* **Not shown:** a better pharmacological prediction, a favourable compound, novelty against the literature.

## SCI46 consumed to the end (P2) — `p2_sci46_it47.md`
Every delta row is classed. The 57-row value table had **no consumer**; `assay_rows_summary.py` is the first, and it found a sentence live on the page ("no neuron or astrocyte data exist for any of these compounds") too strong for the covalent class; a dated correction was added. A clause states that RNA is not function and that a readable gene is not an NRF2-specific readout. Rankings and directions were not changed.

## Two jumps corrected (P3) — `p3_corrections_it47.md`
"In frequency by about a fifth" meant a fall of 18 percent (amplitude −52 percent), not a fall to a fifth; the inference that the amplitude falls more than the frequency is weak (spread as large as the mean; pooled events; no statistics in the delivered text) and is marked so in V21, the IT46 README and the S5 result. `p9_two_levers_it46.md` received a dated update: non-additivity and additivity do not show a shared or independent mechanism, equal cellular variables do not make two network manipulations equivalent, and E_GABA needs rest, threshold, conductance and time. The scientific verification is SCI47 package A.

## Integration items of the operator (2026-11-12)
Mandate association restored (marker as a message of its own; the watch reads RUNNING with this session). The NRF2 mapping now separates observation (none stated), recorded support (with the package's own audit remarks), and prediction (declared missing); the other rows of a package are listed as "not classified as rivals, complementary or compatible". The GSK3 reader cost is the transcript census (output 44,189; context written to the cache 206,000; context re-read from the cache 5,261,125); the other readers are corrected by dated notes.

## Queue and DREAM
`dream_it47.md`: bath-applied pharmacology reaches several cell classes (before any extension: 5 of 75 relation-gene pairs neuron-attributable, 22 not assignable, 48 with no row; `relation_context_summary.py`). The queue item that fills the 48 (cell-class rows for 30 genes, predictions fixed first) is a **separate increment** (branch task/it47b) and is not part of this tree. The Claude Science comparison has a documented entry point only (`claude_science_entry_it47.md`). The next batch: `../next_batch_it47_20261112/BRIEFS.md`.

## Limits
Readers' depth is abstract for several papers; the context tables are RNA class means of different ages and one human sample; translations are the assistant's, not native-reviewed; single cases chosen by a rule fixed beforehand and scored by the builder, with independent readers for the premises.
