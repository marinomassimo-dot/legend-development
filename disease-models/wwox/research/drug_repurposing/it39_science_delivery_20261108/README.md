# Membrane physiology and AMPA/NMDA discrimination — delivery, 2026-11-08

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference. Reference genotype class only. Two packages, each with a producer, an independent blind verifier, a recheck of the corrections and a final correction round: `membrane_hypotheses_20261108/` (A) and `ampa_nmda_discrim_20261108/` (B), task record `ledger/tasks/orchestrator/ORCH-IT39OS-20261108.json`.

## What decision this changes

* A drug arm in the burst slice preparation is not yet a well-posed question. Before any compound, three measurements decide whether the question exists: (1) whether the burst survives a verified AMPA block with recording Mg2+ and K+ measured; (2) whether the NMDAR-dependent component is total NMDAR gain (matched-current d-APV curve) or GluN2B-weighted; (3) whether a blocker-sensitive current (Ba2+-, XE991- or ZD7288-sensitive) differs between genotypes at matched potential, matched deflection and reported capacitance. Until then no HCN, Kv7, AMPA-antagonist or GluN2B-NAM compound is nominated (abstention in both packages), and the carbenoxolone burst fall must not be read as a gap-junction result.
* Nothing changes a rank, a card verdict or a work order.

## Status of the deliverables (nothing is applied to a consumer)

| Layer | A membrane | B AMPA/NMDA |
|---|---|---|
| Sources newly read and receipted | 9 (cap 8; two abstract-only extras, stated) | 8 (cap 8) |
| Of which partial full text / abstract only | 4 / 5 | 7 / 1 |
| Staged receipts (suffix -51/-52 and -61/-62) | 11 | 10 |
| Figures viewed | 34018186 all five; 24953239 Figs 1–6; 34634460 Fig 6 and Supp S2, S4 | 34634460 Figs 1–6 and Supp S1–S4; perampanel Figs 1, 5; brilliant blue FCF Figs 2, 6; Madry Fig 1 |
| Verifier verdicts on numbers/claims (first pass) | 33 supported, 8 partly, 2 not supported, 2 unverifiable; probes 4 supported, 5 partly | all headline WWOX numbers correct; probes 4 supported, 2 partly, 5 mechanisms unverifiable (no primary source read by anyone); matrix 8 supported, 7 partly; hypotheses all partly |
| Hypotheses delivered | 3 (MH1, MH2 conditional, MH3 design control) + abstention on compounds | 3 (BH1–BH3, all partly supported; BH3 near withdrawal of a gap-junction attribution) + abstention on compounds |
| Verification of corrections | recheck by the same verifier, then 7 small fixes | recheck by the same verifier, then 5 small fixes |
| Proposals in `consumer_delta.md` | 7 | 12 |
| Applied to consumers | 0 | 0 |

The 21 staged receipts (15 partial full text, 6 abstract only; none a complete read: reference lists were not read) are in `disease-models/wwox/research/receipt_staging/it39a/` and `it39b/`; all pass `staged_receipt_check.py --check-doi`. Record each `-62` after its `-61` prior, or the `-62` alone. Verifier reads (many at full text) are not receipted.

## Chains (observation → relation → action → context → expected benefit; evidence vs inference)

All hypotheses are IPOTESI; step labels DATO/INFERENZA are in `hypotheses.tsv` of each package.

* **MH1 passive size plus a conductance-level change.** DATO Table 1 (layer II/III pyramidal, P13–P17, neuron-specific deletion): Rin 102.88/143.26/143.03 MΩ, tau 18.55/18.79/21.25 ms, rest −79.25/−75.51/−73.62 mV. INFERENZA: flat tau against Rin +39 percent argues against a pure leak loss at constant capacitance (single-compartment assumption); implied capacitance has about 14 percent uncertainty, so "smaller cells" is a direction of means. Action: matched-potential, matched-deflection comparison with capacitance, seal and access resistance by genotype, then a K-leak difference current in voltage clamp (E_K about −97/−98 mV; the sag peaks lie 16–21 mV below it on the junction-corrected scale). Alternatives kept: smaller cells with a fixed seal leak (A10), selection by Rin/tau criteria, HCN.
* **MH2 an HCN contribution remaining after matching (tool arm only).** Transfer DATO: ivabradine reduces cortical L5/6 sag from about 2.65 to 1.4 mV (rat, 25–35 days) and cortical injection cut absence-seizure time more than thalamic; GAERS Ih rose with lower Rin and unchanged rest and sag (transfer breaker). WWOX premise (a residual sag excess at matched conditions) is not established. Action: Ih in voltage clamp with two blocker chemotypes, then bursts. No increased current is assumed harmful; a blocker response does not prove an HCN defect.
* **MH3 recording, selection and network state.** Bursting in 36/42 KO, 4/23 HT, 0/11 WT slices; the Methods drug list has no AMPA or GABA-A blocker, so intrinsic recordings were probably unblocked (INFERENZA). Action: record with and without blockade and with morphology-based identity; age and layer series.
* **BH1 AMPA dependence.** DATO d-APV 50 µM abolishes the spontaneous bursts; the paper applies no AMPA antagonist; INFERENZA the KO mEPSC (larger at −70 mV, decay about 5 ms) fits an AMPA-type quantum. Action: AMPA antagonist first, d-APV only if bursts persist, plus a matched-effect arm. Abolition alone would not separate AMPA drive from NMDAR-regenerative drive (loss of Mg2+ relief); only persistence under a verified block is informative. Tool: perampanel is the only AMPA compound whose mechanism was read (noncompetitive AMPA/kainate, culture, slow kinetics); NBQX and GYKI 52466 are use-only, mechanism not read.
* **BH2 NMDAR composition at matched current.** DATO the d-APV effect on the evoked delayed response is about 20 percent residual against the wild-type floor (not 40; point estimate, 7–33 percent range). Action: isolated NMDAR EPSC in burst slices, d-APV titration, a GluN2B NAM at matched percent removed, TCN-201 at two measured co-agonist levels with a glycine control, graded Mg2+ and K+. Tools: radiprodil GluN2B-selective in oocytes with 45 percent maximum on triheteromers and very slow washout (activity dependence untested); TCN-201 recombinant only, potency set by glycine.
* **BH3 carbenoxolone attribution.** DATO the burst fall (direction, no recovery) is the only usable carbenoxolone number; in culture 100 µM reduced AMPA EPSC to 63 percent, NMDA EPSC to 69 percent and IPSC to about 50 percent (reversible), broadened spikes and lowered input resistance. Direct NMDAR channel block is neither shown nor excluded; Madry's CA1 result is low-powered and a different readout. Action: carbenoxolone with EPSCs, spike width, input resistance and a coupling readout, a matched-effect control, and brilliant blue FCF with Panx1 engagement. No datum in the sources read separates the gap-junction half from the off-target explanations.

