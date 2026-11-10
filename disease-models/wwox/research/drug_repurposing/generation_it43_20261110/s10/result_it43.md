# IT43 P8: what the path produced for S10 (KEAP1/NRF2), with no new code

Non-canonical working note. Not medical advice. Same `action_search.py`, one new row in `relations_it43.tsv` (`s10/` holds a one-row copy and the outputs). 20 source rows, 14 molecule x relation rows: 8 CANDIDATE, 2 EXCLUDED (direction opposite), 10 UNKNOWN (direction unclear).

## What the rows say, by target
* **KEAP1 inhibition (wanted down):** four ChEMBL curated inhibitor mechanisms (a triterpenoid and three fumarate-ester forms: parent and two prodrug or metabolite entries) and two GtoPdb binders with a typed inhibitor action and pIC50 (a biparatopic binder and a peptide). Five more GtoPdb KEAP1 binders carry action "binding" with no function: UNKNOWN, kept, not read as activators.
* **NFE2L2 activation (wanted up):** one activator row (omaveloxolone) from ChEMBL and the same from GtoPdb: one molecule, two sources.
* **Opposite, excluded but kept as controls:** an NRF2 inhibitor tool (GtoPdb, binding, inhibitor) and one ChEMBL row listing the triterpenoid as an inhibitor of NFE2L2 itself; the same molecule has a clean KEAP1 row, so it stays a candidate by that row: direction is per target, per row.

## Classification (four classes kept apart)
Known in the repository: omaveloxolone (card L01, conditional ex vivo probe, systemic development not supported), the fumarate esters, the triterpenoid and the NRF2 inhibitor tool all appear in earlier cards and packets. Known in WWOX: none (no NRF2 measurement in a WWOX-deficient neural system). New combination for LEGEND, transferred hypothesis, verified-novel: none claimed.

## What the path adds (generation, not coverage)
The existing package (H1-H6) said which explanations compete but named no reagent for the one the search cannot detect. The rows give it: **H5 (a compound benefit independent of NRF2)** is separated by the opposite-direction NRF2 inhibitor tool, which the engine excluded as a candidate and S10 keeps as a *control*: an NRF2-dependent benefit should shrink under it; an NRF2-independent one should not. The functional reference is the activator row; a mechanism discriminator is a KEAP1-binding compound of a different binding mode from the covalent ester forms (the non-covalent binders have affinity but no direction here, so they are discriminators only after their action is read). All conditional on the premise the package could not settle: is NRF2 tone low, already induced, or compartment-specific (H1, H2, H3)? The genetic arm (KEAP1 lowering or NRF2 raising) stays first.

Premise needed: NRF2 protein, nuclear NRF2 and NQO1 activity in a WWOX-deficient neural system, per compartment. Discriminating experiment: activator and a second KEAP1-directed compound with and without the NRF2 inhibitor tool, same oxidative challenge, same network readout. What raises the lead: a response reduced by the inhibitor tool; lowers it: a benefit unchanged by it (H5) or a worsening (H6); reopens: a compartment-specific effect (H3).
Limits: the inhibitor tool's own selectivity is not assessed here (a catalogue row is a granularity, not selectivity); no exposure data; the ions and prodrug-form duplicates noted in IT43 apply (the three fumarate entries are one pharmacology in three forms).
