# ADV-305 result: etifoxine against ganaxolone, from a developmental epilepsy dataset (SCI, window 64fc909a, 2026-11-28)

Hypothesis level; reference genotype class only; not medical advice. Step 0: `STEP0_ADV305_SCI_20261128.md` (prediction held). Step 1 rule: `PREREG_STEP1_ADV305_SCI_20261128.md` (sha256 ee5355cd41d71a7fc44e8b49e491bdb3a13c100cfed7771a1fd30ffd35c4eb57; frozen after the abstract and the printed MEA means were seen, disclosed in the file; the vehicle baselines, n and figures were not). Source: Adair et al., J Pharmacol Exp Ther 2025 (PMID 40561753, PMC12405918), 6-dpf zebrafish Scn1Lab larvae (Fig 3) and embryonic rat cortical cultures under 4-aminopyridine (Fig 4). Extraction by a delegate (legend-delegate, sonnet, effort high): `FIGURE_EXTRACT_PMID40561753_ADV305_SCI_20261128.md`; an independent second reading of the vehicle and 4-AP baselines agreed with the first within the plot resolution (Fig 3 spikes about 810 against 818, firing rate 0.023 Hz, events about 100; Fig 4 4-AP spikes about 405 against the printed 410.5, firing rate about 420). Computation: `replay_adv305.py`, output `replay_adv305_output.txt`.

## Result in one paragraph
**No explanation is favoured by the frozen rule.** Under the quantity as defined for the zebrafish assay (treated over vehicle), E1 (direct GABA-A potentiation), E2 (steroidogenic TSPO) and E3 (steroid-independent TSPO or metabolic) all fail their stated bounds. Under the alternative reading (share of the abnormal activity blocked), E1 and E2 fail and E3 holds in both assays, but every active arm sits at 81 to 100 per cent suppression, so the ordering is ceiling-bound and carries little weight. Both readings are reported because the PREREG defined the quantity on two scales (a flaw in the PREREG, not in the data). Result label: **ambiguous; E1 and E2 not supported on either reading; E3 compatible, not established.**

## Numbers (replay_adv305.py; values PRINTED in the text, vehicle and 4-AP baselines READ from the plots)

| ligand (concentration) | zebrafish spikes, treated/vehicle | zebrafish firing rate | culture spikes, share of the 4-AP rise blocked | culture rate |
|---|---|---|---|---|
| stiripentol (100 microM zebrafish; 5 microM culture) | 0.032 | 0.030 | 1.23 | 1.22 |
| XBD173 (20; 5) | 0.016 | 0.014 | 0.61 | 0.55 |
| etifoxine (7.5; 3) | 0.113 | 0.097 | 1.03 | 1.14 |
| PK11195 (10; 3) | 0.186 | 0.187 | 1.03 | 1.02 |
| Ro5-4864 (10; 1) | 0.82 | 0.75 | 0.29 | 0.40 |

Zebrafish: XBD173, a TSPO ligand with negligible GABA-A affinity, reduces spikes and rate by about 98 per cent, more than etifoxine (about 89 to 90 per cent), against about 97 per cent for the GABA-A modulator stiripentol; PK11195, which does not raise neurosteroid synthesis, still reduces by about 81 per cent. Cultures: etifoxine and PK11195 block the 4-AP rise completely, XBD173 only partly (55 to 61 per cent). Units and n: spikes are counts per well or larva, firing rate is Hz, n per arm is not stated by the paper (legend ranges; dot counts 7 to 11 per drug arm in Fig 3); the paper prints means and SDs of large relative size; no significance claim is made here.

## Reading of each explanation
* **E1** (etifoxine acts here like a GABA-A modulator): not supported; the TSPO-selective XBD173 is at least as strong as etifoxine in the larvae.
* **E2** (steroidogenic TSPO ligands lead, PK11195 trails): not supported; PK11195 equals etifoxine in the cultures and XBD173 is the weakest there, the opposite order from the larvae.
* **E3**: compatible only on the blocked-share scale: etifoxine, XBD173 and PK11195 all suppress and none departs from the others by more than a factor of 2.1; Ro5-4864 is the smallest (0.18 to 0.40), not zero.

## Strong counterexample and a post hoc observation (listed apart, not part of the frozen rule)
Stiripentol, which has no TSPO action, is as large as any TSPO ligand (0.03 of vehicle in larvae; the whole 4-AP rise blocked in cultures): the GABA-A route reaches the same depth. In the cultures the **burst** count behaves differently from spikes and rate: etifoxine and stiripentol suppress it (103.9 and 24.4 per cent of baseline, 4-AP alone about 380), XBD173 and PK11195 do not (319 and 201 per cent; P = .85 and .58), which is the pattern expected if the burst readout needed the GABA-A action; in the larvae the electrographic events fall with all three TSPO ligands (4.5, 3.2, 5.0 against about 100). Cross-assay disagreement on the burst readout; one culture panel only.

## What it changes
* **Etifoxine's role in INV-10: unchanged as a conditional probe, with one addition.** A TSPO-selective comparator, XBD173 (not named anywhere in the repository before this work), should stand beside etifoxine, and ganaxolone is the cleaner GABA-A-only comparator, because a TSPO-selective ligand reproduces the effect of etifoxine in a developmental epilepsy model without any GABA-A potentiation. The model does not tell which of the three routes carries it.
* **The timing question stays a laboratory dependency.** Every arm is pre-incubated 40 minutes to 3 hours, concentrations differ (1 to 100 microM nominal), exposure and chloride are not measured, and no blockade of etifoxine is shown. Missing observation: acute against pre-incubated response of etifoxine, with and without a TSPO or 5-alpha-reductase block, with ganaxolone and XBD173 in the same cells at matched free exposure.
* **Reading flaws to carry:** the paper's own legend and plot disagree in several places (Fig 4 panels B and C are swapped relative to the legend; text and plot differ for PK11195 firing rate, 92.9 printed against about 130 plotted, and for XBD173, 243.8 against about 269; PTZ concentration 7.5 against 20 microM; star counts differ from printed P values in 7 Fig 3 cases); the printed values were used and the plotted ones kept as a sensitivity (PK11195 culture rate blocked 0.91 instead of 1.02; no rule outcome changes). The etifoxine brief says etifoxine raises neurosteroid synthesis in frog explants; this paper's discussion says it does not: disputed, not resolved here.

## Alternative branch (B), registered
Baricitinib against an IL-1 or microglial comparator: no JAK-inhibitor dataset with developmental stage and cell resolution exists (dated searches in step 0); the trophic arm exists and conflicts between Laitman and Steelman. Missing observation: paired pSTAT1 and pSTAT3 with first-sheath or survival readouts in the same developing Wwox preparation under a JAK inhibitor. No analysis was run for B.

## Not done
Fig 1 swim behavior, Fig 2 and Fig 5 (respiration) were extracted but not used in the rule; no supplement exists; no full second extraction of every figure (only baselines). The paper was not graded sentence by sentence; no consumer sentence of the repository was checked.
