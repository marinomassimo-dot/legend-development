# IT46 P3: new case, fixed before execution (S7 raising GABA availability, read against the chloride condition S6)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Written and committed **before** any C1-C4 count, comparison or reading for this case. The IT46 method was built on S10 and S3-Kv7 (IT45) and on the whole role table; S7 was not a case of that construction.

## Selection (mechanical, applied once; no second draw)
Rule fixed here: among the investigations of `investigations_it20.tsv` (rank order), take the highest-ranked one that (a) has a relation row in the IT41-IT44 relation tables, (b) is not a case of IT43, IT44 or IT45 (those used S9, S10, S11, S12, S13, S2, S3 and the pH-K2P package of SCI45), (c) is not gene therapy, (d) is not the pH-K2P relation. Applied: INV-01 gene therapy (excluded); INV-02 and INV-03/04 have no relation row; INV-05 relations S1 and S8 belong to the IT40-IT42 GluN2B and AMPA cases and to IT44 S13 (used); INV-06 has no relation row; INV-07 = S9 and INV-08 = S10 (used); INV-09 no relation row; **INV-10 = S7 (GABA reuptake or GABA transaminase block)** is the first that passes. Context for the direction: relation S6 (chloride-gradient control), written in IT41/IT42.
Why this and not a variant of pH-K2P: it is a different mechanism family (supply of GABA), the sign of the action depends on a condition (the chloride gradient in the cell class and age), and the carded clinical thread (symptomatic response versus development) forces the separation the mandate asks for: WWOX rationale against general antiseizure efficacy.

## Need and snapshot of the inputs
Need: NEED-SEIZURE-CONTROL-SYMPTOMATIC (INV-10). Branch tip when this was written: dac7f36a (from main 142f6c5f). Input digests (first 16 hex of SHA-256):
| input | digest |
|---|---|
| `generation_it44_20261110/pointers_it44.tsv` | c56aa012730c56be |
| `generation_it44_20261110/entity_roles_it44.tsv` | 337aefd68e80f75e |
| `generation_it46_20261111/ladder_it46.tsv` | 27f6e8362565b9d9 |
| `generation_it46_20261111/cell_context_it46.tsv` | aae87173de839114 |
| `ranking_it8_p9_20261029/investigations_it20.tsv` | bbc80d2bbfa9271c |
No new activity read is made for this case unless C2 shows a state other than OK (then the read is a stated addition).

## Baseline and the four arms (same inputs for each; the advantage is attributed to the method only if inputs match)
* **C1** simple target search: the catalogue's curated mechanism rows for SLC6A1 and ABAT (distinct parent molecules, direction).
* **C2** plus the dose-response activity rows already read for S7 and the interaction table (molecules with a catalogue status, counted apart from C1).
* **C3** plus qualification: the ladder rows of S7 (reached / identity / action / transfer / benefit / next verification) and the roles.
* **C4** the contextualised combination: written from the frame below, with relations, alternatives and discriminating results fixed before any compound name is read for this case.

## C4 frame (written now, before names)
| Item | Statement |
|---|---|
| Observation to explain | Reduced inhibition or a net excitatory GABA action in the immature Wwox-deficient cortex is one of several explanations of the burst phenotype (IT41/IT42 frame; chloride state unmeasured). The carded thread reports a symptomatic response without a developmental gain in a few published children. |
| Relation | Raising synaptic GABA (uptake block or transaminase block) restores inhibition **only if** GABA is hyperpolarising in the recorded cells; if the chloride gradient is depolarising, more GABA raises excitation. The sign is conditional. |
| Alternatives | (a) the burst is network-driven by glutamate (IT40-Q01) and GABA supply is irrelevant; (b) GABA acts through tonic receptors, not synaptic; (c) a response that is symptomatic for any antiseizure mechanism and says nothing about WWOX; (d) a transaminase block changes GABA content with effects unrelated to the burst. |
| Discriminating results (written before names) | D1 gramicidin-perforated measurement of the GABA reversal potential in the recorded cell class by genotype: more negative than rest in both genotypes supports a hyperpolarising action; at or above rest in the knockout flips the sign. D2 burst incidence with a GABA-A antagonist in the same slices: no change argues against any GABA contribution. D3 a GABA supply arm and an unrelated antiseizure arm of equal effect on burst incidence: equal means a generic effect, a larger GABA effect means a GABA-specific one. D4 a developmental read-out is not obtainable in a slice, so no benefit in function is claimed. |
| Where the lever is inert or opposite | Depolarising GABA (conditional); glutamate-driven bursts; effect only in wild type. |
| What no table here can say | the cell class and age of GABA reversal (no held cell-class table carries SLC12A2, SLC12A5, GABR*, SLC6A1 or ABAT: `cell_context` returns NOT_IN_TABLE and that stays unknown). |

