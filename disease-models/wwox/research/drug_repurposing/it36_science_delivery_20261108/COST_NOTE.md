# IT36 science session: observable consumption (2026-11-08)

Read from transcripts with `framework/scripts/session_model_census.py` (delegates) and a deduplicated sum of assistant responses by message id (coordinator, from 2026-11-08T08:25Z, the start of this mandate). No conversion to subscription percentages. No quota notice appeared.

## Delegates (seven, one active at a time, no escalation)

| Role | Package | Asked | Read back (census) | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|---|---|
| producer | P1 | sonnet / medium | sonnet-5-5, medium x39 | 39 | 63,794 | 4,156,747 | 186,253 |
| verifier | P1 | sonnet / high | sonnet-5-5, high x23 | 23 | 47,271 | 2,143,122 | 153,510 |
| producer | P2+P3 | sonnet / medium | sonnet-5-5, medium x56 | 56 | 72,079 | 5,744,224 | 191,201 |
| verifier | P2+P3 | sonnet / high | sonnet-5-5, high x42 | 42 | 38,082 | 3,877,215 | 143,544 |
| producer | P4 phase A (unguided) | sonnet / medium | sonnet-5-5, medium x16 | 16 | 15,425 | 861,133 | 83,134 |
| producer | P4 B/C + P5 | sonnet / medium | sonnet-5-5, medium x56 | 56 | 96,422 | 7,688,992 | 252,014 |
| verifier | P4 B/C | sonnet / high | sonnet-5-5, high x41 | 41 | 38,095 | 3,514,501 | 163,403 |
| **delegates total** | | | | 273 | 371,168 | 27,985,934 | |

Birth context 17.5k to 17.9k tokens for every delegate (the typed `legend-delegate` agent). Several delegates reported their own effort as "low" or "5" from inside their runtime; the transcripts read back the requested medium and high, so the self-reports are not used.

## Coordinator

71 responses, claude-sonnet-5-5, output 58,424, cache read 10,649,237, cache written 193,474, peak context 219,242 (this part of the session started from a compacted summary, not from the 734k of the earlier block). The coordinator effort read-back per response was not separated for this block (the whole-session census reads high and max).

## Reading

The coordinator's cache read is about 38 percent of the delegates' combined cache read in this block, against roughly equal in the previous block: starting from a compacted context kept the coordinator much cheaper. Output is dominated by the delegates (371k against 58k). The costliest delegate was the phase B/C producer (252k peak context, 7.7M cache read); the verifier remained the cheaper half of each pair. Comparisons across blocks are limited: packages differ in breadth.
