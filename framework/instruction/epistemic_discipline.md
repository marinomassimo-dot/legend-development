# Epistemic Discipline (public edition)

The single most important part of LEGEND. It governs not only what the system asserts, but what it **rejects** and what it **assumes**.

## 1. The four levels (positive claims)

Every claim is explicitly classified:

- **DATO** (≈ L1, *data*): directly supported by a primary/secondary peer-reviewed source. Traceable, citable, not extrapolated.
- **INFERENZA** (≈ L2, *inference*): plausible, derived from convergence of multiple data points; not demonstrated directly in the specific case at hand. Declared as an inference.
- **IPOTESI** (*hypothesis*): reasonable but not directly supported; marked as hypothesis. Sits between inference and extension.
- **ESPANSIONE** (≈ L3, *extension*): outside the direct gene/disease domain. Useful for strategy space only; cannot enter the current files as consolidated fact without explicit promotion.

Never present inferences as data; never present extensions (or hypotheses) as robust inferences.

## 2. The discipline also applies to PREMISES and NEGATIVES

The four levels above cover only **positive assertions**. A knowledge system that accumulates for months is far more endangered by what it **discards** than by what it asserts.

**The asymmetry that makes negatives the real danger:** a **false positive** gets tested and dies. A **false negative** is **silent, permanent, and self-reinforcing** — once discarded, nobody looks at it again. In a system that compounds over time, a false positive is a cost; **a false negative is a compounding loss.** And tiers, gates, filters, `refuted`, "do not assume that…" are *all machinery that produces negatives.*

> **The most dangerous premises are the ones too obvious to write down.** Nobody annotates *"polyubiquitination leads to the proteasome"* as a claim to cite — it is background knowledge. Precisely for that reason it is never tagged, and therefore never verified. *(It is false as a universal rule: K48 chains commonly support proteasomal turnover, whereas K63 chains have several context-dependent roles, including trafficking and selective autophagy. CMA involvement has to be established for the substrate and context.)*

### Three binding obligations

1. **`PREMISE_TAG` — every rejection, and every non-trivial conclusion, must NAME its load-bearing premise and tag it:** `PREMISE: DATO` · `PREMISE: INFERENZA` · 🔴 `PREMISE: DEFAULT_FROM_TEXTBOOK`.
   > 🔴 A `DEFAULT_FROM_TEXTBOOK` is **not a foundation: it is a research target.** A conclusion resting on one is **provisional by construction.**

2. **`REVIVAL_TRIGGER` — nothing dies in silence.** Every rejection is recorded with **what evidence would reopen it.**

3. **Re-audit rule** — the loop that makes this compound. **Every time a new mechanistic `DATO` arrives, re-scan the dismissal ledger** for rejections whose premise that datum touches. Without this step you have self-*correction*, not self-*improvement*.

## 3. Defaults that have bitten this domain

Before discarding anything, consult the **`DEFAULTS THAT BIT US`** table — textbook defaults that, in real rare-disease work, turned out false:

| Textbook default | Reality |
|---|---|
| polyUb → proteasome | linkage and context matter: K48 commonly supports proteasomal turnover; K63 is multifunctional and can participate in trafficking/selective autophagy, but does not by itself establish CMA |
| misfolded → ERAD / 4-PBA rescue | not necessarily — route must be measured |
| "it is a chaperone" → it helps | a chaperone can escort a client to *degradation* |
| stabilize → restore function | stability and function are separable ("stable but inert" is a demonstrated phenotype) |
| the code does what the docs say | verify against the code, not the documentation |
| the anti-bug tool is immune to the bug | verify the tool, too |

*(These are general-biology and general-engineering defaults, drawn from public literature and practice.)*

## 4. Why this matters

Two real classes of error motivated this layer, both of the form **`P → C`, where C is a rejection and P was never checked — because P was the "obvious" part.** The lesson generalizes to any long-running AI-assisted synthesis: **make the premise explicit, make the rejection reopenable, and re-audit on new evidence.** This is the discipline the failure-aware evaluation (`eval/`) is designed to measure.
