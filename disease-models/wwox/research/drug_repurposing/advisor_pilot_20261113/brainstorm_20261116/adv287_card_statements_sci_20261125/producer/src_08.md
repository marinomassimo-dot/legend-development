# src_08 — F03 p4_card.pharmacology: "mouse brain to plasma ratio about 0.015 to 0.02 and efflux at the blood-brain barrier (abstract level);"

Card: F03_bumetanide_chloride_gradient, /p4_card/pharmacology (sentence begins "IT8 P3 2026-10-29: GtoPdb ... mouse brain to plasma ratio about 0.015 to 0.02 and efflux at the blood-brain barrier (abstract level)"). Cited PMIDs: 25449033, 33279441, 30248303 (pharmacological_qualification_it8_p3_20261029/README.md D3 and cases.json Q08). Species: mouse (the cited ratio); bumetanide.
Held: no PubMed abstract bytes for 25449033 in files/ (search of files/ for the PMID and "Töllner" returned only unrelated full texts and a geo file). What is held: (a) the producer table of the ADV-065 package, advisor_pilot_20261113/brainstorm_20261116/adv065_chloride_nkcc1_sci_20261118/NKCC1_KCC2_TABLE_PRODUCER_DELEGATE_20261118.md, section Q3 (all 13 rows read), which carries a verbatim abstract sentence per paper; (b) locator_audits/2026-10-30_it8_p3_verifier.md ("Re-read at abstract level: PMID 25449033 gives the mouse brain-to-plasma ratio of about 0.015 to 0.02 (confirmed)"); (c) bumetanide_exposure_arithmetic.tsv. Reading depth: table with verbatim abstract sentences (the abstract itself was not held and not re-read here).

## Whole Q3 table (all rows; ratio and exposure content only)
| PMID | first author, year | species | model | finding as tabulated | verbatim sentence |
|---|---|---|---|---|---|
| 28192112 | Römermann 2017 | mouse | BBB transport; Oat3 cells | brain levels typically below NKCC1-inhibitory; passive diffusion limited, Oat3, Oatp1a4, MRP4 efflux | "following systemic administration, brain levels of bumetanide are typically below those needed to inhibit NKCC1" |
| 38823029 | Löscher 2024 | rat | 14 regions, i.v. | brain:plasma 0.004 (amygdala) to 0.022 (olfactory bulb) | "Brain:plasma ratios ranged between 0.004 (amygdala) and 0.022 (olfactory bulb)." |
| 25449033 | Töllner 2015 | mouse | probenecid co-treatment | brain:plasma about 0.015-0.02, unchanged by probenecid, absolute levels rose | "so that the brain:plasma ratio (~0.015-0.02) was not altered." |
| 33279441 | Hampel 2021 | mouse | PK-PD model, equilibrium dialysis | about 6-17 percent of brain concentration free; free brain conc. in NKCC1-inhibitory range at the dose used (10 mg/kg i.v., per abstract) | "only about 6-17% of the brain drug concentration were freely available." |
| 37037061 | Welzel 2023 (a) | rat asphyxia | higher dose | median brain 0.47-0.53 uM, in NKCC1-inhibitory range | quoted |
| 33955541 | Johne 2021 (b) | rat P11 | clinical dose | not NKCC1-inhibitory | quoted |
| 25463517 | Wang 2015 | rat P10 | systemic course | incompatible with NKCC1 inhibition | quoted |
| 30248303 | Brandt 2018 | rat, mouse, neonatal rat slices | equilibrium dialysis | high unspecific brain binding | quoted |
| 25490899 | Donovan 2015 | rat | hippocampal microdialysis | ECF low relative to systemic | quoted |
| 26673740 | Donovan 2016 | human OAT3 cell line | permeability | 53 percent albumin-bound, 77 percent brain-tissue-bound | quoted |
| 24251546 | Töpfer 2014 | mouse and rat | piperonyl butoxide | PBO raised half-life (mice 70 min) and brain levels | quoted |
| 36586153 | Welzel 2023 (b) | rat | torasemide, azosemide | torasemide below NKCC1 range | quoted |
| 29319897 | Donovan 2018 | modelled neonate | PBPK | not robust | quoted |
Table's own summary: "Brain:plasma ratios of about 0.004-0.022 (Löscher 2024, rat, 14 regions) and about 0.015-0.02 (Töllner 2015, mouse)".

## Recomputation
No printed arithmetic. The only mouse ratio in the table is Töllner 2015: about 0.015-0.02 (the table cell and the verifier agree). The range 0.015 to 0.02 is not a spread across documents (one mouse document); the rat figures (Löscher 2024, 0.004 to 0.022) are labelled rat in the table and the sentence says mouse. Efflux at the BBB: Römermann 2017 (mouse; Oat3, Oatp1a4, MRP4) and the probenecid design of Töllner 2015 (absolute levels rose, ratio unchanged); consistent. Limit: the abstract of 25449033 is not held, so "unchanged by probenecid" and "total/total" come from the producer table and the verifier note.
