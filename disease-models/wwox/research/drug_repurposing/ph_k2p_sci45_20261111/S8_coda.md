# SCI45 coda (2026-11-11): what the package changes, a different lever, a revival check, the next brief

Non-canonical research material. Not medical advice; no dose or clinical preference; nothing promoted. Labels DATO / INFERENZA / IPOTESI.

## 1. Queue items done and why

1. **Pointer qualification (S8 item 1)**: `../k2p_pointers_sci45_20261111/` (ONO-TR-772 and four more primary reads, verified).
2. **Decisive open premise (item 2)**: the TREK-1 slope was not obtainable (no stated slope; no 30-37 C source), but the verifier's new source gave the residual current (Imin 0.25), which changed the size check (`size_check_imin.tsv`). Corrected in the package.
3. **Not done, with reason**: Harness anomalies (item 3: none pointed at a number that changes this decision); a public-data reanalysis (item 4: the local GEO raw tables used by SCI44 are no longer on this disk, and the one new fact needed, Kcnk3 class means, already sits in `kchan_expression_mouse.tsv`; the 15 predictions were not rerun).

## 2. A lever different from the first mechanism (DREAM, item 5)

The first mechanism asked whether a lower pH closes a K2P pool and raises Rin. The sources read say something larger about **sign**: an interstitial pH fall acts on at least three targets with opposite effects on excitability.
* K2P (TREK-1, TASK-1): closure, depolarising and more resistive (verified, recombinant; this package).
* NMDA receptors: proton inhibition of GluN1/GluN2 receptors (background knowledge; not read in this package; the SCI42 comparison already uses the pH-dependence of NP10679, 21 nM at pH 6.9 vs 130 nM at 7.6, abstract level).
* Other proton-gated or proton-sensitive conductances (ASIC1a and KATP; background only).
Hence **a lower pH in the knock-out slice would not be simply pro-excitatory**: it could be a partially protective state against NMDAR-dependent bursts while depolarising the cell through K2P. Consequence for the design and for the pharmacology: (i) the pHo-step arm should read burst incidence and the NMDAR-dependent component as well as Rin and rest, in the same slices (IPOTESI); (ii) a pH-dependent GluN2B negative modulator (NP10679, comparator of SCI42) is the tool whose effect would *grow* with an acidic microenvironment; its role in the comparison is a pH-state discriminator, not a lever; (iii) the wrong-sign risk stays: raising pH or buffering acid to "restore" K2P could unmask NMDAR gain. Class: relation known in the literature, combination new in the repository (K2P, NMDAR and tool pH dependence in one condition record); novelty against the literature not assessed.

## 3. Revival triggers

`dismissal_ledger_current.md` triggers on K2P, pH or lactate in a WWOX-deficient system: none fired (no WWOX-deficient neural measurement was added; all new evidence is non-WWOX).

## 4. Next brief

`next_brief_sci45_20261111.md`: the proton sensitivity of NMDA receptors and ASIC1a in juvenile cortical pyramidal neurons, to turn the sign statement above into numbers.
