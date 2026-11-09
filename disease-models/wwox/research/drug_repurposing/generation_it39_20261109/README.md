# IT39: where generation actually stopped, and one change at that point (stage S15)

Non-canonical, not medical advice. This is a **presentation and qualification** change of the proposals' hand-over; selection, eligibility, hand-overs and every existing column are byte-identical to S14. It is not a predictive result.

## P3: five contrasting real cases, traced to the point where the path stopped

| Case | Why it is contrasting | Path (retrieval → representation → catalogue search → composition → qualification → selection → propagation) | Where it stopped |
|---|---|---|---|
| MYC amount versus occupancy (NB-1 E80, an auditor's reading) | a correct, labelled-exploratory relation that arrived only as a limit | retrieved and structured in the package; read by the generator since IT38 as a carried limit on 555 proposals | **propagation**: the limit was present but the measurement that resolves the premise was not attached to the proposal; the file was loaded, the format could express it, the model was not the limit |
| HDAC5 to HIF1A, mixed sign (science re-check) | a relation that could orient a pharmacological question | retrieved and delivered as a `bridges.tsv`; HIF1A is already a pathway member of the PDH need and not an intervention target of any need that touches HDAC5 | **composition**: the bridge adds no reach (measured, not argued); a relation fits the format and has no consumer path |
| Knockdown of HDAC5 versus catalytic inhibition (INV-16 premise) | quantity or presence of a protein is not the activity of its enzyme | the limit "knockdown is not catalytic inhibition" is carried by 20 proposals | **propagation** (the limit travelled; the test did not) |
| HDAC4 results carried to HDAC5, or a class-I compound credited with a class-IIa effect | an improper transfer between molecules and classes that must be prevented | guards exist (the paralogue rule in INV-16; a molecule-scope limit for the potency profile) | **none**: the guard works; S15 leaves those 20 rows unchanged |
| ISRIB and the GSK3 to eIF2B bridge | already consumed, where the right behaviour is not to duplicate | reached since IT36 (probe row, bridge) | **none**: nothing was added |

## P4: the change at the demonstrated stopping point

`run_generation_it21.py` now adds `premise_decisive_test` to each proposal whose chain rests on a premise measured by an investigation (INV-14, INV-16, INV-17): the investigation's own open question and its own `next_test`, joined by id from `investigations_it20.tsv` (the one table that holds the decisive measurement; no registry of its own). It reuses `shared_premise_investigation`; it changes no status, no eligibility, no selection.

## P7: before and after (S14 against S15, `test_stage_it39.py`)

| | S14 | S15 |
|---|---|---|
| proposals / eligible / hand-overs | 994 / 220 / 15 | 994 / 220 / 15, same ids |
| every existing column | , | identical on all 994 rows |
| `premise_decisive_test` filled | no column | 605 proposals (INV-17 555, INV-14 30, INV-16 20); the 389 others are blank |
| hand-overs that carry the measurement that resolves their premise | 0 | 5 of 15 (3 INV-17, 1 INV-16, 1 INV-14) |

What this shows: a researcher reading a hand-over now sees, beside "premise open", what would close it. What it does **not** show: a better selection or any predictive gain, and nothing about the ten hand-overs with no mapped premise. A column that no later step reads would be descriptive only; this one is read by the hand-over table, which is what the next investigation is chosen from.

## Cost

Stage regenerated once end to end (about 6 minutes, 4 GB cap). No delegate for this part.

## P5, a real test: where the path stopped before combining relevant knowledge (S15 baseline, S16 after)

**Question.** The HIF axis: ten H_HARM proposals (three eligible, one hand-over, IT21P2-0014) have the chain `XIAP or KDM4C ... -P(+)-> HIF1A; HIF1A -T(+)-> HK2`. They assume that HIF1A drives the glycolytic module in WWOX-deficient neural cells. Investigation INV-16 already holds the sign problem of the HDAC5 to HIF1A relation (mixed between systems), and its test carries a HIF1A or EPAS1 knockdown arm for the glycolytic readout. **Before:** no premise row mapped those chains, so the proposals carried no investigation and no measurement (the repository held both pieces and joined nothing). **Stopping point:** composition (the premise map), not retrieval and not the model.

**Minimal change.** One row in `generation_it21_p2_20261103/investigation_premises_it32.tsv` (INV-16, the pattern `HIF1A -T(+)-> HK2`, the premise sentence), and `premise_decisive_test` now begins with what the proposal assumes (the matched row's premise) before the open question and the resolving measurement.

**After (`StageS16` in `test_stage_it39.py`).** Ten proposals gain `INV-16`; the hand-over IT21P2-0014 now shows the assumption and the HIF1A or EPAS1 knockdown arm; hand-overs with a premise measurement go from 5 to 6 of 15. Status, hypothesis, eligibility, carried limits, selection and the hand-over ids are identical. **What changed:** one experiment shown beside one hand-over, and ten premise links. **What did not:** the search in the catalogue, the hypothesis and the compound list. No compound is forced.

**The 13th HIF1A chain** (`HIF1A -T(+)-> BNIP3`, three proposals) is not mapped: BNIP3 is a mitophagy gene, and no investigation measures that premise. Left explicit, not forced.

## MYC and HIF, the correspondence of results and explanations (review)

An MYC occupancy that stays the same after a HIF1A perturbation does not show the direction proposed in the Dream chain: it shows only that HIF1A is not needed for that readout. The chain note and INV-17's sentence now require perturbing each side and reading the other, in both directions and in time order.

## DREAM-4 (verified before applying)

`dream4_20261108/DELTA_FOR_IT39.md` was not applied (the needs did not name DL-MECH-181). Applied now: A (WNT O3 limits and the third counter-evidence string) and B (the one sentence in the notes of the ten needs that lean on GSE156243; for MTOR-AUTOPHAGY and REDOX-NRF2 the keyword pass found no composition caveat, which is why the sentence is needed there). Not applied: C (the open-question map has a 200-character cap on the decision column and is derived) and D (nothing to change: the generator already carries `SECOND_SYSTEM_PROGENITOR_GATE_FAILED` and `NPY_SIGN_CONTESTED` as support-limiting seed guards). Separate: the unsent EBI draft stays with the operator.
