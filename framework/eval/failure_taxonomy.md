# Failure Taxonomy — Reusable Reasoning-Failure Gates

The benchmark's authentic core. Each entry is a **reasoning-failure gate** learned from a *real, observed* error during genuine rare-disease research, with a public-literature example. These are not synthetic distractors invented for a benchmark — they are documented failure modes, which is what makes the benchmark hard and honest.

> Public method. No patient referenced. Each gate: the failure → the rule → what a model must do.

## The gates

| Gate | Failure it catches | Rule |
|---|---|---|
| **MECHANISTIC_OVERTRANSFER** | Promoting a specific sub-mechanism to a *different* variant/context on partial evidence (e.g. transferring a lysosomal degradation route measured on one SDR missense to another) | Separate synthesis / solubility / turnover / route / function; a route measured on variant X is a *hypothesis* for variant Y, not a datum |
| **NMD_LAST_EXON** | Applying "premature stop → NMD" without checking the variant is not in the last exon (NMD-escape) | Check exon position before predicting NMD |
| **DEGRADATION_DIRECTION_GATE** | Inverting substrate and regulator ("gene X degrades partner Y" when Y regulates X) | Name the direction; do not infer causality from co-occurrence |
| **MECHANISM_DIRECTNESS_GATE** | Turning marker + phenotype into an unmeasured intermediate ("protein down + seizures ⇒ pathway Z active") | A surrogate is not the mechanism; the intermediate must be measured |
| **PROTEIN_STATE_IDENTITY_GATE** | Reading a rescue vector as if it were a Western blot; conflating abundance with function | Abundance ≠ function; "stable but inert" is a demonstrated phenotype |
| **REPORTER_IDENTITY_GATE** | Accepting a paper's label for a construct without checking the reporter (e.g. an assay named for one repair pathway that actually reads another) | The construct catalog overrides the name given in the text |
| **TARGET_ATTRIBUTION_GATE** | Concluding a rescue identifies the target ("drug D rescues ⇒ D's canonical target is the mechanism") | A pharmacological rescue does not identify the target automatically |
| **KG_EDGE_HAS_NO_SIGN** | Treating a knowledge-graph edge as a directional/therapeutic hypothesis | A KG edge is a *relevance* hypothesis, never a *direction*; read the sign in a loss-of-function model, not a tumor line under chemotherapy |
| **SOURCE_INTEGRITY** | Prioritizing a retracted / corrected paper | Check retraction/correction status before use |
| **READING_DEBT_FALSE_NEGATIVE** | A relevant paper present in the corpus but never read, discarded by ranking | Ranking orders reading; it never authorizes *not reading*. If ranking discards a study, the ranking is broken |
| **EXTERNAL_DOSSIER_CANONICAL_DRIFT_GATE** | An external dossier drifting from the canonical state; a dossier reviving a withdrawn premise | Reconcile every external output against the current state before use |
| **PREMISE / PUBLICATION** | (see [epistemic discipline](../instruction/epistemic_discipline.md)) A conclusion resting on a `DEFAULT_FROM_TEXTBOOK`; a claim leaving the private boundary | Name and tag the load-bearing premise; provenance gates publication |

## How they become benchmark gold cases

Each gate seeds an **error family**. A gate is *not* a benchmark item by itself — it becomes a gold case only after: a **public evidence instance**, an **expected answer**, **independent adjudication**, and a **freeze**. Each family then gets multiple public instances, positive cases and negative controls, and a held-out split (see `README.md`).

## The keystone: the false negative

The most dangerous of all is the **permanent false negative** — a correct lead discarded on an unexamined premise and never revisited. Every gate above, when it fires wrongly, can *create* one. That is why every rejection records a **`REVIVAL_TRIGGER`** (what would reopen it) and why every new mechanistic datum **re-scans past rejections**. The temporal T0→T1 eval (`README.md`) measures exactly this: does the system reopen the right conclusion when the evidence changes?
