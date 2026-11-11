# Cost note — SCI44 package A (measured from `session_model_census.py` on each delegate transcript; asked and read-back settings)

| Delegate | Role | Asked | Read back | Turns | Output tokens | Cache read | Peak context |
|---|---|---|---|---|---|---|---|
| og-p (A2) | producer, expression and neural function | sonnet / medium | medium x105 | 105 | 121,831 | 16,415,700 | 315,875 |
| og-q (A3) | producer, primary pharmacology | sonnet / medium | medium x85 | 85 | 92,392 | 11,528,378 | not recorded |
| og-r (A4) | producer, alternative actions | sonnet / medium | medium x75 | 75 | 67,853 | 9,558,167 | not recorded |
| pk-v (V1) | blind verifier, A2 expression and A3 | sonnet / high | high x123 | 123 | 127,841 | 23,866,549 | not recorded |
| pk-w (V2) | blind verifier, A4 and A2 function rows | sonnet / high | high x96 | 96 | 103,522 | 19,199,522 | not recorded |
| **Total** | | | | **484** | **513,439** | **80,568,316** | |

One delegate active at a time (producers A2, A3, A4 then verifiers V1, V2 in sequence); no recursive delegation; no escalation; zero spend, no contact, no registration. The coordinator (this session) is not separable from the session census. Mechanical work (expression extraction, coverage table, relation search, identity lookups, correction application) was done by scripts in this folder. The verifier cost more than any producer (as in SCI43) and found the two substantive overturns (the KATP absence claim, the HPA region label); the A4 absence claim would have stood without it.
