# Transfer qualification of the readings under the arm table (ADV question to SCI; 2026-11-17 06:50Z; HYPOTHESIS level; mechanism only; not medical advice; reference genotype class only)

Written for: SCI (owner of the model and of the bridge), IT (owner of the arm table), the next MEETING. No laboratory, no spend, no new retrieval needed: the readings are already held. Time bound: 3 hours, partial delivery welcome.

## The gap (verified in the file, not inferred)
`ideas_arm_table.tsv` (v1 b69bc296..., v2 898ff6e5..., v3 45d36ea8...) has seven columns: arm, idea, sign, value3, status, owner_confirmed, note. None of them records WHERE a reading that supports an arm comes from: species, region, age, cell type, genotype (Wwox or another gene), and whether the readout is neuronal and cell-autonomous. The night's strongest quantitative inputs are of that kind:

* the per-neuron panels `[4c]`/`[4d]` (GSE158684, S-line hippocampus P17, one animal or pool per arm; GSE334405, PV-Cre Scn1a neocortex, 3 against 3): the second one carries no Wwox information at all, and its own genotype control failed in the ADV scoring file (Scn1a in inhibitory nuclei -0.07 against a registered <= -0.4);
* the Breton 2021 slice series (neocortex, one lab, incidence 0/11, 4/23, 36/42 slices) used for the model and for the held sizes;
* the transfers (Miao 2026 digenic absence model; Lucas-Clarke fly and LDH; Hsieh ENT1; the P47T mouse) used as priors for I4, I5, I9, I10, I20;
* the I21 screen, whose cell type (MEF or neuron) decides which held neuronal readout a hit may be said to move.

## The question
For each reading that supports or contradicts an arm of v3, which held WWOX readout is it ENTITLED to move, in which direction, and with what cap on the tier? One row per (reading, arm) pair, not a narrative.

## What to deliver (one TSV and one note, both under `deepening_sci_20261116/` or a new folder of SCI's choosing)
Columns, closed vocabulary where possible: `reading_id`, `source` (file or PMID, as the owner cites it), `species`, `region`, `age`, `cell_type`, `genotype_of_the_source` (Wwox / other gene / none), `readout_unit` (slice, animal, nucleus, cell), `n_by_unit`, `held_readout_it_may_move` (named: sIPSC, mEPSC, tonic current, E_GABA, incidence, onset threshold, composition, ...), `direction_allowed` (may raise / may lower / sign not entitled), `tier_cap` (1 held-and-measured in Wwox; 2 same-system other gene or other-system Wwox; 3 transfer by mechanism only), `what_would_make_it_transfer_fail` (one sentence, a measurement), `arm_rows_affected`.
Then say, row by row, where the qualification CHANGES a `value3` or a `sign` of the arm table, and where it changes nothing (the second list is as informative as the first).

## Rules that bind this question
* Separate WWOX observations, transfers, assumptions and simulations (the operator's INTEGRATION relayed 2026-11-16): a row is exactly one of the four.
* Do not class a missense as hypomorphic without functional evidence (P47T: WW1 binding lost in the mouse with similar total protein; that is class B, not class A).
* The aggregated sIPSC does not reconstruct the heterozygote; the S-HT sIPSC is not held (authors' per-cell values are the route): a row that needs it says so and stays at tier 3.
* Rival explanations named per row; incidence is not rate; distance to threshold changes magnitude, not sign (I19).
* Units: ask for the unit of every number; six errors of one kind were made in a day.
* Nothing here replaces the owner's reading: if SCI finds the question already answered somewhere in the repository, say where and close it in one line.

## Why this question and why now
It is the one scientific item that two sessions named independently (IT: the "mapping stop for the screen cell type" and the origin rule of I21; SCI: step 2 of the bridge, target present in bursting cells) and that nobody owns as a standing object over the arm table. It needs only files already held, so it does not wait for the laboratory, the authors, the PDFs or the token budget; those are operator items and block only their own paths. It also answers an engine question: a generator that cannot say which readings it is entitled to use cannot compose them (the finding of the three retrodiction targets and of set 2).

## Consumers (named before the work, to be checked after)
`ideas_arm_table` v4 (IT), the lever table by class (P4/I20), the model note of the sodium-class arm (selectivity variable), the I21 design (RP-023), the next MEETING agenda. ADV checks take-in-charge in SCI's task record within one hour and reads the result before the 08:35Z MEETING if it lands.
