# HCN / Ih in the neuron-deleted Wwox cortex: what the sag, rebound and resting-potential data can and cannot mean (package C, label hc-p, 2026-11-08)

Non-canonical, not medical advice, no dose. Reference genotype class only. The external report was not used (not in the repository). Tables beside this file: `evidence.tsv` (41 rows), `physiology.tsv`, `hypotheses.tsv`, `probes.tsv`, `experiment.tsv`, `queries.tsv`; staged receipts (suffix 94, not recorded) in `receipts/INDEX.tsv`.

## Answer first

No HCN defect is shown in any WWOX preparation. What exists is one current-clamp table (layer II/III pyramidal neurons, P13-17). Read with its own input resistance, it fits a more resistive, more depolarised cell that is driven further by the same current step, and does not need extra HCN. Three hypotheses, one first experiment: sag and rebound at matched starting potential and matched peak excursion, then Ih in voltage clamp (`experiment.tsv` X1-X2).

## DATO

- Table 1 (neuron-deleted model, PMID 34634460, reused): Rin 102.9 / 143.3 / 143.0 Mohm and rest -79.3 / -75.5 / -73.6 mV (WT / HT / KO); sag at -200 pA 1.18 / 2.04 / 2.57; rebound 0.96 / 1.24 / 1.86 (KO only significant). Asterisks are against WT; HT v KO is untested; cells are the unit (`physiology.tsv`).
- Sag is "the most negative membrane deflection" minus its return to steady state; Rin is an I-V slope. No Ih was recorded. The authors' "elevated hyperpolarization-activated current" rests on the larger deflection (E01-E10).
- Other systems: TTX deprivation raised sag and rebound in mouse hippocampal cultures without a change in total HCN mRNA or HCN1 protein; ZD7288 removed sag and rebound, nickel removed only the T-type bump (PMID 33547341, E29-E38). Uncoupling HCN1 from filamin A raised Ih and sag ratio with Rin and rest unchanged (PMID 24403084, E23-E27). Cholesterol extraction raised native HCN opening in rat DRG nociceptors, little effect on the HCN1 voltage sensor (PMID 39548079, E15-E20). ZD7288 blocked sodium current in DRG neurons at lower concentration than HCN current (PMID 22989944, E39-E41).

## INFERENZA

1. Same -200 pA, Rin +40 percent: deflection about 20.6 vs 28.7 mV; peak potential about -101 (WT) vs -106 (HT) and -105 (KO). The genotypes were not compared at the same potential, so absolute sag and rebound rise even if HCN is unchanged. Sag as a fraction of the peak still rises (5.4 to 8.2 percent), so recruitment alone is not shown to be the whole story (Y05-Y07, crude, group means).
2. Rin up with a depolarised rest is the sign of fewer open K+ or leak channels (or a smaller cell: tau flat, implied capacitance lower); open HCN lowers Rin. Kv7, other K+ and leak conductances are different things and none is identified here. The Kv7 lead is neither strengthened nor weakened by a new measurement; what changes is that the same table now has a passive reading that needs no HCN.
3. Lipids (PMID 39548079; its bioRxiv record, PMID 37732182, is the same study, not a second confirmation), filamin/TRIP8b-type scaffolding and homeostatic redistribution are nested ways to change one thing (Ih gating or position). They are not three confirmations, and none has a WWOX link.
4. Deprivation (TTX) is the opposite of hyperexcitability; direction of adaptation in WWOX is unknown, so the 33547341 result is a method precedent (sag moved without a total-protein change), not a prediction.

## IPOTESI (`hypotheses.tsv`)

- HY1 recruitment plus a K+/leak change as the primary difference; test X1-X3. Weakened if KO keeps a larger sag or Ih at matched conditions.
- HY2 Ih/T-type shape the cell response that starts bursts; benefit, harm or neither is open. Test X4-X5, ZD7288 plus a second blocker, nickel/Z944 and Kv7 arms separate, engagement shown first. Sag removed with bursts unchanged supports HCN in sag, not benefit; worsening is not compensation until off-target and compartment are examined.
- HY3 only if X2 finds a different Ih: surface, isoform and compartment read-outs (X6) before any trafficking or lipid line. No supplementation proposal.

## NON RISOLTO

Whether Ih differs at all; the K+/leak identity; whether rebound is Ih, T-type or both; harmful, compensatory or mixed role; any compartment difference between pyramidal and PV cells (not deduced from opposite trajectories, measure it).

## Not found / not reachable

WWOX with HCN, filamin, TRIP8b or membrane-lipid domains in neural cells: 0, 1 (a body-metabolism review), 0 and 6 (unrelated) on PubMed, then Europe PMC co-mention lists screened by title for 12 hits each (`queries.tsv` Q01-Q09). Bounded, not a proof of absence. Publisher XML withheld for PMID 24403084 and 22989944: the PMC page text was read instead, figures never viewed (Q12). Methods and Supplement of 39548079 and 33547341 were not read; the ZD7288-T-current statement of 33547341 sits in a Supplementary figure.

## Notes for the integrator

- New sources 4 of 5 (Stage 1: 39548079, 24403084, 33547341; Stage 2: 22989944 for the ZD7288 gap named in writing; the lipid bridge gap opened no source because no candidate was found). 34634460 reread in part for Table 1 and Methods; another producer (pv-p) holds a claim on it.
- No reopening needed unless a WWOX measurement of Ih, surface HCN or membrane order appears.
