# CC-20261027-SCIENTIST-C-W2-THERAPEUTIC-01

- **Class:** ORDINARY (research layer; touches no consolidated baseline claim; no working-model change).
- **target_wm_version:** none.
- **Source:** `scientist-c`, task `SC-IT2-THERAPEUTIC-20261027`, branch `task/sc-it2-therapeutic`: `research/drug_repurposing/w2_therapeutic_it2_20261027/` (README, two scripts, two derived tables, `build_cards.py`) and cards `research/drug_repurposing/cards/F01..F03`.
- Everything non-WWOX is NOT WWOX EVIDENCE. No new full-text receipt. All INFERENZA and IPOTESI statements are OWED a blind audit by someone other than the producer (README section 7).

## Proposals (for the integrator; none applied by the producer)

1. **Add one HYP entry** to `therapeutic_hypotheses_ledger_current.md` (numbered on `main`; placeholder HYP-20261027-01), initial status `generated`, no ranking line.

### HYP-20261027-01 — Which glutamate receptor carries the raised gain in neuron-specific Wwox loss, and does a partial block reproduce the full block?
- **Track:** A (variant-independent); Track B unmeasured. **Route:** BENEFICIO_PRECOCE (a network-state lever; WWOX function stays lost). **Lever:** 3 (repurposing) + 2. **Tag:** `IPOTESI`.
- **Falsifiable statement:** if bursting in Wwox-deficient neurons reflects a gain in NMDAR or AMPAR function, then a graded partial block by memantine or perampanel lowers burst frequency in knockout and not in wild-type slices; if only the full competitive block (d-APV) works, the dependence is permissive and neither drug is a lever.
- **Expected benefit (endpoint + direction):** lower burst frequency, duration, amplitude and phase-amplitude coupling; a maturation endpoint must be added because burst control is not recovery (N-15). Hypothetical: no memantine or perampanel arm has ever been run on a Wwox system.
- **Evidence PRO:** d-APV abolishes bursting (5 slices, 3 animals); mEPSC amplitude raised; a knockout-specific delayed response is NMDAR-dependent; no memantine or perampanel arm exists in a Wwox system.
- **Context, not evidence for WWOX (other disease):** memantine benefit in 14 of 19 gain-of-function GRIN carriers (4 of them transient, 10 sustained; sustained-only variant-level P = 0.0698) versus 3 of 15 in the comparator (which holds 4 non-pathogenic variants); retrospective, unblinded.
- **Evidence CONTRA:** the same cohort shows 3 of 15 benefit with loss-of-function or indeterminate variants, so a shared NMDAR node does not give the sign; NMDAR dependence is permissive; the AMPAR contribution was never tested; memantine accelerated provoked seizures in an adult rat model; paediatric effectiveness of memantine not established on its label; one adult WWOX case on perampanel plus six drugs had no sustained benefit (n = 1); chronic NMDAR block may cost activity-dependent myelination (unmeasured).
- **Safety (BLOCK-1):** unassessed; `legend-safety-triage` not run; perampanel labelled warnings not retrieved.
- **Translatability:** low until the receptor-level measurement exists.
- **Minimal falsifying experiment:** NMDA:AMPA ratio under voltage control plus graded memantine vs perampanel vs d-APV on burst endpoints in Wwox-deficient vs parental neurons or juvenile slices, with wild type and heterozygote comparators and washout; then a maturation endpoint.
- **Reopening condition after parking:** a receptor-level (NMDAR or AMPAR) measurement in a Wwox system, in either direction.
- **Status:** `generated`. Card `P4-F-01`.

2. **Consequence note on map record R-02 and DL-MECH-002 (one line each, no status change, EXPLORATORY):** the GRIN2A convergence corroborates the node, not the sign of intervention; the GRIN2A variant class in the cohort abstract is not stated (abstract only on file, `NO_RECEIPT`).
3. **Precision note on DL-MECH-031 (one line) and a FIX FOR THE INTEGRATOR on manifest `PMID42422765` entry 43:** entry 43 reads the printed Fig 6E labels (48/30/50/70 percent) as KO relative to WT; the independent verification reads them as the size of the reduction (about 50/72/49/30 percent remaining; cortex and anterior commissure mapping differ). Correct the entry through the manifest path. Note: the "near-complete MBP rescue" of the neuronal AAV rests on representative micrographs; the only MBP quantification is knockout vs wild type (manifest PMID42422765 entries 6, 7, 43). Also mark point 2 (seizure control improves myelination) as an assumption with a counter-precedent (Knowles 2022, abstract only).
4. **Consequence note on map R-07 (one line):** ChEMBL_37 curates bumetanide's mechanism as NKCC2 only; NKCC1 is an activity-table fact (three rows); the experiment specification is in card `F03`.
5. **Owed audits:** blind audit of README section 7 items 1-5 and of the INFERENZA lines of cards `F01..F03`.

## What was NOT proposed
- No change to N-02, N-12, N-13, N-10 or R-04/R-08 status: no executable datum moved them; abstentions with reasons are in README section 1.
- No claim, paper or working-model edit.
