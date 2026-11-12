# SCI48 cost note (observable; read from the delegate transcripts with `framework/scripts/session_model_census.py`, one response counted once)

Non-canonical. Tokens are reported as logged; they are not converted to a share of any plan, and no saving is claimed that was not measured.

| Delegate | Asked | Read back | Turns | Output tokens | Cache read | Notes |
|---|---|---|---|---|---|---|
| Producer nr-z (`legend-delegate`) | sonnet, medium | sonnet x78, medium x78 | 78 (first run 50; extension 1: 3; extension 2: 9; correction round: 16) | 138,695 | 15,327,360 | birth context 18,572 tokens; peak 291k at the second extension and more later; four launches (one dispatch and three resumes by SendMessage, one at a time) |
| Blind verifier nr-y (`legend-delegate`) | sonnet, high | sonnet x73, high x73 | 73 (first run 58; recheck 15) | 132,527 | 16,781,645 | birth context 18,604 tokens; two launches |
| **Total delegates** | | | **151** | **271,222** | **32,109,005** | |

* The coordinator (this session) is not included: it is the transcript of the whole day, not of this mandate (delegation budget, "The coordinator's own cost"); a slice figure would need `--since` and was not computed.
* The verifier cost slightly less output than the producer, and about 10% more cache read, because it re-fetched originals; the first-run verification (58 turns) found the defect that required a producer correction round and a narrow recheck, which is the expensive part of this package: **a candidate list judged complete by one reader's strings was not**, and the second reader's independent strings were what found it.
* Not run: the optional tail (see the task record), a second verifier, any escalation. No ESCALATION line was written. Zero external spend, no new service.
