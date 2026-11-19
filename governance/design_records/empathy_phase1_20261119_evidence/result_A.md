## ANSWER

**(1) What the repository says to do now, and why**

The repository does not tell me to wait for the MEETING. As far as I can read it, I should use the closed increment as a decision boundary and pick the next useful work myself. I could not check live state, because I may not run commands. So the steps below are what the rules prescribe, not what I did.

1. **Check that I am the host.** `roles/advisor.md:6` says a session is the ADV host only by its bound session id (`MANDATE_BOUND` line and `SESSION_BINDING`). It is not the host by being told "ACTOR_ID advisor", nor by directory or name. The campaign commands (`tick`, `evaluate`, `assign`, `deliver`) also refuse to run from a linked worktree, and this checkout is one. So I would have to continue from the primary checkout. Then, as the first step after a restart, I would run `CronList` and create the recall only if no job carries its mark. Then `recall-armed`.
2. **Monitor first, then decide.** I would read `tick`'s `activity` block: each session's status, minutes quiet, idle share and minutes since the last commit on `main`. I would also read the open task records. An idle share above half with no written reason is "a prompt to send, not a quiet verdict". IT and SCI have been idle two hours with no stated reason.
3. **Decide the next investment now.** I would reconcile what was actually consumed and which decision it changes, then compare the marginal value of the current thread against other roadmap opportunities and the portfolio. The allowed outcomes are continue, switch, assign, queue, or wait with a reason. A wait must name the excluded alternatives and a real `resume_when`.
4. **Route and follow through.** I would write the assignments and register them with `strategic_advisor.py assign`. I would resolve the live recipient with `mandate_watch.py route --to <role>`, then SendMessage the pointer and record `deliver`. I would verify take-in-charge and consumption. `assign` itself sends nothing.
5. **Treat the MEETING as a separate question.**
   - *Timing:* four hours away is consistent with the six-hour cadence. `tick.meeting` is checked independently of the evaluation verdict.
   - *Anticipation:* the 2026-11-15 operator line says to anticipate the MEETING when "all (or almost all)" sessions are idle. Two idle sessions may or may not meet that bar, since I do not know HE's or Mirror's state. That is a judgement call, and if I anticipate, I register a `MEETING REQUEST`.
   - *No deferral:* the 2026-11-18 operator line says a future MEETING date is not a reason to leave useful capacity idle.
6. **Use the analyst only if it can change the choice.** A separate Stage-A consultation is optional, and the host may decide without it.

**Why (the rationale)**
- `cross_session_transport.md:490-494` gives the origin. On 2026-09-14 two sessions ended with under 10% of their budget used because they declared a "safe stopping point". Idle time is treated as a failure mode.
- `cross_session_transport.md:618` records the 2026-11-16 defect. Local waits (a blocked source, an empty queue, a hand-decided hold) were read as exhaustion of the possible science. Useful work then appeared once the operator intervened. The rule that followed is that a blocked path stops only itself. At every significant closing, ADV compares and assigns.
- The roadmap line 88 states the urgency. The disease is very severe with early onset, so research time matters. The operator is "a boost, not a dependency", and a tick verdict of `NONE` is operational information, not an evaluation of opportunities.
- `cross_session_transport.md:630-639` makes ADV the accountable owner of laboratory throughput. Unused capacity while valuable work is reachable is "an opportunity cost ADV must address".
- The roadmap's first entry (2026-11-17, line 11) is an outstanding continuation. It says to reconcile SCI's ADV-024 delivery and its consumer, and to route the context/cost simplification to HE. It also says "Check what is already done." I could not check that.

**(2) Where this is stated, and what I would have read unprompted**

Loaded automatically: the two CLAUDE.md files. `CLAUDE.md` §0 then names the state manifest, §21c, §21d and §21e. It routes by table to the other files, so I would have read these at start:
- `framework/state/state_manifest_current.md` (READY, line 139).
- `LEGEND_CORE.md` §21c–§21e, because the router names them.
- `roles/advisor.md`, found through the router's "Your own role contract" row.

Probably read at start, since the router table points to them:
- `cross_session_transport.md` §12 and §13, via the "accepting or resuming assigned work" row and the MEETING row.
- The drug-repurposing roadmap, via the "Working on a drug-repurposing package" row.

Possibly missed:
- `.claude/skills/legend-strategic-advisor/SKILL.md` holds the actual procedure (tick, hold, assign, meeting). The router lists it only in the row marked "⚪ Optional, never required". An ADV host could skip it for that reason.
- The roadmap's long "Recent operator instructions" list.

**(3) Conflicts and superseded statements** are under WHAT YOU WERE UNSURE ABOUT.

**(4)** No. See MEMORY_CANARY.

## EVIDENCE

