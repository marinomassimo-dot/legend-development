# Cost note: queued packages T-type, INV-05, INV-06, INV-07, INV-08

Observable values from the transcripts, one response counted once, tokens as logged; no conversion to plan share or money. Tasks `ORCH-TTYPE-20261107`, `ORCH-INV05-`, `-INV06-`, `-INV07-`, `-INV08-20261107`. All delegates `legend-delegate`; producers asked sonnet/medium and read back claude-sonnet-5-5 with effort medium on every response; verifiers asked sonnet/high and read back high on every response; no other model, no escalation, no resume, one delegate active at a time. No API error or compaction marker in any delegate log; two source-access incidents (below). The coordinator ran claude-sonnet-5-5 at effort high (not medium: not reachable from a prompt).

| Package | Producer turns / output / cache read / peak ctx | Verifier turns / output / cache read / peak ctx | Rows audited | Not plainly supported |
|---|---|---|---|---|
| T-type | 36 / 50,649 / 3,935,505 / 182,504 | 41 / 54,167 / 3,477,872 / 157,012 | 29 | 2 (+ repairs) |
| INV-05 NMDA | 30 / 37,817 / 1,984,517 / 113,730 | 35 / 48,370 / 2,283,638 / 138,314 | 25 | 5 |
| INV-06 myelin | 60 / 69,972 / 8,412,153 / 226,546 | 71 / 65,848 / 6,867,219 / 185,017 | 40 | 3 |
| INV-07 metabolic | 48 / 53,710 / 4,664,790 / 162,686 | 49 / 52,423 / 4,195,000 / 161,465 | 42 | 7 |
| INV-08 NRF2 | 31 / 34,013 / 1,818,108 / 101,533 | 37 / 54,997 / 2,937,169 / 143,689 | 21 | 2 |
| Delegates, ten runs | 438 turns / 521,966 output / 40,575,971 cache read | | 157 | 19 |

Birth context 17,300 to 18,100 tokens in every run (against about 40,000 for a general-purpose delegate).

**Coordinator.** In the window from the first queued package (2026-11-07T19:57Z to 23:13Z): 74 responses, 92,284 output, 37,712,644 cache read (about 510,000 per response), peak context 611,527 tokens; since the start of this scientific session (17:51Z): 134 responses, 166,412 output, 60,003,272 cache read. The coordinator's cache read in the queued window (37.7 million) is about as large as that of the ten delegates together (40.6 million), though it produced about a sixth of their output: the cost of coordination comes from the accumulated context of a very long session, not from the work of each step. This confirms and sharpens the correction already proposed in `nb1_myc_20261107/COST_NOTE.md`: run the secondary coordinator in a fresh session or after a handover note; with that single change the same ten packages would cost the coordinator a few times less. Not changed here because the runtime and the session are not reachable from the prompt.

**Verification yield.** 157 audited rows, 19 not plainly supported (12 percent), plus omissions and repairs in the experiment and chain items; no package was returned clean. The verifier restricted to decisive items plus a declared sample cost 35 to 71 turns (2.3 to 8.2 million cache read) against the producer's 30 to 60.

**Incidents.** (1) A verifier (INV-05) read two PMC pages through a page summariser (WebFetch) after the same pages showed a reCAPTCHA to another client; it said so, its reads are labelled fragment-level, and every later brief carries the instruction to stop on any challenge on any tool (no repeat in the later packages). (2) Producers and verifiers met publisher 403, Cloudflare and reCAPTCHA pages and Europe PMC HTTP 500 on several sources and stopped; the reasons are recorded per package. No usage-limit notice appeared in any log; that does not show the main session's remaining capacity, which was not measured.
