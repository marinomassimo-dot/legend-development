# U1 and the idea-by-arm prediction table (ADV; HYPOTHESIS; not medical advice)
Answer first: the ideas of the round fit one picture, 'REBOUND IGNITION UNDER A FAILED NEOCORTICAL BRAKE', and they disagree on a small number of arms. The pilot should be read as a table in which each arm discriminates between ideas, not as a screen of drugs.
U1. (i) Null neocortical neurons are rebound-prone (T13, I10). (ii) Inhibition arrives late or weak: PV timing (I5), PV immaturity (I9), reduced sIPSC rate (HELD). (iii) An NMDAR-dependent sustainer sets burst duration, with a GluN2B-high early window (I7, WO-11). (iv) Slow variables set the interval: chloride loading (I6), energy and adenosine tone (I4). (v) The hippocampus is spared by a compensation (NPY and others, I3) that the neocortex lacks. (vi) Phenotype and age decide which stage dominates, so pharmacology is phenotype-conditional (I2). (vii) Channel surface levels may be shifted by loss of a PY-motif scaffold (I8).
Predictions by arm (+ raises, - lowers; ? undecided; the owners fill their column in their dossier and may change a sign with a reason):
| Arm | I1 oscillator | I5 PV timing | I9 PV maturation | I3 compensation | I4 metabolic | I10 state |
| T-type blocker | interval + | no change | no change | no change | no change | burden - |
| NMDAR pore blocker | duration - | duration - | duration - | duration - | duration - | burden - |
| GABA-A PAM | rate + (rebound) | rate - | rate - (if mature) | rate - | no change | burden + |
| Sodium-channel blocker | ? | ? | ? | ? | no change | burden + (absence-like) |
| Y2/NPY antagonist | no change | no change | no change | hippocampus unmasked | no change | no change |
| Substrate (glucose lowered, ketone added) | interval changes | no change | no change | no change | interval changes | no change |
| Remyelination mechanism (developmental) | no change | rate - | rate - | no change | no change | no change |
The row that decides between two whole pictures is the GABA-A PAM: rebound (I1, I10) says it ADDS bursts, restoration of inhibition (I5, I9, I3) says it removes them. It is already an arm of the brief.
Next steps: IT keeps the table in ideas_portfolio and adds the columns of I2, I7, I11; SCI and HE add their ideas' columns; the table is frozen by hash before the pilot's results exist.

## Update v2 (ADV, 2026-11-16 18:45Z, after SCI 57406618 and HE 7317ff0e0 / bc6ef3779)
Columns added from the owners' dossiers (ADV reading, each owner confirms or changes a sign with a reason; `?` = the dossier gives no direction; a model-derived sign is MODEL, not evidence):
| Arm | I13 tonic (SCI) | I8 PPxY surface (HE) | I6 chloride (SCI, v3) | K+ leak reading (SCI intrinsic model) |
| T-type blocker | no change | no change | no change | no change |
| NMDAR pore blocker | duration - | duration - | duration - | duration - |
| GABA-A PAM, tonic-preferring (neurosteroid-type label) | rate - (MODEL: tonic weight +20%, rate -77%) | no change | rate - or +, set by E_GABA minus burst-time potential | no change |
| GABA-A PAM, synaptic-preferring (benzodiazepine-type) | about half the tonic effect (MODEL: J_I +20%, rate -37%) | no change | same sign problem | no change |
| GAT-1 blocker (label) | tonic current barely moves in the null, moves in wild type (the surprising prediction); bursts ? | no change | ? | no change |
| Sodium-channel blocker | no change | graded by Nav1.1 density: aggravation route under the shield sign, weakened under the adaptor sign (AH1) | no change | no change |
| Kv7 or K2P opener (leak-type, label) | no change | no change (HE I8 v3: none of the 16 K2P, Kir and Kv7 genes carries a PPxY or LPxY: the scan could have failed and did; parked with a trigger) | no change | rate - (restores a resting conductance) |
| HCN blocker (label) | no change | sag and rebound - if the adaptor sign holds at HCN1 | no change | no change |
The arm that now separates the most rivals is still the GABA-A PAM, split in two by I13 (tonic-preferring against synaptic-preferring); the second is a leak-type opener, which only the K+ leak reading predicts to lower the rate.

**Held-data discriminator that costs nothing: the heterozygote incidence.** Breton 2021: bursts in 0 of 11 (S-WT), 4 of 23 (S-HT) and 36 of 42 (S-KO) neocortical slices; the intrinsic features are a step (S-HT equals S-KO), rebound and mEPSC amplitude are not. Any picture in U1 that makes the intrinsic profile alone sufficient predicts an S-HT incidence near the null's and is contradicted. Read in `CROSS_READING_1_ADV.md`.

**Freeze of this table:** after the owners confirm their columns (due 20:00Z with the v2 dossiers) I hash it and push the digest before any pilot result exists; the table is a statement of what each idea predicts for each arm, and a table that changes after a result is a new table with a new digest.

**HE's I4 column (confirmed by HE 18:40Z):** substrate arm (glucose lowered, ketone added): burst rate changes in null and not in wild type (a genotype-by-substrate interaction, the rejecting observation); GABA-A PAM, T-type and NMDAR rows: no change from I4; valproate-type (HDAC-inhibitor reading): moves the glycolysis and lactate module in the loss direction (post hoc, descriptive), seizure sign unknown; adenosine A1 antagonist step (A, tone times reserve) and agonist step (G, reserve) per the two-step addendum, powered on holding current. I8 v3 outcome: PPxY is a route to a Nav-density component and to the interneuron spike amplitude, weakly to a deflection component, not to the resting conductance that dominates the profile.
