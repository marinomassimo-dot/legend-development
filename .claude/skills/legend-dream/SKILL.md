---
name: legend-dream
description: Light "dream" pass over recent work — reconsider what a session or batch changed, make the lessons findable, look for connections nobody has used, and check that results reached what should consume them. Runs from legend-session-self-eval when something material changed (a verified result, a corrected premise, a changed limit, a repeated error, a resolved question), and on request ("dream", "riconsidera", "collega", "cosa non è stato consumato"). Ends in one line when nothing changed. Uses the active agent only; no service, no spend, no gate.
---

# legend-dream — reconsider, connect, deliver

A pattern, not a pipeline. It reuses the self-evaluation, the discovery ledger, the open-questions map, the shared recipes and the consumer notes that already exist. It adds no registry, no gate, no authority and no schedule. If it ever stops earning its place, remove it (last section).

## When

* **From the session close**, inside `legend-session-self-eval`, after Part 1 and before `legend-capability-scout`: run it only if something material changed — a verified result, a premise corrected, a limit that moved, an error that recurred, a question that closed and can influence other work.
* **On request**, during a session, by name: `legend-dream`, or the helper below.
* **Not** on every answer. Start with `python3 framework/scripts/dream_pass.py quiet --since <ref or date>`; if it prints `quiet:` and you know of no material change, end with one line and write nothing.

## Helper (selects inputs; decides nothing)

```bash
python3 framework/scripts/dream_pass.py consumers --since 2026-11-05   # new research folders and who cites them from outside
python3 framework/scripts/dream_pass.py pointers                        # unsent drafts / operator hand-offs and files naming the same accession without the draft
python3 framework/scripts/dream_pass.py pairs GENE_A GENE_B             # lines naming both, verbatim, table header above each hit
```

`quiet` reports uncommitted changes under its path and says it checks only that path; a git error exits non-zero and is never read as "nothing changed". `pairs` cuts long lines at `--width` and marks how much was omitted with `file:line`; read the full line (`--full`) before relying on a context or a limit.

A folder nobody cites is a place to look, not proof it was ignored (a ledger event or a view may consume it). A co-occurrence orients retrieval; it has no sign and no count is evidence.

## Three ways of reasoning in one pass

**1. Operational memory.** For each lesson or surprise, name the cause before acting: *not kept*; *kept but hard to find*; *found but superseded*; *correct and available but not acting*. Remedy accordingly — a pointer from where a searcher starts, an executable recipe row in `framework/scripts/README.md` §13, a dated correction line (never an edit of history), or a change in the consumer. Put it in the shared home that already exists. Do not copy transcripts and do not lengthen the startup context. A test that includes the private memory index is not a test of the repository.

**2. Connections.** From the results and open questions of the pass, look for: an alternative mechanism; a need linked to a target or intervention; a hypothesis reopened by a changed premise; a pharmacological comparison; a shared uncertainty that is one question for the next batch; an experiment that separates rival readings. Looking beyond the WWOX keyword is allowed if the transfer is stated as a transfer. A new connection is stored as an exploratory lead: `discovery_lead.py check`, `stage --actor <you>`, and `append <spec> --apply` on `main` (tag IPOTESI, with source rows, context, falsifier and transfer limit). It is never a claim and never changes a need, a card or a direction by itself. Do not use citation frequency, graph closeness or number of links as support. An untyped relation may steer retrieval; it does not carry a pharmacological sign or a causal link.

**3. Consumption.** For each result that should have changed something, name the consumer — a need or premise, an open question, a catalogue search, a lead disposition, a comparison or experiment, the choice of the next batch — and show the sentence that proves it was updated. If it was, say so and stop; do not invent a defect. If not, repair the missing hand-off in the existing loop (consumer note, open-questions row, Orchestrator message); do not open a second loop. The Orchestrator keeps the choice of priorities within the operator's mandate.

## Keeping sources, readings and priorities apart

Receipts and historical evidence are not rewritten to fit today's reading; a reading may strengthen, weaken or change context and keeps its provenance. A newer note does not win because it is newer; an older conclusion does not vanish because it is rarely recalled. The same evidence repeated is one origin, not independent confirmations. A derived index must be rebuildable from sources and recognisable as derived; never remove a mandatory scientific link through one. Contested scientific meaning goes to the existing roles and checks, not to this pass.

## Output and cost

* Record only what a reader needs: what changed, which consumer, which pointer was added, which lead was staged, what stays open. A few lines in the session evaluation or the consumer note is enough; a dated `Update` line goes at the foot of an existing note.
* State the model and effort of any delegate, read back afterwards (`delegation_budget.md`); one delegate at a time; no recursive agents, no review battery. A bounded independent check of what decides the result is enough.
* Report measured cost from `framework/scripts/session_model_census.py` apart from estimates; never convert tokens into a share of a plan.

## Change or remove it

* Tighten or loosen: edit this file; the helper is `framework/scripts/dream_pass.py` with its test `test_dream_pass.py`.
* Turn it off: delete the "Dream pass" step in `.claude/skills/legend-session-self-eval/SKILL.md` and the two router rows (`CLAUDE.md` §2, `SKILLS.md`). Nothing else depends on it. Leads it staged remain valid ledger entries.
