# ADV-314 result (SCI, 2026-11-28): what Repudi 2021 prints for N1 and N2

Hypothesis-level; reference genotype class only; nothing here is medical advice. Source: PMID 33914858 (held operator-supplied PDF, sha256 113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c). No delegate; **not blind-checked**. PREREG `PREREG_ADV314_SCI_20261128.md` (sha256 4dd86f6fd52e49c6497f8edb2a7ef85df89c900c793b5c2ce12ce831ce30d1e8), frozen before any figure, supplement or spreadsheet was opened. Arithmetic: `arith_adv314.py`, `arith_output.txt` (`python3 -I`).

## 1. One line per reading
| Reading | Verdict (frozen rule) | Locator |
|---|---|---|
| E-A, a slower N1 in the same recruited population | **NOT PRINTED** (premise unsupported: the one printed composition measure, the N1/N2 peak ratio, differs) | Fig. 5D(ii, iii) and legend, p. 3071 |
| E-B, changed recruitment or responding-fibre proportion | **ALLOWED, not shown** (peak ratio about 2.75 to 0.85; no area, no absolute group value, no input-output curve) | Fig. 5D(iii), p. 3071 |
| "Conduction slowing" or a velocity | **NOT SUPPORTED as stated**: one distance, no velocity; what is printed is a longer N1 latency | Fig. 5D legend; Results p. 3069 |

The two readings are not exclusive.

## 2. What is printed
| Quantity | State |
|---|---|
| N1 and N2 latency | PRINTED as per-slice points in Fig. 5D(ii): 8 slices per group (control from five mice, S-KO from six). Figure marks: N1 `*`, N2 `n.s`. No mean in numbers; "to N1" does not say peak or onset. Readback of means about 2.43 to 3.17 ms (N1) and 6.68 to 8.30 ms (N2). |
| N1 and N2 amplitude | Only the per-slice **peak ratio** N1/N2, Fig. 5D(iii): mean 2.75 to 0.85 (readback), P = 0.0030. No group value of N1 or of N2 alone. |
| N1 and N2 area | NOT PRINTED (query: held PDF text, browser-print text and supplement PDF text, 2026-11-28). |
| Absolute size | One example trace per group, scale bar 0.2 mV and 5 ms, Fig. 5D(i); N1 and N2 are labelled on the knockout trace only. In the examples the knockout's first labelled trough is shallow and its second deep, next to a very deep early trough in the control. One trace each: an illustration, not a measurement. |
| Stimulus intensity, input-output curve, rate, electrode for the callosal experiment | NOT PRINTED. Methods give 0.1 ms pulses "with varying strengths" and 100 µA for the cortical layer V to II/III experiment; no callosal stimulation protocol (same three texts; terms "callosum stimulation", "callosal", "input-output"; 2026-11-28). |
| Distance | One: "vertical distance of 250" µm (legend). Path length along the fibres not printed. |
| Recording site | Results: "recorded from neocortical layer V". So the response is not shown to be a within-callosum fibre volley. |
| Source data | The supplement's three spreadsheets are RNA-seq (two) and primers and antibodies (one); none holds recordings. Europe PMC lists no correction notice (one query, 2026-11-28). |

## 3. A premise in the record to update: the two legend P values are latency tests
The legend places "(N1 *P = 0.0104; N2 = 0.5737 ...)" inside item (i), the traces. The 2026-11-27 clemastine note therefore says it is not stated whether they test latency or amplitude. Panel (ii) itself draws `*` for N1 latency and `n.s` for N2. With 8 against 8, the exact two-sided rank-sum values are U = 8 for 0.0104, U = 26 for 0.5737 and U = 5 for 0.0030. The plotted points give U = 26.5 for N2 latency (close pairs inside the readback) and U = 5 for the ratio; N1 latency reads as U = 7 or 8 (overlapping markers, not resolved). Reading (inference, firm): they are the latency tests.

A second point inside the paper: Results report "significantly lower peak amplitudes of the evoked potentials", but no test of an absolute amplitude is printed; the only amplitude test is the ratio.

## 4. Strong counterexample (frozen): cuprizone callosum, PMID 31140740
Myelinated-axon proportion down about 72 and 89 percent, N1 velocity unchanged, N1 area down, N2 amplitude up (ADV-313 table). The Repudi ratio fall resembles that amplitude pattern, yet there it came **without** a change in N1 velocity. So (a) fewer myelinated axons does not require a later N1, and (b) E-B, although allowed, does not by itself explain the Repudi N1 latency.

**What Repudi's N2 adds:** less than "N2 is unchanged". Means rise 24 percent (ln +0.217), medians 9 percent (ln +0.086); two knockout slices sit near 14.6 and 16.2 ms. P = 0.57 at n = 8 establishes neither a shift nor equality, so N2 cannot serve as the internal control that would confine the effect to myelinated fibres. N1 means move ln +0.27, of the same order as the N2 mean shift.

## 5. Derived arithmetic (not a number the paper states)
If 250 µm were the whole path, N1 would travel at about 0.10 m/s (control) and 0.08 m/s (S-KO), N2 at 0.04 and 0.03 m/s. Adult callosal N1 velocities in the ADV-313 table are about 0.5 and 1.8 m/s in two other preparations; ages differ (here P13 to P17), so this is no test. It does show that the path is longer than the printed vertical distance, or that much of the latency is not travel time, or both. A velocity cannot be derived.

## 6. Predictions
All five met (ratio lower; no absolute group values or areas; no callosal input-output or stimulus rule; one distance; E-A not printed and E-B allowed). They are weak tests: the ratio's P value had been seen before freezing, and the 2026-11-27 clemastine note had already read the bars (not opened before freezing).

## 7. What changes
* **INV-06, named callosal measurement:** N1 and N2 **area and peak** against stimulus intensity (input-output curve); latency (onset and peak) at three or more measured distances; recording site stated (within callosum or cortex); same tract and slices for both genotypes; animal as the unit; EM from the same tract.
* **RP-049 resume condition (ADV owns the row):** the present wording (three distances, absolute early recruitment, EM, or an independent callosal source with a stated intensity) stands. Suggested addition: N1 **and** N2 area or amplitude, and the recording site.
* **Wording (to IT):** `SENTENCES_FOR_IT_ADV314_SCI_20261128.md`.

## 8. Not new, and a duplicate-check miss
`continuous_compounds/clemastine/callosal_propagation.md` (2026-11-27, receipt FTR-20261127-33914858-38) already read the Fig. 5D bars, stated that absolute values are unavailable and set out the slower-travel and fixed-offset readings. ADV-314's duplicate check did not list it. New here: the P values assigned to latency, the rank-sum check, medians for N2, the example traces, the layer V recording site beside the velocity arithmetic, the cuprizone counterexample and the frozen verdicts.

## 9. Limits
Figure values are one session's readback from a raster of 1000 by 887 pixels; slice-level tests, mouse-level uncertainty not recoverable. Small inconsistencies seen and not used: the text's "3.5–4-fold" fewer callosal myelinated axons against its own averages 180 and 55 (3.3-fold), and "6-fold" more unmyelinated optic-nerve axons against 270 and 55 (4.9-fold).
