# Proposed corrections to the operator seat and to two routing labels (2026-11-19)

Non-normative note for ADV and the operator. **Nothing here edits the operator's text**: the roadmap's operator section is the operator's seat, and the router and the ADV skill are labels. Each item is a proposal that ADV or the operator can accept with a dated line. Found by a memory-free cold reader (probe A of `empathy_phase1_20261119.md`) and re-checked by me on the tree at `af34bac9e`.

| # | Where | What it says | Why it looks stale or misleading | Proposed dated line |
|---|---|---|---|---|
| 1 | `roadmap_current.md:107` | the "ADV — Strategic Advisor" session has ACTOR_ID `orchestrator` | superseded by `roles/advisor.md` and `DEC-20261118-ADVISOR-ACTOR` (ACTOR_ID `advisor`, 2026-11-18) | "2026-11-19: since DEC-20261118-ADVISOR-ACTOR the ADV host is ACTOR_ID `advisor`; the text above is history." |
| 2 | `.claude/skills/legend-strategic-advisor/SKILL.md:167` | the presidio is hosted by `ADV`, ACTOR_ID `orchestrator` | same | same wording, in the skill |
| 3 | `SKILL.md:161` against `roadmap_current.md:84` | a pilot of three invocations and three assignments; the roadmap line says seven and nine | continuous mode lifts both caps (`CONTINUOUS.json`, `SKILL.md` "Continuous operation"); the figures are history but read as current | "the pilot ceilings above are history; continuous mode has none" |
| 4 | `roadmap_current.md:105` | remove the recall at expiry | superseded by continuous mode and by the wake-up durability rule (`recall-armed`, renewal from day 5) | dated "superseded by `cross_session_transport.md` section 12, Wake-up durability" |
| 5 | `roadmap_current.md:55` | "at the next active boundary, reconcile the one existing Advisor recall with `strategic_advisor.py recall`" | probably done and replaced by the renewal bookkeeping (the recall is armed 2026-11-18T21:30:39Z, tag `9154b9df`) | dated "done 2026-11-18; see Wake-up durability" or removal by the operator |
| 6 | `CLAUDE.md:100-101` ("Optional, never required") and `SKILL.md:8` | the Strategic Advisor is optional and gates nothing | true of the read-only analyst, not of the ADV host (`roles/advisor.md`; `SKILL.md:105` already says "Accountable host, optional consultant", the router row does not) | split the router row: the analyst stays optional; the host is reached through `roles/advisor.md` |
| 7 | roadmap order | the section says "newest first" | 2026-11-16 entries sit under 2026-11-17 ones; the top block has 11-17 above 11-15 | reorder or drop the claim |

Not proposed: any change of meaning. Items 1 to 5 add a dated line and keep the old text, which is the repository's rule for history.

**Disposition, EMPATHY Phase 2 (2026-11-19, `plan`, operator-authorised implementation).** The current roadmap seat now reconciles identity, continuous mode and the distinction between current guidance and historical pilot instructions; its entire earlier operator block is preserved verbatim in the same file's historical section. The router and ADV skill distinguish the accountable host from the optional analyst. The historical ordering wording is preserved as part of the original, not adopted as a claim about the current section. See [Phase 2](empathy_phase2_20261119.md); this is a reconciliation of documented directions, not a new operator decision or a claim that a recall was rearmed here.
