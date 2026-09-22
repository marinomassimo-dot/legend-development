# COMMIT CANDIDATE — CC-20260922-TAU-DIRECTION-01

**Source:** Scientist F, Domain G node
([`superior_node_search_20260922.md`](../../analysis/superior_node_search_20260922.md)).
**Every quotation below re-read by the Orchestrator in the primary body**, PMID 22193544 /
`PMC3354054` retrieved in full this session. Two were additionally cross-checked against the
repository's own `deepdive_manifests/PMID22193544.json`, where they appear verbatim.
**Change class:** **MINOR** in edit size, 🔴 **HIGH in consequence** — §1 is a directional safety
statement that prevents a whole modality from being imported wrongly.
**Target:** `analysis/mechanism_intervention_map.md` §5 (beside `N-01`) ·
`analysis/therapeutic_routing_and_endpoint_hardening.md:625` (closes a `NOT_LOCATORED` flag) ·
`claim_registry_current.md` `CLAIM 035` (one qualifier).
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R3** — §1 constrains a therapeutic direction, and §2 adds a qualifier to a claim.
**Proposes:** `D-29` — *"when the pathway looks like a known disease, check which way the arrow
points before importing that disease's modality."*

---

## 1 · 🔴 Tau-lowering must not be imported into WWOX-DEE — Tau is the effector of the benefit

The mechanism on record reads like a tauopathy: WWOX loss → GSK3β de-repressed → pTau S396/S404 up
(`CLAIM 035`, `DL-MECH-019`, `CHAIN C`). Tauopathy's dominant modality is **tau-lowering**. Applied
here it would be **backwards**, and the primary says so directly.

