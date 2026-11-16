# I2 per-child re-extraction: rubric v1 (frozen before extraction; IT; non-canonical; not medical advice)

Written for: the delegate that extracts, and the second readers (SCI, ADV, HE) who attack the result. Reference genotype class only. Mechanism labels only; no dose, no recommendation. Frozen by commit and by digest of this file BEFORE the delegate is launched.

## Question the table must be able to answer (declared first)
Does response to a treatment, and worsening on it, segregate by SEMIOLOGY and AGE rather than by genotype? Two circuits are hypothesised (I2): an early spasm / NMDAR-high window, and a later rebound-type absence-like / myoclonic phase. The rubric therefore records, per child, the ordered course of seizure types with ages, and per exposure the semiology and age AT EXPOSURE.

## One row per (child, exposure). A child with no treatment named still gets one row (agent = none).
Columns (TSV, header exactly): report_id; child_label_as_printed; sex_as_printed; genotype_class_as_printed (verbatim variant class words, e.g. biallelic null, missense; no reinterpretation); onset_age_as_printed; onset_age_months (number or blank); semiology_at_onset (closed list below, may hold several separated by `|`); semiology_at_exposure (closed list, only what the text states for that time window; `not_stated` otherwise); age_at_exposure_as_printed; age_at_exposure_months (number or blank); agent_as_printed; mechanism_class (closed list below); status (tried|added|continued|stopped|not_stated); seizure_outcome (resolved|partial|none|worsened|not_stated); worsening_statement (sentence verbatim; empty unless the text says seizures or the course got worse after or during the agent; a failure to respond is NOT a worsening); worsening_semiology (the seizure type that got worse, closed list, else blank); development_outcome (improved|unchanged|worse|not_stated); locator_outcome (verbatim quote with file name); locator_semiology (verbatim quote); locator_age (verbatim quote); co_therapy_at_the_time; attribution (single_agent|polytherapy_not_attributable); notes.

## Closed lists
semiology: epileptic_spasms; infantile_spasms_unspecified; tonic; myoclonic; absence_or_atypical_absence; focal_motor; focal_other; generalized_tonic_clonic; febrile; status_epilepticus; neonatal_seizures; seizures_unspecified; not_stated.
mechanism_class: sodium_channel; t_type_calcium; sv2a; ampa_antagonist; nmdar_pore_blocker; glun2b_nam; gabaa_pam_non_benzodiazepine; benzodiazepine; gaba_transaminase_inhibitor; kv7_opener; carbonic_anhydrase_multi; valproate_type; steroid_acth; ketogenic_diet; cbd_fenfluramine; other_named (name it in notes); none.
Classing rule: assign the class from the agent's name by the usual primary mechanism; where one agent has two primary mechanisms (for example a sodium-channel agent that also has other actions) use the first listed in the closed list and say so in notes. Do not invent a class for an unfamiliar agent: use other_named.

## Rules written first
1. Read only the 16 bundle files; no web, no PubMed, no prior tables of this repository. A child described only in an abstract is extracted at abstract level and marked `abstract_only` in notes.
2. Every non-blank value that is not `not_stated` carries a verbatim locator. No inference: an age is blank unless printed; a semiology is not_stated unless the text names it. Do not convert words such as "early" into months.
3. Worsening is recorded ONLY from a statement in the text; never from relapse, loss of effect or a switch of agent. Where the text says worsening without naming the seizure type, worsening_semiology = seizures_unspecified.
4. A child that appears in two reports is two sets of rows with a note naming the possible link; do not merge.
5. A grouped table row is not a child: record it in a separate file `grouped_rows.tsv` (report_id, row as printed, what it covers) and do not count it.
6. Case reports favour successes; record every statement of failure and worsening with the same care as successes.
7. Deliver also `children.tsv` (one row per child: report_id, label, sex, genotype class, onset age as printed and in months, ordered list of semiologies with ages as printed, number of exposures) and `counts.tsv` (children; exposures; exposures by mechanism class; children with at least one worsening statement; children with a stated onset age; exposures with both a semiology_at_exposure and an outcome).
8. Report in the hand-back: the number of children, the number of exposures, what could not be extracted and why; list any place where the bundle made a column impossible.

## Pre-declared analysis (fixed before the table exists; IT runs it, not the delegate)
A. Feasibility: the segregation question can be addressed only if at least 10 exposures carry both a stated semiology_at_exposure and a stated outcome (resolved|partial|none|worsened) for the same mechanism class or class group; otherwise the result is "the held reports cannot answer it" and the output is the observational design (D5c), not a conclusion.
B. If feasible: contingency of outcome (benefit = resolved or partial; no-benefit = none; worsened apart) by semiology group (spasm group: epileptic_spasms, infantile_spasms_unspecified; rebound group: myoclonic, absence_or_atypical_absence; other) and by class group; report counts only below n = 10 per cell, no percentages, no test claimed below that size.
C. Aggravation: list every worsening statement with class, semiology and age; do not net against benefit.
D. A first look at whether response is a function of age at exposure (months) inside one class; counts, no model, if n < 10.
E. What would count against I2: outcomes by class that are the same in both semiology groups where the cells are filled; or semiology at exposure not distinguishing any pair of children in the table (all spasms).
F. Disclosure: the same 14 reports were extracted once before (sealed table of 206 rows, sha256 9defc654...); that table is not shown to the delegate and is compared only after this extraction is frozen.
