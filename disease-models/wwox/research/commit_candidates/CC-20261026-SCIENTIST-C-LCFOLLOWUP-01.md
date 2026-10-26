# CC-20261026-SCIENTIST-C-LCFOLLOWUP-01

- **Class:** ORDINARY (research layer; touches no consolidated baseline claim; no working-model change).
- **target_wm_version:** none.
- **Source:** the Lucas-Clarke 2026 follow-up of `scientist-c` (task branch `task/sci-c-lc-repurposing`): `research/drug_repurposing/lucas_clarke_followup_20261026/` (needs, compound/source record, MTBLS12344, ToolUniverse trial), four cards `research/drug_repurposing/cards/E01..E04`, two staged leads under `research/lead_staging/scientist-c/`. The paper reading is `scientist-a`'s (`FTR-20261026-42909904-01`, PAPER 567); nothing here is a new full-text read.
- **All fly content is NOT WWOX-DEE EVIDENCE** (a Drosophila amyloid model). Class level; no dose, administration or suitability; not medical advice. Every statement about what a compound would do in WWOX-deficient tissue is INFERENZA or IPOTESI and is OWED a blind audit by someone other than the producer.

## Proposals (for the integrator; none was applied by the producer)

1. **Add two HYP entries to `therapeutic_hypotheses_ledger_current.md`**, numbered on `main` (the producer used the placeholder ids HYP-20261026-10 and HYP-20261026-11), text below. Both enter at the ledger's initial status, not ranked: the ranking line of the ledger is the Orchestrator's, and every dimension would be 1 of 3 on today's evidence.
2. **Append the two staged leads** with `discovery_lead.py append --staged --apply` (framework/scripts, run on `main`) (`lead_isr_signed_readout_gap.json`, `lead_ldh_stiripentol_weak_link.json`).
3. **Consequence note on `HYP-20260709-05`** (DCA), one line, no status or score change: card `E03_pdk_inhibition_dca` keeps the pyruvate branch separate from what the paper measured; three exploratory transcript tests are negatives that do not show normal PDH or lactate; the stated next measurement is the PDH-activity and labelled-glucose assay already implied by `HYP-20260709-01`. (`record_scoped_edit.py`, label EXPLORATORY.)
4. **Registry-surface check, no edit proposed:** `research_lines_current` and the therapeutic strategies surface are not touched; the cards are non-canonical and live in `research/drug_repurposing/cards/`.
5. **Owed audits:** blind audit of the compound statements in `compounds_and_sources.md` section 2 (they are abstract-level and database-row level; none carries a receipt) and of the INFERENZA lines of the four cards.

## HYP drafts (English; the ledger's field set)

### HYP-20261026-10 — Attenuating the integrated stress response in WWOX loss: no signed human readout yet, so the first experiment is the readout
- **Track:** A (variant-independent); Track B (Q230P class) unmeasured. **Route:** BENEFICIO_PRECOCE (a downstream lever cannot restore WWOX function; deep recovery stays with WWOX restoration, card C01). Both dimensions are kept separately: variant-independent does not imply deep recovery, and the route here is partial benefit.
- **Lever:** 2 (pathway compensation) + 3 (repurposing). **Tag:** `IPOTESI`.
- **Falsifiable statement:** if a WWOX-dependent integrated-stress-response elevation exists in WWOX-deficient human neural cells (raised eIF2 alpha phosphorylation and ATF4 protein) and is harmful, then an eIF2B activator reverses that readout and moves a functional endpoint; if eIF2 alpha phosphorylation and ATF4 protein are not raised, or the ISR is adaptive, the strand has no basis for WWOX-DEE.
- **Expected benefit (endpoint + direction):** protection of neuronal function (network excitability, synaptic or myelin endpoints) by reducing a chronic stress response. Hypothetical: no endpoint has been measured under ISR modulation in any WWOX system.
- **Evidence PRO (fly, NOT WWOX-DEE):** Atf4 immunofluorescence rises with neuronal Wwox reduction plus Abeta42 (n 6, P 0.0022; manifest PMID42909904 entries 57, 59). An eIF2B activator improved memory and tau in a mouse amyloid model (abstract-level). A paediatric tolerability dataset for an ISR-attenuating drug exists in vanishing white matter, a disease of eIF2B itself (abstract-level; non-randomised; frequent adverse events).
- **Evidence CONTRA:** without amyloid the fly signal does not change (entry 58); in the one human knockout organoid deposit the ATF4/ISR target set is LOWER than 10,000 random sets (P 0.0005; exploratory, no amyloid, six libraries, uncorrected across nine set tests); Atf4 is never perturbed in the paper, so Atf4-to-Ldh is the authors' inference; an eIF2B activator engaged its target in adult ALS with no clinical benefit (abstract-level); PERK inhibition showed signs of pancreatic toxicity in a mouse model.
- **Safety (BLOCK-1):** yellow, unassessed for WWOX-DEE. Chronic ISR attenuation in a developing brain is an open safety question; compounds of this class have no WWOX or developmental-epilepsy datum. `legend-safety-triage` has not been run.
- **Translatability:** low until Stage 1 below.
- **Minimal falsifying experiment:** Stage 1: eIF2 alpha phosphorylation, ATF4 protein and ATF4-target transcripts in WWOX-deficient versus isogenic human neural cells at matched maturity, with and without a defined proteotoxic challenge. Stage 2 (only if elevated): an eIF2B activator versus vehicle on that readout and one functional endpoint. Fly: an Atf4 loss-of-function arm with Ldh and lactate readouts.
- **Reopening condition after parking:** a raised ISR readout in a WWOX-deficient human neural system.
- **Status:** `generated`. Card `P4-E-01`.

