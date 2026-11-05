# IT29 P10 step 1: the open question (chosen 2026-11-05)

Non-canonical working record, not medical advice. Public edition, WWOX-DEE reference genotype class.

## The question

**Does loss or inhibition of class IIa HDACs (HDAC4, HDAC5, and the paralogs HDAC7 and HDAC9) in the central nervous system move oligodendrocyte differentiation and myelination, in which direction, through which function (catalytic or scaffold), and by which cell (oligodendroglia or the axon-bearing neuron)?**

Stated for the programme: the class IIa thread (HDAC5 to SLC2A1; TMP269, nanatinostat, pracinostat as its compounds) carries a *myelin counter-premise* that is only partly sourced. Is it a real constraint on the lever, a peripheral-nerve artefact, or neutral?

## Where it lives, and why it is still open (files read, not summaries)

| Record | What it says | Why that leaves it open |
|---|---|---|
| `phenotype_first_it29_20261105/p3_B/README.md`, table row "HDAC4 / HDAC5 in CNS oligodendroglia" | `not reached`, all cells empty; the IT28 P3 HDAC5 batch holds no oligodendrocyte content | Explicit gap written by the reader of the principal case |
| `p3_B/evidence_it29_B.tsv` B38, B39 | Only class IIa myelin datum: Schwann cell (PNS), P0-Cre Hdac4 deletion **plus** Hdac5 null; Hdac5 null alone has no phenotype (B39). `transfer_breakers` says "corepressor/scaffold loss; no CNS OL data found" | Double mutant, peripheral, scaffold not catalytic; a catalytic inhibitor of one paralog is a different perturbation |
| Receipt `FTR-20261105-29472387-06` (`fulltext_receipts.py status --pmid 29472387`) | `partial_fulltext_read`: Introduction, Results of the double mutant read; **Methods, Discussion, figures, tables not read** | The decisive genotype table (Hdac4 alone? timing of Cre?) is unread |
| `generation_it22_p1_20261103/decision_scope_it22.tsv`, rows for `IT21P2-0006` (nanatinostat), `target:HDAC5` | IT28 text "HDAC4 and HDAC5 are required for Schwann cell myelination (PMID 29472387), a counter-premise for a myelin rationale"; IT29 text adds class I rows and says "class IIa-selective compounds not covered" | The limit is carried at abstract level and is worded wider than its source (the source needs both paralogs deleted) |
| `inverse_it28_p8_20261105/reconstruction/README.md` row M5; `roadmap_current.md` Standing method (IT28 blind-reconstruction bullet) | Calls the HDAC4/HDAC5 myelin point an omission "closed by a class_limit row" | "Closed" means carried as text, not resolved |
| Task record `ORCH-ROADMAP-IT28-20261105`, challenge `CH-IT28-HDAC5-LEVER`, `reevaluate_when` | "any neural HDAC5 catalytic-dead data appear" | IT29 P3 B/D/E did not read any; condition not met, not examined for myelin |
| `phenotype_first_it29_20261105/SELECTION.md` | HDAC4/5 "needed for myelination (IT28 P3/P4)" | Cited sources do not contain it (see LOG #4) |

## Why this one (decision relevance)

1. Largest consequential asymmetry in the records: class I/pan-HDAC inhibition is signed **adverse** for oligodendrocyte maturation (P3-B B01, B03, B07-B10); class IIa is the one HDAC class where the sign for the CNS is *unknown*, and it is the class of the programme's lead thread and its only selective tool compound (TMP269, identity confirmed, `p11_tmp269/`). A wrong "adverse" would demote a lever on a PNS double mutant; a wrong "neutral" would hide a liability on the exact endpoint where WWOX-neuron-deleted mice are hypomyelinated.
2. It is **executable at zero spend** with open literature, unlike the protein-level ISR or WWOX-patient measurements that need new data.
3. It touches **both** cases: Case 1 signed table (an empty row for a class in the catalogue) and Case 2 (class IIa HDAC in neurons also appears in activity-dependent circuits).
4. It is **not a repeat**: IT28 P3 asked about SLC2A1 in muscle/neural cells (edge validity) and P4 about the ISR; neither read class IIa in myelin. IT29 P3-B explicitly left it.

Competing candidates I considered and set aside: (a) Wong 2018 pyramidal-activity dependence of PV/SST survival (P3-E E33/E34): strong lead, but the next step is a Wwox-specific measurement or a new experiment, not a literature read; (b) GSK3B/EZH2-inhibitor direction (P3-B: not reached): lower programme weight, no live proposal depends on it today; (c) pracinostat assay descriptions (mandate step P11): a pharmacology residue already queued by the operator's record.

## Done v new (step 2)

**Already done; not re-read** (cite only)
* Class I / pan / HDAC3 / PRC2 oligodendrocyte perturbations: `p3_B` rows B01-B16, receipts `p3_B/receipts/`.
* HDAC5 edge origin (muscle knockdown), class IIa scaffold-vs-catalytic in neurons (HDAC4 only), potency discordance: `batch_it28_p3_hdac5_20261105/` (receipts `FTR-20261105-22991226-*`, `-20139990-*`, `-29360358-*`).
* TMP269 structural identity: `p11_tmp269/README.md`.
* WWOX hypomyelination, add-back window, Mbp share: `glia_maturation_it14_p4_20261101`, `snrna_it13b_pv_20261031`, p3_C.
* Neuronal activity as modulator of myelination: p3_B B34-B36.

**New, justified by the new question**
* Re-read PMID 29472387 to completion (Methods, genotype table, Discussion) - a motivated re-read: `reread_reason new_question_outside_prior_coverage`, `prior_receipt FTR-20261105-29472387-06`.
* Any class IIa HDAC datum in CNS oligodendroglia (unreached by anyone).
* Any datum where class IIa deletion/inhibition in **neurons/axons** changes myelin, and where a class IIa **catalytic** mutant or selective inhibitor was used in a glial or myelin context (catalytic v scaffold).
* An adversarial search for evidence that class IIa inhibition is pro-differentiation or neutral for oligodendroglia (to avoid confirming the adverse reading).

## Breadth and stopping rule (step 3)

* **Three readers, three non-overlapping sub-questions** (system boundary: glia in CNS / the PNS source and catalytic-v-scaffold / neurons and the adversarial search). Fewer would put the PNS full read and the CNS search on one reader and risk a skim; more would duplicate because the literature on this specific question is expected to be small.
* **6 to 12 sources read per reader**; a reader stops when its sub-question is answered or the route is exhausted, and says which. No second wave is planned. A second wave opens only if a reader reports a decisive full text it could not reach, or two readers contradict on the same row.
* **A null is a result:** "no CNS class IIa myelin datum found after bounded search" is the expected modal outcome, and it has a defined consequence (see CONSEQUENCES below) so it does not read as failure.
* **Check on return** before consuming: `challenge_batch.py check`, receipts dry-run, and one recomputation of each reader's headline count from its TSV (IT23 verifier lesson). No independent verifier is launched unless the return changes a sign.

## Consequences fixed before the search (pre-registered)

| Return | Consumer action (the Orchestrator, step 5) |
|---|---|
| CNS or neuronal class IIa loss/inhibition **adverse** for myelination | Reword the `target:HDAC5` class_limit to the CNS source; add a signed row (class IIa, adverse) to the case-1 signed table; HDAC4/5-chain proposals carry the limit as a counter-reason, still no veto |
| **Null / neutral** in CNS | Keep the PNS-only wording explicit ("peripheral, double mutant, scaffold"); remove any generalisation to CNS from SELECTION-type text; the lever is not penalised |
| **Nothing found** | Wording becomes "not reached in CNS after bounded search"; the empty `HDAC4 / HDAC5 in CNS oligodendroglia` row stays and is dated |
| Class IIa **favourable** | Record as undetermined unless target-controlled; no promotion |
