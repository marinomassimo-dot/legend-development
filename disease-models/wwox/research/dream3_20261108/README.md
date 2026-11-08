# DREAM-3 pilot — a generative Dream movement and its effect on a fresh searcher

Date: 2026-11-08. Actor: `plan` (Harness Engineering). Pre-registration (committed before the first run): `PRE_REGISTRATION.md`. Exploratory; nothing here is a claim about WWOX biology.

## What was added (small and permanent)

| Where | What |
|---|---|
| `.claude/skills/legend-dream/SKILL.md`, "Connections" | Starts from a recent result and reopens what it touches; movements offered, none required (link separate observations, rival explanation, premise that moved, reopen a dismissal whose `REVIVAL_TRIGGER` moved, a question common to several candidates, a discriminating measurement); the chain *sources → relation → rivals → question → measurement → consumer*; three labels (known-but-unused / new in the repository / novelty against the literature, checked apart); cause, compensation and consequence kept as rivals. Reuses `legend-discovery-method` primitives. |
| `dismissal_ledger_current.md`, entry on the `lde` growth premise | Dated UPDATE line: the "0 PubMed records" count is stale (4 records, none a measurement); trigger (c) still unfired; two other places carry the same unmeasured axis; the two GWAS lists are not a link. |
| `discovery_ledger_current.md` | Exploratory lead `DL-MECH-180` (IPOTESI, falsifier, transfer limit). |

## The case

Question given to a fresh `legend-delegate` (Sonnet, effort as set by the agent definition and not escalated, one delegate at a time), identical in both runs: *what is known and open about the IGF axis in WWOX-deficient animal models, and which single new measurement would be most informative?* Run A read a plain snapshot of `main` at 051d156b (before the Dream result); run B read a snapshot of the task commit (after). Both snapshots were made with `git archive` into a box from `owned_scratch.py --make`, with the pre-registration removed from B; the delegates saw no git history and no other path. Reports: `results/run_A_before_report.md`, `results/run_B_after_report.md`.

## Result against the pre-registered checks

| # | Check | A (before) | B (after) |
|---|---|---|---|
| 1 | Duplicate search avoided | ran the combined PubMed query and fetched metadata for three records | ran the same query once, compared the four PMIDs with the ledger's list, opened no abstract; a second query was malformed and discarded — a small saving, not a clear one |
| 2 | Qualifiers kept | yes (GH "not significant", n, GWAS lists as co-occurrence) | yes, same |
| 3 | Measurement discriminates | yes; three rivals, outcome table; says the weight-matched pair-fed control was "not fully designed" | yes; same rivals plus a weight- and feeding-matched control and a falsifier — but this is the lead's own wording, which B judged "sound": anchoring cannot be excluded |
| 4 | Stale item handled | found and flagged the stale "0" itself, without a date | read the dated update and confirmed today |
| 5 | No effect is valid | — | the controls (GWAS lists not a link; GH finding not re-searched) were passed by **both** arms |

Observed cost, from the delegate transcripts: A birth 17,611 tokens, peak 37,913, output 4,210, cache read 127,465, 8 tool calls, 41 s; B birth 17,892, peak 34,909, output 4,382, cache read 134,637, 9 tool calls, 41 s. No difference beyond noise. The cost of my own work in this pass is not separated here.

## Reading

The current path was already strong on this case: it found the dismissal, kept the qualifiers, named the rivals, refused the two misleading links and flagged the stale count. The Dream result changed one thing a reader can point to — the proposed control design (weight- and feeding-matched animals) is stated up front — and that change is the lead's content being adopted, which is a consumer reading the saved result, not evidence the lead is right. It saved no search worth measuring and changed no cost. The dated correction of the stale "0" is the one repair of a concrete defect (run A had to discover it undated).

## Limits

* n = 1 per arm; a single pair says nothing about reliability.
* The delegates read repository files, not the skill; the pilot tests what a Dream pass leaves behind, not whether the skill text makes a session reason better.
* Context isolation is partial: snapshots remove git history, worktrees and the pre-registration, but the delegate type still receives whatever instructions and memory index the harness attaches to every agent; the transcripts record only the user turns, not that preamble, and the first turn creates ~17.6k tokens in both runs. The private index lists nothing on growth hormone or IGF, so it is unlikely to have mattered here; that is an inference, not a proof. No session's memory was edited.
* Run B was told nothing about DL-MECH-180 yet found it, because the dismissal update points to it — the intended route — but this is also why B could anchor.
* Novelty against the literature was not assessed beyond one PubMed query; the lead claims none.

## Decision

* **KEEP** the dated update on the stale count and the exploratory lead (cheap, a real defect repaired, already in the existing homes).
* **SIMPLIFY** the skill claim: the generative movements and the chain stay as guidance, but nothing here shows that they improve results; do not add machinery for them. Re-test on a case where the baseline does not already succeed (for example a connection that no single file names).
* **DISCARD** nothing.

## Change or remove

Delete the "Connections" paragraphs added to `legend-dream` (they are self-contained), the dated UPDATE line in the dismissal entry, and `DL-MECH-180` (ledger entries are append-only; mark it `closed` with a dated line instead). `owned_scratch.py` is independent of this folder.
