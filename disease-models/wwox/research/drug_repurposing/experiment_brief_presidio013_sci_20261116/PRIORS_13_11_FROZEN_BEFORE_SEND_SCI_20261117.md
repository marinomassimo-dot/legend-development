# Priors for brief section 13.11 (pore-blocker arm beside d-APV in the Breton S-KO slice), frozen before the page is sent anywhere (SCI, 2026-11-17)

Non-canonical. Hypothesis level (IPOTESI): labels, not measurements. Class label only: "a use-dependent pore blocker"; no agent is named as a use, no dose is given, nothing here is a WWOX result, not medical advice. These priors come from the KDS lane note (`advisor_pilot_20261113/brainstorm_20261116/ketamine_deep_adv_20261117/KDS_LANE_B1_B4_D_SCI_20261117.md`, section 5.3) and were written before any data of this kind exist; the held models (oscillator, hysteresis sweep, homeostat toy) are hypothesis generators, not evidence. The page that cites this file's sha256 (brief section 13.11) is sent nowhere before this file is committed.

## Definitions fixed now
* **Block depth** = fractional reduction of the amplitude of the electrically evoked delayed negative deflection (layer V stimulus, field recording in layer II/III), measured before, during and after exposure, in the same slice (the assay of Breton 2021, Supplementary Fig. S3C, which d-APV suppresses reversibly). **Deep** = at least 0.5; **shallow** = under 0.2.
* **Burst rate** = detected bursts per minute per slice with the detection rule of Breton 2021, fixed before data; only slices with at least three baseline bursts enter. Each rate is divided by the same slice's pre-exposure rate, and then by the same ratio in time-matched vehicle slices of the same genotype. Unit of analysis = animal (slices nested).
* **Post-washout window** = 30 to 60 min after the exposure is removed.
* **Sag** = depolarising sag ratio of layer II/III pyramidal neurons to hyperpolarising current steps, with input resistance and resting potential, in the same slices.

## Priors (S-KO, P13-P17, spontaneous bursting; a use-dependent pore blocker and d-APV, block depth matched)
| # | Prediction | Prior |
|---|---|---|
| P1 | at deep block with the pore blocker, the vehicle-normalised burst rate falls by at least one half | 0.70 |
| P2 | at shallow block with the pore blocker: no change (within +-20%) 0.55; a rise of at least 20% 0.20; a fall of at least 20% 0.25 | 0.55 / 0.20 / 0.25 |
| P3 | in the post-washout window, vehicle-normalised burst rate: between 0.7 and 1.3 times pre-exposure 0.55; at least 1.3 (rebound) 0.30; at most 0.7 (lasting suppression) 0.15 | 0.55 / 0.30 / 0.15 |
| P4 | the pore blocker lowers the sag ratio of S-KO pyramidal neurons by at least 20% at the exposure that suppresses bursting | 0.75 |
| P5 | d-APV at the same deep block falls in the same P3 class as the pore blocker | 0.50 |

## Rejecting observations (written now)
* P1 rejected: deep block (verified by the evoked response) with the vehicle-normalised rate within 0.7 to 1.3 of pre-exposure.
* The 'class-specific action' reading (R-D) is supported, not rejected, if the pore blocker's post-washout class differs from d-APV's at matched depth, or if its burst effect is not reproduced by d-APV at matched depth; it is rejected if sag is unchanged and the two agents agree in every readout.
* Rebound (R-B) is rejected if the post-washout window is within 0.7 to 1.3 for both agents with more than five animals per genotype.

## Scoring (when data exist)
Natural-log score of the probability given to the observed class per prediction, in nats, against a uniform prior over the classes of the same prediction (ln 1/2 for P1 and P4 and P5, ln 1/3 for P2 and P3); reported separately from every other line.
