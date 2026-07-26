---
name: legend-safety-triage
description: BLOCK-1 safety/druggability gate for candidate molecules (repurposing or small-molecule) emerging from therapeutic hypotheses. Runs one or more compounds (SMILES) through ADMET-AI (ADMET predictions via Chemprop/TDC — absorption, distribution, metabolism, excretion, toxicity, and above all blood-brain-barrier BBB penetration, essential for a CNS target like WWOX) and medchem/datamol (Lipinski/Veber/CNS drug-likeness rules, PAINS/NIBR/ChEMBL structural alerts, complexity). Returns a triage with red/yellow/green flags and a BLOCK-1 verdict. Use it when the operator says "is this molecule safe/passable?", "run the ADMET triage", "check druggability/CNS", "filter these repurposing candidates", or before promoting a molecule-hypothesis to the therapeutic tracker. READ-ONLY toward the current files; predictions are in-silico HYPOTHESES, not validation. It is NOT medical or toxicological advice.
---

# legend-safety-triage — ADMET / druggability gate (BLOCK-1)

Paths are relative to the workspace root.

## Why this skill exists
In the mission, **safety comes before speed** and **BLOCK-1 beats enthusiasm**. Whenever a therapeutic lever concretizes into a **molecule** (a drug-repurposing candidate, a pathway modulator), before taking it seriously it must be run through a druggability and ADMET sieve. This skill is that sieve, wired onto two real and light tools (CPU, pip):
- **ADMET-AI** — Chemprop models trained on the Therapeutics Data Commons ADMET datasets: predicts absorption, distribution, metabolism, excretion, toxicity from SMILES. Includes decisive endpoints: **BBB penetration**, hERG (cardio), DILI (hepato), CYP, clearance, solubility.
- **medchem** (datamol/RDKit) — drug-likeness rules (Lipinski, Veber, **CNS**, lead-like), structural-alert catalogues (**PAINS**, NIBR, ChEMBL), complexity metrics, query language.

Since WWOX disorders are **CNS** conditions, **BBB penetration** and the **CNS-MPO** rule set carry special weight: a molecule that does not reach the brain is, for a CNS target, of little systemic relevance.

## Human gate
Starts on request or as a downstream step of `legend-hypothesis-forge`/`legend-aso-designer` when a molecule candidate emerges. It needs at least one **SMILES** (or a name/ID to derive it from, e.g. PubChem CID → canonical SMILES).
**It is NOT medical or toxicological advice.** Outputs are **in-silico predictions** = `IPOTESI`, useful to discard/prioritize, never to "promote as safe".

## Discipline — what you may and may not write
- **READ-ONLY** toward the 4 current files, the biomarker/endpoint layer, and the therapeutic tracker.
- **WRITABLE** (carve-out): annotate the triage as a **Safety/ADMET** field in the therapeutic hypothesis ledger entries (or in a triage note if requested). It creates no canonical claims.
- A candidate with a red flag → ledger status `flagged` (it does not die, but does not advance to `proposed-to-portfolio`).
- Code execution: `admet-ai` and `medchem` run locally on CPU. Their **web-apps/APIs** are optional and involve external traffic → to be explicitly authorized; by default use local mode.

## Epistemic discipline (mandatory)
`DATO` (published experimental/pharmacological measure) / `INFERENZA` / `IPOTESI` (in-silico ADMET/rule prediction — the majority here) / `ESPANSIONE`. Never write "safe/toxic": write "**predicted** favourable/unfavourable on endpoint X (model Y)". ADMET predictions have uncertainty; report it.

## Procedure

**0. Input.** Collect the canonical SMILES of the candidates (if you only have a name/CID, derive them). Note the context: CNS target, pediatric CNS context, any co-administration.

**1. Druggability / alerts (medchem).** Apply:
- Rules: Lipinski, Veber, **CNS** (and CNS-MPO if available), lead-like → which they violate and why.
- Structural alerts: **PAINS**, NIBR, ChEMBL → problematic/promiscuous substructures.
- Complexity and reactive/toxicophore functional groups.

**2. ADMET (ADMET-AI).** Predict the panel, highlighting for a CNS target:
- **BBB penetration** (high weight: CNS target).
- **Toxicity**: hERG (cardio), DILI (hepato), mutagenicity/AMES, clint.
- **Pharmacokinetics**: solubility, permeability (Caco-2/PAMPA), CYP (interactions), clearance/half-life.
- Compare against the tool's reference percentiles (ADMET-AI also ranks relative to known libraries).

**3. BLOCK-1 verdict (traffic light).**
- 🔴 **Red** — a serious alert (e.g. toxicophore, high predicted hERG/DILI, null BBB for systemic use on a CNS target): `flagged`, does not advance.
- 🟡 **Yellow** — mitigable concerns (one rule violated, uncertain permeability): advances with caveats and as a datum to clarify.
- 🟢 **Green** — predicted favourable profile: may proceed (still `IPOTESI` until validated).

**4. Output.** Write/update the Safety/ADMET field in the candidate's ledger entry: traffic light, key endpoints with predicted value and model, violated rules, and the **validation step** (the experimental measure that would confirm the prediction). Update the status if `flagged`.

## Closing (mandatory in chat)
1. Traffic light per candidate and the dominant reason.
2. Killer endpoints if present (e.g. "predicted null BBB" for systemic use).
3. What would be needed to confirm in vitro/in vivo.
4. Disclaimer: **"In-silico predictions (IPOTESI), not medical or toxicological advice. They serve to prioritize/discard, not to declare a molecule safe."**

## What NOT to do
- Do not declare a molecule "safe": only "predicted favourable on endpoint X".
- Do not ignore the BBB for a CNS target.
- Do not promote a candidate with an unresolved red flag to the therapeutic tracker.
- Do not touch the current files; do not self-authorize URGENT.