According to PubMed, Wang *et al.*, *Cell Death Differ* 2012
([DOI](https://doi.org/10.1038/cdd.2011.188) — PMID 22193544, `PMC3354054`), Results, verbatim:

> *"**Neither WWOX overexpression nor GSK3β knockdown promoted neurite outgrowth in the Tau knockdown
> condition, indicating that Tau is the effector of both WWOX and GSK3β**."*

And, in the same experiment:

> *"the neurite outgrowth stimulated by RA was **abolished when Tau was knocked down**."*

🔴 **Tau is not the toxin in this pathway. It is the thing the pathway is trying to make functional.**
Knocking it down abolishes the benefit of the two interventions the model is built on — WWOX
restoration and GSK3β inhibition. **A tau-lowering agent would remove the effector both of our gene
therapy and of our downstream kinase arm.**

⚠️ **This is a statement about a direction, not a treatment**, and it is a statement about *this*
pathway in *this* system (SH-SY5Y, RA-differentiated, RNAi). It does not say tau-lowering is unsafe
in general, and it names no molecule. **`BLOCCO 1` untouched; nothing here is medical advice.**

🔵 **No text in this repository states it.** Verified by search. The pathway is recorded; the arrow's
direction is not — and the direction is the part that would be got wrong by anyone importing the
obvious modality. **Proposed:** record it in `mechanism_intervention_map.md` §5 beside `N-01`, as a
directional constraint on the downstream arm.

---

## 2 · ✅ Closes a `NOT_LOCATORED` flag — and the locator arrives with a qualifier the claim lacks

`therapeutic_routing_and_endpoint_hardening.md:625` flags the assertion *"ripristina l'assemblaggio
dei **microtubuli** Tau-dipendente"* as 🔴 **`NOT_LOCATORED` — none of the nine** locators covers it.
**The flag was accurate**: the repository's `PMID22193544.json` manifest contains no
microtubule-assembly locator, confirmed by search for `turbidity` and for the sentence itself.

**The locator exists in the body.** Results, verbatim:

> *"GSK3β diminished the microtubule assembly, as reflected by decreased turbidity. However, the new
> equilibrium reached a **higher turbidity when treated with WT WWOX and GSK3β than with GSK3β
> alone**. Interestingly, the GSK3β-binding deficient WWOX, **WWOX L404A, could not restore the
> microtubule assembly activity**."*

### 2a · 🔴 And the qualifier, which `CLAIM 035` does not carry

**That assay is cell-free.** Methods, verbatim:

> *"Microtubule assembly assays were performed by incubating **tubulin (0.2 mg/l)** (Cytoskeleton;
> Denver, CO, USA) **in cuvettes** at 37 °C in a thermostatic spectrophotometer and measuring the
> **turbidity change at 350 nm** over time."*

Purified tubulin, a cuvette, and a light-scattering readout. **No cell is involved.** The neurite
and pTau limbs of `CLAIM 035` are cellular; **the polymer limb is not**, and reading it as cellular
is an overclaim. **Proposed:** close the flag with the locator **and** attach
`in vitro / cell-free (purified tubulin, turbidimetric)` to the microtubule-assembly limb wherever
it appears.

### 2b · ⚠️ New `REPORTED_UNIT_AMBIGUITY`

The Methods print **`tubulin (0.2 mg/l)`**. Standard tubulin polymerisation assays run at the
**mg/ml** scale, so as printed this is orders of magnitude below a workable concentration. **Same
class as the `digoxin 100 mg/kg` entry already on the register.** 🔴 **No basis to rewrite it** — the
value is recorded **exactly as printed**, flagged, and **not used in any calculation.**

---

## 3 · ✅ Strengthens `CLAIM 035` / `DL-MECH-019` — the loss direction is measured, not inferred

> *"**SH-SY5Y cells in which WWOX expression was reduced by RNAi showed increased pTau S396 levels
> and notably decreased neurite outgrowth**."*

⚠️ **Bounded:** RNAi knockdown in a **neuroblastoma line**, **not** a WWOX-DEE allele, not a patient
cell, not a neuron. It converts *"WWOX loss → pTau up"* from an inference off the overexpression
arm into a **measured** result in one direction in one system, and no further.

---

## 4 · `DIS-010` stands, and is now better evidenced

The repository dismisses direct WWOX–Tau binding (`DIS-010`, `D-14`). The paper's own Discussion
**softens its own negative**, verbatim:

> *"Here, we were not able to detect a Tau–WWOX complex in our co-immunoprecipitation experiment
> from SH-SY5Y cells (); **the inconsistency in results may due to the different expression systems
> used**."*

So the negative is a **system-bounded** negative, not a refutation of the Chen yeast-two-hybrid
result. 🔵 **And nothing in §1–§3 depends on direct WWOX–Tau binding** — the chain runs
WWOX ⊣ GSK3β ⊣ Tau-phosphorylation → microtubule competence, which the L404A mutant isolates at
every step. **`DIS-010` is untouched and its scope is now recorded.**

---

## 5 · 🔴 The wave's main output is a NEGATIVE, and it should be recorded as one

**Domain G returned no node superior to the existing portfolio.** Scientist F's own filter explains
why, and it is worth keeping because it is a statement about the *shape* of the problem:

1. act on the **developmental**, not the seizure, endpoint (`DL-MECH-039`, `N-15`) — this removes
   every symptomatic axis;
2. have a window **still open after diagnosis** (`DL-MECH-011`, P1–P5) — this removes everything
   acting on neurogenesis;
3. have an intervention arm in a WWOX-deficient system — and the downstream census measured
   **exactly four positive arms in the entire literature**.

The best candidate found (Tau's microtubule-binding competence as a target *at the effector*, rather
than at the kinase) **passes (1) and (2) and fails (3) completely.** It stays a **flag with a cheap
first experiment**, not a candidate: pTau S396/S404 + polymerised:free tubulin + MAP2 in isogenic
human WWOX-KO neurons versus parental — **three blots, no new reagent, never done in any human WWOX
system.** Unchanged polymer and unchanged pTau kills it.

⛔ **Two nodes are recorded as FLAG ONLY and must not be scored:** astroglial K⁺/water homeostasis
(Kir4.1/KCNJ10–AQP4) and ER-exit-site/COPII (SEC23IP) — **each rests on two consecutive `IPOTESI`
with no mechanistic bridge**, which by the wave's own rule is not a candidate.
⛔ **YAP/TAZ–TEAD de-repression was built and then killed by this repository's own data**: it
predicts `P47T` should be severe, and `CLAIM 030` records `P47T` as normal protein, binding
abolished, **mild**. Dropped, no `REVIVAL_TRIGGER`.
⛔ **Autophagy–lysosome induction cannot be a node today** — sign contested 2:1, and `TFEB` appears
**zero times** in the tree. Proposing it would be the `D-03` error; it was correctly declined.

---

## 6 · Provenance and integrity

- **Re-read, not accepted.** The body was retrieved by the Orchestrator this session; **all six**
  load-bearing quotations were located in the returned text. Two (`Tau is the effector…`, `reduced
  by RNAi…`) also appear verbatim in `deepdive_manifests/PMID22193544.json`, giving them two
  independent local anchors.
- **Second delegate lead item this session to survive verification unchanged** (after Scientist C's
  bafilomycin finding). Recorded because the base rate matters: of six delegate waves today, two
  arrived clean, two needed correction, and one was a false alarm.
- **No new receipt claimed.** PMID 22193544 already carries five persisted receipts
  (`FTR-20260726-22193544-01`…`-05`) at full-text depth; today's read is a **targeted re-read that
  adds locators, not depth**. The `PMID22193544.json` manifest should gain the microtubule-assembly
  and Methods locators — that is a manifest addition, not a depth change.
- ⚠️ **Extraction defect, again, and in a way that matters here:** the returned text renders `GSK3β`
  as `GSK3` throughout — the Greek subscript is deleted, exactly as italic gene tokens and vector
  exponents are elsewhere. **The `β` has been restored in the quotations above from the manifest and
  from the paper's title context, and that restoration is declared** rather than silent. No other
  character was altered.
- **`UNREAD_PREMISE`: measured at 0 by `growth_anchors.py check` before this candidate was written,
  with Scientist F's own five declared in `FT-131`.** Not predicted.
