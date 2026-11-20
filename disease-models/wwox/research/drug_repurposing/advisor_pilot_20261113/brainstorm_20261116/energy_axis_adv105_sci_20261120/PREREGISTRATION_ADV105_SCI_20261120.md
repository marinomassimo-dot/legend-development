# ADV-105 pre-registration (SCI, 2026-11-20): can correcting brain energy supply or glial state AFTER onset contribute to maintenance or functional recovery, and which agents have juvenile or paediatric exposure data (hypothesis level; exploratory; no dose, schedule or advice; reference genotype class only; not medical advice; written before the external searches)

Source: ADV message of 2026-11-20 to SCI (ADV-105, portfolio row RP-033; `assignments/ADV-105.md` not on main when written). Method and stop rule are SCI's. Effort high, no delegate unless a pivotal number needs a check, no spend; plain clients with a generic client name, no contact parameter, no browser-header spoofing; abstract-only readings marked.

**What I had before writing this (stated).** ADV-101 increments 1 and 2 (timing of hypoglycaemia; the null's lower insulin, higher glucose uptake, lactate; DCA and the ketogenic diet with no pup exposure value in any sheet), ADV-074, ADV-079, card EB-KD-01 (WEAK, five children), ADV-104 (glial readout, Rett microglia contested; preterm rabbit and cuprizone not transferable). Nothing from the external after-onset energy literature.

## Questions and the rule that closes each
A1 energy-supply interventions in neonatal or paediatric epilepsy whose lesion is not a neuronal-protein loss (GLUT1 deficiency, PDH deficiency, congenital lactic acidosis, neonatal hypoglycaemia-seizure models): for each, what changed, at which age, effect on seizures or survival, and **whether the effect was shown AFTER onset** (an effect after onset needs a start age later than first symptoms and an outcome on seizures, function or survival). Closes at **at most 12 searches** in total for A1, A2 and B, or when each named condition has a row or "not found by these routes".
A2 glial-state manipulations after onset in developmental epilepsy or hypomyelination models, with age and endpoint: reuse ADV-104 sources; search only what that note did not cover; closes at the same budget.
B juvenile or paediatric exposure facts per agent (blood ketones, CSF or brain level, label): HE's `sheet_query.py` first, then the searches; "no sheet" is not "incompatible"; an exposure fact is a measured level, a label statement or a stated age of use, never a dose recommendation.
C coherence check against the ADV-101 null-pup facts (hypoglycaemia from the second week with lower insulin, higher glucose uptake, glycolysis, lactate): "coherent", "contradicted" or "not separable", with the reason; a rival is stated.

## Row structure (exploratory evidence kept apart from promotion criteria)
Every row carries: source anchor and depth; context (condition, age, model); what changed; **a competing explanation (for example "energy state is a consequence of seizures")**; **the observation that would weaken the idea**. Promotion criteria (ADV-101 and ADV-104) are unchanged and are **not** requirements to investigate; this note does not apply them as filters.

## Labels fixed now
* **SHOWN AFTER ONSET:** treatment started after first symptoms with a seizure, function or survival outcome and a comparator or a clear before-after; **ASSOCIATED:** an effect without a post-onset start or without a comparator; **NOT FOUND BY THESE ROUTES:** none located (not an absence claim).
* **Coherent with the null-pup facts** only if the intervention acts on a state the null-pup facts show (insulin, glucose uptake, glycolysis, lactate, glucose) in the same direction as the condition it corrects in the source; otherwise "not separable".
* **One paragraph at the end:** whether an energy-supply readout or arm is worth exploring in the null pups, at what age (a post-onset arm?), and what would weaken it. A "no" is allowed.

## Stop rule
Stop at 12 searches or when A1 conditions are exhausted, whichever first; if after-onset evidence is absent for every condition I say so and still give the paragraph. A single catalogue of ketone or exposure values is not extended beyond the agents found. No search is repeated from ADV-101 or ADV-104 (their queries are in their notes).
