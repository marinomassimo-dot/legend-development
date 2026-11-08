# Delegation budget — what a delegate costs, and how a secondary batch lives beside the main session

> **This file routes; it does not legislate.** It is the single home of the delegation settings.
> Scientific standards are unchanged and live in the normative files; nothing here relaxes a
> read depth, a verification or a gate. It adds no scheduler, no registry and no gate: a delegation is
> one line in the task record that already exists. Non-canonical, not medical advice.

**Why it exists.** The parallel batch of 2026-11-05/06 ran 21 delegates, every one at the maximum
effort the session happened to have, 3,400 turns, about 830 million cache-read tokens and 7.5 million
output tokens as first logged (`session_model_census.py --dir <subagents directory>`; the first census counted repeated
rows of one response several times, so these totals are about twice the real ones: see the reconciliation in section 6). Six of the twelve
delegates dispatched as `fable` ran no fable turn. Two account usage limits killed every in-flight
agent, and the main session shared the same account. The scientific yield was real; the shape of the
spend was not chosen by anyone.

## 1 · Settings are stated per delegation

The session's own model and effort bind the session. They authorise nothing for a delegate: an
Orchestrator on a high setting dispatches delegates on the setting the **role** below asks, and says it in the dispatch
(`model`, `effort`) every time. A delegate that inherits the session's effort was not configured.

| Role | Starting setting (revise from measured packages, not from habit) |
|---|---|
| map, census, mechanical extraction, table building | `sonnet`, effort `low` |
| producer reading sources into an evidence table | `sonnet`, effort `medium` |
| verifier (blind quote audit, delta audit), review of conclusions | `sonnet`, effort `high`, in a separate context that reaches the sources |
| decisive conclusion that a verifier could not settle | one escalation, §3 |

The `model` and `effort` parameters are requests. Read them back after the delegate returns (§6).

## 2 · Concurrency

One delegate active while the main session works. A second only when the capacity that day
justifies it, with the reason written in the task record. No recursive delegation: the brief says "do not
start agents". A resume (`SendMessage`) or an escalation is a launch and counts against the same limit.
After an account usage-limit notice, resume the verification and correction work first and drop the widening.

## 3 · Escalation is bounded and written down first

Before a dearer model or a higher effort is used, add to the task record one line: `ESCALATION`
with the difficulty to resolve (one sentence), the output expected, and the setting requested. An independent
review needs a separate context and access to the sources; a different model is an additional
choice, never an automatic requirement.

## 4 · Startup cost

A general-purpose delegate is born with about 40,000 tokens of context; a typed agent with a short
tool list (`wwox-scout`, measured 2026-11-06) is born with about 15,700. Dispatch scientific delegates
as `legend-delegate` ([`.claude/agents/legend-delegate.md`](../../.claude/agents/legend-delegate.md)), which carries
only the tools a reading package uses and loads this file and the brief by pointer. Point at files; do not paste them into the
dispatch. Reuse a verified artefact rather than rebuilding it, and verify a narrow correction narrowly
(the changed rows), unless a wider effect is argued in the record.

## 5 · Small packages to the end

One package at a time: production, verification, correction, delivery, before the queue is widened. Near
exhaustion of the account's capacity, finish the open package and write a `RESUME` line precise enough to
continue (what is done, the first undone file, the setting).

## 6 · Measuring what is observable

After each delegate: `python3 framework/scripts/session_model_census.py <subagents>/agent-<id>.jsonl`
and one line in the task record: role, asked model and effort, model and effort read back, turns, output tokens, cache
read, the file(s) completed. Tokens are reported as logged. They are not converted to a share of any
plan, and no additional spend is enabled to make a package fit.

**Reconciliation of the 7.5 million figure (2026-11-06).** A transcript writes one API response as several rows (one per content block) that repeat the same usage block, and the census summed every row. On 60 real delegate transcripts this gave 5.02 million output tokens against 2.57 million once each response id is counted once (2,855 of 6,272 rows were repeats). The census now counts a response once and keeps its largest output; the 7.5 million above is therefore an over-count by roughly a factor of two and the 3.24 million analysis is the nearer one. Cache read and cache creation were over-counted the same way. Rows without an id are not merged. Regression: `test_session_model_census.py`.

**Measured in IT32 (2026-11-07), each perimeter stated.** (a) The seven IT32 delegate transcripts (three translation jobs, two producers, two verifiers; census with the one-response-once rule): 156,382 output tokens, about 9.09 million cache-read tokens; for every one the effort and model read back equal the dispatch (sonnet; low or medium), birth context 17.5k to 18.1k tokens; the delegates' own statements about their effort were wrong twice, so the transcript is the source. Producers 38.5k and 38.4k output (35 to 39 turns), verifiers 18.9k and 26.3k, translation jobs 6.2k to 17.4k. (b) The coordinator is the main session transcript over all its days and iterations, not IT32 alone: 6,813 turns, effort read back `medium` on 6,799 of them, models sonnet 5.5 (6,334 turns), opus 5 (422), fable 5.1 (37) and others, 5.03 million output tokens: a coordinator can change model mid-run and the dispatch line cannot see it, so the census line is the record. (c) The NB-4 pilot reported its own perimeter (coordinator 27,688 output tokens at effort high, producer 32,487, verifier 66,561, total 126,736): a different session, different counts, not comparable with (a) or (b) and not a share of any plan. The verifier cost twice the producer there; the next two sections address that and wide retrieval.

**Which figure is output (2026-11-08).** The `subagent_tokens` figure in a delegate's completion notice is a total that includes context; it is not output tokens. IT34's blind verifier was reported as "about 40,000 tokens" and read as output: its transcript census gives 8 responses and 7,309 output tokens (birth context 18.5k, peak 38.6k, cache read 192k); more than half of the output (about 4,100 tokens) was writing the audit file and the final message, and the rest was tool calls; reasoning was a small share (three responses carried thinking). The cost of a proportionate verification is therefore mostly startup context and fetched text, not generation. Quote output from `session_model_census.py`, never from the notice.

## 8 · A verifier checks what decides, not the whole search

The verifier gets the decisive statements as (statement, source, locator) triples, not the producer's reasoning, and is asked to check: every proposition a decision rests on; every number that would change a decision; every inference, claim of absence and transfer of context (species, cell type, paralog, disease); and a declared sample of the simple non-decisive controls (say which rows and how many). It does not rebuild the retrieval. If the sample shows an error, the verification extends to that class (for example every quote of that source type); the decisive premises are never reduced to save cost. A correction of substance made after the review is checked again by the same verifier or another.

## 9 · A producer retrieves narrowly

Before reading hits, write the query list; group OR clauses and read the hit count first (a string with 225,128 hits is a query defect, not a search); check the receipt ledger depth before opening a PMID; stop at the first source that answers the stated question or when the route is exhausted, and say which. A failed or partial route is written into the receipt (see the common brief) and is not retried by another route without a stated reason.

## 7 · Not changed

Read depth, verbatim locators, blind audit, adversarial review, the receipt contract, §21c/§21d,
the release gate and the battery. A package that is cheaper and less verified is not a result.
