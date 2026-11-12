# IT46 P9 and P8: two levers aimed at the same outcome, one shared measurement

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. IPOTESI throughout; no compound is nominated and no lever is ranked.

**The outcome both levers aim at.** Lower the incidence of slice-level bursts in Wwox-deficient layer II/III slices (36 of 42 knockout, 4 of 23 heterozygote, 0 of 11 wild-type slices; PMID 34634460 as carried in INV-18) without claiming a benefit in function.
* **Lever A (S3):** raise a Kv7 conductance (compound view V10; design R5a/R5b after the P4 audit).
* **Lever B (S7):** raise GABA availability (compound view V20; D1-D3 of the S7 case).

**What each design had alone.** Each carried "an unrelated arm of equal measured effect" as its control for a generic action (R5b for A, D3 for B).

**The connection (a new combination in the repository, not a result).** The two unrelated arms are **each other's comparators**, and a third, non-specific manipulation can be shared:
| Arm | Purpose |
|---|---|
| Vehicle time control | the burst rate drifts in slice; read first |
| Lever A, concentrations chosen to give two or three measured shifts of the recorded cells' membrane potential and input resistance | mediation (reversal or occlusion by a Kv7 blocker) and dose-effect |
| Lever B, a reversible reuptake blocker at concentrations giving the same measured cellular effect | GABA-specific effect, read with the measured GABA reversal potential (IT46-Q01) |
| One non-specific hyperpolarising manipulation of the slice at the same measured cellular shifts | the shared generic comparator |
Readings, written before any run: A and B both larger than the non-specific arm at equal cellular effect → each has an action beyond hyperpolarisation, and A against B says whether the two act through the same cells (occlusion by combination: a second lever adds nothing when the first already saturates); A equal to the non-specific arm → generic; B larger than the non-specific arm only when the reversal potential is below threshold → GABA-specific and conditional; neither beyond the non-specific arm → both are generic hyperpolarisation or both inert. The genotype-by-drug interaction (knockout against a non-Wwox hyperexcitable preparation at matched baseline burst rate) is the only reading that speaks to the Wwox lesion; it is the same for both levers.

**One sample, two questions.** The same recorded cells give: input resistance, resting potential, threshold, sag (INV-18); the GABA reversal potential by gramicidin-perforated patch (IT46-Q01); and the Ba2+-, Kv7-blocker- and Ih-blocker-sensitive difference currents (IT45-Q01). The **shared measure is not a shared cause**: a smaller Kv7 difference current does not predict a more negative GABA reversal, and neither is tied to the other by any source read.

**Consumer changed.** Open-question row IT46-Q04 (`batch_sci_20261105/map/open_questions_map.tsv`): the combined three-arm design, so that one recording programme answers both IT45-Q01 and IT46-Q01. It does not change INV-18 or INV-10 text (no new premise).

**What would drop it.** A seizure phenotype of the model that is not a slice burst; Kv7 channels absent in the recorded cell class at that age (not held: the RNA is P7 and the table is "shared"); a GABA reversal potential at or above threshold in the knockout (then lever B is excluded, lever A unaffected).

**Update 2026-11-12 (IT47 P3), after review; the text above is left as written.** Four inferences above are stronger than the design supports.
* **Non-additivity.** "A second lever adds nothing when the first already saturates" does not show the same mechanism or the same cells. The same result follows from a ceiling of the endpoint (bursts already abolished), from limits of measurement or power, from exposure that does not reach the target in the slice, or from two different mechanisms converging on one downstream step. Additivity does not show independence either (both doses may be sub-maximal on a shared pathway). Reading a combination needs sub-maximal doses on an endpoint that has not reached its ceiling and a dose matrix, and it supports at most "compatible with a shared step".
* **Equal cellular variables.** Matching the shift of the membrane potential and the change of input resistance of the recorded cells does not make two network manipulations equivalent: they differ in location (soma, dendrite, axon initial segment, terminal), time course (tonic or phasic), voltage dependence, effect on synaptic integration and on release. The "non-specific hyperpolarising arm" is therefore a **comparator with stated limits**, not a null; a difference from it narrows the possibilities and does not isolate one.
* **E_GABA.** The sign of GABA's action is not read from the reversal potential alone: it depends on the reversal potential relative to rest and to spike threshold, on the size and location of the conductance (shunting), on the time course, and on activity-dependent chloride loading that shifts E_GABA during the recording. A single value at P13-P17 under one protocol is a starting point, not the sign.
* **"A larger GABA-specific effect is a GABA-specific result".** It is a result larger than that of the comparator at the matched cellular variables, which keeps the comparator's limits; specificity needs a second route (an antagonist, a reversal or an occlusion with a ceiling-free endpoint).
Whether these arms can be interpreted at all is a physiological question for the SCI47 review; no rule of text settles it.
