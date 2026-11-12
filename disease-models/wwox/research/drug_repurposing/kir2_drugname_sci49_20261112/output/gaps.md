# Gaps and the most informative alternative test (SCI49 package B)

Non-canonical research material. Not medical advice; no dose, schedule, route or recommendation. Reference genotype class only. Labels DATO (read in a source), INFERENZA (own reasoning), IPOTESI.

Perimeter searched: PubMed and Europe PMC strings by compound name and by function (queries.tsv Q01-Q18), ChEMBL by four Kir2 targets and by 14 drug names (Q19-Q21), PubChem BioAssay records for the ML133 probe (Q22), the probe-report abstract (Q06). Not reached: the IUPHAR/BPS service (401, key and registration required), the Bookshelf probe-report page and three PMC pages (interstitials), none retried. Ten compounds examined, ten sources opened beyond the abstract-level (eight with Results read, two abstract-level, see phase_note.md).

## Role 1: a Kir2-versus-other-Kir blocker probe
* DATO: ML133 meets the probe rule at family level. IC50 1.9 uM at pH 7.4 (290 nM at pH 8.5; 10.0 uM at pH 6.5); Kir2.2/2.3/2.6 2.9/4.0/2.8 uM; Kir1.1 above 300, Kir4.1 76, Kir7.1 32.9 uM (21615117, Table 1).
* DATO: limits. Kir6.2/SUR1 7.7 uM in the same table; a PubChem deposit lists hERG Active about 5.0 uM (automated patch clamp, external pH 8.5), against Kir2.1 0.284 uM at pH 8.5. INFERENZA (own arithmetic): ratio about 17.6 at pH 8.5; the hERG value at pH 7.4 is not in the records read; the Kir2-to-Kir6.2 window at pH 7.4 is about 4-fold.
* Missing: isoform selectivity within Kir2.1-2.4 (no source; Kir2.4 never tested in anything retrieved), a K2P counter-screen, a concentration window validated in a cortical pyramidal neuron, and a cortical-slice use (the only native-neuron item is an abstract on dentate granule cells, 40789514). ML133 is described by its authors as limited to in vitro use (high clearance, protein binding).
* Next-generation VU6080824 (0.35 uM, pH 7.4) has no counter-screen in the main text read; VU573 prefers GIRK, Kir2.3 and Kir7.1 and is weak on Kir2.1; PA-6 is nanomolar with a cardiac-channel counter-screen but no other Kir (abstract only); VU0134992 is a Kir4.1 probe (>30-fold over Kir2.1/2.2/1.1 in Tl+ flux, abstract only).

## Role 2: an activator with documented direction
* DATO: flecainide increases Kir2.1 current in CHO cells (EC50 0.8 uM, +22 percent at -120 mV; EC50 0.4 uM, +53.9 percent at -50 mV), by lowering polyamine affinity through Cys311; not Kir2.2/2.3; no change of human atrial IK1 (20713726). Direction and mechanism are documented, but the gain is mainly at potentials positive to EK, the drug is an approved antiarrhythmic with actions I did not read, and its use is a conditional hypothesis that needs the premise on the direction of benefit.
* DATO: zacopride: Kir2.1 outward-current increase under hypoxia in CHO at 100 uM, not Kir2.2/2.3 (28542320); mechanism not documented, one laboratory. No role as an attribution reagent.
* No activator qualifies as a probe. Missing: an activator with a direct, structure-based mechanism acting on the inward current at rest, a counter-screen against other Kir/K2P/hERG/Nav, and a neuron test. Perimeter: as above; not a universal statement of absence.

## Most informative alternative test if no reagent qualifies (INFERENZA from the sources named)
1. Use ML133 as a family-level blocker but with its own control: its potency falls from 1.9 uM (pH 7.4) to ineffective at 3 uM at pH 6.5 in HEK cells (21615117). A pH-paired comparison is a within-reagent check, with the caveat that pH also acts on other channels (K2P pH sensitivity is carried elsewhere in the repository, k2p/ph SCI45 folders, not re-read here).
2. Ba2+ concentration-response in the P13-P17 slice (the repository's own share is a single 60 uM increment, SCI44/IT48); the use of Ba2+ concentration to separate Kir2 from K2P is a recollection, not verified in this package.
3. A genetic arm: overexpression of Kir2.1 in cortical pyramidal neurons is cited in 38411613 (Hsieh 2020, copied, not read).
4. Pair ML133 with a Kir4.1 probe (VU0134992) only to discriminate a glial contribution, not as a neuron-only reagent.
