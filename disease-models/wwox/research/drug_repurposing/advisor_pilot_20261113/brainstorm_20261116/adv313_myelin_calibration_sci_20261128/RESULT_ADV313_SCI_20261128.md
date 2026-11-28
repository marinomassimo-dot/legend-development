# ADV-313 result (SCI, 2026-11-28): the structure-to-conduction calibration table, now readable

Hypothesis-level; reference genotype class only; nothing here is medical advice. No delegate; **not blind-checked**: every number below was extracted by one session. PREREG sha256 d65dfca553a8c6d861d1a5d7c25bea3a926f3e21c207adb29ed686ff371277dd (`PREREG_ADV313_SCI_20261128.md`, frozen before the first new search or fetch; the inclusion rule and thresholds are those of ADV-312, unchanged). Table: `CALIBRATION_TABLE_ADV313_SCI_20261128.tsv`. Searches and routes: `QUERIES_ADV313_SCI_20261128.txt`. Arithmetic: `arith_adv313.py`, `arith_output.txt` (`python3 -I`).

## 1. Label: READABLE (7 counted sources; frozen thresholds 4 for direction, 6 for rank)
Three rows from ADV-312, unchanged (Palma 2022; Crawford 2010; Nr2f1 heterozygotes), and four new ones from the PubMed query set: a diabetic rat corticospinal tract (PMID 34576288), a mouse callosum with cuprizone and with L-NIO stroke (PMID 31140740), a mouse optic nerve with astrocyte exocytosis block (PMID 30373833) and a Fig4 conditional knockout optic nerve (PMID 27008179). The seven come from seven different laboratories, so the count collapsed by laboratory is also 7.

## 2. Readings (natural-log ratios, treated or mutant over control; speed form, slower is negative)
| Source (primary contrast) | Structure | Speed | Direction by the paper's headline EM variable | by g-ratio |
|---|---|---|---|---|
| Palma, clemastine, callosum | myelinated axons -0.142; g +0.024 | -0.170 (N1) | agrees | agrees |
| Crawford, EAE vs normal, callosum | thickness -0.799; g +0.077 | -0.074 (N1) | agrees | agrees |
| Nr2f1 heterozygotes, optic nerve | g -0.161 (relatively thicker); fibre number lower | -0.243 (first component) | agrees | **reverse** |
| Diabetic rat, corticospinal, lumbar | thickness -0.241; g +0.150 | -0.258 (fastest) | agrees | agrees |
| Cuprizone vs sham, callosum | myelinated axons -1.28 and -2.17 (two levels) | +0.036 and +0.012 (N1) | **null conduction** | **null conduction** |
| Astrocyte block, optic nerve | g +0.063 | -0.228 (latency average) | agrees | agrees |
| Fig4 Olig2Cre, optic nerve | myelinated fibres -1.88; g +0.063 | -1.15 (largest peak) | agrees | agrees |

Other contrasts in the same sources: the diabetic rat cervical level has thickness -0.351 with speed -0.028 (a disagreement under the frozen rule; g-ratio barely moves, +0.015); L-NIO stroke has myelinated axons -0.41 with N1 speed -0.13 (agrees); Fig4 SynCre agrees.

* **Direction.** By headline variable, primary contrast: 6 agree, 1 does not (cuprizone). Counting any contrast, two sources hold a disagreeing one (cuprizone; diabetic rat cervical). By g-ratio: 5 agree, 2 do not (Nr2f1 reverse; cuprizone null). **The ADV-312 reading "direction follows the headline structural variable in 3 of 3" does not hold as a general statement.** Which contrast of a source is "primary" was chosen after seeing the numbers.
* **Size.** No rank agreement under any choice of contrast: Spearman rho of |structural| against |speed| log ratios runs from -0.32 to +0.07 over 36 choices of headline variable, and from -0.14 to +0.07 over 8 choices within g-ratio (7 sources). The headline set mixes unlike variables (axon number, thickness, g-ratio), which is why the g-ratio class is given too. Leaving one source out moves rho between -0.49 and +0.37 (headline, first choices) and between -0.43 and +0.14 (g-ratio).
* **Frozen predictions (ADV-312).** E-B (rho 0.7 or more) is met by no combination. E-A's rank part (|rho| below 0.5) holds in all. E-A's direction part ("fewer than 2 disagreements") holds on primary headline contrasts (1) and fails by g-ratio (2) and counting any contrast (2 sources).
* **My ADV-313 predictions.** Table reaching at least 4: yes, but not through Crawford 2009 (closed): wrong on the route. Blades unread: right. "Direction reading unchanged by headline variable": **wrong**.

