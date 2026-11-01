# IT17 P4 — trace of use, report, verification, reconciliation, next package, and resume from a checkpoint

Dated 2026-11-01. This is a real trace of one small package (publication readiness of the shareable view), not a link test. It is one session with background actors; it is **not** an observation across sessions or over days.

| Step | Who | What they were given | What they did | Artefact |
|---|---|---|---|---|
| 1 | Phase-1 actor (fresh context) | a short goal and `CLAUDE.md` as the entry point; no list of rules | read `CLAUDE.md`, the state manifest, LEGEND_CORE 21c-21e (excerpts), `DEPLOY.md`, the patch, the workflow; applied the reserved-act and stop rules and performed no reserved act; did **not** open the Standing method, the roles or the adapter convention | `CHECKPOINT.md` (phase 1), branch `worktree-agent-a2ff4314325568853` at `1ba72683` |
| 2 | Orchestrator | the report | wrote the checkpoint (branch, commit, file, next action, what the actor had and had not read) into step OBJ_P4 of the IT17 record | `ledger/tasks/orchestrator/ORCH-ROADMAP-IT17-20261101.json` |
| 3 | Phase-2 actor (new context) | only the path of the record and "resume from that checkpoint" | merged the named branch, relied on the recorded facts without redoing them, built the checker, the 16 offline tests and the single-act request; read the Standing method this time (found by search, not from the router, as it said itself); performed no reserved act and made no network call outside localhost | commit `be33e9c9` |
| 4 | Verifier (fresh context) | objective and artefacts; asked to form observations before reading the producer's notes | ran the tests, mutated a served copy, read the request against DEPLOY.md and the patch; knew only the brief, and could not avoid seeing the phase-1 half of CHECKPOINT.md (declared) | its report: no false pass of consequence; two medium wording errors in the request (smoke overclaim, missing push of the workflow commit), three low ones, scanner gaps |
| 5 | Orchestrator reconciles | the verifier's findings | fixed the request text and DEPLOY.md wording; **chose the next package from the findings** (scanner gaps) and executed it: `use`/`image`/`xlink:href`, `action`, `srcset` and meta refresh are now seen, with 5 negative fixtures (17 tests pass) | commits on `task/it17` |

Resume from a checkpoint: the phase-1 actor ended after writing `CHECKPOINT.md`; a different actor continued from the record alone. Nothing was lost (the phase-2 actor re-read only what its checker had to parse) and nothing was duplicated (no network fact was gathered twice, no job ran twice). The operator gave no new prompt between the steps.

Findings that changed something: (1) a fresh actor starting from the router did not reach the Standing method, so `CLAUDE.md` now routes to it (a test requires the link); (2) the request text had overclaimed what the `smoke` job enforces.

Limits, stated: the router row was added after the phase-1 actor ran, and phase 2 ran after it but did not use it (it found the method by search); whether a third actor would now follow the router row is untested. The Stop hook is not installed on this host, so the continuity proof rests on the record and the commits, not on hook events. The reserved act (apply the patch, enable Pages, dispatch the workflow) is untouched, and the site is not online.
