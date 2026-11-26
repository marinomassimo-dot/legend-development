"""IT 2026-11-26 (IT28): consumer wording of SCI's ADV-285 (S1 to S8) and ADV-288 (T1 to T8, with the blind corrections of ADV-288 section 4).
Data only; applied by apply_285_288_it28.py after a blind check. Hypothesis level; reference genotype class only; no compound, dose or schedule chosen; nothing here is medical advice."""

F_OLD_PUP = ("a **partial latency prolongation with normal amplitude in heterozygotes, not equal to the null**; the authors write \"a partial Tc-MEP deteriorative change\"; **there is no heterozygote-against-null test**.")
F_NEW_PUP = ("a **latency prolongation in heterozygotes against wild type, with amplitude not different from wild type (59.6 against 59.2 microvolts, n.s.; n = 5, large spread)**; the authors write \"a partial Tc-MEP deteriorative change\"; "
 "**Fig 2c prints a bracket between heterozygotes and nulls on latency marked n.s., and Fig 2b one on amplitude marked * (heterozygote against null), although the Methods name only a one-way ANOVA with no post hoc test, "
 "so the test behind the brackets is unnamed and heterozygotes are not shown to differ from nulls on latency**. The Results call the measure \"onset latency\" while the Methods define latency as shock-artefact onset to the major positive peak, and the knockout line used for the recordings is not stated.")

F_OLD_SLICE = ("a **partial prolongation with normal amplitude in heterozygotes, not equal to the null**; the authors write \"a partial Tc-MEP deteriorative change\"; there is no heterozygote-against-null test.")
F_NEW_SLICE = ("a **latency prolongation in heterozygotes against wild type, with amplitude not different from wild type (n.s.; n = 5, large spread)**; the authors write \"a partial Tc-MEP deteriorative change\"; "
 "**Fig 2c prints a bracket between heterozygotes and nulls on latency marked n.s., and Fig 2b one on amplitude marked * (heterozygote against null), although the Methods name only a one-way ANOVA with no post hoc test, "
 "so the test behind the brackets is unnamed and heterozygotes are not shown to differ from nulls on latency**.")

ROW_OLD = "(partial prolongation, normal amplitude; no heterozygote-against-null test)"
ROW_NEW = "(latency prolongation against wild type, amplitude not different from wild type, n.s., n = 5; heterozygote-against-null brackets printed, latency n.s. and amplitude *, the test unnamed)"

G_OLD_PUP = "a candidate needing re-measurement with a rescue arm and animal-level statistics, not yet an endpoint.**"
G_ADD = (" The held latency is a single-distance first-peak latency (no velocity), the unit is the slice, recorded in neocortical layer V after stimulation of the corpus callosum; the N2 (second-peak) latency, whose identity is not defined in Repudi 2021 (the unmyelinated or partially myelinated label is Palma's) and which is not significantly different (P = 0.5737; wide spread, 8 slices per group), is a candidate within-slice control that the brief does not yet carry; "
 "no held source gives a conduction readout with a drug arm in a Wwox-deficient model, and no WWOX patient report with an evoked-potential or conduction result was found by a title-and-abstract search on two routes (2026-11-25). "
 "**Candidate arm set for a drug test of conduction (ADV-288; hypothesis; no compound, dose or schedule is chosen):** four cells in the same litters (wild type and knockout, vehicle and drug), because in healthy developing wild-type mice the pro-myelinating drug "
 "clemastine (one compound, Palma 2022; daily from P5, slices at P21; one mouse as the unit, n = 10 to 12) slowed callosal N1 conduction velocity (ratio about 0.84 read from Fig 2B; one asterisk, P < 0.05 by its legend, while the text states P < 0.01 and the Methods name a paired t-test for two independent groups), so a wild-type drug-only arm is needed before a knockout effect can be read as rescue; "
 "callosal N1 velocity from the distance-latency slope over at least three electrode distances with N2 as the control, one value per animal, the same animals' g-ratio, seizure status recorded, recording at P17 to P21; "
 "**24 animals per arm planned** (from the held spread, by graph reads, a slowing of the size seen by Palma needs 9 to 24 animals per arm, and at 12 per arm only a ratio of 1.29 or more, or 0.78 or less, is detectable at the upper spread) "
 "with a pilot of at least 8 vehicle animals per genotype to replace the graph-read spread; the comparison stops for a compound if wild-type N1 velocity falls by at least 10 percent with the interval excluding zero.")

INV06_NOTE = (" [IT 2026-11-26, ADV-285 and ADV-288: two Wwox-deficient mouse models have a conduction readout in held full text, with no drug arm: the global knockout in vivo transcranial motor-evoked potential "
 "(Cheng 2020, 3 weeks; amplitude 11.8 against 59.2 microvolts and onset latency 2.44 against 1.39 ms; 4 against 10 animals) and the neuron-targeted deletion callosal N1 latency in slices "
 "(about 3.2 ms in knockout against 2.5 ms in control, read from the graph; 8 slices from 6 knockout animals against 8 slices from 5 control animals; Repudi 2021, Fig 5D); neither separates a myelin cause from an axonal or excitability cause (the Tc-MEP path also includes peripheral nerve and muscle, and the same paper reports sciatic demyelination in the nulls). "
 "In healthy developing wild-type mice the pro-myelinating drug clemastine (one compound; Palma 2022, daily from P5, slices at P21, one mouse as the unit, n = 10 to 12) slowed callosal N1 conduction velocity (ratio about 0.84 read from Fig 2B; P < 0.05 by the figure legend, P < 0.01 in the text), so a pro-myelinating comparison in a Wwox-deficient model is more informative with a wild-type drug-only arm and a conduction readout; no Wwox-deficient study held has both.]")

G_OLD_SLICE = "It is a candidate needing re-measurement with a rescue arm and animal-level statistics, not yet an endpoint."
