# DREAM-1: does consolidated experience change what a fresh session retrieves and does? (2026-11-08)

Non-canonical research material, descriptive notes only. Not medical advice. Zero spend: the Dreams service was not used; delegates ran inside the existing session quota. No ledger, scientific current file, role, authorisation or gate was changed. Pre-registration: [`PREREG.md`](PREREG.md) (commit d21d9900, before any run).

## Answer first

**Verdict: SIMPLIFY.** What LEGEND now reuses: three concrete recipes that existed only as one-line hints (how to copy the checkout for the release battery without letting a test write back; how to measure a vector figure instead of calling it unresolvable; what to do when the permission check refuses a cleanup, and what never to add), and one corrected note (six receipts a consumer note still called "staged" are in the ledger). A fresh session that had these answered completely on 29 of 30 required points; one without them, on 23 of 30. The decision it proposed and its operational result were right in both conditions on all 8 cases, so the gain is in completeness and cost on the three targeted cases, not in avoided wrong actions.

The six-row consolidation I first wrote was cut to the three rows the test showed useful. The other three (pipe exit codes and stream order; `grep` is `ugrep` here; what a research package must not track) were not tested and are not kept in shared text; they stay in the private memory.

## Diagnosis: which of the four problems

| Problem | What was found |
|---|---|
| 1. Not saved | Not the main problem. My first check (fixed-string search of normative files) said six lessons had no shared copy. The delegates then found shared homes for three of them under other wording: the vector-figure route in the scientist standing brief M2 and `paper_packet.py rank`, the battery clone in the module README, and the refusal in the operating convention. The check was too narrow, and the "not saved" count was wrong. |
| 2. Saved but hard to find | The real gap for those three: the pieces were there but the recipe was not (no `get_drawings` step; the clone appeared only inside a skip note; the convention says removing one's own clean worktree is ordinary while the permission check can still refuse it). |
| 3. Found but out of date | One note: a consumer note listed six receipts as "to record (staged)"; all six had been in the ledger (one event each). Both conditions reached the right action by checking the ledger; the note now says so (dated line, not an edit of history). |
| 4. Correct and available but not used | One case: an unsent draft request for the closed accession E-MTAB-14792 exists in the module; **neither condition found or cited it** (D3). Re-check status, no bypass and no e-mail were right in both; the hand-off to the operator was missing in both. This is the clearest unused-relation finding and is not fixed by this consolidation. |

Not every error was memory: the wrong "not saved" count was a retrieval error of mine.

## Before / after (8 cases from real incidents; k1 = current organisation, k2 = consolidated)

Blind grading by a separate context that saw only the question, the rubric and the answer (no condition, no transcript). Retrieval is counted mechanically from the transcripts.

| Case | Kind | Content points present and right (k1 / k2) | Anchor reached the context from repo files | Action and result |
|---|---|---|---|---|
| D1 token figures | control | 4/4 / 4/4 | both | right / right |
| D2 receipts "staged" | stale note | 4/4 / 4/4 | both (ledger) | right / right |
| D3 route failed | control | 3/4 / 3/4 | neither found the unsent draft | right / right |
| D4 figure "unresolvable" | targeted | 1 of 3, 1 partial, 1 absent / 3/3 | k2 only | right / right |
| D5 battery copy | targeted | 2 of 4, 1 partial, 1 absent / 4/4 | both | right / right |
| D6 refused cleanup | targeted | 2 of 4, 1 partial, 1 absent / 4/4 | k2 only (`"${VAR:?}"`) | right / right |
| D7 bridge relation | control | 4/4 / 4/4 | both | right / right |
| D8 misplaced artefact | control | 3/3 / 3/3 | both | right / right |

Totals over 30 required points: k1 23 present, 3 partial, 4 absent; k2 29, 0, 1. Action acceptable and result right: 8 of 8 in both. One qualification missing in k1 (D4: the single-reading caution). Controls and the stale note: no difference in content.

## Cost, observed (census of the transcripts) and estimated

All delegates: `legend-delegate`, model `sonnet` and effort `medium` read back for every run, born at 16.7k to 17.1k tokens (the general-purpose delegates of the System One pilot were born at 39.7k). Totals for the 16 runs: 63 turns, 20,600 output tokens, 1,123,616 cache-read tokens, as logged, not converted to any share of a plan.

| Group (8 or 3 or 4 runs per condition) | Output k1 / k2 | Cache read k1 / k2 | Turns k1 / k2 |
|---|---|---|---|
| all 8 cases | 11,985 / 8,615 | 713,026 / 410,590 | 38 / 25 |
| targeted D4 to D6 | 4,492 / 2,447 | 239,873 / 94,884 | 14 / 7 |
| controls D1, D3, D7, D8 (same content in both) | 5,986 / 5,112 | 406,609 / 271,130 | 20 / 15 |

The controls differ by about a third in cache read with no change of content, so a large part of any cost difference is run-to-run variation, not the consolidation. Observed: the targeted cases were cheaper with the pointers. Estimated, not observed: any saving in a real session; the cost of writing and maintaining the consolidation in the main session was not separated from the rest of the work. One grader run was added.

## What changed, and what was removed

* `framework/scripts/README.md` section 13: three rows (battery copy, vector figure, refused cleanup), each with date, evidence and limit, and each pointing to the existing home first. No new file, registry, wiki, schema or gate.
* One dated correction line in `gsk3_eif2b_20261107/CONSUMER_NOTE.md`. The ledger was not touched.
* Removed after the test: three of the six rows first written. Nothing in the startup context was lengthened.

Maintenance cost: three table rows to re-read when a normative file changes the battery, the clone or the refusal rule; re-test with this folder's cases (`cases.json`, `collect.py`) if a row looks unused.

## Scientific distinctions kept

No claim was promoted or narrowed. The notes describe procedures, not findings. Preserved in the answers and in the new text: a 403 is not absence; a single reading is not adopted as a value; a raster panel stays raster; a bridged relation is a hypothesis with no sign; a refusal is not permanent but only the operator's authorisation lifts it. No new scientific hypothesis arose from the consolidation, so nothing was handed to the queue.

## Limits

* **The memory index reached every delegate.** The session's private memory index is loaded into delegate contexts whatever the instruction says (one delegate said so; others cited memory notes). So condition k1 was not memory-free: the index lines already hinted at D4 to D6. The measured gain is the gain of a shared recipe over a hint, not over nothing, and it does not show what a runtime without the index would do. A cleaner test needs a delegate without that index.
* The cases, the rubric and the consolidation have one author; grading was blind and by a different context, but one grader and one model family. Eight cases per condition: one case is noise.
* Retrospective replay: the states are written after the incidents. No real resumption on a new activity was run.
* The System One pilot ran five general-purpose delegates in parallel, which departs from `delegation_budget.md` sections 2 and 4 (one delegate at a time; typed delegates born smaller). It changed no result there and raised its cost; disclosed here because that protocol was applied to this pilot.

## Candidates not kept, with a reopening condition

Pipe exit code and stream order; `grep` is `ugrep` here; third-party raw downloads in a research package. Reopen if a case from a real incident shows a session repeating one of them, or when a runtime without the private memory takes over work that touches them.

## Reproduce

`cases.json` (8 cases and rubric), `runs.json` (case, condition, delegate id), `transcript_probe.py` and `collect.py` (retrieval and census from the transcripts; they need the local transcripts, which are not in the repository), `results/` (runs, grading).
