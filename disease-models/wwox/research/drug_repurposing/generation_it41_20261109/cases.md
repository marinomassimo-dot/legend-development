# IT41 P2 — four contrasting cases, fixed before any search

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Written 2026-11-09 on fixed references: IT40 published as 31919734 (README and `next_investigations_it40.md` of `generation_it40_20261109/`; packages `membrane_hypotheses_20261108`, `ampa_nmda_discrim_20261108`, `nmda_composition_discrim_20261109`). **The question, rivals, universe, necessary conditions and decision below are not to be rewritten after the search; a later change is a dated addendum, not an edit.**

## Case 1 — a pharmacological relation to search in the catalogue (GluN2B-directed negative modulation, burst slice)

* **Relation.** Action: negative allosteric modulation at the ifenprodil site of GluN2B-containing NMDA receptors. Context: neocortical layer II/III slices of the neuron-specific knockout, P13–P17, bursts under measured bath magnesium. Hypothesised benefit: the burst falls at a smaller measured fraction of the isolated NMDA-receptor current than the full antagonist (d-APV) needs. All IPOTESI; premise open.
* **Question.** Which molecules, beyond the ones the packages name (ifenprodil, Ro 25-6981, radiprodil), carry a documented GluN2B-directed negative-modulating action, and for each what is known of maximum effect (not only potency), species and preparation, triheteromer ceiling, other targets, and exposure?
* **Rivals the search must not hide.** Total NMDA-receptor reduction; a GluN2A-containing component; an insensitive triheteromer pool; a bath-state (magnesium, potassium, zinc, glycine) effect; a release or excitability effect of the tool.
* **Universe.** The compound catalogue (ChEMBL curated mechanisms by the two-gene GRIN1/GRIN2B assembly record and the family record, DGIdb rows by HGNC id) **plus** measured-activity records for GRIN2B where the adapters provide them; not restricted to compounds named in WWOX material. Separate source rows, distinct parent molecules, salts, stereoisomers and assay profiles.
* **Necessary conditions for a molecule to enter the comparison.** Identity resolved to a structure (not a name); a GluN2B-directed negative-modulating action documented in a primary or curated source; the assay context stated (species, system, glycine/glutamate/zinc); a maximum effect or a stated absence of it.
* **Decision it can change.** Whether the minimum interpretable experiment uses one ifenprodil-site NAM only (current INV-05 wording after IT40b), a different-site comparator, or stops at "compare with d-APV only up to the measured removable share".

## Case 2 — a physiological hypothesis whose direction is still conditional (Ih contribution after matching, MH2)

* **Question.** If an Ih (HCN) contribution remains after matching potential and deflection, does a blocker response indicate a difference from wild type or only a contribution as in normal cortex? Direction of any benefit is undecided (a blocker worsened events in cited precedents).
* **Rivals.** Passive/leak reading (MH1); T-type contribution to rebound; off-target sodium block of the tool; other HCN isoform or compartment; recording or selection artefact (MH3).
* **Universe.** Catalogue molecules acting on HCN1–4 by mechanism, with isoform evidence stated per source row; the two tools the packages name are *tools*, not candidates.
* **Necessary conditions.** Engagement shown first; two chemotypes; matched conditions (E1) done before any blocker arm.
* **Decision.** Whether any HCN-directed molecule is nominated for a *tool arm*, and in which order relative to E1. Expected correct output: a conditional proposal that nominates no therapeutic candidate.

## Case 3 — a relation already correctly consumed, to leave unchanged (ISRIB and the GSK3→eIF2B step)

* **Question.** Does the IT40 path leave the IT36 probe row (ISRIB, `NOT_IN_CATALOGUE`, InChIKey fixed, eIF2B1–5) and the narrowed bridge untouched, and add nothing for HIF1A→HK2 (S15/S16 premise row)?
* **Universe.** The existing probe and bridge tables; the S17 regeneration as reference.
* **Necessary condition.** No change in any of the 994 proposals' columns and no new duplicate row.
* **Decision.** None; the correct result is "unchanged", measured.

## Case 4 — abstention or non-transfer is the correct result (Kv7 / resting K+ conductance, MH1; and gap-junction attribution of the burst fall, BH3)

* **Question.** Should an opener of Kv7 channels or a gap-junction-blocking compound be proposed?
* **Rivals.** Smaller cells with a seal leak; a drug response is not a defect of the target; carbenoxolone acts on synaptic currents and excitability in culture and on 11β-hydroxysteroid dehydrogenase in the catalogue.
* **Universe.** Catalogue molecules on KCNQ2–5 and on connexin/pannexin targets, listed only to show what is *not* proposed.
* **Necessary conditions to nominate.** A measured difference current that reverses near E_K in Wwox neurons (E3) and a matched-effect control that fails to reproduce the burst fall (M10); neither exists.
* **Decision.** Keep ABSTAIN; the output is the knowledge that decides it, not a list.

## What a later search may and may not do

It may add molecules to Cases 1 and 2 and may open a second family (P11); it may not change the conditions above. A molecule found by action in Case 1 enters as "emerged from the search" and is marked "new for LEGEND", "new combination" or "known reference" by the rule in P7; "novelty against the literature" needs a separate check and is not asserted.
