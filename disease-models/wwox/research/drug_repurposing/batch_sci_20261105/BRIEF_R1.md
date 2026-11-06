# Brief R1 (label `sb-r1`): restoration after onset in syndromic neurodevelopmental disorder models

Read `BRIEF_COMMON.md` first; it binds. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/r1_restoration_ndd/`. Receipt `NN` = `24`. Scratch (downloads, outside the repository): `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/sb-r1/`. Your sibling `sb-r2` covers developmental and epileptic encephalopathy models, antisense or AAV approaches and human timing precedents; do not read their sources (check with `paper_packet.py claim`).

## Challenge `CH-SB-POSTONSET-RESTORATION` (task record `ORCH-SCIBATCH-DR-20261105`, part 1)

**Question.** In mouse (and, where they exist, other animal) models of neurodevelopmental disorders caused by loss or reduction of a single gene, when the gene's function is restored AFTER the phenotype has appeared, which endpoint classes recover, which do not, and what decides the difference? Endpoint classes, kept apart: survival; seizure or network hyperexcitability; motor; cognition and behaviour; neuronal structure (spines, dendrites, interneuron number); myelin and glia; systemic and metabolic. Every study is placed on the module's own vocabulary: **PREVENTED** (restoration precedes the endpoint's phenotype), **RECOVERED** (restoration follows a manifested phenotype and the endpoint moves toward control), **EARLY-WINDOW** (restoration precedes the measured endpoint but the onset of that endpoint was never located), **UNMEASURED**, **UNVERIFIED**; and as full, partial, none or worse.

**Decision at stake.** The investigation `INV-01` (rank 1: "does neuronal WWOX restoration started after symptom onset recover any endpoint, or only prevent one when given in the neonatal window?") and the work order `NEED-WWOX-GENE-ADDITION`. Every partial-benefit lever in the module is ordered as a bridge to, or a substitute for, restoration; the wet-lab arm is not available here, so the question is what the external precedents say about which endpoints can be expected to recover and under which conditions, and what the single added arm must therefore measure.

## Done: cite, do not repeat

* WWOX studies, prevented versus recovered: `disease-models/wwox/research/drug_repurposing/rescue_window_it6_20261029.md` (read it; its status vocabulary is the one above).
* Three leads of IT8 P5: `advance_it8_p5_20261029/loop2_broad_recovery/README.md`: Shank3 adult restoration (PMID 34253921; Methods and most figures not read), Meis2 (PMID 42587157), Csnk2b (PMID 42190665). Two of three show post-onset restoration of circuit or behaviour endpoints; Methods were not read. You may deepen these three only for a stated reason (set `prior_receipt`); do not count them as new coverage.
* Transfer-condition template for the myelin endpoint (IT29 P3-C) is on the branch `task/it29`: `git -C /home/desktop/legend-development show task/it29:disease-models/wwox/research/drug_repurposing/phenotype_first_it29_20261105/p3_C/README.md`.

## New work (hints only; verify every identifier in PubMed)

Primary studies in which a conditional or reversible allele, an AAV, or a pharmacological or genetic switch re-establishes the gene at a stated age relative to onset, in: Mecp2 (Rett) models; Ube3a (Angelman); Fmr1; Tsc1/Tsc2 and Pten (mTOR pathway; include pharmacological reversal at stated age); Syngap1; Cdkl5; Shank3 (one additional primary study beyond the module's lead). Prefer studies that report a structural or myelin or interneuron endpoint besides the behavioural one, and studies that state the age at which restoration stopped working (critical period).

For every study record: lesion class (null, hypomorph, dominant negative, gain of function); restoration mode (conditional re-expression, AAV, pharmacological, other) and age at restoration relative to onset; which cells were restored (all, neuronal, glial); follow-up time; the untreated same-genotype comparator; the readouts; and the authors' own statement of a limit (incomplete rescue, a critical period, a ceiling). Then add one counter-search: studies where restoration after onset failed, was partial only, or worsened an endpoint.

## Table

`evidence_r1.tsv` columns, in this order: `row_id, role, gene_model, disorder_class, lesion_class, restoration_mode, cells_restored, age_at_restoration_vs_onset, endpoint_class, endpoint_detail, status_vocab, outcome, follow_up, comparator_and_controls, cell_autonomy_stated, authors_stated_limit, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`. `age_at_restoration_vs_onset`: pre_onset | at_onset | post_onset_early | post_onset_advanced | adult | not_stated. `outcome`: full | partial | none | worse | not_measured. `status_vocab`: PREVENTED | RECOVERED | EARLY-WINDOW | UNMEASURED | UNVERIFIED. `role`: support | counter | context.

README addition: a matrix of endpoint class by restoration timing with counts of studies (not a meta-analysis; state publication bias and that models differ), then a section "What the added arm of `INV-01` must measure, given these precedents" in at most 10 lines labelled IPOTESI, and a section "Conditions under which these precedents do not transfer to the neuron-restricted, short-lived, hypomyelinated Wwox null".

## Consequences fixed before you search

| Return | Consumer action |
|---|---|
| structural or myelin endpoints rarely recover after onset while circuit or behaviour endpoints partly do | the "prevented versus recovered" split in `NEED-WWOX-GENE-ADDITION` gets an external-precedent line; the INV-01 added arm is worded per endpoint class |
| at least one well-controlled model shows myelin or interneuron structure recovering after onset | "recovery of structural endpoints after onset is not excluded" is recorded with that source and its conditions |
| recovery depends on a critical period stated by the authors | the period and its anchor become a transfer condition for the timing of the added arm |
| nothing reachable for an endpoint class | stated as UNMEASURED in the matrix with the queries |

Breadth: 8 to 12 sources read at full text. Stop when answered or exhausted and say which.
