# Class-to-member specification step, development trial 1: result (HE; 2026-11-17; non-canonical; not medical advice)

**DEVELOPMENT ON A TUNED-ON TARGET: no claim of improvement; a positive result would only have licensed a trial on a target not used for design.** Written for: ADV, SCI (scores her own forecast; hash in her file `PREDICTIONS_C2M_TRIAL_SCI_INDEPENDENT.md` sha256 148ee1eb8eec4f30395e9c2f301f9d79230b025b82dd654dbec87a5f65f0c5f0, written at 08:41:45Z before any run). Frozen: `FREEZE_C2M_TRIAL.md` sha256 97dafb3ccf4e77d7eb3202ecc99ca9832194e5c84dab8535e0634669e6158c5d; ADV approved the freeze and gave the 'go' on SCI's hash.
## Runs (three tool-free delegates, sonnet, `legend-deepdive`, one at a time; nothing changed after the first run)
| run | input | tokens | tool calls |
|---|---|---|---|
| A1 | enumeration block A (Mg2+, Mn2+, 'metal'; no zinc) | 27,100 | none |
| A2 | enumeration block A | 29,252 | none |
| B1 (control) | enumeration block B (zinc already named as a supply item) | 31,465 | none |
Total **87,817 tokens** (estimate 75k; cap 150k); no usage-limit message. Outputs verbatim: `OUT_A1.txt` bf0b1429, `OUT_A2.txt` 1a7a5676, `OUT_B1.txt` 422af974.
## Result (scored by me, mechanically and by reading; not blind, as the freeze states)
| item | A1 | A2 | B1 |
|---|---|---|---|
| STRICT: zinc listed as a metal-ion member that LOWERS the cyclase activity | NO (0 mentions of zinc) | NO (0 mentions) | YES ('Ca2+ / Zn2+ (competing divalent cations) | lowers' in axis a, and 'Zinc | lowers' in axis d; both in the LOWERING MEMBERS line) |
| LOOSE: an ion other than Mg2+ and Mn2+ listed as lowering | YES (Ca2+ and metal chelators, lowers) | YES (Ca2+ substitution and chelation, lowers) | YES (Ca2+ / Zn2+) |
| Mg2+ and Mn2+ given the raising direction | yes, yes | yes, yes | yes, yes (and Mg2+ depletion lowers) |
| members listed for the metal-ion class (axis a) | 3 (Mg2+, Mn2+, Ca2+/chelators) | 3 | 4 to 5 (Mg2+, Mn2+, Mg2+ depletion, Ca2+/Zn2+, plus dietary Mg2+ and zinc in axis d) |
| 'LOWERING MEMBERS' line includes zinc | no | no | yes |
**STRICT in A1 or A2: 0 of 2. The informative outcome occurred: asked for the members and directions of the metal-ion class named by an enumeration that did not contain zinc, the model listed Mg2+ and Mn2+ as raising, Ca2+ (and chelators) as lowering, and never zinc, in either run.** When zinc was already present in the input (B1) it was kept, given the lowering direction and placed in the metal-ion class as an inhibitory competing cation.
## Predictions scored
HE: zinc as a lowering member in at least one of A1/A2 55 percent (did not occur); in both 30 percent (no); B1 keeps zinc with the lowering direction 85 percent (yes); a loose hit in A 80 percent (yes).
SCI (hash 148ee1eb…, read here only after her file existed; she scores her own): strict in at least one of A1/A2 0.80 (no); in both 0.55 (no); loose in at least one 0.93 and in both 0.80 (yes, yes); B1 keeps zinc as lowering 0.65 (yes); Mg2+ and Mn2+ both raising in A 0.90 (yes, both runs); median metal-class members 5 (3 to 8) (A: 3, B: 4 to 5); median lowering members 2 (1 to 4): A1 and A2 each list one lowering metal-ion member (Ca2+/chelators), B1 two (Ca2+/Zn2+, zinc).
## What it says, and what not
The trial is negative on the case it was written for: a class-to-member step with the explicit instruction to give members and directions does not produce zinc from a metal-ion class whose enumeration names only Mg2+ and Mn2+, in two of two runs; it produces a different lowering ion (Ca2+) and a chelator. So the model does NOT list zinc as an inhibitory member without a cue, even though the T7 probe showed it knows zinc as a general cyclase inhibitor and B1 shows it will say so when zinc is in view. This points the gap away from the specification of the class and toward the point where a member is cued: in the generator, what is in view in the enumeration, and in the composition of the fifteen and the keep rule. It does not license the trial on a target not used for design (no strict positive). Limits: one target (tuned-on); two A runs; scoring by me, not blind; the instruction asks for members and directions explicitly, so the negative is a negative for that instruction; B1 is not a test of emergence.
