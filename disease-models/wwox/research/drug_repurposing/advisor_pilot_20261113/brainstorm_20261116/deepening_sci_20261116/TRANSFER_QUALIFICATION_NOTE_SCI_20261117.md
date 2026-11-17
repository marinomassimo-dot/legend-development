# Transfer qualification of the readings under arm table v3: where it changes a cell and where it changes nothing (SCI, 2026-11-17; non-canonical; hypothesis level; mechanism only; no agent, no dose; not medical advice; reference genotype class only)

Written for: ADV (asked it), IT (arm table v4), the lever table by class, the sodium-class selectivity note, I21/RP-023, the 08:35Z MEETING. Table: `TRANSFER_QUALIFICATION_SCI_20261117.tsv` (61 rows, 19 columns). No prediction is registered here: this is a table of entitlements, my reading of files already held, not a measurement.

**Not answered elsewhere.** I searched the repository for the question before building it (the arm table has no origin column; IT's notes to v3 carry one line on bulk against per-neuron; the I21 parts 2 and 3 carry a mapping stop). Nothing states, per reading and arm, which held readout a reading may move.

## Rules used (so a row can be checked)
* **Row type** is exactly one of WWOX observation (a measurement in Wwox, source named), transfer (another gene, system or species), assumption (not checked against a source here), simulation (a model output; a hypothesis generator, not evidence).
* **Tier cap** is the lower of two things: the tier of the system (1 measured in Wwox in that system; 2 same system other gene, or other-system Wwox; 3 mechanism only) and the tier of the condition under which the effect was seen. Examples: the fly rescue is 2 by system and 3 by condition (the second hit, Abeta42, was present); [4d] is 2 by system (neocortex) and 3 because its genotype control failed; a single-nucleus transcript from the non-bursting hippocampus is 1 for hippocampal neurons and 2 for any arm in the bursting region.
* **Direction** is what the reading may do to the arm cell: may raise (adds support to its stated sign), may lower, or sign not entitled (it may name a setting or a limit, not a sign).
* **Three standing consequences.** (a) A bulk transcript is not a neuronal one (R07 against R08). (b) A reading from another gene may lower the specificity of a Wwox reading; it never raises a lever arm (R09, R10, R12 to R15). (c) A simulation fitted on a held number cannot confirm an arm that rests on that number (R02 and R17), and every S-HT statement is tier 3 until the authors' per-cell S-HT values exist (R05b).

## Where the qualification CHANGES a cell (4 rows, 4 cells; revised after ADV's reading: the I8 row moved to the next list)
| Cell (v3) | Change | Reason (row) |
|---|---|---|
| Sodium-channel blocker (non-selective) / I11b, 'may aggravate' | **sign becomes conditional**: aggravation only if the agent's interneuron effect exceeds its pyramidal effect by about 2.5 in log terms; at equal block the model gives 0 or suppression (within s <= 3) | R17b; the ratio is the unmeasured variable, the KO's own 2.6 is a lesion property (R04) |
| NKCC1-directed or GluN2B-directed route / I17, '+ (neonatal)' | **sign not entitled for Wwox**: neuronal NKCC1 falls (-0.40), KCC2 flat (+0.01), Grin2b -0.12; no transcript shows an excess of either target (the strongest sentence the readings allow; ages unmatched; a transcript is not function) | R08 (P17 mouse against children up to 28 days: ages not matched) |
| Substrate (glucose down, ketone added) / I1 and I4, 'interval changes' | **value3**: if the arm maps onto the resource class, the model moves duration first (x2.5) and the interval little (-17%); the mapping is ASSUMED | R17c |

## Where it adds a cap or a condition and changes no value (33 rows)
The sign stays, the support is re-labelled. The largest groups: (0) **Sodium-channel / I8** (moved here at ADV's reading): the cell's idea concerns Nav1.1 protein; the only transcript read (inhibitory nuclei +0.18 [-0.02,+0.39], n = 1 per arm, pseudo-replicated) gives no per-neuron support for 'graded by Nav1.1 density', protein-level grading is untested, and the available grading variables are the AP-amplitude deficit and the ratio r. (1) **bulk-only transcript support** for the sustainer route of NMDAR/I3 (bulk -1.81, neuronal -0.12, P47T -0.10 and -0.16), for the K2P/Kv7 leak identity (no per-neuron fall; the fall is astrocytic), and for the S-HT sensitivity of the GABA-A arm (R05b not held). (2) **Tonic-selective and ambient-GABA cells (I13)**: the per-neuron Gabrd fall is present in the S-line hippocampus and a second Wwox line shows the direction in bulk, but an epileptic neocortex of another gene falls by -0.66 and seizure references by -0.35: the fall is not specific in direction, so 'where synaptic-selective has little' is not entitled; only the size (2 to 4 times larger) could be Wwox-specific, at n = 1 per arm. (3) **Transfers**: Miao (PV activation, T-type blockade), Lucas-Clarke and the MEF screen add no Wwox readout; the fly Ldh rescue and the glycolytic shift of the MEF background are one origin chain, counted once. (4) **I1 cells fitted on R02**: the model's interval/duration signs for the NMDAR and T-type arms cannot be confirmed by the observation they were fitted on; the paired slice drug test is the confirmation. (5) **K2P/Kv7 leak opener**: an opener acts on the held depolarisation (tier 1); 'leak loss' as its cause stays tier 3.

## Where it changes NOTHING (the informative list, 24 rows; 12 cells are touched by no other kind of row)
* **Tonic-selective / I13 against the sIPSC deficit (R05a):** the held phasic number does not touch a tonic arm. Wrong readout, no move.
* **Aggregated sIPSC against the pre/post tie (LIVE1-H1 and H7):** the -52% cannot separate them; they stay tied until the fractional-block experiment. Both rows read 'none'.
* **K2P/Kv7 opener / I8 (0):** the value rests on HE's absence of PPxY/LPxY motifs; no transcript or slice reading touches it.
* **Persistent-sodium-preferring / I11b, Sodium-channel / I10, Raised ambient GABA / I1-I10 (worsening), Any class by severity / I19, T-type blockade / I1 (Miao), Threshold titration / I15, ENT1 / I4, GABA-AT / I2, T-type-valproate / I2, CCK brake (H6), scaffold (H1):** no held reading is entitled to move them; each stays at its own tier, and the I2 cells stay at their counts (n = 0 in the rebound group).
* **The Miao transfers do not enter any I1 slice cell**: their endpoint is in vivo seizures, not slice interval or duration.

## Limits
* The per-group n of the Breton numbers, the ages of the Breton slices and the recorded cell class of the sIPSC are not carried in my files; the table says so in the rows and does not guess. The hippocampal control count I recorded in [4b] may be the neocortical control count (unchecked).
* R19 (GAD65/67 protein lower) is second-hand through HE's live run; cap 2 until the source is read.
* Sources of the transfers (Miao, Lucas-Clarke, Hsieh, Su) are read through the arm table's own summaries, not re-read by me today.
* Whether the model's S-HT sensitivity is real is the model's open question (it missed twice there).
* The 'changes' list is my reading; IT owns the arm table and decides what v4 says. 4 of 61 rows change a cell (2 sign, 2 value3: the substrate cell appears for I1 and I4); 33 re-label; 24 change nothing.

## Revision 2 (IT's arm table v5 finding, 2026-11-17; ADV relayed it)
* **Two arm keys matched no v4 string**: both were my split of one v4 row, `T-type blockade / Cacna1g deletion (transfer)` with idea `I1/I10`. Corrected: both rows now carry exactly `T-type blockade / Cacna1g deletion (transfer)|I1/I10`; the wording column says 'I1 part' or 'I10 part'. All 66 arm keys of the TSV now match a v4 `arm|idea` string (checked against `ideas_arm_table_v4_20261117.tsv`).
* **Six cells carried a sign with no origin row; one row added for each (five rows; the sixth is the key fix above).**
  * `T-type blocker|I10` ('burden -'): origin R13 (Miao T-type blockade, transfer, tier 3); no held Wwox in vivo reading. Carry 'transfer only'.
  * `NMDAR pore blocker|I4` ('duration -'): origin R17c (model: NMDAR-active agent duration -54%), tier 3; it is the I1 sign carried to I4, no I4-specific reading.
  * `GABA-A PAM|I9` ('rate -, if mature'): the sign has origin R17a (simulation, tier 3); the qualifier 'only after maturation' has **no held reading** (assumption).
  * `GABA-A PAM|I10` ('burden + or 0, in vivo'): **no held reading: the sign is an assumption**; carry '.' or 'assumed' (row A01).
  * `Remyelination mechanism|I5` ('rate -'): origin R08c (composition: oligodendrocyte-lineage share 22.5% to 7.8% in the S-line pool, n = 1 per arm, hippocampus) supports the **premise** at tier 2; the sign has no held reading (assumption).
  * `T-type blockade / Cacna1g deletion (transfer)|I1/I10`: origin R13, tier 3 (two rows, one for each part).
* **New totals:** 66 rows (43 WWOX observations, 10 transfers, 10 simulations, 3 assumptions); tiers 5 / 14 / 47; effects 4 change a cell, 38 re-label, 24 change nothing; 36 distinct cells (of the 75 in v4) have at least one row. The value-of-information counts of the ranking were made on the 32-cell version and are unchanged by these additions (none of the new rows adds a measurement).
