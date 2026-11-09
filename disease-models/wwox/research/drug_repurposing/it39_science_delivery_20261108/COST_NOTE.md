# Observed cost — membrane and AMPA/NMDA packages, 2026-11-08

Perimeter stated: delegate figures from the four transcripts read with the census rule (a response counted once, largest output kept); the coordinator figure is the main transcript restricted to responses after 21:40Z, a window that also contains the closing of the IT38 delivery (landing, a failed-battery diagnosis and a shared-clone incident). Not shares of any plan; not comparable with earlier notes.

| Delegate | Dispatch asked / read back | Turns | Output tokens | Cache-read tokens | Peak context |
|---|---|---|---|---|---|
| A producer | sonnet/medium, medium on every turn | 83 | 136,708 | 15,485,929 | 368,077 |
| A verifier | sonnet/high, high on every turn | 91 | 113,145 | 16,261,113 | 333,925 |
| B producer | sonnet/medium, medium on every turn | 117 | 183,302 | 27,759,505 | 443,582 |
| B verifier | sonnet/high, high on every turn | 80 | 90,638 | 14,250,718 | 338,448 |
| All four | | 371 | 523,793 | 73,757,265 | 443,582 |

Coordinator since 21:40Z: 50 responses, 48,018 output tokens, 21,752,402 cache-read tokens, peak context 492,351. No escalation of model or effort. No external spend; open routes only (PubMed/PMC tools, NCBI, Europe PMC, Crossref, the public PubMed Central open-data bucket by plain curl).

What the cost bought: reading figures and supplements changed numbers that carried hypotheses (the d-APV residual, the perampanel potency, the ivabradine and ZD7288 magnitudes, the E_K comparison); the verifiers' second look after each correction round caught one new overstatement per package. The cost driver is context: images and long article text pushed delegate contexts to 330–440k tokens (the earlier IT38 delegates peaked at 130–260k), so each later turn re-read a large cache. A tighter division (one delegate per source cluster, figures noted to a table and then dropped from context) would lower it; not tried here.
