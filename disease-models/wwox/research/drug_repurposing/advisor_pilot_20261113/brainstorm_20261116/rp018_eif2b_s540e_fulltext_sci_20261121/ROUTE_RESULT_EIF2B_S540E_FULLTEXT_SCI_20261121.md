# Route result: the eIF2B epsilon S540E preprint full text was not reached on 2026-11-21 (SCI window X; this is a route result, not a reading; hypothesis level; not medical advice)

Pre-registration: `PREREGISTRATION_EIF2B_S540E_FULLTEXT_SCI_20261121.md` (commit `5b9105a52`, written before any attempt). Preprint: bioRxiv doi 10.1101/2025.11.03.686297, two versions (v1 2025-11-04, v2 2025-12-09; licence field `cc_no` in the bioRxiv API record, so the text is read for analysis and would never be copied into git).

## What was tried (every attempt, in order, 13:33Z to 13:36Z)
| # | Route | Client | Result |
|---|---|---|---|
| 1 | Europe PMC search by DOI (core record) | curl from this host | HTTP 200; record PPR1113314: `isOpenAccess` N, `inEPMC` N, `hasPDF` N: Europe PMC holds no full text for this preprint (title and abstract only) |
| 2 | bioRxiv API details | curl | HTTP 200; both versions listed with their JATS URLs |
| 3 | bioRxiv JATS source XML, v2 then v1 (one request each, 5 s apart) | curl | HTTP 429, body `error code: 1015` (Cloudflare rate limit) on both |
| 4 | bioRxiv full PDF, v2 (one request) | the `web-fetch` agent (a different network client) | HTTP 429 with `Retry-After: 42`, no body, not a PDF, no captcha page |
| 5 | bioRxiv JATS source XML, v2, one retry after a 90 s pause (longer than the 42 s asked) | curl | HTTP 429, body `error code: 1015` again |

Stop rule of the pre-registration (one retry after a pause, one second lawful route; a captcha is a stop) is met: routes 3 to 5 cover both. Nothing was bypassed: no spoofed headers, no other host serving a copy, no burst. The failure is a rate limit on the publisher, not a challenge page; it is therefore **not a held status** for the paper (a retry window is legitimate and open), and it is not evidence about the paper's content.

## What this changes
Nothing in the evidence: IT47-Q02 stays NARROWED at abstract level exactly as ADV-114 wrote it (one phosphomimetic exists; compared with the phospho-resistant form: not stated in the abstract; readout: a BACE1 5' UTR reporter in SH-SY5Y per the abstract; full text not read). Predictions P1 to P4 and the rejecting observation of the pre-registration are **untested**, not confirmed and not rejected.

## Attempt 2 (2026-11-21, about 14:05Z; the single later request, one Monitor)
| # | Route | Client | Result |
|---|---|---|---|
| 6 | bioRxiv JATS source XML, v2 (one request, about 30 minutes after route 5) | curl | HTTP 429, body `error code: 1015` (17 bytes) |

The planned second attempt is spent with the same result. One further attempt on a **later day** remains allowed by the pre-registration; no other route is tried (no spoofed headers, no other host). IT47-Q02 stays NARROWED at abstract level. Predictions P1 to P4 stay untested.

## Next attempt
One further attempt, separated by at least 28 minutes from the last (a Monitor with a single request, set at 13:37Z), then at most one more on a later day. If it succeeds: read the whole text (Methods, every figure legend, supplement list), record a `FULLTEXT_READ_RECEIPT`, and fill the pre-registered rows. If it fails again: the item goes to the operator supply list only if the operator wants it (a person with browser access can save the PDF; the SHA-256 search route of `evidence_presence.py` applies once a file exists); otherwise the item stays a route result.
