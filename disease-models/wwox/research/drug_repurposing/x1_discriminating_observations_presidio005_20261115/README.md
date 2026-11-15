# PRESIDIO-005: what would separate a soluble signal from a composition difference and from cell contact in INV-06 X1 (2026-11-15)

Written for: the ADV presidio and the IT Orchestrator (the owner of INV-06). Non-canonical research material; not medical advice; reference genotype class only; no compound is nominated. In silico, held files only, no new literature, zero spend. Labels DATO (a statement held in a file), INFERENZA (reasoned here). Task record `ledger/tasks/orchestrator/ORCH-PRESIDIO004B-005-20261115.json`.

## Answer first

**Partly answered already, and the missing piece is a join, not new biology.** The held rows already carry most of the controls of the soluble leg (OQ9, OQ11: a fresh-medium baseline, a mixing arm, a dilution series, purified-neuron medium, a positive-control medium, a detection limit from the monoculture variance). The contact leg lives somewhere else (INV-06 `next_test`: "add a fixed-neuron arm and a factor arm"; it36 `comparison.tsv` ALT2: X1 is conditioned medium, transwell and fixed null neurons) and is in none of OQ9, OQ11 or OQ12. No held row says what each outcome would favour, and none joins the three legs. That table is below (`discriminating_observations.tsv` has the same content with sources per row).

**No single observation separates the three explanations.** The smallest set is four things on one preparation, read in this order:

1. **O0, the premise (gate):** the null-neuron deficit reproduced blind, independent preparations, axon-density denominators (OQ12). Without it, nothing below can be read.
2. **O1 + O2, the soluble leg:** conditioned medium on OPC monoculture, null versus wild-type, matched for neuron number and viability, with a fresh-medium baseline, a mixing arm and a dilution series.
3. **O3, the composition readouts taken in the same dishes:** neuron number, viability, fraction of non-neuronal cells (they carry the null genotype too), axon density and calibre, T3, T4 and a nutrient in conditioned versus fresh medium.
4. **O4, the contact leg:** OPCs on fixed null versus fixed wild-type neurons, and a transwell arm (shared medium, no contact).

O5 (neutralisation of a named candidate) only identifies a candidate inside the soluble explanation and separates nothing between the three; it comes after a positive O1.

## What each outcome favours (E1 soluble, E2 composition, E3 contact or substrate)

| Observation | Result | Favours | Does not say |
|---|---|---|---|
| O1 medium, null v wild-type, positive control working | lower MBP+ share with null medium | E1; E2 in its medium form not yet excluded | which factor; whether neurons or non-neuronal cells release it |
| O1, positive control working | no difference | E3 (not a short-lived factor: conditioning loses those) | that activity is irrelevant |
| O1, positive control failing, purity not shown, or detection limit above the effect | any | nothing (uninformative) | |
| O2 mixing and dilution | effect persists in the mixture and falls graded with dilution | E1 (inhibitor) | |
| O2 | effect vanishes when mixed with wild-type medium | missing cue or depletion (E2 medium form) | |
| O3 | effect tracks neuron number, purity, depletion or axon density | E2 | that a signal is absent, only that it is not needed |
| O3 | effect survives matching and purification | E2 is not the explanation of the medium effect | the co-culture deficit itself; denominators there are scored separately |
| O4 fixed neurons | deficit persists on fixed null neurons | E3 | which surface or matrix cue |
| O4 transwell | deficit recovers across the membrane while conditioned medium (O1) is null | a short-lived or continuously supplied soluble factor (E1) | |
| O4 fixed neurons | fixed wild-type neurons do not support maturation at all | nothing: uninterpretable | no held source says whether they do |

**Compatible with all three** (so not discriminating): a lower MBP+ share in the live co-culture alone; any medium effect without matching or purity; a persisting null-versus-wild-type gap after an OPC-intrinsic reagent (SCI50: predicted by the neuron ceiling and by an OPC-intrinsic block alike); and a change of the expression of a candidate such as CTGF/CCN2 in Wwox-null tissue (ADV-007: composition-explained in the one concordant table, the mouse tables disagree in sign, expression is not secretion).

**Which control interprets a null:** a null from O1 is read only with a medium positive control that works in the same run, neuron purity shown and a detection limit taken from the monoculture's own variance (the co-culture's 20-point gap is not a monoculture limit). A null from O4's fixed-neuron arm is read only if fixed wild-type neurons still support OPC maturation.

## What this does and does not change

* **Decision changed (if a measured premise ever reopens X1):** the arm specification must contain the contact leg (O4) and the composition readouts (O3) beside the soluble controls already held; otherwise a positive O1 cannot be told from depletion or from non-neuronal cells, and a null O1 cannot be told from a lost short-lived factor. It changes no ranking, need or candidate state and it does not reopen the CTGF expression check (closed by the operator on ADV-007's verdict).
* **"Composition" here** means a difference in what the dishes contain (neuron number and viability, non-neuronal cells, axon density and calibre, medium depletion), not in what each neuron releases. ADV-007 used the word for tissue cell-type composition; the two senses are related and not identical, and the presidio may re-scope the term.
* **Not decided here:** whether O4 or O3 is cheaper; no cost, reagent or protocol is proposed; no neutralising reagent is nominated.

## Sources read (held files, in this session)

`myelin_phenotype_first_sci50_20261113/README.md` and `output/hypotheses.md` (H4, its strongest alternatives, the final form), `output/open_questions.tsv` (OQ7, OQ9, OQ11, OQ12), `ctgf_held_data_adv007_20261114/README.md` and `per_table.tsv`, the INV-06 row of `ranking_it8_p9_20261029/investigations_it20.tsv` (next_test clause), and `myelin_generative_it36_20261108/levers_bc/output/comparison.tsv` (ALT2 row, read as a single line). The INV-06 X1 arm text itself (the original (a), (b), (c) statement) was not found in the files searched; its description here comes from those two lines and is second-hand.

## Limits

* The premise is two experiments, n 4 v 4, peripheral DRG neurons, seizure-free dish (SCI50); every outcome above is conditional on OQ12.
* The positive controls (recombinant CTGF, Tsc2-knockdown neuron medium) rest on one paper read at queried depth in SCI50 (authors' claim in Tsc models, not Wwox).
* The outcomes are reasoned (INFERENZA); no measurement was made and none is claimed. No blind verifier (assignment: optional unless a claim changes a row's standing; none does).
* The effect of fixing neurons on the substrate is a known unknown (no held source); the transwell cannot exclude cell-contact-dependent factors released only on contact.

Files: `discriminating_observations.tsv` (6 rows, 9 columns), `consumer_delta.md`.
