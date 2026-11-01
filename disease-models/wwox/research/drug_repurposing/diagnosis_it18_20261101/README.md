# IT18 P0 — diagnosis of the effective capability (2026-11-01)

Non-canonical research material; not medical advice. Baseline checked at the start of IT18 (fetch of the canonical remote): `main` = `development/main` = `82e795d4`, CI of `82e795d4` and of the code commit `10a3d746` both success, one worktree, no active job, IT17 mandate COMPLETE, crontab holds the daily push check, the 05:20 UTC radar and the hourly mandate watch. Same question as IT16: along *WWOX knowledge -> question -> usable data -> method -> hypothesis -> comparison -> next verification -> queue*, what runs, what was measured as an advantage, and what still lacks a validation. This table supersedes `../diagnosis_it16_20261101/README.md` as the latest diagnosis; rows IT17 resolved are dropped, not re-opened.

| Stage | Declared | Implemented | Executed | Advantage measured | Validation missing |
|---|---|---|---|---|---|
| Radar questions | R9 | plan derived from priority surfaces (IT17) | yes, tests and one bounded real run | none beyond tests | the plan produced 0 questions from reopen conditions on the real repository: the CURRENT section links one package README, while the conditions are kept in `reopen_searches*.tsv` and `decisions.tsv` tables that nothing read (cause verified in IT18 P1.1) |
| Radar queries | R9 | key terms by word frequency plus a category anchor | yes | none | queries such as "epilepsy attributed" name no object; pertinence of hits never rated by someone other than the author |
| Compound-target-action | R2/R5 | ChEMBL curated action carried by the catalogue; direction check against GtoPdb (IT17: 923 of 926) | yes | agreement 0.997 on the covered space | six discordances unresolved at source; 83 percent of module mechanism pairs have no independent counterpart |
| Matching (need -> compound) | R5/R6 | cards and ranking pilot use "documented action direction" | yes | none: no comparison of the contextual path against a target-only search | whether the WWOX need direction separates compatible, opposite and indeterminable compounds better than target-only search; only 3 of 23 needs state a direction (down), the rest are uncertain |
| Hypothesis generation | R6 | target-first Q-A/Q-B (IT15) | yes | WWOX contribution counted (IT15 P6) on four edges already in the external network | no test that the WWOX input adds information a target search lacks |
| Evaluation | R3/R7 | sealed freeze 2026-11-01T16:54:06Z, outcome semantics | freeze only | none | no post-freeze outcome exists; nothing predictive can be scored yet (an observation over time, not a task) |
| Catalogue use | R2 | catalogue, reconciliation tables | yes | none | no funnel from source records to identity-resolved to method-usable to evaluated compounds; vigabatrin assertions not recoded in IT17 |
| Presentation | R10 | full view + shareable edition | yes (local) | none | site not online (reserved operator act); direction and abstention not yet visible in the view |
| Continuity | R12 | router row to the Standing method, mandate watch | yes | one fresh actor reached the method in IT17 | the follow-up chosen by a fresh actor concerned reachability, not a module gap |

Principal bottlenecks by decision they block: (1) which compounds a need should propose cannot be said to be better than a target search; (2) the radar has not been shown to find the objects the open conditions name; (3) catalogue availability is a count of records, not of usable evaluated compounds.

## Questions chosen for IT18

1. **Matching.** For a fixed compound universe and fixed information, does the WWOX need context (declared direction on the intervention targets, abstention where the direction is uncertain) separate compatible, opposite and indeterminable compounds better than a target-only search? Reference: independent curated pharmacology, scored as pharmacological compatibility, not as benefit. Design: `../matching_it18_p4_20261101/PRE_REGISTRATION.md`.
2. **Radar.** Do the reopen conditions the module already records generate verifiable questions, and do queries that name the technical object retrieve more pertinent, usable hits than frequency-word queries? Rated by an actor other than the author, denominator kept (`../radar_it18_p1_20261101/`).
3. **Catalogue.** How many of the catalogue's source records are, per stage, identity-resolved, usable by the matching method and actually evaluated, and which of the six IT17 discordances changes a card or a match?

The radar is a means for 1 and 3: its questions come from these gaps.
