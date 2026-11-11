# IT45 P5: four conditions on the executed cases (protocol, then figures)

Non-canonical working note. Not medical advice. No predictive or clinical superiority is shown or claimed: the biology is unvalidated, and a known control is coverage, not discovery.

## Protocol (how to count; written when the S10 and S12 reads already existed, so it fixes the counting, not the outcome)
Cases executed with all four conditions: **S10** (KEAP1/NFE2L2), **S3-Kv7** (the P3 lever case, relation S3 of IT44), **S12** (Kir4.1 buffering). Same inputs per case: the held catalogue cache and the relation row of that case.
* **C1** simple target search: ChEMBL curated mechanism rows by symbol (distinct parent molecules).
* **C2** plus the curated interaction table (GtoPdb) **and** the dose-response activity rows (IC50, EC50, Kd, Ki; Potency read separately and not used here), counted as molecules with a catalogue status.
* **C3** plus qualification: relational verdicts, entity roles (`unclassified` is not `candidate`), comparison tiers and the independent reader's corrections where one was run.
* **C4** plus the contextualised combination: the lever joined to the cell class where the phenotype was recorded, with discriminating results written before the join.
Measures, separately: coverage; identities resolved and unresolved; premises resolved (read in a source and checked) against premises still open; hypotheses formulated; opportunities missed by C1 and recovered by C2; false proposals avoided; change of the next experiment (a stated difference between the experiment C1–C2 would name and the one C4 names); observable cost.
Independence: S10 premises were read by a separate reader (`verify_s10/VERDICTS.md`; 3 of 8 papers in full). S3-Kv7 expression rests on the SCI44 coda, scored by its own producer. S12 has no independent check. The engine's rules and this scorer share facts; the scorer is not an independent truth.

## Results
| Measure | S10 (KEAP1/NRF2) | S3-Kv7 | S12 (Kir4.1) |
|---|---|---|---|
| C1 mechanism-table molecules | 5 | 7 (IT40 mechsearch, 2 openers offered) | 0 (no Kir4.1 enhancer row) |
| C2 molecules with a catalogue status (mechanism + interaction + dose-response) | 14 from tables (IT43) + 7 only from the activity read = 21 | 7 from the mechanism path + 4 only from the activity read (IT44) | 0; 6 activity rows, none with a catalogue status |
| Identity | 10 activity-read molecules carry a catalogue status; 1 is a tool probe without a name; the acid and the methyl ester of one triterpenoid are two structures, not merged | the activity path found one opener (azetukalner) and one withdrawn-class opener (flupirtine) the tables missed | KCNJ10 resolved; KCNJ16 `NO_TARGET_FOR_ACCESSION` (unresolved, a state) |
| Premises resolved / open | resolved: 8 statements corrected or confirmed by reading (see `s10_dose/result_it45.md`); open: NRF2 in a WWOX neural system, neuron/astrocyte data (none) | resolved: cell-class substrate (RNA, P7 mouse); open: Kv7 current at rest, expression at P13–17, whether bursts are intrinsic | resolved: no activator row in the held data; open: Kir4.1/Kir5.1 function in Wwox astrocytes |
| Opportunities missed by C1 and recovered | 7 catalogue-status molecules (the IT44 read listed none: Potency flood) | 4 | 0 |
| False proposals avoided | 1 wrong-target row (a BET inhibitor listed on KEAP1); 1 weak control (the only catalogued NRF2-lowering row lowers general protein synthesis); 197 default rows no longer `candidate` across S1–S13 | quinidine row is an IC50, not an opener row | none |
| Hypotheses formulated | 1 conditional comparison, experiment rewritten (genetic arm, knockdown control, target-gene readout) | 1 conditional lever with 5 discriminating results (R1–R5) | 0 pharmacological; 1 measurement question |
| Next experiment changed (C4 against C1–C3) | yes: IT43 named a compound-with/without-inhibitor-tool design; IT45 replaces the inhibitor tool by knockdown and adds a non-covalent binder, with NQO1 alone ruled out as a readout | yes: C1–C3 offered a Kv7 tool arm or abstention; C4 adds Ba2+/Kv7/Ih difference currents first and an opener only against an equal current-injection hyperpolarisation | no (the lever is empty; the question becomes a measurement) |
| Cost observed | dose-response read 1 min 32 s; reader about 218k tokens, 67 tool calls, about 10 min | no new read; join from held files | read under 1 min; no reader |

## What this does and does not show
* The activity path with the dose-response types read alone recovers molecules the table path cannot; reading the primary documents then **removed or demoted** several of them (one wrong-target row, one weak control, a failed "same assay" premise). Coverage rose and the number of defensible hypotheses rose less: that is the honest relation.
* The combination (C4) changed the next experiment in two of three cases and, in the third, correctly returned "no lever". That shows it distinguishes cases; it does not show that any biological premise is correct.
* Not shown: a better prediction, a new favourable compound, or that the C4 gain would persist on a case chosen by someone else. Three cases, chosen by the same session.
