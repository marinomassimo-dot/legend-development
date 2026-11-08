# Science batch 2: observable consumption (2026-11-08)

Delegates read from transcripts with `framework/scripts/session_model_census.py`; the coordinator is a deduplicated sum of assistant responses by message id from 2026-11-08T12:25Z. No conversion to subscription percentages; no quota notice.

| Role | Package | Asked | Read back | Turns | Output | Cache read | Peak context |
|---|---|---|---|---|---|---|---|
| producer | A | sonnet / medium | sonnet-5-5, medium x54 | 54 | 69,556 | 4,890,740 | 172,705 |
| verifier | A | sonnet / high | high x50 | 50 | 50,270 | 4,518,308 | 160,668 |
| producer | B | sonnet / medium | medium x69 | 69 | 85,086 | 8,775,279 | 221,511 |
| verifier | B | sonnet / high | high x77 | 77 | 61,056 | 8,163,842 | 191,870 |
| **delegates** | | | | 250 | 265,968 | 26,348,169 | |

Birth context 17.6k to 17.9k per delegate. Coordinator (to the delivery, before landing): 26 responses, output 26,144, cache read 7,795,169, cache written 55,756, peak context 325,255 (the session has not been compacted since the previous batch, so the coordinator's context is larger than in the previous block's tail). Delegates' self-reported efforts ("5", "10") disagree with the transcript read-back (medium, high); the read-back is used.

Reading: the coordinator's cache read is about 30 percent of the delegates' combined cache read. Packages differ in breadth, so no comparison with the earlier block is claimed beyond that ratio. A fresh session or a compacted context would lower the coordinator's share further.
