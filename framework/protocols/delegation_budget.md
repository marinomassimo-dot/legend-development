# Delegation budget — what a delegate costs, and how a secondary batch lives beside the main session

> **This file routes; it does not legislate.** It is the single home of the delegation settings.
> Scientific standards are unchanged and live in the normative files; nothing here relaxes a
> read depth, a verification or a gate. It adds no scheduler, no registry and no gate: a delegation is
> one line in the task record that already exists. Non-canonical, not medical advice.

**Why it exists.** The parallel batch of 2026-11-05/06 ran 21 delegates, every one at the maximum
effort the session happened to have, 3,400 turns, about 830 million cache-read tokens and 7.5 million
output tokens as logged (`session_model_census.py --dir <subagents directory>`). Six of the twelve
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

## 7 · Not changed

Read depth, verbatim locators, blind audit, adversarial review, the receipt contract, §21c/§21d,
the release gate and the battery. A package that is cheaper and less verified is not a result.