## What LEGEND held but did not use, and where it should be consumed

A (8 rows, `held_not_used.tsv`): flat tau/implied capacitance (`hcn_20261107` Y03, held as a hint only); NEED-INTRINSIC-EXCITABILITY O1 (Rin saturates at one allele while rest and sag grade with dose); the estimated peak potentials Y05–Y07 never set against E_K; HT with few bursts; the T-type package; the withdrawn Wang 2016 sentence; the Methods drug list; the T-type window-current caveat on ZD7288-subtracted Ih. Consumers: NEED-INTRINSIC-EXCITABILITY and INV-18.
B (9 rows): `needs.json` NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR observations O3, O4, O7, O8; INV-05 in `ranking_it8_p9_20261029/investigations.tsv`; cards F04, F01, P11; `nmda_inv05_20261107` steps X0–X6; HYP-20261027-01; the IT38 tables D06 and D15; the HCN package (pointer arm M18).

## Format limits (precise; for the Orchestrator that integrates)

* `bridges.tsv` cannot hold a conductance-level or composition hypothesis (two HGNC genes required, no sign column); none was written, and no gene–gene link was invented. No `probe_links.tsv` row was justified.
* `needs.json` `observed` (`statement`, `limits`) has no field for recording conditions (matched potential/deflection, capacitance, access resistance, measured versus nominal bath, blockers present) or for text/legend/table/figure disagreement; they go in free-text `limits`. `intervention_direction` is one direction on one entity, so a matched-effect comparison cannot be expressed.
* `investigations_it20.tsv` / `investigations.tsv` `next_test` is one string; it cannot hold ordered application and washout, several experiments with separate decision rules, or matched-effect arms.
* `prediction_matrix.tsv` (B) has no consumer in the generator or the view.

## New measurements required (other literature is not a substitute)

Recording Mg2+, K+ and temperature as measured values with the blockers actually present; whether the burst survives a verified AMPA block; AMPAR/NMDAR ratio and AMPA EPSC kinetics; isolated NMDAR EPSC and matched-current curves with the NAM-sensitive fraction; slice co-agonist level before any TCN-201 arm; a receptor-agnostic release-reducing control on at least two metrics; carbenoxolone's effect on EPSCs, spike width, input resistance and coupling in these slices; Panx1 engagement for brilliant blue FCF; slice equilibration time and the temperature mismatch with the source preparations; TTX/action-potential dependence and heterozygote drug sensitivity; a floor control for the delayed-response metric; a GABA-A arm with an evoked IPSC; capacitance, seal and access resistance by genotype; a Wwox Ba2+-, XE991- or ZD7288-sensitive current. Reads still wanted (open needs, none opened): the neuronal Kv7-opener recording papers' Methods, the Wang 2016 full text, primary mechanism papers for NBQX/GYKI 52466/ifenprodil/Ro 25-6981, the Chepkova carbenoxolone/NMDAR paper.

## Corrections this work makes to the IT38 qualified state (for the integrator)

* IT38 stated the evoked delayed response falls to about 0.4 of baseline under d-APV; against the wild-type floor the residual is about 20 percent (INFERENZA), so it is not evidence of incomplete block.
* Ivabradine "removes sag" becomes "reduces" with sizes; the Fig 2 oral dose-response bars disagree with the text (percentages not quotable); the "thalamocortical, not neocortical" contrast is partly reversed at the injection site.
* The paper's own numbers disagree (baseline 2.29 against 0.84 per minute for the same 119 bursts; carbenoxolone n 36/4 against 13/6; brilliant blue FCF n 73 against 25; Supp S1 126, 102+41 against 119; Fig 4 S-CTL 18 against 31): no comparison rests on a disputed number.
* The perampanel text-versus-figure potency conflict is withdrawn as a probable axis misread (INFERENZA).

## Not reached

Figures 1–5 of 34634460 for Package A (read in Package B); 34018186 supplement; full texts of 22989944, 11466425, 31063701, 15297615 (behind a bot check; not retried); the 40994429 supplement; figures of Tovar, Hansen and Banke (captions only); the reference lists of the main sources.
