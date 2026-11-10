# IT44 P5: comparison of the engine with simple alternatives, protocol fixed before the figures

Non-canonical working note. Written 2026-11-10 before `eval_it44.py` is run; later changes are dated addenda. No predictive validation exists or is claimed. Known controls are coverage, not new data.

## Cases and conditions (same inputs per case)
Cases actually executed with all four conditions: **S3** (Kv7), **S9** (PDK), **S10** (KEAP1/NFE2L2), **S11** (resting K+ openers). Conditions: **C1** simple target search (ChEMBL curated mechanism rows by symbol); **C2** plus the curated interaction table (GtoPdb); **C3** C2 with the relational qualification (verdicts CANDIDATE / UNKNOWN / EXCLUDED) and the entity roles of `entity_roles.py`; **C4** C3 plus the by-target activity pointers (catalogue-status molecules with an OK read state) and, where one was written, the conditional comparison that the generative relation produced.

## Measures, separately
1. **Coverage:** distinct molecules (merged by catalogue parent; labelled forms dropped) in C1, C2, C4.
2. **Identity:** molecules with a catalogue identity (ChEMBL id joined) and, among C4 pointers, those that are a salt/acid/stereo form of a molecule already in C2 (reconciliations, not new molecules).
3. **Opportunities recovered:** C4 pointers not in C2, split by catalogue status (approved, clinical, tool).
4. **Errors introduced or avoided:** E1 direction, E2 site class, E3 subunit transfer (IT42 scorer rules, copied) in C2 versus C3; role errors (ions or endogenous agents shown as drug candidates) in C3 versus the IT43 shortlist; pointers shown as favourable (must be 0).
5. **Hypotheses formulated:** conditional comparisons written (premise, discriminating measure, what moves it); abstentions kept.
6. **Change of the next experiment:** a stated difference between the experiment the case would have named from C1-C2 alone and the one named after C4.
7. **Cost and time:** observed API pages and seconds of the activity path for one fresh read; qualification milliseconds.

## Independence
The decisive premises of S11 were checked by a separate blind reader (`verify_s11/VERDICTS.md`); S3, S9 and S10 premises rest on IT42/IT43 readers. The scorer shares facts with the engine for non-decisive rows; it is not an independent truth. No graph step is used, so no graph baseline or decoy control is added.