## Predicted difference of the method (written before the counts)
1. C4 names the chloride gradient as the premise that decides the sign, with D1, where C1-C3 name a vigabatrin or reuptake-blocker arm and nothing about the sign.
2. C4 separates the WWOX rationale from the general symptomatic efficacy of the class (D3), which C1-C3 do not.
3. The next experiment of C4 differs from the one C1-C3 would name (a measurement of the GABA reversal before any compound arm).
4. The context join adds **nothing** here (all genes NOT_IN_TABLE): the expected contribution of the context part is zero, and a zero is a valid, reported outcome.

## Outcomes that count as failure (reported, then the method is simplified)
* The C4 next experiment equals the C1-C3 one (no change).
* C4 states a premise that the independent reader finds unsupported by the named primary source.
* C4 produces fewer defensible hypotheses than C3 (it only restates).
* C4 recovers no molecule or comparison that C1-C2 missed **and** adds no premise: the method adds nothing for this case.
Counts: ladder rows of S7 by situation; molecules per arm; premises resolved against open; hypotheses formulated; opportunities missed by C1 and recovered; false proposals avoided; change of the next experiment; observable time (wall clock) and tokens.

## Independent verification perimeter
One blind reader (sonnet, high effort; no recursion): receives the C4 frame, the premises C4 relies on with their named primary sources, and the C1-C3 tables; does not receive my conclusions. It reads the primary documents the premises cite (GABA reversal in immature cortical neurons; a symptomatic-versus-developmental discordance in genetic DEE cohorts; the transaminase-inhibitor and reuptake-blocker mechanisms) and returns SUPPORTED / UNSUPPORTED / NOT_REACHED per premise. Not included: the biology of any other relation, the S6 relation search itself.

## Addendum (written before C4 or any scoring; the S7 reader had not returned)
* **Reference for role correctness.** The C3 role counts restate the engine's own labels and cannot show a label is right (HE46 H6). The reference for the S7 rows is the catalogue `modality` field (a field no earlier rule read), reported beside the agreement as: agree / disagree / unverifiable / NO_REFERENCE. Activity-only rows without a catalogue entry are NO_REFERENCE, never counted as agreement.
* **Baseline against variant on the same inputs.** The baseline is the repository at main 142f6c5f (role table without the modality rules, no ladder, no cell-context); the variant is the branch tip. The S7 inputs (relations, activity rows, mechanism rows) are identical.
* **Disclosure.** Before writing the frame above I had seen the S7 relation row, whose wording already says that the direction is conditional on the chloride gradient. The chloride-sign premise is therefore **not new to the repository**; C1-C3 (relation text included) already carry it as words. The method's added contribution has to be judged on the discriminating measurement D1, the separation of WWOX rationale from generic antiseizure effect (D3), the false-link findings of C3 and the order of the next experiment, not on naming the premise.
* **S7 history.** S7 was framed and searched in IT42 (second relation); it had no activity qualification and no contextualised combination before IT46. It is not a case on which the IT46 capabilities were built.
