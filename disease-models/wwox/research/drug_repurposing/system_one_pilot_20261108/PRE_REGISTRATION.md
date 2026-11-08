# Pre-registration: System One pilot, fixed before any model arm was run (2026-11-08)

Non-canonical research material. Not medical advice. Zero spend: no paid API, credit, cloud GPU or metered service. Task branch `task/system-one-pilot`, cut from remote main 85b2432b.

## What is frozen here

| File | sha256 |
|---|---|
| cases_state.tsv (what a chooser sees) | aa798d1f57e7177575b50e435bcf287e9676cc5830bb1f76a1c2f080e87ab46a |
| cases_hidden.tsv (classes, labels, typed facts, sources) | 27cb0075b9c23edc7b245e038aa92ed9ea631cfa68ca6fbb5fbcd53f5a1cf55f |
| arms.py (prompts, rule arm, scorer) | 16522110c6e124b1c2b2c5db026d9e3ff3cc7a42399e8572e58533c488f08840 |
| build_cases.py | 971b0e66be3d36e6cade9eb6100190e5fefde56eefbc048865df597ca5e570fc |

16 new decisions, states reconstructed from repository records as they stand at 2026-11-08, with minimal scenario framing where a record names no requester (N09: the colleague's suggestion; N13 and N15 and N16: the request itself). Outcome labels were written before any model arm ran. Labels are the author's judgement; a separate blind verifier (arm V) is run to show where the labels and an independent reading differ. The set is not a validation of any model, and the IT30 set is only reused as an initial control (separate step, not counted here).

Revision before freezing, disclosed: the rule arm B was run once on its own output before the model arms; two option classes (N08, N12) were changed from DECLARE to OTHER because they assert falsity rather than insufficiency, `known_in_repo` was defined as "a record that answers the question" and corrected for N12 to N16, and rule B's first branch no longer excludes blocked sources. No model arm had run.

## Arms

* **A** current behaviour: a fresh context chooses one letter or NONE with a short note, no scoring structure.
* **B** a simple relevant rule: B(facts) over typed facts written by the author (an upper bound: it needs someone to type the facts), B(keywords) over the state text only.
* **C** structured choice with the model already available: score each option 0-3, choose, NONE allowed, name the missing fact. Fresh context, no tools.
* **V** blind verifier: marks every option REASONABLE / WEAK / UNREASONABLE, several allowed, NONE_SUFFICIENT.
* **A', C'** the same prompts with the option order reversed and relabelled, to see whether the choice follows the position.
* **D** Rizzo Flow native decision API with abstention, run only after A, B, C are scored, in an isolated directory, on this host.

## Measures (counts, no composite score)

Per arm: pick inside the acceptable set (or NONE where no option was adequate); pick equal to the best option where one is named; dominated option picked (an option that repeats recorded work, overclaims or breaks a standing rule); NONE correct and NONE wrong; agreement between original and reversed order; whether the less familiar informative options (N05 open-copy search, N08 citing-paper reading, N10 single-row re-audit, N11 edge screen, N12 cause separation, N13 literature batch) are picked as often as familiar ones. Cost: tokens or characters sent and returned per arm, wall time, effort to prepare the inputs (author time and size of the typed facts), and for D: start-up time, peak memory, latency, CPU use and interference.

Observed saving and estimated saving are reported in separate columns.

## How the result maps to a recommendation (fixed now, not tuned later)

* **KEEP**: D shows a benefit over the best arm that needs no runtime (B or C) on decision quality or on observed cost of the whole flow, on this host, without disturbing other work, and it can be started on request and removed completely.
* **PATTERN ONLY**: structured choice (B or C) is at least as good as A with fewer repeated or wasteful picks, and D adds nothing measurable or costs more than it saves.
* **INCONCLUSIVE**: the 16 cases cannot separate the arms (ceiling or noise), or D could not be run in a form comparable to the others; record the cases and the reopening condition.
* **DISCARD**: structured choice or D worsens decisions or penalises informative options, or the cost exceeds the benefit.

No universal threshold. With 16 cases a difference of one or two cases is noise and is reported as such.
