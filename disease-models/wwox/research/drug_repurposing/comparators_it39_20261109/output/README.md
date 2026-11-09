# Comparators for the priority hypotheses (IT39 P8)

Non-canonical, not medical advice. Extraction and arrangement only: every cell comes from a file named in the brief, no web, no PubMed, no new reading of any paper. No dose, schedule or route is given; in-vitro assay concentrations appear only as the context of a measurement. Source cells use `file:Lnn` (line 1 is the header) or the need id and observation id.

## Answer first

`comparators.tsv` has 38 rows. Rows per role per investigation:

| Investigation | functional_outcome | mechanism_separating | total |
|---|---|---|---|
| INV-03 (T-type) | 3 | 5 | 8 |
| INV-05 (NMDAR) | 3 | 4 | 7 |
| INV-09 (GSK3) | 3 | 7 | 10 |
| INV-10 (seizure, development, function) | 6 | 0 | 6 |
| INV-18 (Ih / HCN) | 2 | 5 | 7 |
| all | 17 | 21 | 38 |

* **INV-10 has no `mechanism_separating` comparator in the files.** Its questions (Q1 to Q7) are about outcome measurement and mediation analysis, not about a pharmacological contrast. The only second, mechanistically different agent mentioned near it (question Q3) belongs to the T-type package and is counted under INV-03.
* In INV-03 the `mechanism_separating` rows are weak by the files' own account: the proposed pair (efonidipine, flunarizine) is a proposal to verify, ML218 and TTA-P2 share the Z944 scaffold, and the genetic arm is "not proposed as the first comparison". Rows exist, but the files say none of them yet discriminates isoforms.
* `antiseizure.tsv` has 15 rows (12 named drugs or regimens, 3 agent classes with no drug named). Every `wwox_specific_rationale` is either a hypothesis the files label as such (ethosuximide: T-type node; lithium: GSK3; memantine and perampanel: HYP-20261027-01) or `NONE_STATED`.

## How a role was assigned (my reading; check it)

The files do not label roles. I used the stated purpose of each comparator in the files:

* `functional_outcome`: a drug or regimen whose reading in the files is the change of the functional result itself (burst, seizure score, sag, clinical seizure or developmental statement).
* `mechanism_separating`: a comparator the files introduce to tell mechanisms apart (matched-current reduction, second chemotype, enantiomer control, genetic perturbation, a Cav3 or Kv7 arm kept separate from the Ih arm, an unrelated-mechanism NAM pair).

Judgement calls that could be read the other way: d-APV in INV-05 and INV-09 is `mechanism_separating` (matched-current role) although it also carries the only WWOX burst result (stated in its cells); Ro 25-6981 and ifenprodil are `mechanism_separating` (the "two unrelated NAMs" design), radiprodil and memantine `functional_outcome`; Z944 is `functional_outcome` under INV-03 and `mechanism_separating` under INV-18; AR-A014418 and SB216763 (INV-09) are `functional_outcome` as the nearest fit, and the cells say the files do not propose them as arms. Efonidipine and flunarizine are assigned first-named and second-named by the order of names in the ranking row; the row does not say which agent has the one T-type target row, so that mapping is an order-based reading, marked in the comparator name.

## Cells left `NOT_IN_FILES` (exact cell value)

* `exposure_or_development_note`: 19 rows. INV-03: lithium, genetic perturbation. INV-09: all ten rows (lithium, CT99021, BRD0705, BRD3731, BRD5648, AR-A014418, SB216763, GSK3A/B genetic, PI4K2A genetic, d-APV carried). INV-10: cannabidiol, perampanel, ethosuximide. INV-18: second Ih blocker, NiCl2, XE991/Kv7 opener, myr-22.
* `context_of_the_measurement`: 2 rows: efonidipine (INV-03, no measurement in the files) and the unnamed second Ih blocker (INV-18, which is also `NOT_IN_FILES` in exposure).
* The comparator identity of the second Ih blocker itself is not in the files (row name says so). Cells that hold partial text such as "NOT_IN_FILES (target not stated ...)" (`target_and_action` for hormonal therapy, cannabidiol and perampanel in `comparators.tsv`, and several cells of `antiseizure.tsv`) are not in the exact count above.

## Notes on what the files override

* Where a probes table carries an audit bracket, the audit wording is used (CT99021 "two sources" is one source; ZD7288 at 50 uM is about 40 times the sodium-current IC50; myr-22 incubation correction; BRD3731 has no structural control; the 2024 vigabatrin case is uninstrumented and untimed with respect to the drug).
* Only the opening part (about 3,500 characters each: access notes, counts and first rows) of the five `verify/` audits was read, plus the audit brackets already inside the probes tables and READMEs. Most audit rows were not read; a probe fact corrected in a part I did not open is not reflected. Treat the override check as partial.

## Excluded or not reached

* CTxB FLIM-FRET (hcn probes P07) is a read-out, not a comparator; left out.
* Ketogenic diet is a comparator in INV-10 but not in `antiseizure.tsv` (not a drug).
* `aed_compare_it31_20261107/output/README.md` is cited by the INV-10 README as the home of the general-activity wording for perampanel and ethosuximide. It is not among the named inputs, so I did not open it; the `general_anticonvulsant_activity` column holds only what the named files say.
* `outcome_domain_reported` allows a value joined by a semicolon only where the file reports two domains separately (vigabatrin: seizure and development); the kept-separate note states each.
