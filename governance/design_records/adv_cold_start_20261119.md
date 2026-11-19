# Cold-start test of the ADV host role, from the repository only (2026-11-19)

Non-normative record. Author: Harness Engineering (`plan`), requested by the ADV host. Tree examined: `development/main` at `d7d112948`, which already holds the host charter and `roles/advisor_practice.md` (commit `7703d73c8`).

## Question

A fresh session with no conversation history is told only that it is the ADV host and receives the 07:18 scenario of the earlier retrieval probes (no commit since 06:20; IT and SCI idle since about 05:38; MEETING at 05:25, next at 11:25). Does it assign instead of waiting, does it find the charter, the practice rules and the operator's standing guidance, and how many turns does it need?

## Method and isolation (declared)

`claude -p` in a clean detached checkout of main, model `sonnet` (claude-sonnet-5-5), effort medium, tools Read, Grep and Glob only, 30 turns maximum, no session persistence, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. Two prompts, one run each: **N** states the facts only; **W** adds the earlier conclusion "nothing to assign: roles in motivated wait" as a cue to wait. The prompts name no file. The only entry is the repository's own router (`CLAUDE.md`, "Acting as the ADV host" row), which the CLI injects as project instructions. Inherited and not removable: that router, the one-line language rule of the user-level instructions, the repository skills (available, not forced) and the model's training. Both runs answered the memory canary "no private memory visible". Commands and results: [`adv_cold_start_20261119_evidence/`](adv_cold_start_20261119_evidence/).

## Result

| | N (facts only) | W (with the "wait" cue) |
|---|---|---|
| Decision | assign now: SCI and IT, with content | assign now: SCI, IT, a conditional one to HE; rejects the earlier "motivated wait" explicitly as the failure of practice rule 3 |
| First file opened | `roles/advisor.md` | `roles/advisor.md` |
| Charter found, "Engine" clause applied | yes | yes |
| Practice rules found and applied | yes (rules 1-5, 7, 16, 20) | yes (rules 3, 4, 9, 14, 17, 20, 22) |
| Operator's standing guidance | seen only as cited in the contract and in `cross_session_transport.md` | same, plus the portfolio; the EMPATHY section and `mandate_continuity.py guidance` not read |
| §21c-§21e, roadmap, `CONTINUOUS.json` | not read | not read |
| Tool turns / calls | 5 result turns, 11 calls (CLI: 10 turns) | 5 turns, 13 calls (CLI: 13 turns) |
| Reported cost (notional under OAuth) | 0.13 USD, 291k cache-read tokens | 0.28 USD, 409k cache-read tokens |

Reading: from the router row alone a fresh session reaches the contract, then the charter, then the practice rules, within three to four reads, and **acts as the charter says**; the cue to wait did not hold in the one run that carried it. The role text is findable and cheap to reach, which matches the earlier probes (retrieval is not the weak point).

## What the probes did not show, and what they cannot

- **The same weak spot as in the earlier probe C:** neither run opened §21c, §21d or §21e, the roadmap operator section or the EMPATHY recall, although the router names them before the first act. The role files carry enough for this decision; whether a decision that needs a reserved-decision boundary would find it is not tested.
- **The scenario clock is not the checkout's clock.** The tree contains material dated after 07:18 (later assignments, a later MEETING). Both runs noticed it; N took the latest assignment identifiers from the log as live, W flagged the inconsistency and refused to rely on the later passages. A real cold start on a live tree has the same property, so what matters is that the session says so and checks `git log` and the assignment list before sending; W did, N did partly.
- **No commands.** Neither run could execute the tick, the activity block or the guidance command, so idle time came from the prompt. That part of the role (reading the real activity) is untested here.
- **Single model and effort.** The ADV host runs on a stronger model at higher effort in a long warm window; these are Sonnet at medium effort, cold, one run per prompt. Nothing here says the warm host behaves the same. The earlier 07:18 failure was a warm-window application failure, which a cold probe cannot reproduce.
- The cost figures are the CLI's notional figures, not spend.

## Pointers for ADV (observations, no change made)

1. The router row works as the single entry; no extra pointer was needed to reach the contract, charter and practice rules.
2. If the standing guidance is meant to be read at a cold start, neither run followed the EMPATHY link in the charter's first bullet; a short sentence in the charter naming `mandate_continuity.py guidance` as the first command of a recall would be the smallest change to test (not made here; the charter is ADV's file).
3. A cold host takes assignment identifiers from the log: a "next free identifier" line in the practice file or the tick would stop it reusing numbers from a stale reading (N read the log as ending at ADV-085 and proposed ADV-086 and ADV-087, while ADV-086 already existed on main).