### HYP-20261026-11 — LDH lowering as a partial-benefit lever: one fly precedent, a weak approved candidate, no human WWOX datum
- **Track:** A; Track B untested. **Route:** BENEFICIO_PRECOCE (allele-blind, downstream, partial by construction).
- **Lever:** 2 + 3. **Tag:** `IPOTESI`.
- **Falsifiable statement:** if lactate or LDH activity is raised and contributes to dysfunction in WWOX-deficient human neural cells, then lowering LDH activity lowers lactate and improves a functional endpoint; if lactate and LDH activity are not raised independent of maturity, or lowering LDH worsens function, the lever has no basis.
- **Evidence PRO (fly, NOT WWOX-DEE):** Ldh RNAi added to Abeta42 plus Wwox RNAi improved climbing at 14, 21 and 28 days (entries 50-54); Ldh transcript and lactate rise in that genotype (entries 29, 39, 40, 43). Stiripentol is an approved paediatric epilepsy drug with a nominal LDH link; an LDHA-directed oligonucleotide is approved for primary hyperoxaluria (liver-directed).
- **Evidence CONTRA:** the Ldh rescue lacks an Ldh-alone arm, a Wwox-mRNA check and a lactate readout, and the authors cite Ldh knockdown as detrimental in other fly amyloid models (entry 56); lactate falls nominally without amyloid; LDHA in the human knockout organoid is as consistent with immaturity as with WWOX loss; stiripentol inhibits LDH only weakly in the retrieved measurements and has other pharmacology; human lactate in WWOX deficiency is reported normal or extremely low (DL-BIO-008, DL-BIO-009).
- **Safety (BLOCK-1):** yellow, unassessed. Stiripentol's labelled use is with another antiseizure drug; interactions are not assessed here. Research LDHA inhibitors have no CNS or paediatric datum.
- **Translatability:** low.
- **Minimal falsifying experiment:** lactate (enantiomer- or isotope-resolved) in the double-RNAi fly genotype plus an Ldh-alone arm and Wwox mRNA in the double line; LDH activity and the lactate-to-pyruvate relationship in WWOX-deficient versus isogenic human neural cells at matched maturity; then stiripentol against a selective LDHA tool at matched exposure.
- **Status:** `generated`. Card `P4-E-02`.

## What was NOT proposed
- No change to `HYP-20260709-01` (ketogenic; card `E04` is an abstention that points at its existing Seahorse falsifier) and no change to the PDK/DCA safety position.
- No claim, paper or working-model edit. Scientist A's preprint-versus-published file was not redone.
- ToolUniverse: WATCH for the PDK2 compounds-for-target query only; nothing adopted.

## Harness change landed on the task branch (T0, §21e)
`framework/adapters/orphadata.py` percent-encodes the name (a multi-word name raised an unhandled `InvalidURL` and aborted the caller); `framework/adapters/_http.py` returns `(0, error text)` for a `ValueError` such as `InvalidURL`, as its docstring promises for transport failures. Measured: the offline adapter selftest is green; the live query for a multi-word name now answers (see the lucas_clarke_followup record). A name-substring match by the Orphadata service for "vanishing white matter" returned an unrelated disorder: the adapter is not a disease-name lookup and must not be quoted as one.
