# ADV-151 integration: the seven decisions D01 to D07 (IT, 2026-11-21)

Source: `../../../advisor_pilot_20261113/brainstorm_20261116/adv151_seven_design_decisions_sci_20261121/REPLACEMENTS_FOR_IT_ADV151_SCI_20261121.tsv` (main 959ec9f2f). Applied by `../integrate_adv151_it_20261121.py` (idempotent; every numeric token of an inserted text traced to the row's column, another row's column, the older texts or the current text; the only identifier outside them is 1.4286, the reciprocal named in D05; the run printed `unlisted tokens: []`). Old markers and sentences are in the History section "Decision markers and sentences replaced on 2026-11-21". Public, disease-level; no dose; not medical advice.

| Row | Item | Applied as |
|---|---|---|
| D01 | C09 | note; the stage 1 row now lists the flat-profile panel cell at one exposure; dose check in stage 2 |
| D02 | C30 | note (e2 list kept; PTH and lipid only as an optional extension) plus a laboratory question on blood volume |
| D03 | C31, Q57 | note (one combined add-on, serial in the same pups, split only if blood volume forces it) plus a laboratory question; marker Q57 replaced by a pointer |
| D04 | C35, Q70 | the multiplicity bullet rewritten: k per genotype per session (6 in wild type per age, 2 in knockout and heterozygote), levels 99.17% and 97.5%, planning total about 354 unchanged; marker Q70 (how many comparisons) replaced by a pointer because the rule answers it |
| D05 | R2C01 | endpoints 0.7 and 1.43 belong to the specificity class; the no-specificity band is the open interval; the thresholds row, the L1 row, the quoted row of note Q82 and the band of note Q73 reworded; TWO NOTES NOT DECIDED (rounded reciprocal 1/0.7 = 1.4286; point ratio or interval scoring) carried as OPEN-GAP D05a and D05b, owner the design team with the laboratory, before data, as a pre-registration amendment, with the options; no deviation from the frozen priors file is adopted |
| D06 | R2C09 | primary = knockout ethosuximide ratio at the assay age (exposure fixed by the laboratory before data), judged at 95%; every other ratio descriptive; item (ii) of the order of hypotheses says so; plus a laboratory question |
| D07 | R2C10 | prediction P5 kept two-sided and frozen; a ratio of at least 1.43 is knockout-attenuated and does not qualify the cohort by itself; the cohort condition now reads "rejected on the side of an interaction ratio at most 0.7" |

Marker totals in the governing text (before the History): CONFLICT-OPEN 0 (was 0); OPEN-GAP 79 to 75: design team 34 to 27 (seven decisions, Q57 and Q70 closed; D05a and D05b added), laboratory 37 to 40 (D02, D03, D06), operator 8 to 8.