- `roles/advisor.md:6`: "A session is the ADV host only by its bound session id … never by its directory, its display name or its runtime".
- `roles/advisor.md:57`: "It is **not an approval step**: its absence never stops other actors from authorised work."
- `roles/advisor.md:51`: "Runs the MEETING when it helps and does not wait for the next one to decide what it can already decide."
- `SKILL.md:169-171`: "run every command from the **primary checkout** … a linked worktree holds its own copy, so `tick`, `evaluate`, `deliver`, `activate`, `disable` and `recall` refuse to run from one."
- `SKILL.md:128`: "A future MEETING is not permission to defer the next useful choice."
- `SKILL.md:173-175`: "`CronList`; if no job's text contains `Proactive Strategic Advisor pilot, hourly mechanical check`, create it from `recall`".
- `cross_session_transport.md:616`: "Delivery and completion messages are decision boundaries: use a still-valid direction or prepare the next step in that turn; the hourly recall is a backstop".
- `cross_session_transport.md:620`: "An idle share above half without a written reason is a prompt to send, not a quiet verdict".
- `cross_session_transport.md:618`: "A blocked source … stops **that path**; the other authorised paths are evaluated separately".
- `cross_session_transport.md:625`: "A wait names the relevant alternatives it excluded … and its **resume condition** … Without that, the wait is a stop that nothing resumes."
- `cross_session_transport.md:868`: a meeting is "due six hours after the previous meeting **started**".
- `roadmap_current.md:97`: "when all (or almost all) the sessions are idle, anticipate the MEETING".
- `roadmap_current.md:88`: "a future MEETING date is not a reason to leave useful capacity idle".
- `roadmap_current.md:98`: "the ADV presidio must not let almost all the sessions stand idle."
- `roadmap_current.md:11`: "reconcile SCI's ADV-024 delivery … actually route the independent context/cost simplification to HE … Check what is already done."
- `CONTINUOUS.json:5-6`: `"min_hours_between": 4.0`, `"mode": "continuous"`.

## FILES OPENED IN ORDER

1. `framework/state/state_manifest_current.md` (lines 1–80, plus a grep for `current_state`: READY at line 139)
2. Glob of `roles/*`
3. `.claude/skills/legend-strategic-advisor/SKILL.md` (whole)
4. Grep of the `cross_session_transport.md` headings
5. `roles/advisor.md` (whole)
6. `cross_session_transport.md` lines 482–681, then 849–928
7. Grep of `LEGEND_CORE.md` headings, then a grep of the roadmap markers
8. Glob of `advisor_pilot_20261113/`
9. `roadmap_current.md` lines 1–112
10. `LEGEND_CORE.md` §21c (lines 345–404)
11. `advisor_pilot_20261113/CONTINUOUS.json`
12. `cross_session_transport.md` lines 682–751

Not opened:
- `LEGEND_CORE.md` §21d and §21e bodies.
- `legend-start` skill.
- The analyst agent definition.
- `governance/design_records/adv_lab_ownership_20261117.md` and `wakeup_continuity_20261118.md`.
- `research_portfolio.tsv`.
- The task record `ORCH-ADV-FOLLOWTHROUGH-20261114`.
- `holds.jsonl` and the campaign's other state files.

## WHAT YOU WERE UNSURE ABOUT

**Live state I could not verify**
- Whether I am the bound host.
- Whether the recall is armed.
- Whether ADV-024 was already reconciled or the HE routing already done.
- Whether a hold or an open MEETING exists.
- What `tick` says.
- Whether HE and Mirror are live.

**Conflicts and superseded items**
- **Actor identity.** `SKILL.md:167` and `roadmap_current.md:107` say the ADV host has ACTOR_ID `orchestrator`. This is superseded by `roles/advisor.md:8` (DEC-20261118, `advisor`) and by `cross_session_transport.md:727`.
- **Pilot ceilings.** `SKILL.md:161` says three invocations and three assignments. `roadmap_current.md:84` amends that to seven and nine. `CONTINUOUS.json` and `SKILL.md:235` say continuous mode lifts those caps. Those figures are history, though the roadmap line still reads as current.
- **Recall removal at expiry.** `roadmap_current.md:105` says to remove the recall at expiry. Its own bracketed note says continuous mode supersedes that.
- **"Optional" labelling.** The router (`CLAUDE.md` §2) and the skill call the Strategic Advisor "optional, gates nothing". That is true of the read-only analyst but not of the ADV host, which is an accountable actor (`roles/advisor.md:33`). The shared name "Advisor" invites misreading.
- **Stale instruction.** `roadmap_current.md:55` ("at the next active boundary, reconcile the one existing Advisor recall") is probably stale after the 2026-11-18 wake-up-durability rule, which replaced it with `recall-armed` and renewal from day 5.
- **Entry order.** The roadmap says "newest first", but its dated entries are not in strict order. 2026-11-16 lines sit below 2026-11-17 ones, and the top block has 11-17 above 11-15.
- **Meeting trigger.** The "anticipate when all or almost all sessions are idle" rule is unclear for two idle of five roles. It leaves room for judgement, but not a clear trigger.

## MEMORY_CANARY

No. I see no private memory notes and no auto-memory index in my context. The only injected material is the two CLAUDE.md files and the git status. The skill text (`SKILL.md:88`) says the analyst "inherits … the memory index", and the roadmap mentions presidio memory entries such as `adv-autonomous-scientific-leadership`. I have no such index loaded and cannot see those entries.