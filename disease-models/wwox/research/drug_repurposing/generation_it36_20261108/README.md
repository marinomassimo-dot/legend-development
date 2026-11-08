# IT36 measurement: what the generation path reaches, before and after (2026-11-08)

Non-canonical, not medical advice. This measures **reach and representation**, not prediction. Nothing here shows that any listed compound helps; the unguided comparison is retrospective and was not isolated (see the last section).

## Answer first

* **What changed in the machinery.** (1) Precedent relations (`bridges.tsv`) and probe entries (`probe_links.tsv`) are now read from the folder of the package that read the sources, with a validator; the hand-kept `needs/bridges_it35.tsv` is gone. (2) A tool compound the catalogue does not hold can be joined at read time as one row for its target group (the complex), never as a headline link. The first user is ISRIB.
* **What it reaches (DATO, computed 2026-11-08 against the cached catalogue, `repurposing_search.py need <id>` with and without `--bridges packages --probes packages`).**

| Need | A: before (no bridges, no probes) rows / headline records / probes | B: with the links | Reading |
|---|---|---|---|
| NEED-ISR-ATTENUATION | 78 / 12 / 0 | 171 / 12 / 1 | the 93 added rows are pathway members through the GSK3B-EIF2B5 bridge (no sign); the one probe is ISRIB, shown once with 5 of 5 subunits matched; headline unchanged |
| NEED-PDH-PYRUVATE-AXIS | 209 / not recomputed here / 0 | 293 / unchanged / 0 | 84 pathway members through HDAC5-SLC2A1; headline unchanged (IT35 figure 12/12, 8/8, 81/80 stands) |
| NEED-MYELINATION | 546 / 214 / 0 | 546 / 214 / 0 | nothing added: no bridge or probe touches it, on purpose (see below) |
| NEED-LACTATE-LDH | 12 / 10 / 0 | 12 / 10 / 0 | nothing added |

* **C: a simple baseline (look up the gene symbol in the ChEMBL human mechanism rows, no need).** THRA 8 rows, THRB 11 rows, SLC16A1 0, SLC2A1 0, EIF2B5 0. So for the thyroid-receptor lever the baseline reaches more than a need-based search does, because no need carries THRA or THRB as a target; that lever was reached in LEGEND by another route (investigation INV-12, compound list from the phenotype-first step), not by the need path. For the energy and ISR targets the baseline reaches nothing.
* **Where the chain stops, by cause (measured, not argued).**
  * ISRIB: stopped at *identity absent from the catalogue*; now passes the need stage as a labelled probe. It still stops at *azione e contesto irrisolti* beyond that: no ISRIB experiment in a WWOX system, no source ties it to the GSK3 serine (`nb2_isrib_it36_20261108/output/probe_entry.tsv`).
  * Thyroid-receptor lever (H1): reached through INV-12; the missing piece is a measured hormone baseline of the co-culture medium (`levers_bc/output/consumer_delta.md`), now written into INV-12.
  * Energy supply to the oligodendrocyte lineage (H2): *relation not represented* as a gene-to-gene precedent (it is a process: supply to a lineage). It is carried as a pointer in INV-07, with sign undetermined and the WWOX-side lactate data pointing up. It was deliberately not turned into a bridge from the myelin markers to the lactate transporter: that would list transporter blockers under a myelin need with no source for the sign.
  * The WWOX-ERBB4 physical relation (science delivery, `bridge_rows.tsv`) and the HDAC5-HIF1A mixed-sign relation were **not** ingested as bridges: HIF1A is not an intervention target of any need that touches HDAC5, so the row would add nothing today; ERBB4 would widen the WWOX gene-addition needs with no relation. Both stay in their packages.
* **Generation (the second phenotype, myelination, from the science session).** The unguided producer, given only the observations, offered 6 alternative explanations. 5 were already represented in LEGEND (INV-06, INV-12); one was a new inference at the level of a thread: energy supply to the oligodendrocyte lineage, with undetermined sign (`myelin_generative_it36_20261108/levers_bc/output/comparison.tsv`). Two conditional pharmacological hypotheses came out of the informed step, each with two arms and neither favourable. The informed audit of 32 rows found 30 supported, 1 overshoot, 1 misapplied (corrected before delivery).
* **Errors of transfer introduced by the links:** none found. The regression `test_bridged_rows_leave_the_headline_unchanged_and_carry_no_sign` and the probe tests hold (sign columns refused; a pathway member never reaches the probe; the complex is one row).
* **Not shown:** a predictive gain. What was measured is representation and reach. A probe being reachable is not a candidate.

## What the comparison can and cannot say

Hidden from the unguided brief: the originating paper's title and every repository file. Accessible to it: PubMed and the open web. Recovered during the run: the originating paper was found by search (reported by the producer, as in the HCN case), so the condition is retrospective and not isolated. The 5-of-6 overlap with LEGEND's own investigations is a statement about coverage of this phenotype, not about superiority of either condition. The one new thread (energy supply) is a transfer at abstract level.

## Cost (transcript census, one response counted once, tokens as logged)

Coordinator-side delegates this iteration: package-to-consumer map builder 34 turns, output 41,858, cache read 2,877,017; two translation runs about 8 turns each, output about 17,000 each. Settings requested `sonnet`, effort `low`; read back `low` on every turn. No conversion to a plan share.
