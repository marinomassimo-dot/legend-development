# Round-3 cold read of the current text after the ADV-144 integration: comparison with the criteria fixed before dispatch (IT, 2026-11-21)

Reader: new cold reader, sonnet, effort high (read back with session_model_census.py: asked model sonnet, effort read back high x11); same model family as the producers, so no independence from the model family is claimed. It saw only the text (692 lines, 39 design-team answers, 67 OPEN-GAP, 13 CONFLICT-OPEN in the body). Its files are in this folder.

| Criterion (fixed before dispatch) | Result |
|---|---|
| 1. Every unanswerable question maps to a marker or an answer | NOT MET for 9 of 86 questions (no nearest marker): Q001 (what the bracketed notes are) and Q016 (replication stimulus against non-floor requirement) are the ones that block; Q003 to Q006, Q036, Q041, Q062, Q073 do not block. Q037 (one single figure for an application) and Q046 (pilot ages) are only partly mapped. |
| 2. No new conflict introduced by the integration | NOT MET: the reader lists 13 unmarked conflicts (C001 to C013). Placed next to older sentences by the integration: C001, C002, C004, C005, C007, C010, C013 (and C006, C017, C018, which the answers already flag but whose body sentences stand). Inherited from the older texts: C009, C011, C012. |
| 3. Governance unaided | MET: the reader states which text governs, what it replaces and where the earlier statements went, from the status box alone; it adds that the status of the bracketed notes is not defined (Q001, repaired). |
| 4. Blocking count (measurement) | 16 of 86 (round 2: 15 of 84; first read: 27 of 85). Definitions differ between the three readers; the ten that block now are doses (own regimen, owner laboratory and operator), contact route and terms, pilot ages and series size, a single animal figure, wild-type source, and the status of the notes. |

## Repair (dated, old text kept; script `repair_adv146_it_20261121.py`, checker rerun)
- Status box: new bullet defining the bracketed design-team notes and their statuses; the "no number is new" bullet now says that figures in the notes carry the status the note states; "stage" in a quoted note with a seizure meaning is a grade; a body reference to a numbered older line points to a text kept in the repository (C007, C011, C013, Q001, Q006).
- The stage-3 marker R2Q43 was inside the stage table: moved below it (Q005).
- New CONFLICT-OPEN markers, owner SCI: R3C01 (replication stimulus against the non-floor requirement), R3C02 (P11 as further age against the rule sentence), R3C04 (pilot ages P11 and P14 against the P12 to P17 window), R3C05 (E2 against the floor rule), R3C09 (75 litters), R3C10 (panel, unresolved age); new OPEN-GAP R3Q37 (single figure for an application).
- Not repaired, by choice: C008 (the 45 minutes in a note is a Cheng 2020 Methods statement per SCI's classification; the doses remain the gap already marked Q13 to Q15); C012 (group sizes of Cheng 2020; no effect on a run); C003, C014 to C016 are already partly marked; C006, C017, C018 are answered by notes whose neighbouring sentences are kept by design.
- Handed to SCI: the six new CONFLICT-OPEN and the one new OPEN-GAP marker above; and the ten numbers of the answers that are in no numeric_tokens column (see RECONCILIATION_ADV144_IT_20261121.md).
