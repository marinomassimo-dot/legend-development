# POST HOC addendum (not pre-registered; requested by ADV after delivery): T-type, Kv7 and NMDA-receptor subunit transcripts in the same mouse file (SCI, 2026-11-19; hypothesis level; no dose; not medical advice; the pre-registration and its result note are not edited)

**Label.** Genes were chosen by ADV after the ADV-088 result, not before the first count; the file (E-MTAB-6798 `Mouse.RPKM.txt`, sha256 in `input_digests.sha256`), the tissue (Brain), the ages (P0, P3, P14, P28, P63; four samples per age), the unit (RPKM) and the plateau (mean of P28 and P63) are those of the pre-registration. Script `posthoc_targets.py`; table `posthoc_targets_timecourse.tsv`. Basis limits as in the result note: whole brain, bulk transcript, one dataset, no P7, P10, P17 or P21, no layers, no protein, not the knockout.

## Answer first
**The ethosuximide target family (T-type, Cacna1g, Cacna1h, Cacna1i) is on a flat phase between P14 and P28 in this dataset, and the change in its composition lies between P3 and P14.** So a response that changes across a P14 to P28 age series would not be explained by T-type transcript level in bulk; below P14 the composition differs, which is a different target mix, not a delayed version of the same. Kcnq2 is the one gene of the set on a rising phase within P14 to P28.

## Mean RPKM per age (replicates at P14 and P28 in the table file)
| Gene | P3 | P14 | P28 | P63 | Phase in P14 to P28 | Where the change lies |
|---|---|---|---|---|---|---|
| Cacna1g (Cav3.1) | 23.1 | 21.3 | 18.3 | 17.9 | flat to slightly falling (P14 replicates 19.5 to 24.4; P28 13.7 to 19.9) | little change P3 to P63 |
| Cacna1h (Cav3.2) | 23.8 | 10.0 | 11.5 | 11.2 | flat (about +15 percent; P14 9.3 to 10.8, P28 10.4 to 12.2) | **falls to less than half between P3 and P14** |
| Cacna1i (Cav3.3) | 5.5 | 14.4 | 13.6 | 13.1 | flat (P14 13.7 to 16.1, P28 13.3 to 14.0) | **rises about 2.6 times between P3 and P14** |
| Kcnq2 (Kv7.2) | 23.4 | 25.4 | 37.9 | 37.6 | **rising (+49 percent; P14 23.6 to 27.1, P28 36.2 to 39.5: no overlap)** | between P14 and P28 |
| Kcnq3 (Kv7.3) | 10.7 | 21.1 | 20.1 | 17.2 | flat | rises about twice between P3 and P14 |
| Grin2b (GluN2B) | 24.9 | 29.4 | 26.2 | 23.9 | flat to slightly falling | little change |
| Grin2a (GluN2A) | 0.52 | 4.08 | 4.92 | 3.15 | mostly complete by P14 (+20 percent to P28; P14 3.3 to 5.0, P28 4.5 to 5.5, overlapping) | rises about eight times between P3 and P14 |
Plateau-based fractions for Grin2a are not meaningful here (P63 is lower than P28, so the pre-registered plateau gives 1.22 at P28 and 1.01 at P14); the raw means above are the reading.

## What it adds to the age questions (nothing is changed; the age decision is the laboratory's)
1. **Ethosuximide age series (pup brief section 2, item 3):** the T-type transcripts give no reason, at bulk level, for a response to change between P14, P17, P21 and P28; a change there would point to something other than target transcript level (the PV and GABAergic maturation of the time course, protein, region, pharmacokinetics: none tested here). **For the age floor:** ages below P14 sit where Cav3.2 transcript is more than twice the P14 level (at P3) and Cav3.3 about 0.4 of it, so an earlier age is a different target mix; P14 is the start of the flat phase.
2. **Kv7 arm (class label only):** Kcnq2 transcript rises by about half between P14 and P28, so an age series for a Kv7-class agent would run across a rising phase of Kcnq2 (and not of Kcnq3); same-day littermate controls at each age matter more for that arm than for the T-type arm.
3. **NMDA-receptor pore-blocker arm (class label only):** the GluN2B transcript is flat across P3 to P63 and GluN2A is mostly in place by P14, so P14 to P28 is a flat phase for the subunit composition; the large change in subunit mix lies before P14 (relevant to the slice package ages P9 to P12 against P13 to P17: the early arm would see a lower GluN2A).
4. **One more reason for litter-matched, same-day controls and age in days:** none of these genes is steady before P14.

## What it cannot tell
Same limits as the result note, plus: T-type channels are concentrated in particular regions (thalamus, with others), so a whole-brain mean can hide a regional rise or fall; transcript level is not channel function or drug sensitivity; four samples per age, and for Cacna1g the P28 spread includes one low sample (13.7); nothing here measures the knockout.
