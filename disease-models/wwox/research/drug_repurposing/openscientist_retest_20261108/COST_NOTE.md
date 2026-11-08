# Observed cost — OpenScientist/Dismech full-input repeat, 2026-11-08

Perimeter stated. Figures are read from transcripts with `session_model_census.py` (a response counted once, largest output kept) and, for the coordinator window, from the main transcript restricted to responses after 17:36Z on 2026-11-08 (the census command has no time filter; the window sum was computed with the same one-response-once rule). They are not shares of any plan and are not comparable with the earlier mandates' notes.

## Delegates (22 delegates, one active at a time, no recursion)

* Dispatch: producers `legend-delegate`, asked sonnet/medium, read back medium on every turn; verifiers asked sonnet/high, read back high on every turn. Phase 2 and the correction round of each producer ran in the same conversation by message (so the producer's context was reused, not rebuilt). Birth context 17.6k to 18.2k tokens each.
* Producers (11): 447 turns, 781,014 output tokens, 45,014,482 cache-read tokens.
* Verifiers (11): 512 turns, 588,244 output tokens, 60,989,988 cache-read tokens.
* All 22: 959 turns, 1,369,258 output tokens, 106,004,482 cache-read tokens; peak context 262,856 (the membrane verifier); largest producer peak 195,094.
* Per report, producer then verifier output tokens: ISR 48,231 / 46,811; T-type 79,016 / 38,112; NMDA 80,610 / 43,041; myelination 68,274 / 52,985; PDH 71,214 / 48,287; NRF2 63,263 / 56,382; GSK3 77,494 / 50,438; seizures 72,829 / 59,936; PV 71,113 / 51,837; HDAC5 65,182 / 59,700; membrane 83,788 / 80,715.
* No escalation of model or effort was used.

## Coordinator (this session, window from 17:36Z)

132 responses, 87,956 output tokens, 27,463,923 cache-read tokens, peak context 348,437. The window contains the setup, eleven dispatch/review/correction cycles, the delivery documents and the landing checks. The coordinator's effort was not re-read for this window.

## Elapsed

Setup at 17:36Z; the last correction round ended about 21:00Z; about 3 h 25 min for the eleven reports, roughly 18 to 20 minutes each (producer two phases, verifier, correction round), then the delivery documents and checks.

## External spend

None. No paid service, API key, cloud GPU, account, registration or e-mail. Open routes only (PubMed and PMC tools, NCBI E-utilities, Europe PMC, Crossref, PubChem; plain curl with the default user agent). One verifier tried a browser-style header once and the session classifier refused; nothing was obtained that way.

## What the cost bought, and where it was wasted

The verifier's cost exceeded the producer's in cache reads (because it reads the original and the sources afresh) and was lower in output; its findings changed a statement in every package (eight to sixteen corrections each). The Phase-1 reading (about 50k tokens of context each) was cheap and produced the item lists. The waste was in repeated retrieval of the same few papers by different packages (for example the neuron-deleted slice paper, the 2026 myelination review, the lithium seizure paper) and in producers' unreceipted abstract views beyond the five-source cap in two packages; a shared per-session retrieval cache would have saved reads but was not built (no new infrastructure).
