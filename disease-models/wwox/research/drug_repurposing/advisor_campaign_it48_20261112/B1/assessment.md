## Response to the intended action

**Increment 1 (IT47-Q01 and Q02 on the GSK3 / eIF2B thread): I disagree with it as the first slot.** I would not drop it, but it should come second or be shrunk.

- **IT47-Q01 is not literature-executable.** `next_batch_it47_20261112/BRIEFS.md` B3 puts it in the wet block: "the catalytically dead epsilon in tissue with intact Gsk3b". `p4_gsk3/result_it47.md` line 15 shows the blind reader found no such arm in the one source it checked. Searching more papers can at most return a bounded "not found". Because that "not found" would come from a source set the reader and the package already covered, it would look like progress without changing any decision. It would also have to be written as a measure of reach, never as "no such arm exists".
- **IT47-Q02 is genuinely zero-spend.** `result_it47.md` line 16 records the state: "unvalidated" rests on abstract-level searches, and the DYRK2 requirement rests on one open full text in cardiomyocytes. A full-text pass can improve those two statements.
- **Strongest point for the intended action.** The thread has a pre-registered case and a blind reader. The reader's finding on E15 is already consumed on the card. A Q01/Q02 pass would therefore be cheap to integrate. This is better than my Stage A item on integration cost and on the certainty of finishing.
- **What Q01/Q02 can change.** Only the wording of two prerequisites inside INV-09. B3 already sends the decisive measurement, the baseline and the null H5, to the wet lab, which is not available. The result can sharpen a design that nobody can run now. It cannot demote the thread. The thread already has its next experiment re-ordered (`result_it47.md` line 12).
- **Why I keep the SCI43 item first.** The juvenile Ba²⁺-sensitive share, with its second route and a second reading of the eight rows, can remove KH1's magnitude from the whole K branch. That is a decision-level change, and Q01/Q02 is not one. The SCI43 brief is also the oldest unexecuted written brief.
- **If the Orchestrator wants to stay on INV-09, a refinement.** Run Q02 only, as a single bounded full-text task. Add the neuron/WWOX search for DYRK2 and a phosphomimetic via a second route. Leave Q01 as a recorded wet prerequisite, with its "not found" stated as reach. Fold both into the INV-09 card and GSK3-H1 only if the answer changes a prerequisite. This costs less than the full increment.

**Increment 2 (provisional): integrating IT47-Q04 into the IT46-Q04 two-lever design review.**
- This is a sound, small integration. `cell_context_sci47_20261112/README.md` §Verification item 2 states that the biological inferences behind it were never verified. It sits on the public page in five languages.
- I would therefore put the SCI47-B inference verification before the integration, or alongside it. Integrating an unverified OPC specificity control into a design review compounds the exposure.
- If the SCI43 item takes slot 1, the Q04 integration and the condition-record application (`S7_coda.md` §4) are the better slot 2. Between those two I prefer the condition record, because it serves four questions.

## 1 · Principal decision

Which two bounded increments the IT48 campaign should buy, and whether the intended INV-09 literature pass (Q01/Q02) should lead.

## 2 · Leading recommendation

My Stage A view is unchanged. Slot 1 is the SCI43 juvenile Ba²⁺-sensitive share, with the Kir2 drug-name route and a second reading of D01–D04, D07, D08, D11 and D13. Slot 2 is the condition record, or the SCI47-B verification followed by the Q04 integration. INV-09 Q02 alone is acceptable as a reduced slot 2 if the Orchestrator prefers to stay on that thread.

## 3 · Relevant alternatives

- **The intended action (Q01 + Q02).** It has the advantage of continuity and a pre-registered case. It is weak on decision value, because Q01 is wet in substance and Q02 changes wording only.
- **Q02 alone.** This is the achievable core of the intended action.
- **The Stage A alternatives.** The condition record, the SCI47-B verification and the unmapped hypothesis rows still stand. KH1–KH5 should be mapped after the SCI43 result.

## 4 · Why now

Nothing in the intended action ties it to the 24 h window. The SCI43 reopen condition has been outstanding for four iterations while its premise kept being used. Check for a SCI48 delivery before dispatch, to avoid a duplicate (memory file *check-integrator-before-queue-item.md*: SCI46 duplicated an IT46 package).

## 5 · Evidence and uncertainty

**Facts.**
- BRIEFS B3 lists Q01 as wet.
- `result_it47.md` lines 15–16 give the Q01/Q02 evidence state.

**Uncertainty.**
- I did not open the Q01/Q02 rows of `open_questions_map.tsv`. Their stated stop criteria might be narrower than the BRIEFS line suggests.
- Access risk for the SCI43 sources is unchanged from Stage A.

## 6 · Next bounded action

**Principal question:** the juvenile Ba²⁺-sensitive share of the layer II/III resting conductance, with a second independent reading of the eight rows.

**Result that would count:**
- a share table by family with its preparation fields and locators; or
- a bounded "not found" after two routes, written as a measure of reach.

Either result is then written into the KH1 disposition and the INV-18 `next_test` field.

## 7 · What would change my view

- If the map rows for Q01/Q02 show a source class not yet searched, for example a tissue dead-epsilon paper, Q01 becomes executable and the intended action gains.
- If the SCI43 sources prove unreachable by every permitted route, slot 1 collapses to the condition record, and the intended Q02 becomes the natural slot 2.
- A SCI48 delivery that covers the K-branch shares would remove the SCI43 item.

## 8 · Resource implications

- **Delegates.** One producer and one distinct verifier per increment, strictly sequential.
- **Spend.** Zero.
- **Integration.** Edits to the generator rows, investigations, hypotheses or ladder stale the generated dossiers. Run `build_questions.py --write` and the touched-folder suites before any battery. The browser tests need `CHROME_BIN`.

## 9 · Inspected

- **Stage B reads:** `generation_it47_20261112/p4_gsk3/result_it47.md` (full); `next_batch_it47_20261112/BRIEFS.md` (B3 and B5 lines only, via grep context).
- **Brief content:** the saved Stage A assessment and the intended action, as given in the brief.
- **Not opened:** the Q01/Q02 rows of `open_questions_map.tsv`; `prereg_it47.md`; `verify/VERDICTS.md`; the dashboard (not re-fetched). My Stage A inspection list carries over.

## 10 · Freshness and exposure

- **Exposure.** At Stage B I was given the intended action by design. At Stage A I had not opened it.
- **Staleness.** The grep showed `brief_B.md`, `B1/brief.md` and `A1/meta.json` as new files mentioning IT47-Q01..Q04. I did not open them. CI and Pages state remain unchecked.