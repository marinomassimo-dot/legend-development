# Answers (SCI49 package B, producer kz-z, 2026-11-12)

Non-canonical research material. Not medical advice; no dose, schedule or recommendation. Labels DATO / INFERENZA / IPOTESI.

**The question.** Are there compounds with documented pharmacology that make a Kir2 lever testable in the P13-P17 L2/3 Wwox pyramidal neuron, with the Ba2+-sensitive resting conductance as the observation?

* DATO (blocker probe): yes at family level, with limits. ML133 blocks Kir2.1/2.2/2.3/2.6 at 1.9/2.9/4.0/2.8 uM (pH 7.4), spares Kir1.1, 4.1, 7.1 (21615117). Limits: Kir6.2 7.7 uM; hERG Active about 5 uM in a PubChem deposit at pH 8.5; no isoform selectivity; no K2P test; no cortical neuron test read.
* DATO (activator): no probe. Flecainide has a documented direction and mechanism in CHO cells (Kir2.1 only, Cys311; 20713726); zacopride is thinly documented. Both would be conditional on the direction-of-benefit premise, which is not assumed.
* INFERENZA: a mechanism can be measured now (ML133 with a pH control, Ba2+ concentration-response, a Kir4.1 comparator); no treatment is proposed.
* Juvenile share: none found at P13-P17 in the strings listed (not an absence claim); nearest are P21 L5 mPFC (WNK3 KO paper, 200 uM Ba2+, room temperature) and P26-P51 L2/3 mPFC (mTOR paper, concentration not read).
* Hypotheses: three (H1 attribution with ML133 and pH control; H2 conditional activator; H3 indirect Kir4.1 contribution).

**Priors K1-K7.**
* K1 held, refined: ML133 IC50 1.8-1.9 uM at pH 7.4 (290 nM pH 8.5), little Kir2 discrimination, spares Kir1.1/4.1/7.1; added Kir6.2 7.7 uM and a hERG deposit row (C01, C02).
* K2 partly: no Kir2-selective activator probe, but flecainide has a documented direct mechanism (polyamine affinity, Cys311), restricted to Kir2.1; zacopride mechanism undocumented (C10, C11).
* K3 partly: chloroquine 8.7 uM held (C09); PA-6 is nanomolar but not an approved drug; quinacrine, tamoxifen, carvedilol, pentamidine itself, dronedarone were not examined at primary level.
* K4 held within the perimeter: no source tests a Kir2 modulator in L2/3 pyramidal neurons at P13-P17 or in a Wwox slice; the one native-neuron ML133 item is a dentate granule cell abstract.
* K5 held: the name route and the literature give ten compounds, while ChEMBL by name gave zero activity rows on the four Kir2 targets and its Kir2.1 rows are mostly counter-screen negatives of other programmes (the SCI43 negative was an artefact of the by-symbol route, with the added fact that ChEMBL is itself thin).
* K6 failed within the perimeter: no juvenile P13-P17 source found at all (B01).
* K7 partly: recombinant separation exists (VU0134992 versus Kir2; ML133 weak on Kir4.1), the slice statement is INFERENZA not tested.

**Generative contribution (separate from corrections).** A reader can now write a concrete first Kir2 test (ML133 at pH 7.4 versus pH 6.5 with Ba2+, OQ1), name the window problem (Kir6.2, hERG) before measuring, and see that no activator is usable as a probe. The corrections are separate: ChEMBL by symbol undercounted tools; the PubChem hERG row corrects a clean-hERG reading of ML133.

## Correction round (2026-11-12, after the blind verifier V12; earlier text above kept)
V12: 60 rows, 34 correct, 20 defective, 5 unverifiable. Cell edits are in CORRECTIONS.tsv.
* **Blocker probe (corrected):** ML133 is a probe at family level only. Kir2.1-2.3/2.6 IC50 1.9-4.0 uM at pH 7.4; Kir6.2/SUR1 7.7 uM and hERG (about 5 uM, deposit, final pH unstated) lie within a few-fold; like-for-like on the automated platform hERG is about 2.7-fold more potent than Kir2.1 (13.63 uM). The earlier 17.6-fold "window" is withdrawn. No K2P data; no isoform selectivity; no cortical-neuron test. The pH control is withdrawn as not clean.
* **Activator (corrected):** documented direct-mechanism Kir2.1 activators exist (flecainide, propafenone EC50 12 nM, timolol; Cys311), all restricted to homotetrameric Kir2.1 (heteromers with Kir2.2 or Kir2.3 not increased) and untested in neurons; zacopride, tetramisole and sildenafil remain claims without a direct mechanism.
* **K1-K7 re-scored:** K1 held (plus Kir6.2 and hERG deposit). K2 failed in part (direct-mechanism activators exist beyond flecainide). K3 held with a nuance (dronedarone is Kir2.1-over-2.2/2.3 in oocytes but multi-channel; PA-6 nM but experimental). K4 held within both perimeters. K5 held. K6 not supported within both perimeters (neither reader found a P13-P17 source). K7 held (recombinant separation exists; slice not tested; VU0134992 equal on Kir3 and Kir4.2).
* **Hypotheses:** H1 kept and revised; H2 dropped; H3 reduced to a design note.
* **Generative contribution after the review:** a reader can now run a first Kir2 test only with a slice positive control and a K2P/TASK arm (the pH 6.5 arm no longer serves), knows ML133's competing targets are within a few-fold, and has a short list of Cys311 activators that would act only if cortical Kir2 is homotetrameric Kir2.1 (OQ9). Corrections (hERG window, activator count) are separate from this.

<!-- v12-recheck -->

## Recheck correction (2026-11-12, Orchestrator)
V12 recheck count: 87 verdict lines (60 first-pass rows including one source_silent, 27 item-R rows). The activator sentence is corrected: flecainide, propafenone (EC50 12 nM, abstract level) and timolol raise Kir2.1 current through Cys311 in recombinant cells and spare Kir2.2/2.3 homomers; **only flecainide was tested on Kir2.1+2.2 and Kir2.1+2.3 heteromers (not increased)** and on native guinea-pig ventricular IK1 (+19.5 percent); none is tested in neurons; flecainide and propafenone are also Na+ channel blockers; zacopride, tetramisole (rat myocytes) and sildenafil (Kir2.2 at 10 uM, mixed effect) are claims without a direct mechanism. H1 in its final form is in `hypotheses.md`; OQ1 and OQ5 are rewritten accordingly.