## 3. The frozen strong counterexample is met (cuprizone, PMID 31140740), with both readings
Definition: myelinated-axon density or proportion changed by 25 percent or more, with a conduction change below 0.05 in natural log. Here the proportion of myelinated axons falls by about 72 percent (+0.16 mm) and 89 percent (-1.59 mm) and N1 velocity changes by +0.036 and +0.012; the paper's text says velocity was not altered.
* **Reading 1:** a large demyelination need not move the measured velocity, so a velocity cannot stand in for the structural readout, nor the reverse.
* **Reading 2:** the functional effect is there but in another feature. N1 area fell at both levels (N1 amplitude at +0.16 mm; not significant at -1.59 mm) and N2 amplitude rose. N1 velocity then belongs to the fibres that still conduct in the fast component.
* **Limits of the source:** one distance (0.75 mm, from the stimulus artefact), no distance series; velocity and structure read from figures; the supplement's overall g-ratio panel at +0.16 mm prints values above 1 and a lower cuprizone mean, against its own Figure 3D; the plots show more points than the legend's group sizes.

**Inference (not tested within one paper):** which CAP component the velocity belongs to matters. Fig4 measures the largest peak, whose identity moves to a slow velocity when most fibres lose myelin (1.9 to 0.6 m/s); cuprizone measures the fast N1 peak, which keeps its velocity while shrinking. Both pictures fit fibres leaving the fast component.

## 4. Quality notes on the new rows
* Diabetic rat: g-ratio and thickness come from combined optical and electron micrographs (a stricter electron-only rule would drop it, leaving 6 sources: still readable and still at the rank threshold); the conduction path (cortex to stimulation level) is longer than the segment measured structurally; separate animals; axonal atrophy accompanies the myelin change.
* Astrocyte block: authors attribute part of the slowing to nodal-gap widening, so the speed change is not all thickness.
* Fig4: structure read from figures by eye (large effects); dominant-peak velocity is a different quantity from N1 velocity.
* Rank over sources that use different conduction quantities (N1, fastest latency, first component, latency average, largest peak) is descriptive at best.

## 5. Leads, routes and what stays open
* **Blades 2022:** no lawful machine route to the article body (publisher subscription; University of Melbourne repository answers with a challenge page, not bypassed). Its open supplement holds model values only. A person with a browser can try https://hdl.handle.net/11343/301987 (listed as a submitted version; access not verified).
* **Crawford 2009** (two papers): closed, no PMC record; same laboratory as Crawford 2010. A 2013 paper of that laboratory (PMID 23603111) has g-ratios in text and CAP amplitudes only in a figure; not counted.
* **Abstract-only sources of ADV-312:** Luo 2018, taiep, md and LES rats: closed. Balraj 2023 and CRMP2 knockout (PMID 37479154, EM and callosal CAP by abstract) answered 403 on every open copy.
* **Peripheral nerve stratum:** not searched (the CNS leads did not fail).
* **Distance series:** only two of the seven measure velocity from several stimulating-to-recording distances (Palma 2022; Crawford 2010, 0.5 to 2.5 mm), both ADV-312 rows; none of the four new ones does as far as their Methods passages read here show.
* **Not reached:** an electron-only source with a distance-series velocity and EM in the same animals (the ADV-312 registered missing observation stands).
* **Search limits:** eight PubMed queries, titles and abstracts; recall unknown; the new sources are those with an open PMC body.

## 6. What changes
Compound briefs may not keep a structural myelin statement alone, and N1 velocity alone is not enough as the named functional readout either. Wording for IT: `SENTENCES_FOR_IT_ADV313_SCI_20261128.md`; it replaces ADV-312 lines Z1 and Z3 and narrows Z2 (none of Z1 to Z4 was found in any card or brief on 2026-11-28).
